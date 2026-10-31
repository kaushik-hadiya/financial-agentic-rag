# Learning Log

## 2026-10-31: Project setup
- **Built:** a uv project with dev tools (ruff, pytest), `src/settings.py` using
  pydantic-settings, and `.env.example`. Started with `uv init --package`, then simplified to
  plain scripts in `src/` run with `uv run src/<file>.py` (no package, no entry point).
- **Learned:** dependencies vs dev dependency groups, `uv.lock`, `uv run`, `BaseSettings` +
  `SecretStr`, `@lru_cache`, `if __name__ == "__main__"`, imports resolve from the folder of
  the file you run, relative paths like `Path("docs")` depend on the folder you run from,
  reading a ruff error (EXE002 is caused by the NTFS drive making every file executable).
- **Open questions:** which embedding model/provider to use with OpenRouter?

## 2026-10-31: Choosing a PDF parser and parsing the reports
- **Built:** compared Docling, Marker and LlamaParse on real pages, then parsed all 1,513 pages
  of 5 annual reports (Ather, Ola, Swiggy, Eternal, Bajaj) with LlamaParse's agentic tier into
  `parsed/<company>/page_NNN.md`. The script skips companies that are already parsed.
- **Learned:** test parsers on your own hardest pages (Docling broke the multi-level equity
  table; LlamaParse kept it with HTML rowspan/colspan and also read Bajaj's ₹ correctly),
  uv package indexes (CPU-only PyTorch), `.fuse_hidden` files mean a process still has the file
  open, reading tracebacks bottom-up, "name resolution" errors mean the internet/DNS dropped,
  pydantic `hide_input_in_errors` keeps secrets out of error messages.
- **Open questions:** how to chunk HTML tables without splitting rows? Which embedding model
  via OpenRouter? Remove footer/logo noise before or after chunking? Should the parse script
  retry by itself when the internet drops?
