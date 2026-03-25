# Chamada de Ferramentas

**Tool Calling** · *Function Calling*

Mecanismo que permite a um [LLM](../ia-generativa/modelos-de-linguagem-grande-porte.md) propor [ações](../agentes-ia/acoes.md) estruturadas (geralmente em JSON) em vez de apenas gerar texto. O modelo "escolhe" qual função chamar e com quais parâmetros, e um orquestrador executa a chamada e devolve o resultado. Existem dois padrões: nativo da API (como OpenAI `tools` e Anthropic `tool_use`, com schemas JSON) e in-band (descrições de [ferramentas](../agentes-ia/ferramentas.md) inseridas diretamente no [prompt](../ia-generativa/prompt.md)). É o mecanismo central que viabiliza o [loop de agente](../agentes-ia/loop-de-agente.md).


**Tags:** [`agents`](../tags.md#agents) · [`workflow`](../tags.md#workflow)

---

[:material-arrow-left: Voltar para Agentes de IA](index.md){ .md-button }
[📝 Editar este termo](https://github.com/seu-usuario/glossario-ia/edit/main/glossario.yaml){ .md-button .md-button--primary }
