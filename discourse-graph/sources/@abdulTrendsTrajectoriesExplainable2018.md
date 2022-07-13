---
title: @abdulTrendsTrajectoriesExplainable2018
url: https://roamresearch.com/#/app/megacoglab/page/tLR0eAc3d
author: Joel Chan
date: Sun Aug 23 2020 16:25:45 GMT-0400 (Eastern Daylight Time)
---

- #references

    - Title: Trends and Trajectories for Explainable, Accountable and Intelligible Systems: An HCI Research Agenda

    - Meta:

        - Tags: #ref/Paper #ref/Review #[[P/Material Knowledge of ML for Design]]

        - Authored by::  Ashraf Abdul ,  Jo Vermeulen ,  Danding Wang ,  Brian Y. Lim ,  Mohan Kankanhalli

        - Year: [[2018]]

        - Publication: Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems  - CHI '18

        - URL: http://dl.acm.org/citation.cfm?doid=3173574.3174156

        - Citekey: abdulTrendsTrajectoriesExplainable2018

    - Content

        - Placeholder

        - Abstract

            - Advances in artificial intelligence, sensors and big data management have far-reaching societal impacts. As these systems augment our everyday lives, it becomes increasingly important for people to understand them and remain in control. We investigate how HCI researchers can help to develop accountable systems by performing a literature analysis of 289 core papers on explanations and explainable systems, as well as 12,412 citing papers. Using topic modeling, co-occurrence and network analysis, we mapped the research space from diverse domains, such as algorithmic accountability, interpretable machine learning, context-awareness, cognitive psychology, and software learnability. We reveal fading and burgeoning trends in explainable systems, and identify domains that are closely connected or mostly isolated. The time is ripe for the HCI community to ensure that the powerful new autonomous systems have intelligible interfaces built-in. From our results, we propose several implications and directions for future research towards this goal.

    - #[[📝 lit-notes]]

        - [[Wei-Wei Chi]]

            - there seems to be a usability gap between work that's done in AI/ML on [[explainable AI]] and what "real users" can understand and do something with

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FnmzHOollZ6.png?alt=media&token=c88eecf9-010e-45d7-ada0-46042196d6f8) (p. 1)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FavfS-FYEyv.png?alt=media&token=e036e1f0-6a0b-4100-85a2-517657ab1ee8)  (p. 2)

                - not sure what "real" users means: seems like when they say "real users" they really mean less technical people???

                    - possible connections to [[SEO]] - not a lot of "rigorous" rules/explanations, but a LOT of hacking around, sharing case studies, heuristics and best practices??

                        - this is what [[Wei-Wei Chi]] learned in undergrad (marketing, specializing in SEO and digital marketing)

                - cited thse papers

                    - 50: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FEBAPhG2H9d.png?alt=media&token=39d3dc5b-f0e4-4e6f-8129-96a6a3635484)

                    - 100: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F351N2FdTJT.png?alt=media&token=8a2b9da4-70a8-4016-a797-c882c1c14476)

                    - 132: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_dUF-xEe37.png?alt=media&token=766ce7ce-973a-4774-b4ae-424d03225938)

            - possibly explaining the usability gap, research on [[explainable AI]] in AI/ML tends to be disconnected from the [[HCI]] community

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb53K0lAv9b.png?alt=media&token=85d397f3-bb6a-4051-8eeb-520713dbd661) (p. 2)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FwjtmGm4UhP.png?alt=media&token=81748724-fcf0-4ccb-b479-6d910f21f6a2) (p. 4)

        - [[Joel Chan]]

###### Discourse Context



###### References

[[October 12th, 2020]]

- {{[[TODO]]}} Lit notes on [[@abdulTrendsTrajectoriesExplainable2018]] for joint processing next meeting

    - Rationale: our perspective on [[material knowledge]] has [[explainable AI]] as a major [[SOTA]] to build off of (what is "left out" from explainability? at a high level can map to the "explicit" dimension of knowledge, what can be formally shown and explicitly described)

    - Note also that the [[machine teaching]] approach is another SOTA competitor to the overall framing that [[material knowledge]] is important for design: could become obsolete, if this pathway really works!

        - In the limit also, this line of research assumes that you do *NOT* need [[material knowledge]] of ML, only your domain, if the system works well enough (h/t [[Wei-Wei Chi]])
[[October 26th, 2020]]

- re: [[@abdulTrendsTrajectoriesExplainable2018]] cc [[Q: What is perceptual / material knowledge and how does it matter for creative work?]]

    - issues:

        - [[@yangDesignAIProducts2020]] seems to be much more about the material properties of a finished ML component

            - whereas last semester, it was more about the essence of what should be taught, at a deeper level of knowledge than what seems to be shallower for designers

        - maybe the nature of the knowledge

        - [[@yangDesignAIProducts2020]] and the UX of AI stuff at [[CSCW2020]] seems to sometimes be more about designing the UX of the user interacting with the system that has ML in it (trust, recovering from errors, accountability, etc.)

            - we're not interested in this

        - we are not targeting the super deep "designing the ML itself" (aka inventing new wood), which undoubtedly requires very deep and rigorous knowledge of the ML, proofs, etc.

        - we *are* interested in situations where you are designing the *system*'s fundamental capabilities when ML is involved (aka designing a new chair with the wood)

    - remindings of last semester

        - [[interactive ML]] seems to be closer to what we're interested in, compared to [[explainable AI]], which almost targets the user of the system directly, more than the designer of the system

            - systems like [[sys/TensorFlow Playground]] are more about helping someone gain intuition about how it works for the purpose potentially of doing something with it (vs., simply understanding a fixed point of what the system did to/for me)

    - eval still seems to be an open challenge, possibly: see [[@kahngHowDoesVisualization2019]] for an example: Eval was basically not really directly targeting knowledge gain at all! They even have a full discussion section saying that needs to be done!

    - potential connections to [[adaptive expertise]]
