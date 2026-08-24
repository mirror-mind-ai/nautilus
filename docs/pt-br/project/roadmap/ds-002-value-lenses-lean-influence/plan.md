[< Story](index.md)

# Plan, DS-002 Define Value Lenses and Lean Influence

## Pull

This story is pulled because the definition of Value Generation now needs a more precise account of value. Nautilus has an integrative definition of value, but pragmatic audiences also recognize Lean value: value perceived by the customer as benefit worth choosing, using, or paying for. The documentation should hold both without collapsing one into the other.

## Prepare

The current documentation already places Value Generation at the center of the method, with Realization as the disciplined means and Impact as the later response of the world. The next refinement is to clarify that value can be read through multiple lenses.

The update must remain bilingual. Every public documentation change in `docs/` needs a corresponding Portuguese version in `docs/pt-br/`.

## Scope

- Update `method/value-generation.md` and `pt-br/method/value-generation.md` with the canonical definition of integrative value.
- Add a section distinguishing value lenses, not value stages.
- Introduce the pragmatic value lens and cite Lean as an influence.
- Clarify that pragmatic value asks whether someone perceives enough benefit to receive, use, pay, or continue.
- Clarify that integrative value asks whether the Human Territory becomes more integrated, capable, clear, trustworthy, or continuous.
- Update Impact and Evidence only if needed to preserve the distinction between contact, response, field effect, pragmatic value, and integrative value.
- Update slides only if there is a compact, presentation-worthy phrasing.
- Run MkDocs validation.

## Non-Goals

- Do not reduce Nautilus to Lean Management.
- Do not define integrative value as a later stage after pragmatic value.
- Do not require market payment, usage, or customer perception for every valid form of value.
- Do not redesign the whole method ontology.

## Implementation Approach

Start with the Value Generation page. Add a concise definition:

English: Value is the contribution that increases the integration of the Human Territory, expanding its capacity to act, learn, sustain relationships, and continue with more coherence.

Portuguese: Valor é a contribuição que aumenta a integração do Território Humano, ampliando sua capacidade de agir, aprender, sustentar relações e continuar com mais coerência.

Then add value lenses:

```text
Pragmatic lens: is the value perceived by those who receive, use, pay, choose, or continue?
Integrative lens: does the contribution increase integration in the Human Territory?
```

Use Lean as an influence for the pragmatic lens, not as the governing frame of Nautilus.

## Test Strategy

Run MkDocs build and search for language implying value lenses are sequential stages or that Lean defines Nautilus value completely.

## Validation Route

Navigator reviews the Value Generation page and any changed Impact, Evidence, and slide sections in the MkDocs viewer.

Pass condition: the reader can understand that pragmatic and integrative value are lenses that may converge, diverge, or appear separately.

Fail condition: the docs imply that integrative value must pass through pragmatic value first, or that customer payment is the final definition of value in Nautilus.

## Checkpoint

Implementation must not start until the Navigator approves this plan.
