---
title: @cohanSPECTERDocumentlevelRepresentation2020
url: https://roamresearch.com/#/app/megacoglab/page/0Q9ohSiFm
author: Joel Chan
date: Wed Jan 13 2021 18:06:22 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: SPECTER: Document-level Representation Learning using Citation-informed Transformers

    - Meta:

        - Authored by:: [[Arman Cohan]] [[Sergey Feldman]] [[Iz Beltagy]] [[Doug Downey]] [[Daniel S. Weld]]

        - Year: [[2020]]

        - Publication: arXiv:2004.07180 [cs]

        - Zotero link: [Zotero Link](zotero://select/items/1_I83JVMAB)

        - URL: [Cohan et al. (2020). SPECTER: Document-level Representation Learning using Citation-informed Transformers. arXiv:2004.07180 [cs]](http://arxiv.org/abs/2004.07180)

    - Content

        - Abstract

            - Representation learning is a critical ingredient for natural language processing systems. Recent Transformer language models like BERT learn powerful textual representations, but these models are targeted towards token- and sentence-level training objectives and do not leverage information on inter-document relatedness, which limits their document-level representation power. For applications on scientific documents, such as classification and recommendation, the embeddings power strong performance on end tasks. We propose SPECTER, a new method to generate document-level embedding of scientific documents based on pretraining a Transformer language model on a powerful signal of document-level relatedness: the citation graph. Unlike existing pretrained language models, SPECTER can be easily applied to downstream applications without task-specific fine-tuning. Additionally, to encourage further research on document-level models, we introduce SciDocs, a new evaluation benchmark consisting of seven document-level tasks ranging from citation prediction, to document classification and recommendation. We show that SPECTER outperforms a variety of competitive baselines on the benchmark.

###### Discourse Context



###### References

[[January 13th, 2021]]

- Online evals like [[@cohanSPECTERDocumentlevelRepresentation2020]] are powerful, but... they don't differentiate between staying within and crossing knowledge boundaries.

    - They *might* be able to (and if we could get our hands on data, we could maybe explore those distinctions, but there is a lot of "usage" that we can't see that we would really need to understand what is going on)

    - What we want to know is the latter: to what extent, under what conditions is it possible to use literature discovery tools *alone* to cross boundaries? And/or where do they sit in the stream of practices for *actually* crossing boundaries?

        - On the flip side, what are the relevant "metrics of success"? Where are the best spots to "cut off" and sample and observe what is happening? And even amongst people, what variations might we describe in efficacy? And where might literature discovery tools like ours fit in?

        - In fact, in many cases we can think of, they might play almost no role at all! You bump into someone at a conference and get recommended some stuff to read and some ideas to consider. You go to a workshop expressly because it's interdisciplinary, and get exposed to new ideas there. Where might search engines fit in?
