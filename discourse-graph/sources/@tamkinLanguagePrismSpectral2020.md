---
title: @tamkinLanguagePrismSpectral2020
url: https://roamresearch.com/#/app/megacoglab/page/1CjnC5SV5
author: Joel Chan
date: Thu Dec 03 2020 14:17:02 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Language Through a Prism: A Spectral Approach for Multiscale Language Representations

    - Meta:

        - Authored by:: [[Alex Tamkin]] [[Dan Jurafsky]] [[Noah Goodman]]

        - Year: [[2020]]

        - Publication: arXiv:2011.04823 [cs]

        - Zotero link: [Zotero Link](zotero://select/items/7_NF7ENUQU)

        - URL: [Tamkin et al. (2020). Language Through a Prism: A Spectral Approach for Multiscale Language Representations. arXiv:2011.04823 [cs]](http://arxiv.org/abs/2011.04823)

    - Content

        - Abstract

            - Language exhibits structure at different scales, ranging from subwords to words, sentences, paragraphs, and documents. To what extent do deep models capture information at these scales, and can we force them to better capture structure across this hierarchy? We approach this question by focusing on individual neurons, analyzing the behavior of their activations at different timescales. We show that signal processing provides a natural framework for separating structure across scales, enabling us to 1) disentangle scale-specific information in existing embeddings and 2) train models to learn more about particular scales. Concretely, we apply spectral filters to the activations of a neuron across an input, producing filtered embeddings that perform well on part of speech tagging (word-level), dialog speech acts classification (utterance-level), or topic classification (document-level), while performing poorly on the other tasks. We also present a prism layer for training models, which uses spectral filters to constrain different neurons to model structure at different scales. Our proposed BERT + Prism model can better predict masked tokens using long-range context and produces multiscale representations that perform better at utterance- and document-level tasks. Our methods are general and readily applicable to other domains besides language, such as images, audio, and video.

###### Discourse Context


