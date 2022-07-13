---
title: @wallaceExtractingPICOSentences2016
url: https://roamresearch.com/#/app/megacoglab/page/1mralw6Tf
author: Joel Chan
date: Mon Jun 15 2020 23:45:06 GMT-0400 (Eastern Daylight Time)
---

- #references

    - Title: Extracting PICO sentences from clinical trial reports using supervised distant supervision

    - Meta:

        - Tags: #ref/Paper #[[D/Synthesis Infrastructure]]

        - Authored by::  [[Byron Wallace]] ,  Joël Kuiper ,  Aakash Sharma ,  Mingxi Zhu ,  Iain J. Marshall

        - Year: [[2016]]

        - Publication: The Journal of Machine Learning Research

        - URL:

        - Citekey: wallaceExtractingPICOSentences2016

    - Content

        - Placeholder

    - #lit-context

        - first eval was retrospective, on annotated data, any sentence that wasn't in original annotation was deemed irrelevant (even though it might be), so likely to be pessimistic measure of performance

    - #[[📝 lit-notes]]

        - the [[supervised distant supervision]] is also a contribution that can be generalized from the particular domain / task, which is aimed at dealing with [[distant supervision]] situations where you think you might be able to "supervise" the mapper that will provide noisy labels for your dataset based on the external db

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FshY-m7xdqL.png?alt=media&token=a96073a0-7aff-411f-a710-bd4e7d8851f3) (p. 9)

        - in a retrospective evaluation making predictions on 133 manually labeled articles, the [[supervised distant supervision]] approach achieved [[measure/precision]] scores of approximately .3 for population and intervention, and .14 for outcomes, for top 3

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FNTW7rAR1ME.png?alt=media&token=c8d6fda9-21eb-4d33-aaaa-546b3debd386) (p. 19)

            - Advantage of [[supervised distant supervision]] only comes into play when considering top 10 and top 20 results ([[metric/recall]] is probably higher than baselines)

            - But, keep in mind that first eval was retrospective, on annotated data, any sentence that wasn't in original annotation was deemed irrelevant (even though it might be), so likely to be pessimistic measure of performance

        - in a prospective evaluation making predictions for 50 articles, and then having experts manually label the top 3 predictions from each system, the [[supervised distant supervision]] approach achieved [[measure/precision]] @3 scores of approximately .9 for all [[PICO frames]] elements

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkVu3_OTPYO.png?alt=media&token=aae981b7-12c2-4524-8575-e7158191bc42) (p. 21)

###### Discourse Context



###### References

[[June 15th, 2020]]

- TONs of great work in [[NLP]] tools for knowledge base construction and assisting with [[systematic review]]s; one prominent example is [[sys/RobotReviewer]] led by [[Byron Wallace]] -  two cornerstones: automated extraction of [[PICO frames]] (crucially, with grounding / [[context]] in specific text segments in full-text; method described in #[[@wallaceExtractingPICOSentences2016]], as well as automated estimation of "risk of bias"

    - NOTE: the existence of these (increasingly mature) systems is great for us, since:

        - in other words, our innovations will be about the *interface* with the human workflows, not the fundamental computational methods; the less we have to do on that front, the better!

        - they are quite cagey about being fully automated (rightly so!) (cf. #[[@oconnorStillMovingAutomation2019]])

        - we care about integrating these into existing workflows, not replacing human work

    - See also this series of workshops:

        - [BioNLP Workshop - ACL Wiki](https://aclweb.org/aclwiki/BioNLP_Workshop)

        - [1st Workshop on Scholarly Document Processing](https://ornlcda.github.io/SDProc/)

            - #quotes

                - - First Workshop on Scholarly Document Processing

                - Accelerating scientific discovery, informing policy, and educating the public through machine understanding of scientific knowledge

                - We are delighted to announce that [[Steinn Sigurðsson]], Scientific Director of [[arXiv]] and Professor in the Department of Astronomy & Astrophysics at The Pennsylvania State University, will give a keynote presentation at the workshop!

        - [SciNLP: Natural Language Processing and Data Mining for Scientific Text](https://scinlp.org/#registration) (I'm going)

            - #quotes

                - - SciNLP: Natural Language Processing and Data Mining for Scientific Text

                - The primary goal of this half-day workshop is to bring together researchers from diverse fields who are interested in extracting and representing knowledge from scientific text, and/or applications or methods for improving access to and understanding of such knowledge. Such research includes, but is not limited to:

                - Methods in natural language processing and data mining for extracting and representing knowledge from scientific text (e.g. information extraction, entity normalization, discourse analysis, parsing, summarization, text generation, question answering, knowledge base construction, weak/distant supervision, crowdsourcing),

                - Applications of these methods to improving scientific knowledge discovery and/or understanding (e.g. automated literature review, search and recommender systems, techniques for data exploration and visualization),

                - Fairness (e.g. augmented or assistive paper reading, concept simplification, scientific education and literacy),

                - Science of science studies (in particular, studies that shed light on phenomena that can motivate future research in above-mentioned areas), and

                - Datasets, Resources (e.g. treebanks, knowledge bases), and Tools (e.g. software libraries, annotation interfaces) for conducting research in such areas.

                - We welcome research relevant to processing text in any domain of science (e.g. Biology, Medicine, Computer Science, Physics, Economics, Sociology, etc.) that can come from a variety of text sources (e.g. scholarly papers, surveys and technical reports, patents, tweets by scholars, blogs/tutorials, etc.)
[[July 23rd, 2020]]

- reminded today of [[sys/RobotReviewer]], which is evidence of the initial feasibility of obtaining hooks for [[context queries]], at least in the medical domain (see, e.g., [[@wallaceExtractingPICOSentences2016]])

    - they focus on extracting into very structured [[PICO frames]], with [[Risk of Bias scores]], very table-like

        - we can focus on extending this to more exploratory and heterogenous [[synthesis]] tasks
