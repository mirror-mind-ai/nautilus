# Mission

## Definition

A Mission is a named intention of realization.

It gathers a direction before Nautilus attempts to act. In this version, a Mission does not execute, assign roles, produce delivery, collect evidence, mark realization, or integrate learning. It only gives form to the movement that may become work.

## Why Mission comes before execution

Nautilus treats formulation as its own chamber.

In many systems, the passage from intention to task happens too early. A person feels a direction, the system asks for an action, the agent starts producing. The risk is execution carrying an intention that is still foggy.

The Mission prevents this leap. It allows the movement to be named before it is operationalized.

## Minimal form

The first Mission fixture carries only the fields required for formulation recognition:

```yaml
mission:
  id: mission-001
  title: Formulate the first Nautilus mission
  purpose: Prove that Nautilus can name a directed intention before execution.
  status: formulated
```

## Fields

| Field | Function |
| --- | --- |
| `id` | Stable Mission identifier |
| `title` | Short name for the intention |
| `purpose` | Reason why the intention matters now |
| `status` | Minimal Mission state in the current chamber |

## Current status

The only stabilized status in this slice is `formulated`.

This is deliberate. Other states should enter only when the grammar of execution, delivery, evidence, and realization is introduced in a way recognized by the components of the Nautilus Family.

## Well formulated Mission

A well formulated Mission does not need a complete plan. It needs to make the movement readable.

It should name a directed intention, explain why it matters now, and remain proportional to the formulation chamber.

## Poorly formulated Mission

A Mission is not yet whole when:

- the title is too generic to orient;
- the purpose does not explain situated relevance;
- the intention depends on hidden execution;
- the `status` promises more than the current chamber recognizes;
- the other Nautilus components could not recognize the same fields.

## Main anti-pattern

The main anti-pattern is smuggling execution into formulation.

Example: a Mission that already contains a detailed plan, role assignment, final criteria, evidence, and closure may be valuable, but it exceeds the current slice. It should be decomposed or wait until the method has chambers capable of sustaining it.

## Next evolution

The next evolution of Mission should clarify when a formulated Mission becomes ready for execution and which fields can enter without breaking recognition across Method, Protocol, Mirror Extension, and Harness.
