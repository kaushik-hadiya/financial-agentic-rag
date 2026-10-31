"""Parse every page of each PDF with LlamaParse and save one Markdown file per page.

Run from the project root:  uv run src/parse_pdfs.py
Output: parsed/<company>/page_001.md, page_002.md, ...
Cost: "agentic" tier is ~10 credits per page. PDFs that are already parsed are skipped,
so running this again does not spend credits twice.
"""

from pathlib import Path

from llama_cloud import LlamaCloud

from settings import get_settings

OUTPUT_DIR = Path("parsed")

# Word in the PDF file name -> output folder name.
COMPANIES = {
    "ATHERENERG": "ather",
    "OLAELEC": "ola",
    "SWIGGY": "swiggy",
    "ETERNAL": "eternal",
    "BAJAJ-AUTO": "bajaj",
}


def find_pdf(docs_dir: Path, name_part: str) -> Path:
    """Return the one PDF whose file name contains `name_part`."""
    matches = list(docs_dir.glob(f"*{name_part}*.pdf"))
    if len(matches) != 1:
        raise FileNotFoundError(
            f"Expected 1 PDF matching {name_part!r}, found {len(matches)}"
        )
    return matches[0]


def parse_pdf(client: LlamaCloud, pdf: Path) -> list:
    """Upload a whole PDF to LlamaParse and return its list of page results."""
    with pdf.open("rb") as file:
        result = client.parsing.parse(
            tier="agentic",
            version="latest",
            upload_file=file,
            expand=["markdown"],
            verbose=True,
        )
    return result.markdown.pages


def save_pages(pages: list, out_dir: Path) -> list[int]:
    """Write each page to out_dir/page_NNN.md. Return page numbers that failed."""
    out_dir.mkdir(parents=True, exist_ok=True)
    failed = []
    for page in pages:
        if not page.success:
            print(f"  Page {page.page_number} failed: {page.error}")
            failed.append(page.page_number)
            continue
        out_file = out_dir / f"page_{page.page_number:03d}.md"
        out_file.write_text(page.markdown, encoding="utf-8")
    return failed


def main() -> None:
    settings = get_settings()
    client = LlamaCloud(api_key=settings.llama_cloud_api_key.get_secret_value())

    for name_part, folder in COMPANIES.items():
        out_dir = OUTPUT_DIR / folder
        if out_dir.exists() and any(out_dir.glob("page_*.md")):
            print(f"Skipping {folder}: already parsed in {out_dir}")
            continue
        pdf = find_pdf(settings.docs_dir, name_part)
        print(f"Parsing {pdf.name} (all pages) ...")
        pages = parse_pdf(client, pdf)
        failed = save_pages(pages, out_dir)
        print(f"Saved {len(pages) - len(failed)} pages to {out_dir}, failed: {failed}")


if __name__ == "__main__":
    main()
