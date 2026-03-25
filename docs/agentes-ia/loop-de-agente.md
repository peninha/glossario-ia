# Loop de Agente

**Agent Loop**

Ciclo fundamental que sustenta todo [agente](../agentes-ia/agente.md) de IA: enviar [observações](../agentes-ia/observacoes.md) e contexto ao [modelo](../conceitos-fundamentais/modelo.md) → verificar se a resposta contém [chamadas de ferramentas](../agentes-ia/chamada-de-ferramentas.md) → executar as ferramentas → realimentar o modelo com os resultados → repetir até que a tarefa esteja concluída. É o padrão arquitetural canônico sobre o qual frameworks como LangGraph, OpenAI Agents SDK e [OpenClaw](../infraestrutura-processos/openclaw.md) convergem.


**Tags:** [`agents`](../tags.md#agents) · [`workflow`](../tags.md#workflow)

---

[:material-arrow-left: Voltar para Agentes de IA](index.md){ .md-button }
[📝 Editar este termo](https://github.com/seu-usuario/glossario-ia/edit/main/glossario.yaml){ .md-button .md-button--primary }
