---
title: [[QUE]] - Can deep learning discover analogical representations?
url: https://roamresearch.com/#/app/megacoglab/page/7ArZLTQUN
author: Unknown
date: Wed Jul 06 2022 00:17:25 GMT-0400 (Eastern Daylight Time)
---

- # Synthesis

    - Content

        - current belief: probably not?

        - need to really clarify/sharpen this question: it's too vague atm. i think right now it's a high-level proxy for the question "if we just use the SOTA language models, will that enable us to find analogical ideas/papers across domains?"

        - so basically, the reasoning for being cautious about deep learning per se goes as follows:

            - [[[[CLM]] - Analogies are fundamentally about relational similarity]]

            - to reason about similarity between relations, we need to have good representations of relations (e.g., [[relational categories]], as in [[@gentnerRelationalCategories2005]]).

            - [[[[CLM]] - Relational categories are almost overwhelmingly expressed as verbs]] #[[Z]]

            - therefore, computational models of semantics that do poorly with verbs should also do poorly with relations, and therefore struggle with [[analogy]]

            - one strong representative of deep learning representations of semantics is [[word embeddings]], such as [[sys/word2vec]] (was the first model to make waves for apparently being able to do [[analogy]])

            - There is some evidence that [[[[CLM]] - Vector-space models of language struggle with relational similarity]]

            - therefore, we are skeptical that deep learning-based semantics (without explicit searching / tuning for relational structure) will succeed at giving us computational [[analogy]]

        - HOWEVER

            - There is some emerging evidence that [[[[CLM]] - [[transformer language model]]s have some analogical reasoning ability]]

                - #SupportedBy

                    - [[[[EVD]] - given one set of objects from a few classic analogies such as solar system / atom, [[sys/GPT-3]] was able to complete the corresponding objects on the other side for a few examples - [[@stayMachinamentaFormingExtended2020]]]]
- ---
- # Sources

    - [[@stayMachinamentaFormingExtended2020]]

    - [[@teamWorldCreationAnalogy2020]]

    - [[@brownLanguageModelsAre2020]]
- ---
- Meta

    - Related projects: [[D/Computational Analogy]]

###### References

[[May 22nd, 2020]]

- Rediscovered this paper while rummaging through old notes on [[[[QUE]] - Can deep learning discover analogical representations?]] - [[@ichienVerbalAnalogyProblem2020]]

    - It's published in BRM, quite far from ML/NLP venues, but is similar in spirit to our goal for [[P/Computational [[analogy]] Dataset]]
[[August 6th, 2020]]

- [[[[QUE]] - Can deep learning discover analogical representations?]]

    - [Word meaning in minds and machines](https://arxiv.org/abs/2008.01766)

    - [Forming Extended Analogies with GPT-3](https://machinamenta.blogspot.com/2020/08/forming-extended-analogies-with-gpt-3.html)

        - [[@stayMachinamentaFormingExtended2020]]

    - [Can GPT-3 Make Analogies?](https://medium.com/@melaniemitchell.me/can-gpt-3-make-analogies-16436605c446) from [[Melanie Mitchell]]

        - [[@mitchellCanGPT3Make2020]]

        - [[@mitchellFollowupCanGPT32020]]
[[June 18th, 2021]]

- {{[[TODO]]}} [[Joel Chan]] Circle back to [[[[QUE]] - Can deep learning discover analogical representations?]] with this stuff, maybe branch off to more granular questions. Something like a "how can we re-represent unstructured text with sufficient structure to facilitate computational analogical reasoning?" #Backlog

    - See e.g., these citations from [[@cheongAutomatedExtractionFunction2017]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkCktxH2fwn.png?alt=media&token=ab13eb14-5a94-45fb-bb10-6f28ca6052ef)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FcClnauGv3z.png?alt=media&token=48fcbeab-c072-4ae5-8c43-55dfe552bbbf)
[[November 28th, 2020]]

- let's actually try it out! start with [[[[QUE]] - Can deep learning discover analogical representations?]]

    - see: [skip-gram model](((4xz52frAQ))) with vanilla BOW contexts performed ~50% worse on verbs compared to nouns and adjectives in terms of predicting [human similarity judgments on SimLex999](((n3Xi0Tp0B)))

        - this is an empirical NLP paper, but we should be able do basically the same thing with eval sections from good NLP systems papers

        - ultimately we don't care if an artifact just exists, or is "intended to do X": we only take notice if we have some reason to believe that it can in fact do X. then it tells us something about the way the world could be

        - note: this could also potentially be done through argumentation: we'd just want to make clear in the micropub (e.g., XYZ proposed design X, and argued that it can do X because of THEORY)
[[🌱🌾 Research Garden]]

- [[[[QUE]] - Can deep learning discover analogical representations?]]

    - [[[[CLM]] - Vector-space models of language struggle with relational similarity]]
[[March 4th, 2021]]

- Can now play with and try to replicate [this]([[[[EVD]] - given one set of objects from a few classic analogies such as solar system / atom, [[sys/GPT-3]] was able to complete the corresponding objects on the other side for a few examples - [[@stayMachinamentaFormingExtended2020]]]]) from [[@stayMachinamentaFormingExtended2020]] for [[[[QUE]] - Can deep learning discover analogical representations?]]

    - Has also been replicated by [[@teamWorldCreationAnalogy2020]], which extends it to world-building:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FFteLleqIY3.png?alt=media&token=9b0fad37-cdc8-4119-be2c-2f45509c4b5d)
[[November 10th, 2021]]

- There's also some emerging evidence that [[[[CLM]] - [[transformer language model]]s have some analogical reasoning ability]], contra [[[[QUE]] - Can deep learning discover analogical representations?]]

    - another line of evidence for this might be the insane performance of giant language models like [[sys/GPT-3]]
