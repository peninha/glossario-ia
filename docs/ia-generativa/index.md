# Conceitos Relacionados à IA Generativa

Conceitos específicos da inteligência artificial generativa e modelos de linguagem

## Termos nesta categoria

<div class="grid cards" markdown>

- **[Ajuste Fino](ajuste-fino.md)**

    *Fine-Tuning*

    Etapa em que o [modelo](../conceitos-fundamentais/modelo.md) é refinado com [dados](../conceitos-fundamentais/dados.md) específicos, adaptando-o a tarefas ou contextos particulares.

- **[Ajuste por Instrução](ajuste-por-instrucao.md)**

    *Instruction Tuning*

    Técnica para treinar [modelos](../conceitos-fundamentais/modelo.md) a seguirem melhor instruções dadas em linguagem natural.

- **[Alucinação](alucinacao.md)**

    *Hallucination*

    Quando um [modelo](../conceitos-fundamentais/modelo.md) generativo cria informações falsas ou inventadas que parecem plausíveis.

- **[Aprendizado por Reforço com Feedback Humano](aprendizado-por-reforco-com-feedback-humano.md)**

    *Reinforcement Learning from Human Feedback* · `RLHF`

    Método de alinhar [modelos](../conceitos-fundamentais/modelo.md) generativos às preferências humanas, usando reforço baseado em feedback de avaliadores.

- **[Dados Sintéticos](dados-sinteticos.md)**

    *Synthetic Data*

    [Dados](../conceitos-fundamentais/dados.md) gerados artificialmente a partir de [modelos](../conceitos-fundamentais/modelo.md) de IA, diferentes de dados gerados por humanos.

- **[Destilação](destilacao.md)**

    *Distillation*

    Técnica que treina uma IA aluna menor a imitar uma IA professor maior, usando os [dados sintéticos](../ia-generativa/dados-sinteticos.md) gerados pela IA professor. Resultado: [modelo](../conceitos-fundamentais/modelo.md) mais leve e rápido, com boa parte do desempenho preservado.

- **[Vetorização Semântica](embeddings.md)**

    *Embeddings*

    Representação matemática de palavras, frases ou documentos em vetores, permitindo que [modelos](../conceitos-fundamentais/modelo.md) entendam relações semânticas entre eles.

- **[Redes Adversárias Generativas](gans.md)**

    *Generative Adversarial Networks* · `GANs`

    [Modelos](../conceitos-fundamentais/modelo.md) que usam duas [redes neurais](../conceitos-fundamentais/redes-neurais-artificiais.md) em competição (gerador e discriminador) para criar conteúdos melhores.

- **[IA Generativa](ia-generativa.md)**

    *Generative AI*

    Área da IA voltada para a criação de novos conteúdos — textos, imagens, sons, vídeos — a partir de padrões aprendidos em grandes volumes de [dados](../conceitos-fundamentais/dados.md).

- **[Janela de Contexto](janela-de-contexto.md)**

    *Context Window*

    Limite máximo de [tokens](../ia-generativa/token.md) (palavras, caracteres) que um [modelo de linguagem](../ia-generativa/modelos-de-linguagem.md) pode processar em uma única interação. Determina quanto texto o modelo "lembra" durante a conversa e afeta diretamente o custo computacional e a qualidade das respostas.

- **[Mistura de Especialistas](mixture-of-experts.md)**

    *Mixture of Experts* · `MoE`

    Arquitetura em que vários "especialistas" (sub-redes) coexistem e um roteador escolhe apenas alguns para cada entrada/[token](../ia-generativa/token.md). Isso permite um [modelo](../conceitos-fundamentais/modelo.md) grande (com muitos [parâmetros](../conceitos-fundamentais/parametro.md)) rodar com um custo de computação menor.

- **[Modelos de Difusão](modelos-de-difusao.md)**

    *Diffusion Models*

    [Modelos](../conceitos-fundamentais/modelo.md) de IA usados na geração de imagens, que criam figuras a partir de ruído, refinando-as progressivamente até se tornarem claras. Recentemente, modelos de difusão começaram a ser usados para geração de texto também.

- **[Modelos de Linguagem](modelos-de-linguagem.md)**

    *Language Models* · `LMs`

    [Modelos](../conceitos-fundamentais/modelo.md) capazes de compreender e gerar texto em linguagem natural.

- **[Modelos de Linguagem de Grande Porte](modelos-de-linguagem-grande-porte.md)**

    *Large Language Models* · `LLMs`

    [Modelos de linguagem](../ia-generativa/modelos-de-linguagem.md) com bilhões de [parâmetros](../conceitos-fundamentais/parametro.md), capazes de compreender e gerar texto em linguagem natural com alta qualidade. Exemplos: GPT-4, Claude, LLaMA. Requerem infraestrutura computacional significativa para [treinamento](../conceitos-fundamentais/treinamento.md) e [inferência](../conceitos-fundamentais/inferencia.md).

- **[Modelos de Linguagem de Pequeno Porte](modelos-de-linguagem-pequeno-porte.md)**

    *Small Language Models* · `SLMs`

    [Modelos de linguagem](../ia-generativa/modelos-de-linguagem.md) com menos [parâmetros](../conceitos-fundamentais/parametro.md) (milhões a poucos bilhões), otimizados para eficiência computacional e execução em dispositivos com recursos limitados. Equilibram qualidade e velocidade para aplicações específicas.

- **[Modelos de Raciocínio](modelos-de-raciocinio.md)**

    *Reasoning Models*

    [Modelos de linguagem](../ia-generativa/modelos-de-linguagem.md) que podem realizar tarefas de raciocínio complexo por meio de técnicas como [cadeia-de-pensamento](../habilidades-praticas/cadeia-de-pensamento.md) e [auto-reflexão](../habilidades-praticas/auto-reflexao.md) que produzem uma série de [tokens](../ia-generativa/token.md) internos, que são então usados para gerar a resposta final. O modelo utiliza mais tempo de computação para gerar respostas mais precisas para tarefas complexas.

- **[Modelos Multimodais](modelos-multimodais.md)**

    *Multimodal Models*

    Sistemas de IA capazes de processar e gerar múltiplos tipos de [dados](../conceitos-fundamentais/dados.md) simultaneamente (texto, imagem, áudio, vídeo). Permitem tarefas como descrição de imagens, geração de conteúdo baseado em diferentes mídias e compreensão contextual rica.

- **[Prompt](prompt.md)**

    *Prompt*

    A entrada (pergunta, instrução ou comando) que o usuário fornece para que o [modelo](../conceitos-fundamentais/modelo.md) generativo produza uma resposta.

- **[Quantização](quantizacao.md)**

    *Quantization*

    Reduz a precisão numérica de [pesos](../conceitos-fundamentais/pesos-e-vieses.md)/ativações (ex.: 16→8→4 bits) para economizar **memória, custo e tempo de [inferência](../conceitos-fundamentais/inferencia.md)**. Pequena perda de acurácia é comum.

- **[Geração Aumentada por Recuperação](rag.md)**

    *Retrieval-Augmented Generation* · `RAG`

    Técnica que combina geração de texto com recuperação de informações em bases externas (ex.: documentos, web, bancos de dados), aumentando a precisão das respostas.

- **[Speech to Text](speech-to-text.md)**

    *Speech to Text* · `STT`

    Tecnologia que converte fala humana em texto escrito, permitindo que sistemas de IA compreendam comandos de voz, transcrevam conversas e facilitem a interação por voz. Base da tecnologia de reconhecimento de fala.

- **[Text to Speech](text-to-speech.md)**

    *Text to Speech* · `TTS`

    Tecnologia que converte texto escrito em fala natural, permitindo que sistemas de IA "falem" com entonação, ritmo e pronúncia humanas. Usada em assistentes virtuais, audiobooks e acessibilidade.

- **[Token](token.md)**

    *Token*

    Unidade mínima em que o texto é dividido para processamento. Pode ser uma palavra, parte dela ou até um caractere.

- **[Transformer](transformer.md)**

    *Transformer*

    Arquitetura de [rede neural](../conceitos-fundamentais/redes-neurais-artificiais.md) que revolucionou a [IA generativa](../ia-generativa/ia-generativa.md), permitindo o processamento eficiente de sequências longas de [dados](../conceitos-fundamentais/dados.md).

- **[Treinamento Prévio](treinamento-previo.md)**

    *Pretraining*

    Fase inicial em que o [modelo](../conceitos-fundamentais/modelo.md) aprende padrões gerais da linguagem ou de imagens a partir de enormes conjuntos de [dados](../conceitos-fundamentais/dados.md).

</div>

**Total de termos:** 25

