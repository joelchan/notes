---
title: @artsParadiseNoveltyLoss2018a
url: https://roamresearch.com/#/app/megacoglab/page/4K-tb4egG
author: Joel Chan
date: Fri Jul 16 2021 10:08:04 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: Paradise of Novelty—Or Loss of Human Capital? Exploring New Fields and Inventive Output

    - Meta:

        - Authored by:: [[Sam Arts]] [[Lee Fleming]]

        - Year: [[2018]]

        - Publication: Organization Science

        - Zotero link: [Zotero Link](zotero://select/items/7_RYGUQPSN)

        - URL: [Arts & Fleming (2018). Paradise of Novelty—Or Loss of Human Capital? Exploring New Fields and Inventive Output. Organization Science](https://pubsonline.informs.org/doi/10.1287/orsc.2018.1216)

    - Content

        - Abstract

            - Does a person become more or less creative when exploring a new field? Exploring new fields exposes a person to new knowledge that might increase the novelty of inventive output; at the same time, exploration means a lack of prior expertise and a learning challenge that might harm the value of that output. Using new combinations as a measure of novelty and citations as a measure of value, we demonstrate correlations between exploring new fields and increased novelty—but decreased value—in an inventor–firm fixed effects panel. The negative effect of exploring new fields on value is muted when the novice collaborates with experts or uses the scientific literature in the new field. We find consistent results using an unintended change in noncompete labor law as an exogenous influence on exploring new fields. The research illustrates two opposite influences of exploration on creative output and suggests how inventors can reduce the downside of entering a new field.

###### Discourse Context

- **Informs::** [[QUE - How might domain distance modulate the effects of analogies on creative output]]
- **SourceFor::** [[EVD - patents filed by inventors who was new to the patent's field tended to be more novel; this was less true if they collaborated with an expert in the new field - @artsParadiseNoveltyLoss2018a]]
- **SourceFor::** [[EVD - patents filed by inventors who was new to the patent's field tended to receive slightly fewer..., except when they collaborated with an expert in the new field - @artsParadiseNoveltyLoss2018a]]

###### References

[[Playground ]]

- [[EVD]] - patents filed by inventors who was new to the patent's field tended to be more novel; this was less true if they collaborated with an expert in the new field - [[@artsParadiseNoveltyLoss2018a]]

    - x

        - 875.5

    - y

        - 468

    - color
[[July 27th, 2021]]

- [[@artsParadiseNoveltyLoss2018a]] for [[[[QUE]] - How might domain distance modulate the effects of analogies on creative output?]] | if inventor files a patent in a new field they haven't explored before, their patent tends to be more novel; there's also a citation penalty, but this gets canceled out if they collaborate with an expert in the new field

    - #inspectionalread

        - correlation + natural experiment from unintended change in noncompete labor law

        - exploring new fields ++ novelty but --value (proxied with raw citations)

            - per [[@wangBiasNoveltyScience2017]] be super careful about this outcome measure of value given [long vs. short run differences for highly novel stuff]([[[[EVD]] - highly novel papers were more likely to be in the top 1% of citations in the long run, but not in the short run, and particularly in other fields - [[@wangBiasNoveltyScience2017]]]])

        - the relevance for our question here is that inventors who explore a new field (to the extent that it is different from their own) and then later go on to invent new things that are better are at least possibly (we don't know for sure) doing a form of [[far analogies]] or [[🧱 conceptual combination]]: tough to distinguish.

            - i really want to watch out for whether they make any attempt to trace actual relationships between the things cited and the things proposed, *conceptually* (in content terms)

    - what did they do?

        - study 1: correlational study

            - estimation strategy: inventor-firm fixed effects panel models

            - sample: ~400k inventors of ~2.7M patents, across ~47k firms

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FdyjoiND2vv.png?alt=media&token=7615e687-e83d-407d-8a19-494d2b216557)

            - dependent measure: novelty = number of pairwise subclass combinations in the focal patent that appear for the first time in the patent database

                - similar to [[@wangBiasNoveltyScience2017]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F9pJaGcW9qX.png?alt=media&token=2444d022-6de2-4b97-8b62-423841d3967c) (p. 5)

            - dependent measure: "value" = number of forward citations in the 10 years after the patent is approved

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FmB38E0LsgV.png?alt=media&token=eee81c34-f24d-4e6e-bb1a-d431242edcc3) (p. 5)

            - independent variable: exploring new fields = 0 or 1 (if focal patent has no overlapping classes with all prior patents from the same inventor)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F1GILaZHVqd.png?alt=media&token=0a89b928-a7c3-436b-80db-d0d523ece9b4)

            - independent variable: expert team  = 1 if at least one co-inventor has prior patent with same class as focal patent (else 0)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FfrkO7dQ822.png?alt=media&token=e7279055-8d18-40c1-9908-7f5fe17be67a)

        - study 2: natural experiment with michigan antitrust reform act

            - sample: ~29k inventors of ~162k patents in michigan vs. not-michigan who filed patents after moving firms within the same state between 1975 and 1995 (+/- 10 yrs of MARA law passing)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FGxeeSY0OtD.png?alt=media&token=4f97dd03-f445-4261-b26e-efc97e191660) (p. 11)

            - context: Michigan Antitrust Reform Act (MARA)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FhHQz0nQ18U.png?alt=media&token=e6f1d15f-174c-407b-b01c-205cbf973cab) (p. 11)

            - estimation strategy: [[difference in difference analysis]]

    - side notes

        - #[[➰ breadcrumbs]] more citations for the [[outsider innovation]] effect, leaning a bit more on the "useful naivete" mechanism rather than "transferring in new things" piece

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMp_l1KJlvH.png?alt=media&token=d5f64e51-1f83-483e-a03f-5e18a188cb19)

    - what did they find?

        - there's also a result here that is similar to what [[@kneelandExploringUnchartedTerritory2020]] finds re: science citations: positive effect of citing nonpatent prior art (mostly science pubs)

        - [[[[EVD]] - patents filed by inventors who was new to the patent's field tended to be more novel; this was less true if they collaborated with an expert in the new field - [[@artsParadiseNoveltyLoss2018a]]]]

        - [[[[EVD]] - patents filed by inventors who was new to the patent's field tended to receive slightly fewer citations, except when they collaborated with an expert in the new field - [[@artsParadiseNoveltyLoss2018a]]]]

    - what might this mean?

        - the results about expert collaborations in new fields reversing negative effects on forward citations (without canceling out novelty advantage) is really interesting and relevant for [[[[QUE]] - What are the most efficient routes to useful cross-boundary knowledge?]]
[[Playground ]]

- [[EVD]] - patents filed by inventors who was new to the patent's field tended to receive slightly fewer citations, except when they collaborated with an expert in the new field - [[@artsParadiseNoveltyLoss2018a]]

    - x

        - 2317.080953012566

    - y

        - 790.7690687248261

    - color
