---
title: @bosselutCOMETCommonsenseTransformers2019
url: https://roamresearch.com/#/app/megacoglab/page/RXDR90Dqy
author: Joel Chan
date: Thu Apr 30 2020 22:01:47 GMT-0400 (Eastern Daylight Time)
---

- #references

    - Title: COMET: Commonsense Transformers for Automatic Knowledge Graph Construction

        - Tags:: #ref/Paper #[[D/Computational Analogy]]

    - Authored by::  Antoine Bosselut ,  Hannah Rashkin ,  Maarten Sap ,  Chaitanya Malaviya ,  Asli Çelikyilmaz ,  Yejin Choi

    - Year: 2019

    - Publication: ACL

    - URL:

    - PDF

        - :hiccup [:iframe {:width "650px", :height "650px", :src "https://drive.google.com/file/d/1aVC4RdGKVxQWKxd6UkfZHL7HmCrnXzvd/preview"}]
- #lit-context
- #[[📝 lit-notes]]

    - Key figure

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Lj_3UBnU?alt=media&token=34c03a1f-af4c-47cb-b78f-00fc61f3c038)

    - #Claim [[fine-tuning]] pre-trained [[transformer language model]] on a symbolic [[Knowledge Base]] enables it to approach human performance at generating [[common sense]] inferences

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FeAYVLxVtH7?alt=media&token=76f9bd1b-f15d-4b70-9fb4-4a6e089e8efb)

###### Discourse Context



###### References

[[April 30th, 2020]]

- New approach of using [[Embeddings]] (basically do [[fine-tuning]] with a [[Knowledge Base]] on pre-trained [[sys/GPT-2]])  ([[@bosselutCOMETCommonsenseTransformers2019]], described in [[@pavlusCommonSenseComes2020]])

    - The resulting model can predict "inferences" that are like [[common sense]], given some seed sentence

        - Example: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fk5bx88KA--?alt=media&token=e0f891de-22e6-488c-943d-3efc3ccd9c0a)

        - Reminds me of the stuff that [[Andrew McCallum]] does with his [[Knowledge Base]] stuff, using [[Embeddings]] to overcome the fact that [[[[CL]] - Symbolic knowledge bases are brittle]]
