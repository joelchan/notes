---
title: @schwartzSymmetricPatternsCoordinations2016
url: https://roamresearch.com/#/app/megacoglab/page/YISbCAAwe
author: Joel Chan
date: Sun Nov 29 2020 04:23:08 GMT+0800 (Malaysia Time)
---

- [[references]]

    - Title: Symmetric Patterns and Coordinations: Fast and Enhanced Representations of Verbs and Adjectives

    - Meta:

        - Tags: [[DComputational Analogy]]

        - Authored by:: [[Roy Schwartz]]

        - Year: [[2016]]

        - Publication: Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies

        - Zotero link: [Zotero Link](zotero://select/items/1_ICHZUYRN)

        - URL: [Schwartz et al. (2016). Symmetric Patterns and Coordinations: Fast and Enhanced Representations of Verbs and Adjectives. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies](https://www.aclweb.org/anthology/N16-1060)

    - Content

        - Abstract

            - undefined

    - #lit-context

        - model: skip-gram model (basically vanilla [[sysword2vec]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F-FSYIjSoqE.png?alt=media&token=50367b84-0e98-415c-8870-424ce8bc37f8) (p. 502)

        - see also past work Schwartz et al 2015

        - training corpus: 8G words corpus generated by [[sysword2vec]]

            - code.google.com/p/word2vec/source/

        - dataset: SimLex999, which has human judgments of **similarity**, not relatedness

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fq_lAs0abLu.png?alt=media&token=394e0a4e-b522-43d5-856b-7dc90d646f9b) (p. 502)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FOq095aUkRu.png?alt=media&token=dcd3bfd0-f085-41d8-992c-d9dac535f912) (p. 500)

            - this distinction is critical, allows us to distinguish between synonyms and antonyms!

                - many past datasets, such as RG-65, MC-30 and Word-Sim353 have human judgments of relatedness

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FIlxl9ZRunn.png?alt=media&token=3a2ee09e-b53b-4500-9616-21863bb90469)

        - contexts for sg model

            - symmetric pattern contexts

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fer0OR4Mg6T.png?alt=media&token=11f5a173-0aeb-4f08-a928-817c2e271aca) (p. 501)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyjztuvEapk.png?alt=media&token=b95def1b-3125-47fd-a482-b43fa5a7f60d)

                - basically a special kind of co-occurrence that tries to guarantee that the two words have the same semantic function

    - [[📝 lit-notes]]

        - some past work on semantic limitations of word embeddings

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0NMJSvAWGR.png?alt=media&token=b9310537-835e-44af-bb75-37bcfdc7ed90) (p. 501)

        - [[observation-notes]]

            - [skip-gram model](model: skip-gram model (basically vanilla [[sysword2vec]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQaUi4LKQaY.png?alt=media&token=ed225ecb-949e-497c-a8d5-c60d4a86c8b7) (p. 502)

            - [skip-gram model](model: skip-gram model (basically vanilla [[sysword2vec]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQaUi4LKQaY.png?alt=media&token=ed225ecb-949e-497c-a8d5-c60d4a86c8b7) (p. 502)

        - commentary

            - curious how this changes when we have more dynamic, contextual embeddings, as with [[sysBERT]]

###### Discourse Context

- **Informs::** [[CLM - Vector-space models of language struggle with relational similarity]]
