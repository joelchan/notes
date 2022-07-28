---
title: [[CLM]] - Vector-space models of language struggle with relational similarity
url: https://roamresearch.com/#/app/megacoglab/page/kbaLG0Pl8
author: Joel Chan
date: Fri May 22 2020 23:05:34 GMT+0800 (Malaysia Time)
---

- [[🌲 zettels]]

    - Tags: [[DComputational Analogy]]

    - Description

        - [[@schwartzSymmetricPatternsCoordinations2016]]

        - Another example: word2vec and glove did really well with four-term analogy word problems that were based on case relations, but really struggled with problems based on similarity, contrast, non-attribute relations, and causal relationships [[@chenEvaluatingVectorspaceModels2017]]

        - although this provocative paper [[@linWhyDoesDeep2017]]

            - makes me wonder: are words/sentences compositional, local, symmetrical in the same sense as images?

            - some work on [[relational categories]]

            - more thoughts here: [what we're learning about openIE, KB, BOW stuff](https://docs.google.com/document/d/1TfLHKx0UoDY5MPIaYr4xvBd6b21K7IhR5qwOlhkz5QQ/edit?usp=sharing)

            - it's not clear to me that this is a fundamental limitation of the model itself (e.g., the optimization objective of predicting a masked word given its context, for example).

                - could well be the data it's trained on

                - there's some evidence that if you change the type of context used for training, you can close some of the gap between "[[entity categories]]

                    - for example, [[@schwartzSymmetricPatternsCoordinations2016]]

        - Counterexample: [[@luEmergenceAnalogyRelation2019]]
- 

###### Discourse Context

- **Informs::** [[QUE - Can deep learning discover analogical representations]]
- **Informed By::** [[@luEmergenceAnalogyRelation2019]]
- **Informed By::** [[@chenEvaluatingVectorspaceModels2017]]
- **Informed By::** [[@schwartzSymmetricPatternsCoordinations2016]]
- **Informed By::** [[@gentnerRelationalCategories2005]]
- **Informed By::** [[@linWhyDoesDeep2017]]
