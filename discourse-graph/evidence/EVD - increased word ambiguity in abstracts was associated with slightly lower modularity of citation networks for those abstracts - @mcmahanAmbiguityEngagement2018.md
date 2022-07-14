---
title: [[EVD]] - increased word ambiguity in abstracts was associated with slightly lower modularity of citation networks for those abstracts - [[@mcmahanAmbiguityEngagement2018]]
url: https://roamresearch.com/#/app/megacoglab/page/0dCO_io-p
author: Joel Chan
date: Mon Jul 12 2021 12:35:18 GMT-0400 (Eastern Daylight Time)
---

- Summary::

    - Increased word [ambiguity]([[ambiguity]] operationalized as word synonym entropy) in [abstracts](((6qjlnVVFu))) was associated with a [small reduction](((UM_VbavN0))) in [modularity](((WjBY2ojmx))) of citation networks for those abstracts, controlling for covariates like number of citations, subject-level modularity, and distribution/span of years)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FYK5hjRvILZ.png?alt=media&token=91149ef7-7b6d-4595-ba46-553a1e300607) (p. 891)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ff1KNxVhp1L.png?alt=media&token=360f4488-5542-48a5-b832-624d4cecda87) (p. 892)

    - Note: this effect was ~order of magnitude smaller than effects of number of disciplines and subject-wide modularity
- **Grounding Context**

    - sample: ~1.1M abstracts from Web of Science (after trimming for min. threshold citations, and at least 5 usable terms for ambiguity measure in abstract)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6swfV2e5lD.png?alt=media&token=663be791-00fa-43a8-939e-16b1e2b3839b) (p. 880 - 881)

    - [[ambiguity]] operationalized as word synonym entropy

        - define as posterior distribution over pr(M | t, c) (probability of each possible meaning for a given token in a given context) - see Appendix A (how to build "meaning graph" for each token), and Appendix B (how to estimate ambiguity)

            - very similar to [[LDA]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkBZZ_HTTGv.png?alt=media&token=1b9f4a7c-5f25-4555-82c0-4f2785d46fb6) (p. 898)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyJ2BvBP1aJ.png?alt=media&token=06e19e17-993e-43dc-9095-47215d99ff63)

        - meaning simplified to proxy into synonyms from Moby and WordNet thesauri

            - would prefer to define as cliques in synonym graph, but... for reasons, decided to simplify to just directed edges + the neighborhood

        - examples (from data)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FjNbxETh3nc.png?alt=media&token=7bf4a619-0ca2-4960-81e6-cc1096a24ba9)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FgI8AhKGeTl.png?alt=media&token=ae39c2be-5b06-48f4-bb34-4216808fc838) (p. 885)

        - validated against human judgments (see Appendix C)

    - "engagement" operationalized as graph entropy over subgraph from each article for max (1k cites, 3 recursive runs), computed in terms of maximal [[network modularity]] (intuitively, a kind of "cliqueiness" or fragmentation, so higher here = lower engagement, i think)

        - toy example:

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FAUmk1jo2Ua.png?alt=media&token=c9ed7651-5fea-44fe-994a-c769e70cb68d)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzWrx4znKTB.png?alt=media&token=ac0e15f3-3cfc-4454-82ab-bf0acb1a3689) (p. 880)

        - examples (from data):

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKUb7aKx_yi.png?alt=media&token=d9e03062-c18f-432c-896a-32a3062151ed)

        - network modularity correlated at -.76 with topological entropy for random sample of 1.2k abstracts

###### Discourse Context

- **Supports::** [CLM - ambiguity in scholarly communication facilitates within- and cross-field integration of discourse - @mcmahanAmbiguityEngagement2018.md](CLM - ambiguity in scholarly communication facilitates within- and cross-field integration of discourse - @mcmahanAmbiguityEngagement2018.md)
- **FromSource::** [@mcmahanAmbiguityEngagement2018.md](@mcmahanAmbiguityEngagement2018.md)
