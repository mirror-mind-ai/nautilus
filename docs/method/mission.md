# Mission

## Definition

A Mission is a unit of realization in conduct.

It gives form to a movement that still needs to be conducted by Participants in a Journey. A Mission is not a task with a more important name. It is the responsibility frame that holds value, authority, Participants, proportional scope, possible Delivery, Evidence, and Integration before a Realization can be recognized.

In the current version, a Mission is still primarily formulative. It does not execute by itself, assign complete roles, produce Delivery, collect Evidence, mark Realization, or integrate learning. It names the movement that may become work and makes it recognizable enough to be conducted.

## Mission, task, and execution

A task is a unit of execution inside an assumed frame.

A task can have intention, Delivery, and Evidence. For example, starting a documentation server has an intention, a resulting availability, and a verifiable response. These elements alone do not make the task a Mission. They only make the task well described.

A Mission differs from a task because it carries responsibility for the frame itself. It asks what Realization is being conducted, why it matters now, who participates, what authority is present, what counts as sufficient progress, what Evidence can sustain recognition, and what learning should be preserved.

A Mission may contain many tasks. A task may serve more than one Mission by producing Evidence or learning for multiple fields of responsibility. But a task does not need to preserve the full meaning of the Journey in order to be executed.

## Mission and Realization

Mission and [Realization](realization.md) are not separate substances. They are different moments of the same movement.

A Mission is Realization before recognition, while it is still being conducted. A Realization is the recognition that value has become available in the [Human Territory](human-territory.md), sustained by Evidence.

A Mission can fail, be abandoned, be reformulated, generate partial Realizations, or reveal that the desired Realization was wrongly named. For this reason, not every Mission becomes a Realization. But every Mission points toward a possible Realization.

## Why Mission comes before execution

Nautilus treats formulation as its own chamber.

In many systems, the passage from intention to task happens too early. A person feels a direction, the system asks for an action, the agent starts producing. The risk is execution carrying an intention that is still foggy.

The Mission prevents this leap. It allows the movement to be named before it is operationalized.

## Mission shapes

A Mission does not need to have a single closed output.

Some Missions are constructive. They create a new capability, artifact, structure, or state. For example, creating a cinemateca feature in a museum product is a constructive Mission when the responsibility is to make a new product capability available.

Some Missions are cadenced. They preserve a rhythm of value generation through repeated curatorial or operational movement. For example, sustaining a daily publication rhythm for museum pieces is a cadenced Mission when the responsibility is not one isolated piece, but the continued availability of curated pieces with enough quality and coherence.

Different Mission shapes require different Evidence. A constructive Mission may be recognized through a new capability that works. A cadenced Mission may be recognized through continuity with sufficient quality over time.

## Mission field

A Journey may contain simultaneous Missions.

These Missions may have different natures, such as editorial work and product work. They may share tasks, Evidence, and learning without becoming the same Mission. A publishing task may advance an editorial Mission while revealing friction that informs a product Mission.

The Mission field is the visible relation among active Missions, tasks, Evidence, learning, and boundaries of responsibility.

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

It should name a directed intention, explain why it matters now, show the responsibility frame that distinguishes it from a task, and remain proportional to the formulation chamber.

## Poorly formulated Mission

A Mission is not yet whole when:

- the title is too generic to orient;
- the purpose does not explain situated relevance;
- the intention is only a task inside an assumed frame;
- the responsibility frame is hidden;
- the intended Realization cannot be recognized;
- the intention depends on hidden execution;
- the `status` promises more than the current chamber recognizes;
- the other Nautilus components could not recognize the same fields.

## Main anti-pattern

The main anti-pattern is smuggling execution into formulation.

Example: a Mission that already contains a detailed plan, role assignment, final criteria, evidence, and closure may be valuable, but it exceeds the current slice. It should be decomposed or wait until the method has chambers capable of sustaining it.

A second anti-pattern is inflating tasks into Missions. A large task remains a task when it only executes part of a frame. A small Mission remains a Mission when it holds responsibility for a complete movement of Realization.

## Practice: Extract Missions from Agent-Human Interactions

Nautilus can use agent-human conversations as material for Mission formulation.

The practice [Extract Missions from Agent-Human Interactions](practices/extract-missions-from-agent-human-interactions.md) observes a real interaction and asks whether it contains only tasks or whether a Mission candidate is emerging.

This practice preserves the conversational nature of agentic environments. The human does not need to fill an ontology before acting. The interaction can be revisited, and the Mission can be extracted from the trace of intention, responsibility, Delivery, Evidence, and Integration.

## Next evolution

The next evolution of Mission should clarify when a formulated Mission becomes ready for execution and which fields can enter without breaking recognition across Method, Protocol, Mirror Extension, and Harness.
