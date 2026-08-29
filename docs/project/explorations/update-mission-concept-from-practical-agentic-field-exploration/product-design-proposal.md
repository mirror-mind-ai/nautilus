# Product Design Proposal: Update Mission Concept from Practical Agentic Field Exploration

## Product Intent

A exploração prática refinou o conceito de Missão no Nautilus Agentic Method a partir de interações reais em ambiente agêntico. O método deve atualizar sua documentação para distinguir Missão de tarefa, diferenciar Missão de Realização, reconhecer Missões simultâneas e cadenciadas, introduzir a prática Extract Missions from Agent-Human Interactions e representar tarefas que servem como evidência ou aprendizado para mais de uma Missão.

## User-Facing Behavior

A rodada de exploração consolidou necessidades importantes de atualização do método Nautilus a partir do conceito de Missão. O método precisa distinguir Missão de tarefa sem depender apenas de intenção, entrega e evidência, pois tarefas também podem conter esses elementos. Precisa diferenciar Missão de Realização como momentos do mesmo fenômeno: Missão é realização em condução; Realização é missão ou valor reconhecido como tornado disponível. Precisa reconhecer Missões simultâneas em um mesmo campo, inclusive Missões de naturezas diferentes, como construção de produto e sustentação editorial cadenciada. Precisa admitir Missões recorrentes ou cadenciadas, não apenas esforços fechados por entrega única. Precisa formular uma prática experimental para extrair Missões de interações humano-agente, usando conversas reais como matéria-prima para identificar tarefas, Missões candidatas, evidências e integrações. Também precisa representar relações entre Missões, tarefas, evidências e aprendizagens quando uma tarefa serve a mais de uma Missão.

## What The Product Should Feel Like

The product should preserve the exploratory shape discovered by Explorer Mode. It should show the user what is happening at the product level, not expose implementation mechanics first.

## Interaction Flow

- User works in Explorer Mode while uncertainty is still alive.
- Explorer surfaces story changes visibly.
- Explorer names attractors and proposes small experiments.
- Explorer proposes Builder handoff only when the user asks or confirms readiness.
- Builder begins only after explicit confirmation.

## Product-Level States

- Exploratory Story active.
- Attractor proposed or accepted.
- Experiment proposal proposed or accepted.
- Builder handoff proposed.

## Acceptance Behavior

- The user can understand what is being proposed without reading implementation details.
- The proposal preserves uncertainty and open questions.
- The proposal gives Builder enough product shape to create roadmap or story plans.

## Explicit Non-Goals

- This document does not define implementation architecture.
- This document does not create delivery tasks by itself.
- This document does not replace Builder planning.

## Open Product Questions

- Which behavior is necessary for the first delivery slice?
- What should remain exploratory after Builder starts?
- What user validation will prove the product behavior works?
