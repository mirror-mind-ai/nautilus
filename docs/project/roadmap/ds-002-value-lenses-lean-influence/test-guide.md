[< Story](index.md)

# Test Guide, DS-002 Define Value Lenses and Lean Influence

## Automated Validation

```bash
.venv/bin/mkdocs build
rg "stage|etapa|customer payment is the final|pagamento.*definição final|Lean defines Nautilus|Lean define Nautilus" docs/method docs/pt-br/method docs/presentations docs/pt-br/presentations --glob "*.md"
```

## Navigator Validation

Open the MkDocs viewer and inspect:

- Value Generation
- Impact
- Evidence, if changed
- Intro slides, if changed

Pass condition: pragmatic and integrative value read as lenses, not stages.

Fail condition: Lean becomes the governing definition of Nautilus value or integrative value appears dependent on market recognition.

## Validation Evidence

Automated validation passed.

```text
mkdocs build: Documentation built successfully
validation search: matches were expected statements saying lenses are not stages, plus unrelated words such as backstage and smoke checks. No result says that Lean fully defines Nautilus value or that customer payment is the final definition of value.
```
