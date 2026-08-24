# Markdown viewer

A documentação do Nautilus Agentic Method usa MkDocs Material como viewer navegável.

## Rodar localmente

A partir da raiz da jornada:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Depois abra:

```text
http://127.0.0.1:8000
```

## Gerar site estático

```bash
mkdocs build
```

O site será gerado em `site/`.

## Convenção

Os arquivos Markdown continuam sendo a fonte de verdade. O viewer apenas oferece navegação, busca e leitura confortável. Quando o método mudar, atualize os documentos em `docs/method/` e deixe apresentações e casos canônicos coerentes com eles.
