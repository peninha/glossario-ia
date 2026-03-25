# Roteamento de Agentes

**Agent Routing**

Lógica que decide qual [agente](../agentes-ia/agente.md) especializado deve lidar com cada tarefa ou requisição em um [sistema multiagente](../agentes-ia/sistemas-multiagentes.md). Pode ser determinístico (baseado em regras ou pathfinding em grafo) ou dinâmico (avaliado por [LLM](../ia-generativa/modelos-de-linguagem-grande-porte.md)). Técnicas avançadas incluem *self-healing routing*, que utiliza grafos para encontrar caminhos alternativos automaticamente quando uma rota falha, recorrendo ao LLM apenas quando não há caminho viável. Relaciona-se com [handoff de agentes](../agentes-ia/handoff-de-agentes.md) e [orquestração](../agentes-ia/orquestracao.md).


**Tags:** [`agents`](../tags.md#agents) · [`multiagents`](../tags.md#multiagents)

---

[:material-arrow-left: Voltar para Agentes de IA](index.md){ .md-button }
[📝 Editar este termo](https://github.com/seu-usuario/glossario-ia/edit/main/glossario.yaml){ .md-button .md-button--primary }
