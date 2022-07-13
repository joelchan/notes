---
title: @brownLanguageModelsAre2020
url: https://roamresearch.com/#/app/megacoglab/page/FOlF6PJzi
author: Jason Ding
date: Thu Nov 04 2021 19:46:28 GMT-0400 (Eastern Daylight Time)
---

- Title: Language Models are Few-Shot Learners
- Meta:

    - Tags: #ref/Paper

    - Authored by::  [[[Tom B. Brown]], et al.

    - Year: [[2020]]

    - URL: [Brown et al. (2020) Language Models are Few-Shot Learners.](https://arxiv.org/abs/2005.14165)

    - Citekey: brownLanguageModelsFew2020
- Content

    - Abstract

        - Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.
- Title:: Language Models are Few-Shot Learners
- Author(s):: [[Tom B. Brown]], [[Benjamin Mann]], [[Nick Ryder]], [[Melanie Subbiah]], [[Jared Kaplan]], [[Prafulla Dhariwal]], [[Arvind Neelakantan]], [[Pranav Shyam]], [[Girish Sastry]], [[Amanda Askell]], [[Sandhini Agarwal]], [[Ariel Herbert-Voss]], [[Gretchen Krueger]], [[Tom Henighan]], [[Rewon Child]], [[Aditya Ramesh]], [[Daniel M. Ziegler]], [[Jeffrey Wu]], [[Clemens Winter]], [[Christopher Hesse]], [[Mark Chen]], [[Eric Sigler]], [[Mateusz Litwin]], [[Scott Gray]], [[Benjamin Chess]], [[Jack Clark]], [[Christopher Berner]], [[Sam McCandlish]], [[Alec Radford]], [[Ilya Sutskever]], [[Dario Amodei]]
- Abstract:: Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.
- Type:: [[Article]]
- Publication:: arXiv:2005.14165 [cs]
- URL : http://arxiv.org/abs/2005.14165
- Date Added:: [[July 31st, 2021]]
- Zotero links:: [Local library](zotero://select/groups/2451508/items/J2CBTDKN), [Local library](https://www.zotero.org/groups/2451508/items/J2CBTDKN)
- Tags:: #[[Computer Science - Computation and Language]]
- [[Notes]]

    - Comment: 40+32 pages

###### Discourse Context

- **Informs::** [[CLM - transformer language models have some analogical reasoning ability]]
- **Informs::** [[QUE - Can deep learning discover analogical representations]]
- **Informs::** [[QUE - What do we know about transformer language models' natural language generation capabilities]]

###### References

[[December 1st, 2021]]

- material: machine-generated with [[sys/GPT-2]] and [[sys/GPT-3]] via "three-shot" setting from [[@brownLanguageModelsAre2020]], with default temperature param (0.7)

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCiawOljogK.png?alt=media&token=75dcc940-4d38-4a2a-b4b7-80c084264e34)
[[November 16th, 2021]]

- We'll start with [[@brownLanguageModelsAre2020]]

    - Hmm interesting - here they seem to anticipate later results on potential advantages of *fewer* (and maybe no???) examples for [[few-shot learning]]? Here they discuss the hypothesis that brittleness and vulnerability to adversarial attacks might grow larger as the training data grows: [[[[CL]] - Potential to exploit spurious correlations in training data fundamentally grows with expressiveness model and narrowness of training distribution]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F-PPevoPi2O.png?alt=media&token=d480395a-2198-4eb0-bc0a-ccf9029e54a2) (p. 3)

    - The basic intuition for how the language models work:

        - I don't full understand the details yet of how the training and the model for [[sys/GPT-3]] work. But I do know that:

            - The architecture is a [[transformer architecture]]

                - One of the secret sauces is [[self-attention]], which helps with the problem of updating weights appropriately for connections to context beyond the immediate surroundings of a word/token

                    - Original source for this is [[@vaswaniAttentionAllYou]]

            - The encoding of words/tokens is [[Byte-Pair Encoding (BPE)]]

                - in this way it reminds me of [[charNN]] architectures

            - It's the same basic architecture as [[sys/GPT-2]], which is described in [Radford et al. (2019)]([[@radfordLanguageModelsAre2019]])

            - [[dataset/Common Crawl]] is the base, but with some mods:

                - filtering for "quality" (see Appendix A)

                - fuzzy deduplication (see Appendix A)

                - enriching with some other curated datasets, e.g., WEbText, Wikipedia

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ff-olxLm3nt.png?alt=media&token=61808470-eeac-4eaf-809e-7da99bba0901) (p. 8)

        - They are trained in an unsupervised fashion to basically do one task: predict some word(s)/token(s) of set size M based on some context of word(s)/token(s) of set size N.

    - Technically what distinguishes the [[few-shot learning]] paradigm from [[fine-tuning]] is that you basically condition the output with some demonstrations and instructions, but don't allow any weight updates (so the underlying model is fundamentally the same)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft426DcxvAq.png?alt=media&token=4a311fb0-6fdd-4e2a-88ea-8c01b276e2ad) (p. 6)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQRpWGIQXPo.png?alt=media&token=38b562e0-f2e0-4168-b93b-9644ba23823f) (p. 7)
[[QUE - What do we know about transformer language models' natural language generation capabilities]]

- And some good video explainers/discussion of [[@brownLanguageModelsAre2020]] and [[sys/GPT-3]]

    - WE GOT ACCESS TO GPT-3! (With [[Gary Marcus]], Walid Saba and [[Connor Leahy]]) - YouTube: https://www.youtube.com/watch?v=iccd86vOz3w

        - Note: [[Connor Leahy]] is the guy who recreated GPT-3 when OpenAI was still going back and forth about releasing the models

        - Connor mentions at ~01:31:40 that [[sys/GPT-3]] does surprisingly well at poems, and poorly at math, and he suspects it's because of "the BPE" thing

            - Digging, this is [[Byte-Pair Encoding (BPE)]], which I got from here: The GPT-3 Architecture, on a Napkin: https://dugas.ch/artificial_curiosity/GPT_architecture.html

                - And links to this: https://huggingface.co/transformers/tokenizer_summary.html#byte-pair-encoding

                    - Which is... really really interesting. the base tokens aren't actually words, but byte (character) groups

                - > For efficiency, GPT-3 actually uses byte-level Byte Pair Encoding (BPE) tokenization. What this means is that "words" in the vocabulary are not full words, but groups of characters (for byte-level BPE, bytes) which occur often in text. Using the GPT-3 Byte-level BPE tokenizer, "Not all heroes wear capes" is split into tokens "Not" "all" "heroes" "wear" "cap" "es", which have ids 3673, 477, 10281, 5806, 1451, 274 in the vocabulary. [Here](https://huggingface.co/transformers/tokenizer_summary.html) is a very good introduction to the subject, and a [github implementation](https://github.com/huggingface/tokenizers) so you can try it yourself.

    - GPT-3: Language Models are Few-Shot Learners (Paper Explained) - YouTube: https://www.youtube.com/watch?v=SY5PvZrJhLE
