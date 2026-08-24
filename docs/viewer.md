# Markdown viewer

The Nautilus Agentic Method documentation uses MkDocs Material as its navigable viewer.

## Run locally

From the journey root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

## Build static site

```bash
mkdocs build
```

The site will be generated in `site/`.

## Convention

Markdown files remain the source of truth. The viewer only provides navigation, search, and comfortable reading. When the method changes, update documents in `docs/method/` and keep presentations and canonical cases coherent with them.
