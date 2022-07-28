---
title: [[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?
url: https://roamresearch.com/#/app/megacoglab/page/y33fB8TjN
author: Joel Chan
date: Wed Nov 10 2021 22:37:39 GMT+0800 (Malaysia Time)
---

- # Synthesis

    - [[CLM - transformer language models have some analogical reasoning ability]]
- ---
- # Sources

    - [[@bommasaniOpportunitiesRisksFoundation2021]]

    - [[@brownLanguageModelsAre2020]]

    - analogy-making

    - more about prompting

        - [[@reynoldsPromptProgrammingLarge2021a]]

        - [[@liuPretrainPromptPredict2021]]

        - Reframing Instructional Prompts to GPTk’s Language: https://arxiv.org/pdf/2109.07830.pdf

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FYj-mRZEIWL.png?alt=media&token=cd44c0a6-e30d-40f0-8d8a-8bc44cb11213)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FbEntv-u_pj.png?alt=media&token=ec1e7ba1-4bcf-4ff4-a19d-7d7e0a6b8714)

            - [[prompt programming]]

        - New model! [[sysT0]]

            - https://twitter.com/srush_nlp/status/1450539883081179139?s=20

            - https://twitter.com/mark_riedl/status/1450273843008974856?s=20

    - [[@clarkAllThatHuman2021]]
- ---
- # Meta

    - Tags:
- Pulling on this thread [[@bommasaniOpportunitiesRisksFoundation2021]]
- Collecting some other papers on [[prompt programming]]
- Maybe more here also from [[orgOught]]
- And some good video explainers/discussion of [[@brownLanguageModelsAre2020]]

    - WE GOT ACCESS TO GPT-3! (With [[Gary Marcus]]

        - Note: [[Connor Leahy]]

        - Connor mentions at ~01:31:40 that [[sysGPT-3]]

            - Digging, this is [[Byte-Pair Encoding (BPE)]]

                - > For efficiency, GPT-3 actually uses byte-level Byte Pair Encoding (BPE) tokenization. What this means is that "words" in the vocabulary are not full words, but groups of characters (for byte-level BPE, bytes) which occur often in text. Using the GPT-3 Byte-level BPE tokenizer, "Not all heroes wear capes" is split into tokens "Not" "all" "heroes" "wear" "cap" "es", which have ids 3673, 477, 10281, 5806, 1451, 274 in the vocabulary. [Here](https://huggingface.co/transformers/tokenizer_summary.html) is a very good introduction to the subject, and a [github implementation](https://github.com/huggingface/tokenizers) so you can try it yourself.

                - And links to this: https://huggingface.co/transformers/tokenizer_summary.html#byte-pair-encoding

                    - Which is... really really interesting. the base tokens aren't actually words, but byte (character) groups

    - GPT-3: Language Models are Few-Shot Learners (Paper Explained) - YouTube: https://www.youtube.com/watch?v=SY5PvZrJhLE
- Title:: The Illustrated Transformer [[@alammarIllustratedTransformer]]
- [[@branwenGPT3CreativeFiction2020]]
- [[@lescaoHowManyData2021]]

###### Discourse Context

- **Informed By::** [[EVD - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes - @clarkAllThatHuman2021]]
- **Informed By::** [[CLM - transformer language models have some analogical reasoning ability]]
- **Informed By::** [[@alammarIllustratedTransformer]]
- **Informed By::** [[@reynoldsPromptProgrammingLarge2021a]]
- **Informed By::** [[@brownLanguageModelsAre2020]]
- **Informed By::** [[@liuPretrainPromptPredict2021]]
- **Informed By::** [[@branwenGPT3CreativeFiction2020]]
- **Informed By::** [[@bommasaniOpportunitiesRisksFoundation2021]]
- **Informed By::** [[@lescaoHowManyData2021]]
- **Informed By::** [[@clarkAllThatHuman2021]]
