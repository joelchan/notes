---
title: [[CLM]] - Vector-space models of language struggle with relational similarity
url: https://roamresearch.com/#/app/megacoglab/page/kbaLG0Pl8
author: Joel Chan
date: Fri May 22 2020 11:05:34 GMT-0400 (Eastern Daylight Time)
---

- #[[🌲 zettels]]

    - Tags: #[[D/Computational Analogy]] #[[Z]]

    - Description

        - [[@schwartzSymmetricPatternsCoordinations2016]] reported that a [skip-gram model](((4xz52frAQ))) with vanilla BOW contexts performed ~50% worse on verbs compared to nouns and adjectives in terms of predicting [human similarity judgments on SimLex999](((n3Xi0Tp0B)))

        - Another example: word2vec and glove did really well with four-term analogy word problems that were based on case relations, but really struggled with problems based on similarity, contrast, non-attribute relations, and causal relationships [[@chenEvaluatingVectorspaceModels2017]]

        - although this provocative paper [[@linWhyDoesDeep2017]], which i dont' fully understand yet, suggests there might be something about the family of functions that deep learning approximates, that is well-tuned to certain kinds of phenomena, and not others: basically argues that success of deep/cheap learning hinges on the shared physics properties of processes it is good at modeling (i.e., symmetry, locality, polynomial log-probability in data)

            - makes me wonder: are words/sentences compositional, local, symmetrical in the same sense as images?

            - some work on [[relational categories]] (e.g., [[@gentnerRelationalCategories2005]]), suggests these properties might hold better for some kinds of words/sentences (e.g., nouns or [[entity categories]]) than others (e.g., verbs, [[relational categories]])

            - more thoughts here: [what we're learning about openIE, KB, BOW stuff](https://docs.google.com/document/d/1TfLHKx0UoDY5MPIaYr4xvBd6b21K7IhR5qwOlhkz5QQ/edit?usp=sharing)

            - it's not clear to me that this is a fundamental limitation of the model itself (e.g., the optimization objective of predicting a masked word given its context, for example).

                - could well be the data it's trained on

                - there's some evidence that if you change the type of context used for training, you can close some of the gap between "[[entity categories]]" and "[[relational categories]]"

                    - for example, [[@schwartzSymmetricPatternsCoordinations2016]] showed that [skip-gram model](((4xz52frAQ))) with [[symmetric pattern contexts]][*](((b_Wq1X-o3))) performed about as well on verbs compared to sg-bow predictions for nouns and adjectives in terms of predicting [human similarity judgments on SimLex999](((n3Xi0Tp0B))); there was a slight reduction in performance for nouns with sg model using symmetric pattern contexts

        - Counterexample: [[@luEmergenceAnalogyRelation2019]]
- 

###### Discourse Context

- **Informs::** [QUE - Can deep learning discover analogical representations.md](QUE - Can deep learning discover analogical representations.md)
- **Informed By::** [@luEmergenceAnalogyRelation2019.md](@luEmergenceAnalogyRelation2019.md)
- **Informed By::** [@chenEvaluatingVectorspaceModels2017.md](@chenEvaluatingVectorspaceModels2017.md)
- **Informed By::** [@schwartzSymmetricPatternsCoordinations2016.md](@schwartzSymmetricPatternsCoordinations2016.md)
- **Informed By::** [@gentnerRelationalCategories2005.md](@gentnerRelationalCategories2005.md)
- **Informed By::** [@linWhyDoesDeep2017.md](@linWhyDoesDeep2017.md)

