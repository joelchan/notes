---
title: @clarkAllThatHuman2021
url: https://roamresearch.com/#/app/megacoglab/page/RPAPEO0TQ
author: Joel Chan
date: Wed Dec 01 2021 10:48:39 GMT-0500 (Eastern Standard Time)
---

- Title:: All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text
- Author(s):: [[Elizabeth Clark]], [[Tal August]], [[Sofia Serrano]], [[Nikita Haduong]], [[Suchin Gururangan]], [[Noah A. Smith]]
- Abstract:: Human evaluations are typically considered the gold standard in natural language generation, but as models' fluency improves, how well can evaluators detect and judge machine-generated text? We run a study assessing non-experts' ability to distinguish between human- and machine-authored text (GPT2 and GPT3) in three domains (stories, news articles, and recipes). We find that, without training, evaluators distinguished between GPT3- and human-authored text at random chance level. We explore three approaches for quickly training evaluators to better identify GPT3-authored text (detailed instructions, annotated examples, and paired examples) and find that while evaluators' accuracy improved up to 55%, it did not significantly improve across the three domains. Given the inconsistent results across text domains and the often contradictory reasons evaluators gave for their judgments, we examine the role untrained human evaluations play in NLG evaluation and provide recommendations to NLG researchers for improving human evaluations of text generated from state-of-the-art models.
- Type:: [[Article]]
- Publication:: arXiv:2107.00061 [cs]
- URL : http://arxiv.org/abs/2107.00061
- Date Added:: [[December 1st, 2021]]
- Zotero links:: [Local library](zotero://select/groups/2451508/items/6ZS8ZUHC), [Local library](https://www.zotero.org/groups/2451508/items/6ZS8ZUHC)
- Tags:: #[[Computer Science - Computation and Language]]
- PDF links : [Clark et al_2021_All That's 'Human' Is Not Gold.pdf](zotero://open-pdf/groups/2451508/items/9QNEKI47)
- [[Notes]]

    - Comment: references added, corrected typo

###### Discourse Context

- **Informs::** [[QUE - What do we know about transformer language models' natural language generation capabilities]]
- **Informs::** [[QUE - How does the choice of what data we about scholarly papers we index influence performance for information retrieval systems]]
- **SourceFor::** [[EVD - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes - @clarkAllThatHuman2021]]
- **SourceFor::** [[EVD - crowd workers mostly relied on form vs. content heuristics to make their judgments about human-likeness of generate text - @clarkAllThatHuman2021]]

###### References

[[December 1st, 2021]]

- [[@clarkAllThatHuman2021]] for [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] | crowd workers couldn't really distinguish gpt-3-generated stories, news stories, and recipes from human-generated ones

    - #inspectionalread

        - why am i interested in this paper, and how does this overlap with the main questions of the paper?

            - i'm generally wanting to get a good detailed empirical feel for language models' NLG capabilities, and am particularly interested in its failure modes.

            - here the authors seem to care mostly about a methodological issue: how do we evaluate NLG output from langauge models?

                - they're cranky that we do this often with non-experts in small batches, despite knowing that evaluations with end-users in an applied setting is best

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FtRFAsEwBI9.png?alt=media&token=0bc9e258-2d76-493e-ac45-f6077662a20e)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FOhV_EivltK.png?alt=media&token=977481a4-3bf0-4e04-8637-41ad638a883b) (pp. 1-2)

        - what are the parts of this paper i want to pay attention to?

            - they basically do two studies: one where they do a basic comparison with no particular specialized training (headline finding is that ppl are at chance in distingujsihing human from GPT-3), and one where they experiment with three different training regimes to try to improve people's discrimination abilitiy)

            - of special note in 2.5 is an analysis of the annotation rationales

    - #[[🧱 foraging]]

    - #analyticalread

        - methods notes

            - task: evaluate 5 passages, some by humans and some by machine (blind to condition), and rate text on 1-4 scale in terms of "degree machine" (low to high)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FI8lF9ZFzQb.png?alt=media&token=2fef2240-8d49-41a4-b598-79c10d9fbcb6) (p. 2)

            - dataset: stories (from Reddit WritingPrompts, local news articles, and recipes from recipeNLG dataset)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMUvFzwgNlM.png?alt=media&token=8b563d3c-1833-4c0a-a5c7-4182591fc2fe) (p. 3)

            - material: machine-generated with [[sys/GPT-2]] and [[sys/GPT-3]] via "three-shot" setting from [[@brownLanguageModelsAre2020]], with default temperature param (0.7)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCiawOljogK.png?alt=media&token=75dcc940-4d38-4a2a-b4b7-80c084264e34)

            - participants: N = ~780, 1170 [[MTurk]] workers with > 95% acceptance rate from US

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FJjrb2-oOTo.png?alt=media&token=7182b1dd-2838-42e0-adbe-99f75a63d230) (p. 4)

            - training: instructions, examples (3 practice rounds of actual task, with correct answer and explanation), and comparison (similar to example, but with pairs, rather than single examples)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F8lIlvFtGu-.png?alt=media&token=3b4643bf-0fb0-411e-b719-ab0ce4b5880c) 
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDxCa6VCYTW.png?alt=media&token=ed9a865b-cb7c-44c9-bd05-600305a047f1) (pp. 5-6)

        - results

            - [[[[EVD]] - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes - [[@clarkAllThatHuman2021]]]] #Informs

                - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F2CwlElMZI0.png?alt=media&token=c5e633b8-dde0-46b0-9888-a0211e9a6abc)

                - note: they were slightly better at this (above chance) for stories and news for [[sys/GPT-2]] generated text

                - training with examples and feedback only slightly improved accuracy (unclear if now diff. from chance)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQLgvpzFhNK.png?alt=media&token=262d4eac-9fdc-45fd-82cf-3f35273dc6e0) (p. 7)

                - basic result seems to be replicated by https://arxiv.org/pdf/2109.06835.pdf

                - also note: inter-rater reliability was very low!

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDaICOXT-Br.png?alt=media&token=d1dcd340-ae02-495c-b090-c5a5f43d69e1) (p. 4)

            - [[[[EVD]] - crowd workers mostly relied on form vs. content heuristics to make their judgments about human-likeness of generate text - [[@clarkAllThatHuman2021]]]]

                - crowd workers mostly relied on form vs. content heuristics to make their judgments

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDaICOXT-Br.png?alt=media&token=d1dcd340-ae02-495c-b090-c5a5f43d69e1) (p. 4)

    - #lit-context

        - this paper involves [[Noah A. Smith]], who i respect a lot for a clear-headed take on NLP, as well as carefulness in work

        - this is also a #preprint

        - later work that cites this is an [award-winning](https://twitter.com/wellecks/status/1465833346122928128?s=20) [[NeurIPS]] paper that proposes a new eval approach for open-ended text generation: [[@pillutlaMAUVEMeasuringGap2021]]
[[December 1st, 2021]]

- [[[[EVD]] - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes - [[@clarkAllThatHuman2021]]]] #Informs

    - crowd workers were at chance accuracy in distinguishing human-written from GPT-3-written stories, news stories, and recipes

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F2CwlElMZI0.png?alt=media&token=c5e633b8-dde0-46b0-9888-a0211e9a6abc)

    - note: they were slightly better at this (above chance) for stories and news for [[sys/GPT-2]] generated text

    - training with examples and feedback only slightly improved accuracy (unclear if now diff. from chance)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQLgvpzFhNK.png?alt=media&token=262d4eac-9fdc-45fd-82cf-3f35273dc6e0) (p. 7)

    - basic result seems to be replicated by https://arxiv.org/pdf/2109.06835.pdf

    - also note: inter-rater reliability was very low!

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDaICOXT-Br.png?alt=media&token=d1dcd340-ae02-495c-b090-c5a5f43d69e1) (p. 4)
[[December 1st, 2021]]

- [[[[EVD]] - crowd workers mostly relied on form vs. content heuristics to make their judgments about human-likeness of generate text - [[@clarkAllThatHuman2021]]]]

    - crowd workers mostly relied on form vs. content heuristics to make their judgments

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDaICOXT-Br.png?alt=media&token=d1dcd340-ae02-495c-b090-c5a5f43d69e1) (p. 4)
