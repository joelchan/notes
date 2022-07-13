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

###### References

[[Week of April 18th, 2022]]

- stuff for [[prompt programming]] and [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] / [[[[QUE]] - How does prompt programming work?]]

    - 2202.12837.pdf https://arxiv.org/pdf/2202.12837.pdf [[@minRethinkingRoleDemonstrations2022]] "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F37qNnSXsBv.png?alt=media&token=eed68472-972b-43ac-9e10-9db60243ed85)

    - On NYT Magazine on AI: Resist the Urge to be Impressed | by Emily M. Bender | Apr, 2022 | Medium https://medium.com/@emilymenonbender/on-nyt-magazine-on-ai-resist-the-urge-to-be-impressed-3d92fd9a0edd

    - [2109.01247] Do Prompt-Based Models Really Understand the Meaning of their Prompts? https://arxiv.org/abs/2109.01247 [[@websonPromptBasedModelsReally2022]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fmsmqa2vW92.png?alt=media&token=78f5688d-cbf2-414f-8d29-ead07b6272c3)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F9oJLhdQG2V.png?alt=media&token=7c3a6a97-0b06-480f-823b-85cc000fc1ff)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FbAfnWeS-gk.png?alt=media&token=a950f21a-7775-43a0-9919-5eff6156f7b8)
[[Arvind Srinivasan]]

- [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]]

    - And some good video explainers/discussion of [[@brownLanguageModelsAre2020]] and [[sys/GPT-3]]
[[NowReading]]

- [[@bommasaniOpportunitiesRisksFoundation2021]] for [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] |

    - I like using the term [[foundation model]]

    - key aspects/implications: 1) emergence, and 2) homogenization

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRhjyDD3UWc.png?alt=media&token=3d102583-a236-4c1d-b064-755bef1d386a) (p. 3)

    - claims to follow up on #[[➰ breadcrumbs]]

        - non-experts struggle to distinguish text generated by [[sys/GPT-3]] from human-generated text

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FTcMjslH-Ab.png?alt=media&token=4369585e-2913-464b-b8f4-87154538d43b) (p. 22)

        - previous SOTA for text-generation was via linguistic sub-tasks

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fox-g1DVufB.png?alt=media&token=9cec7ca1-d809-4a3b-814d-7e101f122c23)

        - joint-training of language models over high- and low-resource languages can support multilingual abilities

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyIHyCPcSF7.png?alt=media&token=9d99b599-c6ff-4c1b-8fc6-c5e4000f915a)

            - but be careful: not clear how this works when we don't have English in the mix

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FBZ_s-S0Fkn.png?alt=media&token=093fca22-53a9-4462-9987-e5a90d71c706)

        - can be difficult to get [[transformer language model]] to consistently perform intended task, and we still don't really understand what [[transformer language model]] are capable of. here are some leads on solutions (e.g., [[prompt programming]])

    - questions that come to mind:

        - are there common "checklists" of things we need to do when exploring a new prompting-based task?
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
[[November 16th, 2021]]

- On my mind: [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] and [[[[QUE]] - How might AI systems assist with problem (re)formulation?]]

    - Want to think through two things: 1) what's a basic intuition for how they work, and 2) let's start compiling some evidence we have on its capabilities

    - We'll start with [[@brownLanguageModelsAre2020]]

        - Hmm interesting - here they seem to anticipate later results on potential advantages of *fewer* (and maybe no???) examples for [[few-shot learning]]? Here they discuss the hypothesis that brittleness and vulnerability to adversarial attacks might grow larger as the training data grows: [[[[CL]] - Potential to exploit spurious correlations in training data fundamentally grows with expressiveness model and narrowness of training distribution]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F-PPevoPi2O.png?alt=media&token=d480395a-2198-4eb0-bc0a-ccf9029e54a2) (p. 3)

        - The basic intuition for how the language models work:

            - I don't full understand the details yet of how the training and the model for [[sys/GPT-3]] work. But I do know that:

                - The architecture is a [[transformer architecture]]

                    - One of the secret sauces is [[self-attention]], which helps with the problem of updating weights appropriately for connections to context beyond the immediate surroundings of a word/token

                        - Original source for this is [[@vaswaniAttentionAllYou]]

                - The encoding of words/tokens is [[Byte-Pair Encoding (BPE)]]

                    - in this way it reminds me of [[charNN]] architectures

                - It's the same basic architecture as [[sys/GPT-2]], which is described in [Radford et al. (2019)]([[@radfordLanguageModelsAre2019]])

                - [[dataset/Common Crawl]] is the base, but with some mods:

                    - filtering for "quality" (see Appendix A)

                    - fuzzy deduplication (see Appendix A)

                    - enriching with some other curated datasets, e.g., WEbText, Wikipedia

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ff-olxLm3nt.png?alt=media&token=61808470-eeac-4eaf-809e-7da99bba0901) (p. 8)

            - They are trained in an unsupervised fashion to basically do one task: predict some word(s)/token(s) of set size M based on some context of word(s)/token(s) of set size N.

        - Technically what distinguishes the [[few-shot learning]] paradigm from [[fine-tuning]] is that you basically condition the output with some demonstrations and instructions, but don't allow any weight updates (so the underlying model is fundamentally the same)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft426DcxvAq.png?alt=media&token=4a311fb0-6fdd-4e2a-88ea-8c01b276e2ad) (p. 6)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQRpWGIQXPo.png?alt=media&token=38b562e0-f2e0-4168-b93b-9644ba23823f) (p. 7)
