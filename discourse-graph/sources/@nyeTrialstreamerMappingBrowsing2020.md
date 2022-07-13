---
title: @nyeTrialstreamerMappingBrowsing2020
url: https://roamresearch.com/#/app/megacoglab/page/b3geQJUqR
author: Joel Chan
date: Thu Mar 24 2022 20:51:19 GMT-0400 (Eastern Daylight Time)
---



###### Discourse Context



###### References

[[Week of March 21st, 2022]]

- [[@nyeTrialstreamerMappingBrowsing2020]]

    - from [[Ani Nenkova]] and [[Byron Wallace]], building on their work with [[sys/RobotReviewer]]

        - notes I sent on this to the [[org/JellyPBC]] slack

            - seems like SOTA is still working from abstracts, not many folks at all working on full-text, in part bc of difficulty of scaling training data (our superpower)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzvTuiYhSoi.png?alt=media&token=68c151d2-bde2-428b-a70e-26c51f17433c)

            - > the system extracts descriptions of trial participants, the treatments compared in each arm (the __interventions__), and which outcomes were measured. The system then attempts to infer which interventions were reported to work best by determining their relationship with identified trial outcome measures. In addition to summarizing individual trials, these extracted data elements allow automatic synthesis of results across many trials on the same topic. We apply the system at scale to all reports of randomized controlled trials indexed in MEDLINE, powering the automatic generation of __evidence maps__, which provide a global view of the efficacy of different interventions combining data from all relevant clinical trials on a topic. We make all code and models freely available alongside a demonstration of the web interface

            - SOTA is F1 of ~.7 (precision way lower than recall in their formulation, might be task-specific optimization). this feels about right, and gives a sense of the difficulty of the problem even with these constraints (only RCTs, only medical)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDdarxyd5qV.png?alt=media&token=a0634916-56cc-44a7-af78-5f228d61ee08)
