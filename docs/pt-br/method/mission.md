# Missão

## Definição

Uma Missão é uma intenção nomeada de [realização](realization.md).

Ela reúne uma direção antes que Nautilus tente agir. Nesta versão, uma Missão não executa, atribui papéis, produz [entrega](delivery.md), coleta [evidência](evidence.md), marca realização ou integra aprendizado. Ela apenas dá forma ao movimento que pode se tornar trabalho.

## Por que Missão vem antes de execução

Nautilus trata formulação como uma câmara própria.

Em muitos sistemas, a passagem de intenção para tarefa acontece cedo demais. A pessoa sente uma direção, o sistema pede uma ação, o agente começa a produzir. O risco é a execução carregar uma intenção ainda nebulosa.

A Missão impede esse salto. Ela permite que o movimento seja nomeado antes de ser operacionalizado.

## Forma mínima

A primeira Mission fixture carrega apenas os campos necessários para reconhecimento de formulação:

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

Ela deve nomear uma intenção dirigida, explicar por que essa intenção importa agora e permanecer proporcional à câmara de formulação.

## Missão mal formulada

Uma Missão ainda não está inteira quando:

- o título é genérico demais para orientar;
- o propósito não explica relevância situada;
- a intenção depende de execução escondida;
- o campo `status` promete mais do que a câmara atual reconhece;
- os outros corpos Nautilus não conseguiriam reconhecer os mesmos campos.

## Anti-padrão principal

O principal anti-padrão é contrabandear execução para dentro da formulação.

Exemplo: uma Missão que já contém plano detalhado, atribuição de papéis, critérios finais, evidências e fechamento pode ser valiosa, mas excede a fatia atual. Ela deve ser decomposta ou aguardada até que o método tenha câmaras capazes de sustentá-la.

## Próxima evolução

A próxima evolução da Missão deve esclarecer quando uma Missão formulada se torna pronta para execução e quais campos entram sem quebrar a correspondência entre Method, Protocol, Mirror Extension e Harness.
