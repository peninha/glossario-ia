# Agentes de IA

Conceitos relacionados a sistemas de IA que atuam como agentes autônomos

## Termos nesta categoria

<div class="grid cards" markdown>

- **[Ações](acoes.md)**

    *Actions*

    O que o [agente](../agentes-ia/agente.md) pode fazer: responder em texto, clicar/navegar, chamar ferramentas (APIs), executar código, mover atuadores (no caso de robôs).

- **[Agente](agente.md)**

    *Agent*

    Sistema que percebe o [ambiente](../agentes-ia/ambiente.md), decide e age para atingir [objetivos](../agentes-ia/objetivo.md). Pode ser puramente digital (bot, assistente) ou físico (robô). Opera no ciclo *perceber → decidir → agir*.

- **[Agente Autônomo](agente-autonomo.md)**

    *Autonomous Agent*

    Sistema de IA que opera independentemente com mínima supervisão humana, tomando decisões e executando [ações](../agentes-ia/acoes.md) baseadas em seus [objetivos](../agentes-ia/objetivo.md) e percepções do [ambiente](../agentes-ia/ambiente.md). Pode aprender e adaptar-se a mudanças, mas mantém limites de segurança e conformidade definidos por humanos.

- **[Agente de Código](agente-de-codigo.md)**

    *Coding Agent* · `SWE Agent`

    [Agente](../agentes-ia/agente.md) especializado em engenharia de software que autonomamente lê documentação, escreve código, executa testes e faz debug. Exemplos: Claude Code, GitHub Copilot Agent, Cursor Agent, Devin e OpenHands.

- **[Agente de Navegador](agente-de-navegador.md)**

    *Browser Agent*

    [Agente](../agentes-ia/agente.md) de IA que automatiza a navegação web, compreendendo conteúdo de páginas e executando workflows multi-etapa. Exemplos: OpenAI Operator, Google Project Mariner, Perplexity Comet.

- **[Ambiente](ambiente.md)**

    *Environment*

    O contexto onde o [agente](../agentes-ia/agente.md) atua (tudo que está "fora" dele). Pode ser totalmente ou parcialmente observável, determinístico ou estocástico, estático ou dinâmico.

- **[Autonomia e Supervisão Humana](autonomia-e-supervisao-humana.md)**

    *Human-in-the-Loop* · `HITL`

    Definição de níveis de autonomia, checkpoints de aprovação, trilhas de auditoria e limites de escopo para segurança, conformidade e alinhamento com [objetivos](../agentes-ia/objetivo.md) humanos.

- **[Chamada de Ferramentas](chamada-de-ferramentas.md)**

    *Tool Calling* · `Function Calling`

    Mecanismo que permite a um [LLM](../ia-generativa/modelos-de-linguagem-grande-porte.md) propor [ações](../agentes-ia/acoes.md) estruturadas (JSON) em vez de apenas gerar texto. O modelo "escolhe" qual função chamar e com quais parâmetros.

- **[Enxame](enxame.md)**

    *Swarm*

    Abordagem multiagente inspirada em inteligência de enxame (formigas, abelhas, cardumes), em que muitos [agentes](../agentes-ia/agente.md) simples cooperam com regras locais para resolver problemas. Utiliza mecanismos como votação, leilão de tarefas, sinais/"feromônios" virtuais e difusão de mensagens para convergência.

- **[Estado](estado.md)**

    *State*

    Representação do que é relevante no momento para decidir. Pode ser o próprio contexto de um [LLM](../ia-generativa/modelos-de-linguagem-grande-porte.md), uma memória de curto prazo ou um "estado oculto" quando parte do [ambiente](../agentes-ia/ambiente.md) não é observável.

- **[Exploração vs. Aproveitamento](exploracao-vs-aproveitamento.md)**

    *Exploration vs. Exploitation*

    Dilema fundamental em [aprendizado por reforço](../conceitos-fundamentais/aprendizado-por-reforco.md): explorar novas [ações](../agentes-ia/acoes.md) para descobrir melhores [recompensas](../agentes-ia/recompensa.md) ou aproveitar o conhecimento atual para maximizar o retorno conhecido.

- **[Ferramentas](ferramentas.md)**

    *Tools*

    Conectores e interfaces externas que um [agente](../agentes-ia/agente.md) pode acionar para ampliar suas capacidades: calculadora, navegação e busca web, [RAG](../ia-generativa/rag.md)/bases de conhecimento, planilhas e bancos de dados, interpretador/execução de código, automações e serviços de terceiros, além de atuadores físicos (robótica).

- **[Habilidades de Agente](habilidades-de-agente.md)**

    *Agent Skills*

    Capacidades reutilizáveis e instaláveis que estendem o repertório de um [agente](../agentes-ia/agente.md) além de suas [ferramentas](../agentes-ia/ferramentas.md) básicas, encapsulando comportamentos completos com instruções, contexto e lógica.

- **[Handoff de Agentes](handoff-de-agentes.md)**

    *Agent Handoff*

    Transferência de controle entre [agentes](../agentes-ia/agente.md) especializados em [sistemas multiagentes](../agentes-ia/sistemas-multiagentes.md). Quando um agente determina que outra especialidade é necessária, ele passa a tarefa e o contexto para o agente adequado.

- **[Loop de Agente](loop-de-agente.md)**

    *Agent Loop*

    Ciclo fundamental por trás de todo [agente](../agentes-ia/agente.md): enviar contexto ao modelo → verificar chamadas de [ferramentas](../agentes-ia/ferramentas.md) → executar → realimentar → repetir. É o padrão canônico de todos os frameworks agênticos.

- **[Memória e Contexto](memoria-e-contexto.md)**

    *Memory and Context*

    Mecanismos para manter continuidade: [janela de contexto](../ia-generativa/janela-de-contexto.md) (curto prazo), memória vetorial/BD (longo prazo) e logs. Ajudam a não "recomeçar do zero" a cada passo.

- **[Objetivo](objetivo.md)**

    *Goal*

    Define o que o [agente](../agentes-ia/agente.md) busca e orienta suas decisões e [ações](../agentes-ia/acoes.md). Exemplos: "responder ao cliente", "navegar até um destino", "resolver um problema matemático". O objetivo serve como bússola para o comportamento do agente.

- **[Observações](observacoes.md)**

    *Observations* · `Percepção`

    Informações que o [agente](../agentes-ia/agente.md) recebe do [ambiente](../agentes-ia/ambiente.md): texto de usuários, páginas web, leituras de sensores, respostas de APIs etc. Servem de base para decidir a próxima [ação](../agentes-ia/acoes.md).

- **[Orquestração](orquestracao.md)**

    *Orchestration* · `Planner-Executor, Críticos, Supervisores`

    Coordenação de múltiplos [agentes](../agentes-ia/agente.md) ou componentes com papéis especializados: planejadores que definem estratégias, executores que realizam [ações](../agentes-ia/acoes.md), críticos que avaliam resultados e supervisores que mantêm controle geral.

- **[Persona ou Papel](persona-ou-papel.md)**

    *Role*

    Configuração que define estilo, tom, personalidade e características de um [agente](../agentes-ia/agente.md). (ex.: "tutor paciente", "analista jurídico cauteloso").

- **[Planejamento](planejamento.md)**

    *Planning*

    Escolha de sequências de [ações](../agentes-ia/acoes.md) para alcançar [objetivos](../agentes-ia/objetivo.md).

- **[Política](politica.md)**

    *Policy*

    Regra que mapeia [estados](../agentes-ia/estado.md)/[observações](../agentes-ia/observacoes.md) em [ações](../agentes-ia/acoes.md). Pode ser uma [rede neural](../conceitos-fundamentais/redes-neurais-artificiais.md) treinada, um conjunto de regras ou um [prompt](../ia-generativa/prompt.md) que orienta decisões de um [LLM](../ia-generativa/modelos-de-linguagem-grande-porte.md)-agente.

- **[Recompensa](recompensa.md)**

    *Reward*

    Sinal (geralmente numérico) que indica sucesso parcial ou total — comum em [aprendizado por reforço](../conceitos-fundamentais/aprendizado-por-reforco.md). Exemplo: nota ao concluir uma tarefa.

- **[Roteamento de Agentes](roteamento-de-agentes.md)**

    *Agent Routing*

    Lógica que decide qual [agente](../agentes-ia/agente.md) especializado deve lidar com cada tarefa em um [sistema multiagente](../agentes-ia/sistemas-multiagentes.md). Pode ser determinístico (regras/grafos) ou dinâmico (avaliado por LLM).

- **[Sistemas Multiagentes](sistemas-multiagentes.md)**

    *Multi-Agent Systems* · `MAS`

    Vários [agentes](../agentes-ia/agente.md) cooperando com papéis complementares (ex.: pesquisador, redator, revisor). Exigem protocolos de comunicação e estratégias de coordenação.

- **[Uso de Computador](uso-de-computador.md)**

    *Computer Use*

    Capacidade de [agentes](../agentes-ia/agente.md) de IA interagirem com interfaces gráficas como um humano: movendo o mouse, clicando, digitando e lendo a tela. Inaugurado pela Anthropic em outubro/2024.

</div>

**Total de termos:** 26

