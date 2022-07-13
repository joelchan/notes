---
title: @holsteinImprovingFairnessMachine2019
url: https://roamresearch.com/#/app/megacoglab/page/8rSbK6y5G
author: Joel Chan
date: Fri Oct 30 2020 13:48:12 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: Improving fairness in machine learning systems: What do industry practitioners need?

    - Meta:

        - Authored by:: [[Kenneth Holstein]] [[Jennifer Wortman Vaughan]] [[Hal Daumé III]] [[Miro Dudík]] [[Hanna Wallach]]

        - Year: [[2019]]

        - Publication: Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems  - CHI '19

        - Zotero link: [Zotero Link](zotero://select/items/1_MSEVHASJ)

        - URL: [Holstein et al. (2019). Improving fairness in machine learning systems: What do industry practitioners need?. Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems  - CHI '19](http://arxiv.org/abs/1812.05239)

    - Content

        - Abstract

            - The potential for machine learning (ML) systems to amplify social inequities and unfairness is receiving increasing popular and academic attention. A surge of recent work has focused on the development of algorithmic tools to assess and mitigate such unfairness. If these tools are to have a positive impact on industry practice, however, it is crucial that their design be informed by an understanding of real-world needs. Through 35 semi-structured interviews and an anonymous survey of 267 ML practitioners, we conduct the first systematic investigation of commercial product teams' challenges and needs for support in developing fairer ML systems. We identify areas of alignment and disconnect between the challenges faced by industry practitioners and solutions proposed in the fair ML research literature. Based on these findings, we highlight directions for future ML and HCI research that will better address industry practitioners' needs.

    - #[[📝 lit-notes]]

        - #[[observation-notes]]

            - while most systems for detecting and mitigating bias appear to take the dataset as fixed, in practice ML engineers most often felt that the dataset was the most important place to intervene

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fgd8yYJxm9z.png?alt=media&token=4476db85-ba98-48a2-b564-e846cf578635)

###### Discourse Context



###### References

[[October 30th, 2020]]

- [[Hal Daumé III]] was part of committee, pointed to recent study of ML engineers in practice [[@holsteinImprovingFairnessMachine2019]]

    - one of the themes in the paper stands out and helps us think through more of the complexity of what [[material knowledge]] might be for ML: while most systems for detecting and mitigating bias appear to take the dataset as fixed, in practice ML engineers most often felt that the dataset was the most important place to intervene

        - this makes me think about the target and source of [[material knowledge]] for ML being distributed across, at minimum:

            - the model (ML engineers should have this)

            - the data (domain experts should have this, I think?)

            - the context of use, maybe??

        - designing in isolation is like designing with one eye closed, or with  gloved hands - critically limited!

    - we should talk to him re: [[P/Material Knowledge of ML for Design]]!
