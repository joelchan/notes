---
title: @linWhyDoesDeep2017
url: https://roamresearch.com/#/app/megacoglab/page/RyneYsQKq
author: Joel Chan
date: Sat Nov 28 2020 16:12:18 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Why does deep and cheap learning work so well?

    - Meta:

        - Authored by:: [[Henry W. Lin]] [[Max Tegmark]] [[David Rolnick]]

        - Year: [[2017]]

        - Publication: Journal of Statistical Physics

        - Zotero link: [Zotero Link](zotero://select/items/1_694HBKAX)

        - URL: [Lin et al. (2017). Why does deep and cheap learning work so well?. Journal of Statistical Physics](http://arxiv.org/abs/1608.08225)

    - Content

        - Abstract

            - We show how the success of deep learning could depend not only on mathematics but also on physics: although well-known mathematical theorems guarantee that neural networks can approximate arbitrary functions well, the class of functions of practical interest can frequently be approximated through "cheap learning" with exponentially fewer parameters than generic ones. We explore how properties frequently encountered in physics such as symmetry, locality, compositionality, and polynomial log-probability translate into exceptionally simple neural networks. We further argue that when the statistical process generating the data is of a certain hierarchical form prevalent in physics and machine-learning, a deep neural network can be more efficient than a shallow one. We formalize these claims using information theory and discuss the relation to the renormalization group. We prove various "no-flattening theorems" showing when efficient linear deep networks cannot be accurately approximated by shallow ones without efficiency loss, for example, we show that $n$ variables cannot be multiplied using fewer than 2^n neurons in a single hidden layer.

    - #lit-context

        - source was twitter post by [[Sebastian Gehrmann]]: might have more commentary there

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FEVlc8ANpz7?alt=media&token=4a2bdaea-74e3-4843-b578-55c3ca588172)

    - #[[📝 lit-notes]]

        - basically argues that success of deep/cheap learning hinges on the shared physics properties of processes it is good at modeling (i.e., symmetry, locality, polynomial log-probability in data)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6wrXDINkYy?alt=media&token=d87b7507-e509-48cc-af4c-90d6c940c033)

###### Discourse Context

- **Informs::** [[CLM - Vector-space models of language struggle with relational similarity]]

###### References

[[CLM - Vector-space models of language struggle with relational similarity]]

- although this provocative paper [[@linWhyDoesDeep2017]], which i dont' fully understand yet, suggests there might be something about the family of functions that deep learning approximates, that is well-tuned to certain kinds of phenomena, and not others: basically argues that success of deep/cheap learning hinges on the shared physics properties of processes it is good at modeling (i.e., symmetry, locality, polynomial log-probability in data)

    - makes me wonder: are words/sentences compositional, local, symmetrical in the same sense as images?

    - it's not clear to me that this is a fundamental limitation of the model itself (e.g., the optimization objective of predicting a masked word given its context, for example).

        - there's some evidence that if you change the type of context used for training, you can close some of the gap between "[[entity categories]]" and "[[relational categories]]"

            - for example, [[@schwartzSymmetricPatternsCoordinations2016]] showed that [skip-gram model](((4xz52frAQ))) with [[symmetric pattern contexts]][*](((b_Wq1X-o3))) performed about as well on verbs compared to sg-bow predictions for nouns and adjectives in terms of predicting [human similarity judgments on SimLex999](((n3Xi0Tp0B))); there was a slight reduction in performance for nouns with sg model using symmetric pattern contexts

        - could well be the data it's trained on

    - some work on [[relational categories]] (e.g., [[@gentnerRelationalCategories2005]]), suggests these properties might hold better for some kinds of words/sentences (e.g., nouns or [[entity categories]]) than others (e.g., verbs, [[relational categories]])

    - more thoughts here: [what we're learning about openIE, KB, BOW stuff](https://docs.google.com/document/d/1TfLHKx0UoDY5MPIaYr4xvBd6b21K7IhR5qwOlhkz5QQ/edit?usp=sharing)
