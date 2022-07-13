---
title: @chanSOLVENTMixedInitiative2018
url: https://roamresearch.com/#/app/megacoglab/page/K8c6pu1a_
author: Joel Chan
date: Sun Mar 22 2020 15:22:15 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: SOLVENT: A Mixed Initiative System for Finding Analogies between Research Papers

    - Meta:

        - Authored by:: [[Joel Chan]] [[Joseph Chee Chang]] [[Tom Hope]] [[Dafna Shahaf]] [[Aniket Kittur]]

        - Year: [[2018]]

        - Publication: Proceedings of ACM Human-Computer Interaction: CSCW

        - Zotero link: [Zotero Link](zotero://select/items/1_VZ5EKL6B)

        - URL: [Chan et al. (2018). SOLVENT: A Mixed Initiative System for Finding Analogies between Research Papers. Proceedings of ACM Human-Computer Interaction: CSCW](undefined)

    - Content

        - Abstract

            - Scientific discoveries are often driven by finding analogies in distant domains, but the growing number of papers makes it difficult to find relevant ideas in a single discipline, let alone distant analogies in other domains. To provide computational support for finding analogies across domains, we introduce SOLVENT, a mixed-initiative system where humans annotate aspects of research papers that denote their background (the high-level problems being addressed), purpose (the specific problems being addressed), mechanism (how they achieved their purpose), and findings (what they learned/achieved), and a computational model constructs a semantic representation from these annotations that can be used to find analogies among the research papers. We demonstrate that this system finds more analogies than baseline information-retrieval approaches; that annotators and annotations can generalize beyond domain; and that the resulting analogies found are useful to experts. These results demonstrate a novel path towards computationally supported knowledge sharing in research communities

    - #lit-context

        - embeddings

            - TF-IDF-weighted average of embeddings from [[doc2vec]] model with 600D trained on ~4000 CHI/CSCW papers from 2010 - 2017

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkhYtHaHvfw.png?alt=media&token=32b11865-e018-4004-84b6-fc3d31eb8999) (p. 8)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUi3Ep6p7y3.png?alt=media&token=04de7dd8-7874-400d-a897-da956857664a) (p. 6)

        - dataset

        - ground truth analogies between research papers

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fqrg6032YlJ.png?alt=media&token=c8fe360d-b92c-4e3e-bc56-123092b2783b) (p. 9)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fz5G6xlwmlh.png?alt=media&token=39729138-acd0-43cc-ae61-1a93e87b8d89)(p. 10)

    - #[[📝 lit-notes]]

        - cosine distance between embeddings from spans labeled by humans for purpose/mechanism was able to achieve precision@5 of .7 for recovering "ground truth" analogies between research papers, compared to cosine distance between embeddings for all words in the abstract (precision@5 = ~.67)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FTLhymXMfea.png?alt=media&token=930e34f7-7a25-45e9-92a2-f5ee26ef9d09)

###### Discourse Context

- **Informs::** [[CLM - People rapidly reject analogical matches when there is a clear attribute mismatch]]
- **Informs::** [[CLM - Core attribute mismatches in analogical inspiration harm creativity]]
- **Informs::** [[QUE - How can we augment scientific creativity with computational analogy]]

###### References

[[QUE - How can we augment scientific creativity with computational analogy]]

- I'm a bit nervous about these numbers because we're still using the CSCW 50 papers from [[@chanSOLVENTMixedInitiative2018]] as our test set. This is a low-hanging fruit thing that is worth exploring further, and we'll need much more data for this

    - can reach out ot [[Kenneth Huang]] who has ~11k COVID-19 papers annotated

        - caveat is that purpose accuracy is... not great - F of about .6

        - not sure how this intersects with genre stuff though... important open question and threat for our approach. we're making a major assumption that enough of what we need is in abstracts. is that true?

            - could be nuanced: abstract could be enough for purpose

            - but other stuff we need to get from

                - full-text

                - citation statements

                - etc

        - --> [[dataset/CODA-19]]

            - https://twitter.com/windx0303/status/1258427687191883778

        - also shows later in [[@huangCODA19UsingNonExpert2020]] that [[sys/SciBERT]] actually does a really good job, about .7ish as well

        - some nice comments in a submission here:

            - https://openreview.net/forum?id=XOkm8xdns5R&noteId=KMIbNQ-oqQK
[[WP Augmenting scientific creativity with analogical inspirations]]

- The [prediction model]([[SpanRel]] model with spans of up to 3-tokens long (majority vote label from the component tokens in each span), fine-tuned [[ELMo]] 5.5B embeddings as features, L2 regularizer, and Adam optimizer, with a .001 learning rate, batch size of 32, and dropout rate of 0.3) achieved F1 scores of about .64 when predicting purpose/mechanism spans for the 50 papers in [[@chanSOLVENTMixedInitiative2018]], annotated by experts

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F36f_QbCHs6.png?alt=media&token=0b99d205-4254-4eda-9192-62af68ef552e)
[[July 2nd, 2021]]

- [[@chanSOLVENTMixedInitiative2018]] (I know we shared this dataset, so should be straightforward to track down

    - can draw the papers from here: https://github.com/oasisresearchlab/knowledge-collider/tree/master/author-sourcing/use-labels/use-labels-pipeline (have to stitch together the titles/abstracts with the analogy pairs)
[[August 20th, 2020]]

- [[Mixed-Initiative]]? expansion on [[@chanSOLVENTMixedInitiative2018]] - success metric - increase / maintain / match annotation quality while reducing time / cost

    - intuition: mixed crowds, maybe a play off of [[data programming]]
[[QUE - How can we augment scientific creativity with computational analogy]]

- And also science papers [[@chanSOLVENTMixedInitiative2018]]

    - New stuff from [[Hyeonsu]], with case study data
[[CLM - People rapidly reject analogical matches when there is a clear attribute mismatch]]

- Some related examples of this, e.g., with concrete materials, in our case study in [[@chanSOLVENTMixedInitiative2018]]

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F9Ij8F-s10Y.png?alt=media&token=d43b5ab4-7ccb-4b0f-84d8-827c7a0088a5)
[[November 10th, 2020]]

- q: how confident are we in [[@chanSOLVENTMixedInitiative2018]] results?

    - limitations:

        - doesn't tell us about
