"""Agentic RAG over company annual reports (PDFs in `docs/`).

Run from the project root:  uv run src/main.py
"""

from settings import get_settings


def main() -> None:
    """Start the app. For now it only checks that the PDFs can be found."""
    settings = get_settings()
    pdfs = sorted(settings.docs_dir.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs in {settings.docs_dir}")


if __name__ == "__main__":
    main()
