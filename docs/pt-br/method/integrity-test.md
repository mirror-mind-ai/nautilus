# Teste de Inteireza da Missão

O Teste de Inteireza da [Missão](mission.md) verifica se uma Missão está suficientemente formulada antes de avançar.

## Fundamento aristotélico

O teste se apoia, implicitamente, na leitura aristotélica das quatro causas. Ver [Influências aristotélicas](aristotelian-influences.md).

Uma Missão minimamente inteira precisa ter contexto e materialidade suficientes no [Mapa Agêntico](agentic-map.md), forma reconhecível, movimento autorizado e finalidade situada. Ela também precisa ter um contorno de responsabilidade visível que a distingue de uma tarefa. Isso impede que a Missão seja apenas uma intenção vaga, uma tarefa apressada ou uma execução escondida.

## Perguntas do teste

Uma Missão minimamente inteira responde quatro perguntas:

| Causa | Pergunta Nautilus | Função |
| --- | --- | --- |
| Material | Há contexto e materialidade suficientes no [Mapa Agêntico](agentic-map.md) para saber do que a Missão é feita? | Impedir que a Missão fique abstrata demais |
| Formal | Que intenção dirigida está sendo nomeada? | Dar forma reconhecível ao movimento |
| Eficiente | Que movimento está autorizado agora, e a Missão continua sem execução escondida? | Separar formulação de execução prematura |
| Final | Por que essa intenção importa agora? | Situar a finalidade da Missão |

Além dessas quatro perguntas, a versão experimental aplica duas verificações de reconhecimento:

- Method, Protocol, Mirror Extension e Harness conseguem reconhecer os mesmos campos mínimos?
- isso é uma Missão ou é apenas uma tarefa dentro de um quadro assumido?

## Critério de passagem

A Missão passa no teste quando as quatro causas estão suficientemente respondidas, a verificação de reconhecimento comum passa e tudo permanece proporcional à câmara de formulação.

Passar no teste não significa que a Missão foi executada. Significa que ela ganhou forma suficiente para ser reconhecida.

## Critério de falha

A Missão falha quando faltam contexto e materialidade suficientes no [Mapa Agêntico](agentic-map.md), a intenção é vaga, o propósito é ausente, a execução aparece de modo prematuro ou a forma mínima não é reconhecível pelos componentes da família Nautilus.

A falha não é erro moral nem descarte. É informação sobre a forma. A Missão pode ser ajustada até ficar inteira.

## Exemplo mínimo

```yaml
mission:
  id: mission-001
  title: Formulate the first Nautilus mission
  purpose: Prove that Nautilus can name a directed intention before execution.
  status: formulated
```

Leitura pelo teste:

| Causa ou verificação | Resposta |
| --- | --- |
| Material | O contexto mínimo é a primeira câmara de formulação de Missões no método Nautilus, com um artefato YAML simples como materialidade inicial |
| Formal | Formular a primeira Missão Nautilus |
| Eficiente | Apenas formulação está autorizada; o status é `formulated` |
| Final | Provar que Nautilus consegue nomear intenção antes de execução |
| Reconhecimento comum | Sim, os campos mínimos são reconhecíveis |

## Uso humano

O teste deve ser usado como conversa, não como burocracia.

Ele ajuda o [Participante](participant.md) a perceber se já existe forma suficiente para seguir ou se ainda há névoa na intenção.

## Uso agêntico

Um agente pode usar o teste como guarda de fase.

Se o usuário pede execução quando a Missão ainda não está inteira, o agente deve ajudar a formular antes de agir. Se o usuário adiciona detalhes demais, o agente pode separar formulação de execução.

## Fronteira com tarefa

Uma tarefa pode ter intenção, Entrega e Evidência. O Teste de Inteireza não deve tratar esses elementos, sozinhos, como prova de Missão.

Há Missão quando o Participante consegue nomear o contorno de responsabilidade: que Realização está sendo conduzida, por que ela importa agora, quem participa, que movimento está autorizado, o que conta como suficiente e o que talvez precise ser integrado.

## Fronteira

O Teste de Inteireza não aprova plano, não autoriza execução, não valida [Entrega](delivery.md) e não reconhece [Realização](realization.md). Ele pertence à câmara de formulação.
