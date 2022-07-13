---
title: @reynoldsPromptProgrammingLarge2021
url: https://roamresearch.com/#/app/megacoglab/page/osjzDlWxb
author: Joel Chan
date: Sun May 02 2021 23:56:03 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm

    - Meta:

        - Authored by:: [[Laria Reynolds]] [[Kyle McDonell]]

        - Year: [[2021]]

        - Publication: arXiv:2102.07350 [cs]

        - Zotero link: [Zotero Link](zotero://select/items/7_54CF96FW)

        - URL: [Reynolds & McDonell (2021). Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm. arXiv:2102.07350 [cs]](http://arxiv.org/abs/2102.07350)

    - Content

        - Abstract

            - Prevailing methods for mapping large generative language models to supervised tasks may fail to sufficiently probe models' novel capabilities. Using GPT-3 as a case study, we show that ^^0-shot prompts can significantly outperform few-shot prompts^^. We suggest that the function of few-shot examples in these cases is better described as locating an already learned task rather than meta-learning. This analysis motivates rethinking the role of prompts in controlling and evaluating powerful language models. In this work, we discuss methods of [[prompt programming]], emphasizing the usefulness of considering prompts through the lens of natural language. We explore techniques for exploiting the capacity of narratives and cultural anchors to encode nuanced intentions and techniques for encouraging deconstruction of a problem into components before producing a verdict. Informed by this more encompassing theory of prompt programming, we also introduce the idea of a metaprompt that seeds the model to generate its own natural language prompts for a range of tasks. Finally, we discuss how these more general methods of interacting with language models can be incorporated into existing and future benchmarks and practical applications.
- 

###### Discourse Context



###### References

[[September 29th, 2021]]

- Possible starting point: [[@reynoldsPromptProgrammingLarge2021]]

    - This could also spin off into a separate study on [[Human-AI Interaction]] for [[few-shot learning]] in systems like [[sys/Elicit]]
[[November 10th, 2021]]

- Thinking in particular of playing more with natural language prompts and templates, rather than adding more examples, riffing off of [[@reynoldsPromptProgrammingLarge2021]]

    - [[@teamWorldCreationAnalogy2020]] also found similar things in their experimentation (better results with natural language prompt)
[[November 18th, 2021]]

- read [[@reynoldsPromptProgrammingLarge2021]]: prompt programming

    - examples may not always help: the semantic meanings of examples may be seen as task instructions

        - in general, examples are more efficient and informative in context, both from the perspective of a human and a language model

        - a prompt could embed examples in a context which makes it clear that the examples are independent instances of a function rather than a sequential pattern that should be extrapolated

    - prompts are for task location: rather than learning how to perform the task from the examples, the examples may simply serve to instruct GPT-3 on what task it is to solve and encourage it to follow the structure of the prompt in its response.

    - treat GPT-3 as human writers: prompts could be improved by simple changes in formatting which make the prompt closer to natural language as a human would write it

        - GPT-3's resemblance not to a single human author but a superposition of authors, which motivates a subtractive approach to prompt programming

    - the more redundancy reinforcing the desired behavior the better, as is arguably demonstrated by the effectiveness of the few-shot format

    - GPT-3 demonstrates nuanced understanding of analogies [World Creation by Analogy](https://aidungeon.medium.com/world-creation-by-analogy-f26e3791d35f)

    - it is helpful to approach prompt programming from the perspective of constraining behavior: we want a prompt that is not merely consistent with the desired continuation, but inconsistent with undesired continuations

    - serial reasoning: it is reasonable to expect that some tasks may be too difficult to compute in a single pass but solvable if broken up into individually tractable sub-tasks [GPT-3 Creative Fiction](https://www.gwern.net/GPT-3)

        - Q: shall we try to use GPT-3 for "sequential" problem reframing and solving? Although it doesn't support human-in-the-loop, but it's worth a try. #[[➰ breadcrumbs]]

    - metaprompt programming: serializing metaprompt (metaprompts are bold)

        - example 1 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FJLt2HTmdTk.png?alt=media&token=62487913-03ff-46b8-94f0-56508038ade6)

        - example 2![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FlwP8goVr93.png?alt=media&token=af4b1e0f-4700-4fed-9f1e-16ed26680ffd)
[[March 31st, 2022]]

- we might replicate/extend [[@reynoldsPromptProgrammingLarge2021]]

    - {{[[TODO]]}} evidence note [[@reynoldsPromptProgrammingLarge2021]]
