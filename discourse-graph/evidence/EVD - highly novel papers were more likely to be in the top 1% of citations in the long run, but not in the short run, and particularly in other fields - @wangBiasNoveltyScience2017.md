---
title: [[EVD]] - highly novel papers were more likely to be in the top 1% of citations in the long run, but not in the short run, and particularly in other fields - [[@wangBiasNoveltyScience2017]]
url: https://roamresearch.com/#/app/megacoglab/page/9NG2IaU62
author: Joel Chan
date: Mon Jul 19 2021 11:27:49 GMT-0400 (Eastern Daylight Time)
---

- Summary::

    - key figure:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMD9uL1xKBl.png?alt=media&token=ff1de385-c3e5-49de-b11a-42c225f0e74d)

    - novelty --> higher p(BIG HIT)  (5.2)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6ganK-2hEw.png?alt=media&token=6a447273-1af8-4a46-8c17-c376e5270146)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FrilTSueU7H.png?alt=media&token=05997334-255e-4017-8f6c-626b5d721113) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fatvuh0YQt1.png?alt=media&token=4f1ca1b7-81be-495c-80f9-e4305f6bf8e4)(p. 6)

    - novelty --> bigger delayed recognition penalty (lower p(hit) in short run, higher p(hit) in longer run, past 7 years) (5.4)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FENes506qrD.png?alt=media&token=ce78933b-86b9-4420-9bcf-f4e5eef56547) (p. 6)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0wQd8m9h4v.png?alt=media&token=a9c77f8a-d416-4868-bb6d-1a2b04a999c2) (p. 11)

    - novelty --> higher p(cited by BIG HIT) (5.2)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FgTX3fsqB4F.png?alt=media&token=b63b706f-b668-4f9a-b8b9-22893d03c8a0)

    - novelty --> greater impact from (more) distant fields (5.3)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FWiDUGn3J5I.png?alt=media&token=8cdb3a0f-9e44-4f88-8e6b-b9a610b0e1bf)
- **Grounding Context**

    - sample: 661,643 papers published in 2001 from 251 subject categories, retrieved from  [[Web of Science]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FVYIDxSOBLg.png?alt=media&token=7c165565-4a9e-466c-af5d-5f14a16d78a9) (p. 4)

    - novelty = difficulty-adjusted first-time combination of journals

        - novelty per paper is sum over journal pairs binary novel/not multiplied by cosine distance between the co-citation vectors of the journal

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkcP0aTxEQZ.png?alt=media&token=74d3a02c-c7e8-4368-bdf9-41671c3dee31)

        - difficulty is proxied by the cosine similarity between the co-citation vectors of the journals

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FHHLCWvv1L4.png?alt=media&token=784a0747-d383-4b08-bd51-903e6693dac3)

        - filter out journals that don't really get citations (er.... whyyyyyy if more novel papers tend to get published in lower impact factor journals on average). pay close attention to Appendix III

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0Gkaoda-lr.png?alt=media&token=e22d1308-f7c2-4e10-af0a-4cab485716f3)

        - in this sense, it could be related to [[far analogies]], but perhaps more closely to [[🧱 conceptual combination]]

        - why might journals be a reasonable proxy for conceptual chunks? domains?

            - better than keywords? (maybe too granular?)

            - or subject areas? (maybe too coarse?)

                - some have used [[MeSH]] headings.

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fu-fHUaHEJU.png?alt=media&token=1d010c7d-505f-4af5-aea7-087e8877b43e)

                    - might depend on there being a reasonably complete and high-quality ontology or controlled vocabulary

            - [[@uzziAtypicalCombinationsScientific2013]] makes the same move (journals as proxies of bodies of knowledge)

    - for analysis, novelty was binned into three categories (no novelty, >= 1 novel combination, but overall score < 99th percentile for subject category, >= 99th percentile for subject category) due to a highly skewed distribution

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fyhp_0sx_40.png?alt=media&token=298a87ad-d5f2-4616-ae87-f5bc5ad942d3)

        - not sure about this; would like to see robustness checks with a different estimation strategy. but ok i guess.

    - properties of novelty score: as expected, highly skewed (~89% of papers do not make novel combinations, and ones that do only score modestly after difficulty adjustment)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FrbtFk4kNEa.png?alt=media&token=a5a76e16-a2b8-475a-a74b-8610cbebfde5) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fsc2n6w-OiT.png?alt=media&token=e56f301d-a632-4a5b-81e4-5e4e30adef60) (p. 4)

    - results robust to categorical conception of novelty, as well as filtering of sample (see 5.7)

###### Discourse Context

- **Informs::** [[QUE - How might domain distance modulate the effects of analogies on creative output]]
- **Supports::** [[CLM - Analogical distance of inspirations for an idea are positively related to the idea's creativity]]
- **Consistent With::** [[EVD - papers with high median conventionality and high tail atypical combinations of journals they ...erage to be in top 5 percent of citation distribution - @uzziAtypicalCombinationsScientific2013]]
- **Consistent With::** [[EVD - highly novel papers had higher variance in their citation outcomes over a 15-year window, biased towards the higher impact tail of the distribution - @wangBiasNoveltyScience2017]]
- **FromSource::** [[@wangBiasNoveltyScience2017]]

###### References

[[August 9th, 2021]]

- emphasizing a lot the so-called "reception side" of things (cf. [[[[EVD]] - highly novel papers were more likely to be in the top 1% of citations in the long run, but not in the short run, and particularly in other fields - [[@wangBiasNoveltyScience2017]]]])

    - Lo and Kennedy mentioned a couple times:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQTbvYLIHNM.png?alt=media&token=d36b60a5-ea5b-4fef-b234-f73a757c89de)

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FiFUJ2rIIc4.png?alt=media&token=5d099fce-44b6-46ac-8514-c9dccb48d6a6)

    - Zuckerman an important ref i think, probably theory, seminal claims/hypotheses (but probably not empirical evdience?) interesting: coming at it from sociology, and grounded in film industry. be careful!

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fh-s0tKiYni.png?alt=media&token=ac087ac4-e6c5-4030-b299-03aad89e2ba9)
[[December 21st, 2021]]

- the primary task will be to replicate and extend these results from Wang et al on [bias against novelty]([[[[EVD]] - highly novel papers were more likely to be in the top 1% of citations in the long run, but not in the short run, and particularly in other fields - [[@wangBiasNoveltyScience2017]]]]) - we want to know if the basic result varies by field according to the [[hierarchy of the sciences]]

    - secondarily, we might see if the effect in Uzzi et al (where a [mix of conventional and atypical combinations of citations led to much higher p(home run)]([[[[EVD]] - papers with high median conventionality and high tail atypical combinations of journals they cited were 2x more likely than average to be in top 5 percent of citation distribution - [[@uzziAtypicalCombinationsScientific2013]]]])) varies across fields

    - this will involve the following steps:

        - gain access to a suitable dataset (ideally from the authors) with enough variation in fields ([Wang's](sample: 661,643 papers published in 2001 from 251 subject categories, retrieved from  [[Web of Science]] ) for comparison; other leads include [[@mairesseNoveltyScienceImpact2018]]

        - prepare dataset, with these substeps:

            - compute combination / novelty scores (from [Wang](novelty = difficulty-adjusted first-time combination of journals))

                - note: wang et al normalized these measures across fields for easier comparison. we will likely need to finesse and refine the measure to account for a priori field-varying factors in things like article length, citation practice,s etc.

            - impute [hierarchy of sciences]([[hierarchy of the sciences]]) [classification](classify journals by [[hierarchy of the sciences]]) to articles: roughly, math, physical sciences, biological sciences, social sciences, and humanities (see [this ordering](((CaQWGh1pG))), for example)

            - (bonus): do more detailed subfield analyses to classify and identify subsets of data where we have a more direct measure of degree of [[codification]] (see [definition](core definitions of [[codification]] on pp. 303-305) from [[@zuckermanAgeAgingAge1972]])

            - compute citation outcome measures, including not just raw total cituations, but citations at long and short run (15-year and 3-year windows, respectively, as per [[@wangBiasNoveltyScience2017]])

            - classify journals by [[hierarchy of the sciences]]

        - construct appropriate regression models to test hypotheses

            - [[Generalized Negative Binomial (GNB) model]] and [[logistic regression]]
