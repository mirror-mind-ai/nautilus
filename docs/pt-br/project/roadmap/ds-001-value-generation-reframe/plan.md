[< Story](index.md)

# Plan, DS-001 Reframe Nautilus around Value Generation

## Pull

This story is pulled because the method's conceptual center changed: Realization remains essential, but it is now understood as the means by which Nautilus conducts Value Generation. Without an Ariad story, this insight would spread through the documentation as unsynchronized wording changes.

## Prepare

Current baseline already contains Realization and Impact as distinct concepts. The new work is to introduce Value Generation as the central layer while preserving the earlier distinction: Realization is what the Journey can conduct; Impact is what the world does after realized value becomes available.

The update must remain bilingual. Every public documentation change in `docs/` needs a corresponding Portuguese version in `docs/pt-br/`.

## Scope

- Define the canonical short description in English and Portuguese.
- Create `method/value-generation.md` and `pt-br/method/value-generation.md`.
- Update home, overview, conceptual arc, grammar, glossary, realization, impact, evidence, delivery, integration, and relevant influence pages.
- Extend the Aristotelian influence page from metaphysical actualization toward ethical orientation.
- Update slides and facilitator notes after the method pages stabilize.
- Run MkDocs validation.

## Non-Goals

- Do not redesign the whole method ontology.
- Do not change Protocol, Mirror Extension, or Harness implementation in this story.
- Do not promise that Impact is controllable.
- Do not replace Realization with Value Generation.

## Implementation Approach

Start with the canonical definition and Value Generation concept page. Then update the foundation pages that orient the reader. After that, revise the concept pages that depend on the new hierarchy. Presentations should be updated last, because they should compress the stable method body rather than drive it.

Suggested conceptual hierarchy:

```text
Value Generation
  is conducted through Realization
    made available in the Human Territory
      sustained by Evidence
        followed by Impact
          integrated as future capacity
```

Candidate definition:

English: Nautilus is a method for continuous value generation through human-agentic collaboration.

Portuguese: Nautilus é um método para geração contínua de valor por meio de colaboração humano-agêntica.

## Test Strategy

Run MkDocs build and check for broken links. Search for obsolete claims that Realization is the final center of the method or that Impact is required to recognize Realization. Review English and Portuguese pages together for conceptual equivalence.

## Validation Route

Navigator reviews the home page, method overview, Value Generation page, Realization page, Impact page, and intro slides in the MkDocs viewer. The pass condition is that the method reads as Value-centered without losing the precision of Realization and Impact.

## Checkpoint

Approved by the Navigator. Implementation may start.
