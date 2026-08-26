[< Story](index.md)

# Plan, DS-003 Publish Method Principles

## Pull

This story is pulled because the principle inventory has reached a stable enough set. The method should now publish the principles as a coherent architecture instead of leaving them only as planning notes.

## Prepare

The current inventory defines strategies for six principles:

- Grow without Losing Form as the founding umbrella principle.
- Value as Direction, using `value-generation.md` as the principle page.
- Form in Service of Realization, using `grammar.md` as the principle page.
- Grounded Progress, using `evidence.md` as the principle page.
- Reliable Continuity, using `reliable-continuity.md` as the principle page.
- Integrated Expansion, using `integration.md` as the principle page.

Human Territory Centrality and Human-Agentic Collaboration remain in evaluation and should not be promoted in this story.

The update must remain bilingual. Every public documentation change in `docs/` needs a corresponding Portuguese version in `docs/pt-br/`.

## Scope

- Rewrite `docs/method/principles.md` and `docs/pt-br/method/principles.md` around the approved principle architecture.
- Add or adjust opening sections in the five principle pages so each page clearly carries its principle name and canonical sentence.
- Preserve existing conceptual content where useful, but subordinate it to the principle framing.
- Update home, overview, and reading paths only if needed.
- Update MkDocs navigation only if the current navigation hides the principle architecture too much.
- Keep the principles inventory as planning record, not public method canon.
- Run MkDocs validation.

## Non-Goals

- Do not promote Human Territory Centrality or Human-Agentic Collaboration as principles.
- Do not create separate principle pages if existing concept pages can carry the principle well.
- Do not redesign the whole ontology.
- Do not change Protocol, Mirror Extension, or Harness implementation.

## Implementation Approach

Canonical order:

```text
Founding principle:
  Grow without Losing Form

Operating principles:
  Value as Direction
  Form in Service of Realization
  Grounded Progress
  Reliable Continuity
  Integrated Expansion
```

Canonical sentences:

```text
Grow without Losing Form:
Each advance should expand the Journey's capacity while preserving the coherence that allows it to continue.

Value as Direction:
Every Journey should orient its Realization by the value it seeks to make available in the Human Territory.

Form in Service of Realization:
Each form in the method should help value become realized in the Human Territory without imposing more complexity than the Journey needs to carry.

Grounded Progress:
A Journey should only recognize progress when there is a trustworthy trace that value was made available, transformed, or learned in the Human Territory.

Reliable Continuity:
Each turn of the Journey should preserve enough form for the next one to begin with more capacity, not reconstruction.

Integrated Expansion:
Each Realization should expand the Journey's capacity without breaking the form that allows it to continue.
```

Portuguese canonical sentences:

```text
Crescer sem Perder a Forma:
Cada avanço deve ampliar a capacidade da Jornada preservando a coerência que permite continuar.

Valor como Direção:
Toda Jornada deve orientar sua Realização pelo valor que busca tornar disponível no Território Humano.

Forma a Serviço da Realização:
Cada forma do método deve ajudar o valor a se realizar no Território Humano sem impor complexidade maior do que a Jornada precisa carregar.

Avanço Sustentado:
Uma Jornada só deve reconhecer avanço quando houver lastro suficiente de que valor foi tornado disponível, transformado ou aprendido no Território Humano.

Continuidade Confiável:
Cada giro da Jornada deve preservar forma suficiente para que o próximo comece com mais capacidade, não com reconstrução.

Expansão Integrada:
Cada Realização deve expandir a capacidade da Jornada sem romper a forma que permite continuar.
```

## Test Strategy

Run MkDocs build and search for obsolete candidate names that should no longer appear as principle names in public method pages.

```bash
.venv/bin/mkdocs build
rg "Proportional Evidence|Evidência Proporcional|Integration before Expansion|Integração antes da Expansão|Formal Proportionality|Proporcionalidade Formal" docs/method docs/pt-br/method docs/index.md docs/pt-br/index.md
```

## Validation Route

Navigator reviews:

- Method principles page.
- Value Generation.
- Grammar.
- Evidence.
- Reliable Continuity.
- Integration.

Pass condition: the reader can understand the principle architecture without needing the internal inventory.

Fail condition: the docs still read as a list of scattered concepts rather than a coherent principle set.

## Checkpoint

Approved by the Navigator. Implementation may start.
