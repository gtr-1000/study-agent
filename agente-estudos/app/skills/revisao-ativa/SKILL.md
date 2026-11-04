---
name: revisao-ativa
description: Gera flashcards de recuperação ativa e um quiz de 5 perguntas com gabarito comentado a partir de um material de estudo (texto, resumo, anotações ou tópico detalhado). Use quando a pessoa quiser praticar recuperação ativa, criar flashcards, fazer um quiz ou testar o que aprendeu.
---

# [IMPORTANTE] UTILIZAR ESTA SKILL PARA REVISÃO ATIVA (FLASHCARDS E QUIZ)

Esta skill transforma um material de estudo em um pacote de **recuperação ativa** (*Active Recall*): um conjunto de flashcards (frente e verso) e um quiz de **exatamente 5 perguntas** com gabarito comentado ao final.

## Regra de Ativação (Gating Rule)

Verifique se a conversa já contém a informação obrigatória abaixo:

| # | Informação obrigatória | Exemplo |
|---|---|---|
| 1 | **Material de estudo** (texto colado, resumo, anotações ou descrição clara dos conceitos estudados) | "Aqui está meu resumo sobre closures e escopo léxico em JavaScript: ..." |

* **Se a pessoa pedir flashcards ou quiz sem enviar o material de estudo (ou citar apenas um tema vago, como "faz um quiz"):** **NÃO chame** a ferramenta `load_skill_resource` e não carregue nenhum arquivo de `references/` ou `assets/`. Faça **uma única mensagem**, curta e amigável, pedindo que ela cole o material de estudo (resumo, anotações ou trecho) ou indique os pontos específicos que acabou de estudar.
* **Se o material de estudo estiver presente:** prossiga imediatamente para as instruções abaixo.

## Instruções (apenas depois que o gating for satisfeito)

1. Use a ferramenta `load_skill_resource` para ler `references/workflow.md`.
2. Siga **estritamente** os passos de `references/workflow.md`, que indicam como extrair os conceitos-chave, estruturar os flashcards, elaborar o quiz de 5 perguntas e preencher o `assets/revisao_template.md`.

## Regras gerais

* Responda sempre em **português do Brasil**, num tom de mentor: direto, encorajador e focado em testar a compreensão real (não apenas memorização mecânica).
* Baseie os flashcards e as perguntas **no material fornecido**, evitando cobrar tópicos que não foram abordados no material.
* O quiz deve ter **exatamente 5 perguntas**, combinando compreensão conceitual e aplicação prática.
