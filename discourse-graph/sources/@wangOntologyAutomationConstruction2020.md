---
title: @wangOntologyAutomationConstruction2020
url: https://roamresearch.com/#/app/megacoglab/page/dS_Ij9maI
author: Joel Chan
date: Tue Oct 27 2020 16:34:06 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: An ontology automation construction scheme for Chinese e-government thesaurus optimizing

    - Meta:

        - Authored by:: [[Hao Wang]] [[Wei Zhang]] [[Sanhong Deng]] [[Baolong Zhang]]

        - Year: [[2020]]

        - Publication: Proceedings of the Association for Information Science and Technology

        - Zotero link: [Zotero Link](zotero://select/items/1_NMVKJ7UJ)

        - URL: [Wang et al. (2020). An ontology automation construction scheme for Chinese e-government thesaurus optimizing. Proceedings of the Association for Information Science and Technology](https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/pra2.243)

    - Content

        - Abstract

            - To optimize the term hierarchy in the manual e-government thesaurus, we combine the mainstream knowledge organization technology to form a complete set of ontology automation construction scheme. We build an e-government knowledge base by using subject words in the Comprehensive E-government Thesaurus as the term set and encyclopedia text as the corpus. The specific work includes the extraction of semantic features from the bag-of-words model, determination of the number of clusters by linear and nonlinear dimensionality reduction, division of terms by spectral clustering, social network analysis to determine the class label, and storing knowledge ontology via OWL. The recall rate of term hierarchy in the ontology is excellent, indicating the ontology has good knowledge extensibility, and also proving the efficiency of the scheme proposed in this work. Besides, the application model of a term hierarchy in information retrieval can show a richer semantic relation than the original thesaurus to guide the retrieval extension of government information resources.

###### Discourse Context



###### References

[[October 27th, 2020]]

- An Ontology Automation Construction Scheme for Chinese E-government Thesaurus Optimizing [[@wangOntologyAutomationConstruction2020]]

    - Seems relevant for the [[context snapshots]] / [[[[PTN]] - flexible compression]] stuff - input is some set of keywords and raw text, and output is an [ontology]([[ontologies]]).

    - Recall > precision, but overall F1 not too bad, in the 70s

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FfQJSmE0idx.png?alt=media&token=7aaa6348-9bd0-4f68-83f3-a5bdf7b03b8f)

    - What caught my eye was the use of relatively simple methods, like [[TF-IDF]] and [[spectral clustering]]
