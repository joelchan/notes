---
title: @alammarIllustratedTransformer
url: https://roamresearch.com/#/app/megacoglab/page/lUvhPcj64
author: Joel Chan
date: Sun Aug 02 2020 23:48:31 GMT-0400 (Eastern Daylight Time)
---

- Title:: The Illustrated Transformer
- Author(s):: [[Jay Alammar]]
- Abstract:: Discussions:
Hacker News (65 points, 4 comments), Reddit r/MachineLearning (29 points, 3 comments)


Translations: Chinese (Simplified), Japanese, Korean, Russian

Watch: MIT’s Deep Learning State of the Art lecture referencing this post

In the previous post, we looked at Attention – a ubiquitous method in modern deep learning models. Attention is a concept that helped improve the performance of neural machine translation applications. In this post, we will look at The Transformer – a model that uses attention to boost the speed with which these models can be trained. The Transformers outperforms the Google Neural Machine Translation model in specific tasks. The biggest benefit, however, comes from how The Transformer lends itself to parallelization. It is in fact Google Cloud’s recommendation to use The Transformer as a reference model to use their Cloud TPU offering. So let’s try to break the model apart and look at how it functions.

The Transformer was proposed in the paper Attention is All You Need. A TensorFlow implementation of it is available as a part of the Tensor2Tensor package. Harvard’s NLP group created a guide annotating the paper with PyTorch implementation. In this post, we will attempt to oversimplify things a bit and introduce the concepts one by one to hopefully make it easier to understand to people without in-depth knowledge of the subject matter.

A High-Level Look
Let’s begin by looking at the model as a single black box. In a machine translation application, it would take a sentence in one language, and output its translation in another.
- Type:: [[Webpage]]
- Publication::
- URL : http://jalammar.github.io/illustrated-transformer/
- Date Added:: [[August 1st, 2021]]
- Zotero links:: [Local library](zotero://select/groups/2451508/items/9ZI9DC2H), [Local library](https://www.zotero.org/groups/2451508/items/9ZI9DC2H)

###### Discourse Context

- **Informs::** [[QUE - What do we know about transformer language models' natural language generation capabilities]]
