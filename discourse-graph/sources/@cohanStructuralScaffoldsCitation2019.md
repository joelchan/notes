---
title: @cohanStructuralScaffoldsCitation2019
url: https://roamresearch.com/#/app/megacoglab/page/lrCperobF
author: Joel Chan
date: Thu Feb 20 2020 12:54:12 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Structural Scaffolds for Citation Intent Classification in Scientific Publications

    - Meta:

        - Authored by:: [[Arman Cohan]] [[Waleed Ammar]] [[Madeleine van Zuylen]] [[Field Cady]]

        - Year: [[2019]]

        - Publication: arXiv:1904.01608 [cs]

        - Zotero link: [Zotero Link](zotero://select/items/1_SQL8XFLI)

        - URL: [Cohan et al. (2019). Structural Scaffolds for Citation Intent Classification in Scientific Publications. arXiv:1904.01608 [cs]](http://arxiv.org/abs/1904.01608)

    - Content

        - Abstract

            - Identifying the intent of a citation in scientific papers (e.g., background information, use of methods, comparing results) is critical for machine reading of individual publications and automated analysis of the scientific literature. We propose structural scaffolds, a multitask model to incorporate structural information of scientific papers into citations for effective classification of citation intents. Our model achieves a new state-of-the-art on an existing ACL anthology dataset (ACL-ARC) with a 13.3% absolute increase in F1 score, without relying on external linguistic resources or hand-engineered features as done in existing methods. In addition, we introduce a new dataset of citation intents (SciCite) which is more than five times larger and covers multiple scientific domains compared with existing datasets. Our code and data are available at: https://github.com/allenai/scicite.

    - #[[📝 lit-notes]]

        - substantially less than half of citations are "meaningful": many are simply "background" citations.

            - This is probably an underestimate (some of the background citations might be meaningful rather than simply saying "crowdsourcing" is a thing; these might be more towards the end of the intro, or in the discussion when implications are discussed)

###### Discourse Context



###### References

[[February 20th, 2020]]

- Reminded of the structural scaffolds paper [[@cohanStructuralScaffoldsCitation2019]] bc I was annoyed with not being able to explore citations of a paper I was interested in. Tried in [[sys/scite.ai]], saw that there were only "mention" type citations. Curious again about the question "how informative are citations?" - one common use case that is hard is actually following a line of thought, how it has been developed, contradicted, refined, etc.

    - There's probably a similar result in the "influential citations" work by [[sys/Semantic Scholar]] [[R: valenzuelaIdentifyingMeaningfulCitations2015]] - as a sample, the paper I was looking at had 90 citations on SS, but only 13 were "influential". This is not conceptually identical to "meaningful" (in the sense of developing a line of thought), but should overlap some in practice

    - [[Stian Håklev]]: I remember work on [[citation ontologies]] a few years ago by a researcher working for Springer? I have slides if you're interested. Never seen them in the wild though. Would be interesting to think about citations that are both much more precise about the kind (agrees-with, defines, provides-empirical-evidence) etc, and also about the target (pointing to a specific paragraph etc). And of course the whole metadata thing is maddeningly frustrating - it was 10 years ago, and it's not hugely better today... One of the canonical papers I read was **__Why can't I manage academic papers like MP3s? The evolution and intent of metadata standards__** (article) Howison, J. and Goodrum, A.

        - Why is it easier for me to press a button and get a graph of all of my Twitter followers, and all of their followers, sorted by different indices, than taking a seminal paper in a field, and getting a graph of all the cited works, and the works they cite, etc?

    - One striking observation in [[@cohanStructuralScaffoldsCitation2019]]: substantially less than half of citations are "meaningful": many are simply "background" citations. ((wfq4THZ2-))

        - #example-of [[[[CLM]] - Citation practices in science are far from optimal]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FL9jYzbpuHI?alt=media&token=a5566f45-858e-4d2d-989f-b433ab6485c6)
[[February 20th, 2020]]

- One striking observation in [[@cohanStructuralScaffoldsCitation2019]]: substantially less than half of citations are "meaningful": many are simply "background" citations. ((wfq4THZ2-))

    - #example-of [[[[CLM]] - Citation practices in science are far from optimal]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FL9jYzbpuHI?alt=media&token=a5566f45-858e-4d2d-989f-b433ab6485c6)
