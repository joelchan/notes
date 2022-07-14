---
title: [[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?
url: https://roamresearch.com/#/app/megacoglab/page/y33fB8TjN
author: Joel Chan
date: Wed Nov 10 2021 09:37:39 GMT-0500 (Eastern Standard Time)
---

- # Synthesis

    - [[[[CLM]] - [[transformer language model]]s have some analogical reasoning ability]]
- ---
- # Sources

    - [[@bommasaniOpportunitiesRisksFoundation2021]]

    - [[@brownLanguageModelsAre2020]]

    - analogy-making

    - more about prompting

        - [[@reynoldsPromptProgrammingLarge2021a]] - CHI poster that explores the conditions under which zero-shot prompting may be better than few- or n-shot (only explores French-to-English translation though)

        - [[@liuPretrainPromptPredict2021]] - systematic survey of methods

        - Reframing Instructional Prompts to GPTk’s Language: https://arxiv.org/pdf/2109.07830.pdf

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FYj-mRZEIWL.png?alt=media&token=cd44c0a6-e30d-40f0-8d8a-8bc44cb11213)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FbEntv-u_pj.png?alt=media&token=ec1e7ba1-4bcf-4ff4-a19d-7d7e0a6b8714)

            - [[prompt programming]]

        - New model! [[sys/T0]] directly optimizes for multitask prompt learning, and outperforms [[sys/GPT-3]] with 16x fewer params! (also available on [[huggingface]])

            - https://twitter.com/srush_nlp/status/1450539883081179139?s=20

            - https://twitter.com/mark_riedl/status/1450273843008974856?s=20

    - [[@clarkAllThatHuman2021]] - recent study asking non-experts to compare human- and machine-generated text ([[sys/GPT-2]] and [[sys/GPT-3]]) for stories, news articles, and recipes
- ---
- # Meta

    - Tags:
- Pulling on this thread [[@bommasaniOpportunitiesRisksFoundation2021]] for [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] |
- Collecting some other papers on [[prompt programming]]
- Maybe more here also from [[org/Ought]]'s reading list: https://docs.google.com/document/d/1Z1mQ47FqzNBzNvalWgSnyGph7A4Q7MndOEqsqv_mto0/edit#heading=h.4khaz12c49ll
- And some good video explainers/discussion of [[@brownLanguageModelsAre2020]] and [[sys/GPT-3]]

    - WE GOT ACCESS TO GPT-3! (With [[Gary Marcus]], Walid Saba and [[Connor Leahy]]) - YouTube: https://www.youtube.com/watch?v=iccd86vOz3w

        - Note: [[Connor Leahy]] is the guy who recreated GPT-3 when OpenAI was still going back and forth about releasing the models

        - Connor mentions at ~01:31:40 that [[sys/GPT-3]] does surprisingly well at poems, and poorly at math, and he suspects it's because of "the BPE" thing

            - Digging, this is [[Byte-Pair Encoding (BPE)]], which I got from here: The GPT-3 Architecture, on a Napkin: https://dugas.ch/artificial_curiosity/GPT_architecture.html

                - > For efficiency, GPT-3 actually uses byte-level Byte Pair Encoding (BPE) tokenization. What this means is that "words" in the vocabulary are not full words, but groups of characters (for byte-level BPE, bytes) which occur often in text. Using the GPT-3 Byte-level BPE tokenizer, "Not all heroes wear capes" is split into tokens "Not" "all" "heroes" "wear" "cap" "es", which have ids 3673, 477, 10281, 5806, 1451, 274 in the vocabulary. [Here](https://huggingface.co/transformers/tokenizer_summary.html) is a very good introduction to the subject, and a [github implementation](https://github.com/huggingface/tokenizers) so you can try it yourself.

                - And links to this: https://huggingface.co/transformers/tokenizer_summary.html#byte-pair-encoding

                    - Which is... really really interesting. the base tokens aren't actually words, but byte (character) groups

    - GPT-3: Language Models are Few-Shot Learners (Paper Explained) - YouTube: https://www.youtube.com/watch?v=SY5PvZrJhLE
- Title:: The Illustrated Transformer [[@alammarIllustratedTransformer]]
- [[@branwenGPT3CreativeFiction2020]] GPT-3 Creative Fiction · Gwern.net: https://www.gwern.net/GPT-3#prompts-as-programming
- [[@lescaoHowManyData2021]] how many data points is a prompt worth? "prompting is often worth 100s of data points on average across classification tasks"

###### Discourse Context

- **Informed By::** [EVD - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes - @clarkAllThatHuman2021.md](EVD - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes - @clarkAllThatHuman2021.md)
- **Informed By::** [CLM - transformer language models have some analogical reasoning ability.md](CLM - transformer language models have some analogical reasoning ability.md)
- **Informed By::** [@alammarIllustratedTransformer.md](@alammarIllustratedTransformer.md)
- **Informed By::** [@reynoldsPromptProgrammingLarge2021a.md](@reynoldsPromptProgrammingLarge2021a.md)
- **Informed By::** [@brownLanguageModelsAre2020.md](@brownLanguageModelsAre2020.md)
- **Informed By::** [@liuPretrainPromptPredict2021.md](@liuPretrainPromptPredict2021.md)
- **Informed By::** [@branwenGPT3CreativeFiction2020.md](@branwenGPT3CreativeFiction2020.md)
- **Informed By::** [@bommasaniOpportunitiesRisksFoundation2021.md](@bommasaniOpportunitiesRisksFoundation2021.md)
- **Informed By::** [@lescaoHowManyData2021.md](@lescaoHowManyData2021.md)
- **Informed By::** [@clarkAllThatHuman2021.md](@clarkAllThatHuman2021.md)

