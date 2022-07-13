---
title: @dasigiDatasetInformationSeekingQuestions2021
url: https://roamresearch.com/#/app/megacoglab/page/RReUZWjHT
author: Joel Chan
date: Tue Jul 13 2021 10:12:20 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers

    - Meta:

        - Authored by:: [[Pradeep Dasigi]] [[Kyle Lo]] [[Iz Beltagy]] [[Arman Cohan]] [[Noah A. Smith]] [[Matt Gardner]]

        - Year: [[2021]]

        - Publication: Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies

        - Zotero link: [Zotero Link](zotero://select/items/7_2T68G8UV)

        - URL: [Dasigi et al. (2021). A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers. Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies](https://aclanthology.org/2021.naacl-main.365)

    - Content

        - Abstract

            - Readers of academic research papers often read with the goal of answering specific questions. Question Answering systems that can answer those questions can make consumption of the content much more efficient. However, building such tools requires data that reflect the difficulty of the task arising from complex reasoning about claims made in multiple parts of a paper. In contrast, existing information-seeking question answering datasets usually contain questions about generic factoid-type information. We therefore present Qasper, a dataset of 5049 questions over 1585 Natural Language Processing papers. Each question is written by an NLP practitioner who read only the title and abstract of the corresponding paper, and the question seeks information present in the full text. The questions are then answered by a separate set of NLP practitioners who also provide supporting evidence to answers. We find that existing models that do well on other QA tasks do not perform well on answering these questions, underperforming humans by at least 27 F1 points when answering them from entire papers, motivating further research in document-grounded, information-seeking QA, which our dataset is designed to facilitate.

###### Discourse Context



###### References

[[July 13th, 2021]]

- Also want to note here from paper ([[@dasigiDatasetInformationSeekingQuestions2021]]) , three observations:

    - Base performance without gold evidence is.... errrr teens for extractive/abstractive, ~40-60 for yes/no and unanswerable (so ~30ish overall)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkPyM7xsKnd.png?alt=media&token=ffbc2531-bdf4-4c85-9f5d-2f5512806fb8)

    - People >>>>>>> the model for selecting evidence (people ~70, best model ~30)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FctcBBjk80X.png?alt=media&token=cf9e69ae-193d-40f4-8e48-7da7ebcc248d)

    - With gold evidence, performance goes wayyyyy up (yes/no and unanswerable become trivial, extractive/abstractive goes up to ~60ish max), but is still a bit lower than lower bound of human performance

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FlS4GUcwvxY.png?alt=media&token=09900962-e7eb-4d41-b153-4fc456904987)
