# OpenClaw

**OpenClaw**

Framework e sistema operacional open-source para [agentes de IA](../agentes-ia/agente-de-ia.md) autônomos. Adota a filosofia *Markdown-as-Config*: identidade, [memória](../agentes-ia/memoria-e-contexto.md) e comportamento do agente são definidos em arquivos Markdown (SOUL.md, AGENTS.md, MEMORY.md), sem necessidade de código personalizado. A arquitetura se baseia em um *Gateway* daemon que gerencia ciclos de vida dos agentes, roteamento de canais e [estado](../agentes-ia/estado.md) de sessão, funcionando como o kernel do sistema operacional agêntico. Executa o [loop de agente](../agentes-ia/loop-de-agente.md) de forma serializada por sessão, integra-se ao [MCP](../infraestrutura-processos/mcp.md) e conecta-se a canais como Slack, Discord e Telegram.


**Tags:** [`agents`](../tags.md#agents) · [`workflow`](../tags.md#workflow)

---

[:material-arrow-left: Voltar para Infraestrutura e Processos](index.md){ .md-button }
[📝 Editar este termo](https://github.com/seu-usuario/glossario-ia/edit/main/glossario.yaml){ .md-button .md-button--primary }
