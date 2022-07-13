---
title: @mcmahanAmbiguityEngagement2018
url: https://roamresearch.com/#/app/megacoglab/page/GhXXnn8RT
author: Joel Chan
date: Wed Feb 03 2021 08:59:24 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Ambiguity and Engagement

    - Meta:

        - Authored by:: [[Peter McMahan]] [[James A. Evans]]

        - Year: [[2018]]

        - Publication: American Journal of Sociology

        - Zotero link: [Zotero Link](zotero://select/items/7_TT9UR5DL)

        - URL: [McMahan & Evans (2018). Ambiguity and Engagement. American Journal of Sociology](https://www.journals.uchicago.edu/doi/10.1086/701298)

    - Content

        - Abstract

            - undefined

###### Discourse Context

- **Informs::** [[QUE - How can we best bridge private vs. public knowledge]]
- **SourceFor::** [[EVD - increased word ambiguity in abstracts was associated with slightly lower modularity of citation networks for those abstracts - @mcmahanAmbiguityEngagement2018]]
- **SourceFor::** [[EVD - LDA-powered measure of ambiguity significantly predicted crowd workers' judgment of sentence ambiguity - @mcmahanAmbiguityEngagement2018]]

###### References

[[July 12th, 2021]]

- [[@mcmahanAmbiguityEngagement2018]] for [[[[QUE]] - How can we best bridge private vs. public knowledge?]] | word ambiguity in scholarly abstracts correlated with decreased fragmentation of resulting citations; idea of ambiguity stimulating engagement as a positive outcome

    - # #inspectionalread

        - Key concepts:

            - ambiguity

                - [[semantic noise]]

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FnSVOOEXhCw.png?alt=media&token=98ff09c4-aaa4-4627-ac6d-fd307ba6458b)

            - [[[[PTN]] - boundary object]]

            - culture (as applied to science and scholarship)

                - maybe similar to [[@cetinaEpistemicCulturesHow1999]]?

        - Approach

            - Coming from sociological background and stance (in American Journal of Sociology), but is computational social science

            - Draws on [[information theory]], including [[@shannonMathematicalTheoryCommunication1948]] and [[Shannon Entropy]].

                - Shannon and Weaver 1963 is key ref

        - Claimed contributions

            - model of ambiguous expression in scholarly literature

            - results that show how ambiguity acts like a [[[[PTN]] - boundary object]] that stimulates social learning (not sure how this is going to be shown)

    - # Implications / Discussion

        - Authors want to claim that reductions in ambiguity could be bad for science bc they reduce fragmentation. And therefore we should be careful about trying to remove ambiguity.

            - But I'm not entirely convinced, for two reasons.

                - Effect size here is very small.

                - Not clear to me that fragmentation per se is bad - feel like we need to have a sense of useful "set points" or equilibria for this parameter.

                    - See, e.g., suggestions of [[Zollman Effect]]

            - In favor of this:

                - ideas around [[🧱 sensemaking]] and [[[[PTN]] - incremental formalization]] (see, e.g., [[@shipmanFormalityConsideredHarmful1999]])

                - phenomenon of [[Scatter]] is thought to be [major reason interdisciplinarity is hard]([[[[CLM]] - Interdisciplinary synthesis is hard because of scatter in the literature]])

                - Representing ideas more abstractly in terms of [[Schemas]] in can facilitate [analogical]([[analogy]]) transfer

        - Other connections/seeds for thought

            - Against "objectivity theater" (h/t [[Alan (Red) Ransil]])

            - What are the implications here for [[interoperability]], maybe vs. standardization?

                - Cc [[[[CLM]] - Knowledge is fundamentally contextual]] and potentially [[[[CLM]] - Universal Semantic Webs are neither feasible nor useful]]

                    - Past thinking on this:

                        - A fundamental uncertainty is whether the relatively formalized nature of [[[[PTN]] - discourse graph]] can be integrated with the open-ended, seemingly unstructured, backtrack-ridden, speculative and "half-baked" nature of thinking that underlies real synthesis (see [[@gruberDarwinManPsychological1974]] for vivid descriptions of this). Some past work on whether/how formality can be integrated into systems for supporting thinking suggests there is a real danger that imposing such formalisms may yield more harm (e.g., by cutting off speculative lines of inquiry, imposing too much overhead) than benefits in settings characterized by context-dependent, evolving requirements for formal structure, such as creative knowledge work in uncharted domains (see [[@shipmanFormalityConsideredHarmful1999]] for an excellent introduction to this). A related danger is that the kinds of knowledge that is necessary for

            - Really [fun example](Bookmarking [[@ceccarelliShapingScienceRhetoric2001]] for later reading, on how [[ambiguity]] in [[synthesis]] can spur the creation of new interdisciplinary fields: example here is the claim that ambiguous metaphors in Erwin Schrodinger's synthesis in 1944 was instrumental in sparking the birth of molecular biology) of Schrodinger's "unoriginal and untrue" lectures catalyzing molecular biology, discussed further in [[@ceccarelliShapingScienceRhetoric2001]]

        - Complaints

    - # Methods

        - [[ambiguity]] operationalized as word synonym entropy

            - define as posterior distribution over pr(M | t, c) (probability of each possible meaning for a given token in a given context) - see Appendix A (how to build "meaning graph" for each token), and Appendix B (how to estimate ambiguity)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyJ2BvBP1aJ.png?alt=media&token=06e19e17-993e-43dc-9095-47215d99ff63)

                - very similar to [[LDA]]

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkBZZ_HTTGv.png?alt=media&token=1b9f4a7c-5f25-4555-82c0-4f2785d46fb6) (p. 898)

            - meaning simplified to proxy into synonyms from Moby and WordNet thesauri

                - would prefer to define as cliques in synonym graph, but... for reasons, decided to simplify to just directed edges + the neighborhood

            - validated against human judgments (see Appendix C)

            - examples (from data)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FgI8AhKGeTl.png?alt=media&token=ae39c2be-5b06-48f4-bb34-4216808fc838) (p. 885)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FjNbxETh3nc.png?alt=media&token=7bf4a619-0ca2-4960-81e6-cc1096a24ba9)

        - "engagement" operationalized as graph entropy over subgraph from each article for max (1k cites, 3 recursive runs), computed in terms of maximal [[network modularity]] (intuitively, a kind of "cliqueiness" or fragmentation, so higher here = lower engagement, i think)

            - examples (from data):

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKUb7aKx_yi.png?alt=media&token=d9e03062-c18f-432c-896a-32a3062151ed)

            - network modularity correlated at -.76 with topological entropy for random sample of 1.2k abstracts

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzWrx4znKTB.png?alt=media&token=ac0e15f3-3cfc-4454-82ab-bf0acb1a3689) (p. 880)

            - toy example:

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FAUmk1jo2Ua.png?alt=media&token=c9ed7651-5fea-44fe-994a-c769e70cb68d)

        - sample: ~1.1M abstracts from Web of Science (after trimming for min. threshold citations, and at least 5 usable terms for ambiguity measure in abstract)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6swfV2e5lD.png?alt=media&token=663be791-00fa-43a8-939e-16b1e2b3839b) (p. 880 - 881)

    - # Key claims and results

        - [[[[CLM]] - ambiguity in scholarly communication facilitates within- and cross-field integration of discourse - [[@mcmahanAmbiguityEngagement2018]]]]

            - [[SupportedBy]]

                - [[[[EVD]] - increased word ambiguity in abstracts was associated with slightly lower modularity of citation networks for those abstracts - [[@mcmahanAmbiguityEngagement2018]]]]

                - [[[[CLM]] - ambiguity can be measured using word-level synonym entropy - [[@mcmahanAmbiguityEngagement2018]]]] (warrant)

                    - see Appendix C

                    - [[[[EVD]] - LDA-powered measure of ambiguity significantly predicted crowd workers' judgment of sentence ambiguity - [[@mcmahanAmbiguityEngagement2018]]]]

    - # Misc notes

        - There's something really important here, I think, about the connection between ambiguity and generativity... more than you can credibly claim

            - Makes me think also of the [[[[CLM]] - Expert designers are solution-oriented]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FFF9L7fI31t.png?alt=media&token=344f5a8a-467d-43f8-a5ad-fbe5ca4e3935) (p. 867)

        - And something else about collective uncertainty: bringing a space together

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FxhG27IkPN9.png?alt=media&token=55fb4f15-7adf-4c47-96da-cf1de55b9d0d)

        - Bookmarking [[@ceccarelliShapingScienceRhetoric2001]] for later reading, on how [[ambiguity]] in [[synthesis]] can spur the creation of new interdisciplinary fields: example here is the claim that ambiguous metaphors in Erwin Schrodinger's synthesis in 1944 was instrumental in sparking the birth of molecular biology

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fehxr8yC9Az.png?alt=media&token=c9bba4d7-f9a0-4d3b-b4fe-4312d095fa9c)

            - relevant for [[[[QUE]] - What are the most efficient routes to useful cross-boundary knowledge?]]: answer here is - sometimes through inspirational public syntheses that are both unoriginal and untrue????

            - and also there is something here about [[[[CLM]] - Paths to creative breakthroughs are frequently oblique]]: look at this! objectively speaking, schrodinger's book/lecture was both unoriginal and untrue!!! but yet it had a really big impact!!! why???

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FEwF8ALOHO-.png?alt=media&token=c2a9fb8f-d883-4823-9fc4-c2300c9b013a) (p. 67)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FPg8rJHUtFG.png?alt=media&token=c36ea158-9027-4a0e-b391-1531cc57dd54) (p. 67)

        - Came across this note in Evernote from [[February 26th, 2019]] in google search:

            - Not published yet. Key finding: jargon can balkanize field, hindering integration, but not always. Scientists' awareness of other work is independent of their ability to understand it.

        - Example of ambiguity and engagement: [[social capital]] facilitates conversations between sociology and economics

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fi0vtFM_k2U.png?alt=media&token=dbff99ed-16ac-4881-bde2-ee922e218b73)

        - Scope of claim: social/human "sciences" only, or also natural sciences? Authors want to go further than just human sciences.

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FejbUC9dxv8.png?alt=media&token=1950275c-3416-466c-b4ea-efaf346bf16d)

    - # Goals

        - understand possible positive functions of ambiguity in scholarly discourse

        - figure out a way to quantitatively study this question!
[[July 12th, 2021]]

- [[[[CLM]] - ambiguity can be measured using word-level synonym entropy - [[@mcmahanAmbiguityEngagement2018]]]] (warrant)

    - see Appendix C

    - [[[[EVD]] - LDA-powered measure of ambiguity significantly predicted crowd workers' judgment of sentence ambiguity - [[@mcmahanAmbiguityEngagement2018]]]]
[[July 12th, 2021]]

- [[[[CLM]] - ambiguity in scholarly communication facilitates within- and cross-field integration of discourse - [[@mcmahanAmbiguityEngagement2018]]]]

    - [[SupportedBy]]

        - [[[[EVD]] - increased word ambiguity in abstracts was associated with slightly lower modularity of citation networks for those abstracts - [[@mcmahanAmbiguityEngagement2018]]]]

        - [[[[CLM]] - ambiguity can be measured using word-level synonym entropy - [[@mcmahanAmbiguityEngagement2018]]]] (warrant)

            - see Appendix C

            - [[[[EVD]] - LDA-powered measure of ambiguity significantly predicted crowd workers' judgment of sentence ambiguity - [[@mcmahanAmbiguityEngagement2018]]]]
[[QUE - How can we best bridge private vs. public knowledge]]

- [[@mcmahanAmbiguityEngagement2018]]

    - Ambiguity in language can be helpful for integrating work: even [[Charles Darwin]] and [[Thomas Kuhn]] were examples of work where language was ambiguous, and this ended up having positive effects on the science
[[February 3rd, 2021]]

- Here is the paper [[@mcmahanAmbiguityEngagement2018]]

    - They make an explicit connection to [[[[PTN]] - boundary object]]s!

    - I think the lesson here is: if you try to pretend the ambiguity doesn't exist, or force it to go away (necessary maybe for machine Reasoning over Knowledge Graph), then you run into problems
