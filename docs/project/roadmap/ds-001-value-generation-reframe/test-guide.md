[< Story](index.md)

# Test Guide, DS-001 Reframe Nautilus around Value Generation

## Automated Validation

```bash
.venv/bin/mkdocs build
rg "method for conducting human-agentic Realization|method for conducting human-agentic realization|eight founding concepts" docs --glob "*.md" --glob "!site/**"
```

## Navigator Validation

Open the MkDocs viewer and inspect the updated reading path:

- Home
- Method overview
- Value Generation
- Realization
- Impact
- Conceptual Arc
- Intro slides

Pass condition: the reader can understand that Nautilus is centered on Value Generation, conducts that value through Realization, and observes Impact without claiming control over it.

Fail condition: the docs still imply that Realization is the ultimate center or that Impact is required to recognize Realization.

## Validation Evidence

Pending.
