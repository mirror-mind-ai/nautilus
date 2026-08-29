# Missão

## Definição

Uma Missão é uma unidade de realização em condução.

Ela dá forma a um movimento que ainda precisa ser conduzido por Participantes em uma Jornada. Uma Missão não é uma tarefa com nome mais importante. Ela é o contorno de responsabilidade que sustenta valor, autoridade, Participantes, escopo proporcional, possível Entrega, Evidência e Integração antes que uma Realização possa ser reconhecida.

Na versão atual, uma Missão ainda é principalmente formulativa. Ela não executa por si, não atribui papéis completos, não produz Entrega, não coleta Evidência, não marca Realização e não integra aprendizado. Ela nomeia o movimento que pode se tornar trabalho e o torna reconhecível o suficiente para ser conduzido.

## Missão, tarefa e execução

Uma tarefa é uma unidade de execução dentro de um quadro assumido.

Uma tarefa pode ter intenção, Entrega e Evidência. Por exemplo, subir um servidor de documentação tem intenção, uma disponibilidade resultante e uma resposta verificável. Esses elementos, sozinhos, não tornam a tarefa uma Missão. Eles apenas tornam a tarefa bem descrita.

Uma Missão se distingue de uma tarefa porque carrega responsabilidade pelo próprio quadro. Ela pergunta que Realização está sendo conduzida, por que ela importa agora, quem participa, que autoridade está presente, o que conta como avanço suficiente, que Evidência pode sustentar o reconhecimento e que aprendizado deve ser preservado.

Uma Missão pode conter muitas tarefas. Uma tarefa pode servir a mais de uma Missão ao produzir Evidência ou aprendizado para múltiplos campos de responsabilidade. Mas uma tarefa não precisa preservar o sentido inteiro da Jornada para ser executada.

## Missão e Realização

Missão e [Realização](realization.md) não são substâncias separadas. São momentos diferentes do mesmo movimento.

Uma Missão é Realização antes do reconhecimento, enquanto ainda está sendo conduzida. Uma Realização é o reconhecimento de que valor se tornou disponível no [Território Humano](human-territory.md), sustentado por Evidência.

Uma Missão pode falhar, ser abandonada, ser reformulada, gerar Realizações parciais ou revelar que a Realização desejada foi mal nomeada. Por isso, nem toda Missão se torna Realização. Mas toda Missão aponta para uma Realização possível.

## Por que Missão vem antes de execução

Nautilus trata formulação como uma câmara própria.

Em muitos sistemas, a passagem de intenção para tarefa acontece cedo demais. A pessoa sente uma direção, o sistema pede uma ação, o agente começa a produzir. O risco é a execução carregar uma intenção ainda nebulosa.

A Missão impede esse salto. Ela permite que o movimento seja nomeado antes de ser operacionalizado.

## Formas de Missão

Uma Missão não precisa ter uma única saída fechada.

Algumas Missões são construtivas. Elas criam uma nova capacidade, artefato, estrutura ou estado. Por exemplo, criar uma feature de cinemateca em um produto museu é uma Missão construtiva quando a responsabilidade é tornar uma nova capacidade de produto disponível.

Algumas Missões são cadenciadas. Elas preservam um ritmo de geração de valor por meio de movimento curatorial ou operacional repetido. Por exemplo, sustentar um ritmo diário de publicação de peças em um museu é uma Missão cadenciada quando a responsabilidade não é uma peça isolada, mas a disponibilidade contínua de peças curadas com qualidade e coerência suficientes.

Formas diferentes de Missão exigem Evidências diferentes. Uma Missão construtiva pode ser reconhecida por uma nova capacidade funcionando. Uma Missão cadenciada pode ser reconhecida por continuidade com qualidade suficiente ao longo do tempo.

## Campo de Missões

Uma Jornada pode conter Missões simultâneas.

Essas Missões podem ter naturezas diferentes, como trabalho editorial e trabalho de produto. Elas podem compartilhar tarefas, Evidências e aprendizados sem se tornarem a mesma Missão. Uma tarefa de publicação pode avançar uma Missão editorial enquanto revela fricção que informa uma Missão de produto.

O campo de Missões é a relação visível entre Missões ativas, tarefas, Evidências, aprendizados e fronteiras de responsabilidade.

## Forma mínima

A primeira fixture de Missão carrega apenas os campos necessários para reconhecimento de formulação:

```yaml
mission:
  id: mission-001
  title: Formulate the first Nautilus mission
  purpose: Prove that Nautilus can name a directed intention before execution.
  status: formulated
```

## Campos

| Campo | Função |
| --- | --- |
| `id` | Identificador estável da Missão |
| `title` | Nome curto da intenção |
| `purpose` | Razão pela qual a intenção importa agora |
| `status` | Estado mínimo da Missão na câmara atual |

## Status atual

O único status estabilizado nesta fatia é `formulated`.

Isso é deliberado. Outros estados só devem entrar quando a gramática de execução, entrega, evidência e realização for introduzida de modo correspondente nos quatro corpos.

## Missão bem formulada

Uma Missão bem formulada não precisa conter plano completo. Ela precisa tornar legível o movimento.

Ela deve nomear uma intenção dirigida, explicar por que essa intenção importa agora, mostrar o contorno de responsabilidade que a distingue de uma tarefa e permanecer proporcional à câmara de formulação.

## Missão mal formulada

Uma Missão ainda não está inteira quando:

- o título é genérico demais para orientar;
- o propósito não explica relevância situada;
- a intenção é apenas uma tarefa dentro de um quadro assumido;
- o contorno de responsabilidade está escondido;
- a Realização pretendida não pode ser reconhecida;
- a intenção depende de execução escondida;
- o campo `status` promete mais do que a câmara atual reconhece;
- os outros corpos Nautilus não conseguiriam reconhecer os mesmos campos.

## Anti-padrão principal

O principal anti-padrão é contrabandear execução para dentro da formulação.

Exemplo: uma Missão que já contém plano detalhado, atribuição de papéis, critérios finais, evidências e fechamento pode ser valiosa, mas excede a fatia atual. Ela deve ser decomposta ou aguardada até que o método tenha câmaras capazes de sustentá-la.

Um segundo anti-padrão é inflar tarefas em Missões. Uma tarefa grande continua sendo tarefa quando apenas executa uma parte de um quadro. Uma Missão pequena continua sendo Missão quando sustenta responsabilidade por um movimento completo de Realização.

## Prática: Extrair Missões de Interações Humano-Agente

Nautilus pode usar conversas humano-agente como material para formulação de Missões.

A prática [Extrair Missões de Interações Humano-Agente](practices/extract-missions-from-agent-human-interactions.md) observa uma interação real e pergunta se ela contém apenas tarefas ou se uma Missão candidata está emergindo.

Essa prática preserva a natureza conversacional dos ambientes agênticos. O humano não precisa preencher uma ontologia antes de agir. A interação pode ser revisitada, e a Missão pode ser extraída do rastro de intenção, responsabilidade, Entrega, Evidência e Integração.

## Próxima evolução

A próxima evolução da Missão deve esclarecer quando uma Missão formulada se torna pronta para execução e quais campos entram sem quebrar a correspondência entre Method, Protocol, Mirror Extension e Harness.
