---
title: [[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?
url: https://roamresearch.com/#/app/megacoglab/page/U8F4kbPuu
author: Joel Chan
date: Wed Aug 19 2020 22:34:39 GMT+0800 (Malaysia Time)
---

- [[🌲 zettels]]

    - Tags: [[DSolution-Diversity]]

    - Description

        - Goal: We would like to choose one or more optimizers for [[DSolution-Diversity]]

        - Working synthesis of principles (lots of [[Z]]

            - **Limited memory**

                - cf. [[THE - Search in Associative Memory (SIAM)]]

                - Optimization algorithms that require significant "working memory" are psychologically implausible, since people have Limited [[working memory]]

                - Similarly, psychologically plausible optimization algorithms should have limited lookahead or function approximation (cf. [[tmodelBVSR]]

            - **Problem dependency**

                - A range of optimizers may be psychologically plausible, since information-processing principles apply to all problems but apply differently as problems become more ill structured [[@reedStructureIllStructuredWellStructured2015]]

            - **Expertise dependency**

                - Lots of studies showing that experts and novices have different processes

                - Might be a different way of saying problem dependency: for experts, many problems are routine; when they tackle nonroutine problems, they might start to look like novices (this is a point that [[Herbert Simon]]

            - **Satisficing over optimizing**

                - This comes again in part from **Limited memory**, and also from general models and phenomena around [[decision-making]]

                    - A possible implication of this for modeling is that we should only study up to a short number of runs, not necessarily to convergence

            - **Depth first and opportunistic**

                - Relatedly, there is a general tendency to explore deeper down (the specification hierarchy) of a solution angle, rather than exploring many different solution angles in parallel, in part due to **Limited memory**

                    - There is some evidence (again cf. **Expertise dependency**) that a depth-frist orientation might be more characteristic of novices (see, e.g., [[@ballProblemsolvingStrategiesExpertise1997]]

            - **Nonrandomness in sampling**

                - It should be possible to "bias" the algorithm (cf. [[🧱 fixation]]

                    - So "memoryless" functions are a bad fit

                - People are bad at randomness

                - And often use some kind of [[design heuristics]]

                - Search is also often in __lower dimensional space__ (e.g., [[Chunking]]

                    - A variant of this is that designers may compose and iterate and recombine ideas, rather than sample points in a design space

            - **Co-evolving problem and solution space**

                - Skilled designers rarely take the design space as "given"; instead, they actively reformulate the problem in conjunction with making design moves.

                    - More in [[CLM - Design proceeds by co-evolution of problem and solution space]]

            - **Has the capacity for "high temperature" search**

                - cf. [[tmodelBVSR]]

            - [[serial order effect]]

                - roughly: ideas can get better over time

                    - although there are later models that dispute this based on protocol studies. important to think carefully about the difference, since there seems to be a systematic difference by methodology

                        - reminiscent of the arguments about [[nominal groups]]

                - indicating a role for [[executive function]]

        - "Handles" for optimizers

        - Phenomena

            - Explore vs. exploit

                - Related to [[🧱 fixation]]

            - Top-down vs. bottom-up

                - Designers frequently deviate from a normative top-down, structured design approach [[@ballProblemsolvingStrategiesExpertise1997]]

            - [[🧱 fixation]]

                - [[structured imagination]]

            - [[CLM - Design proceeds by co-evolution of problem and solution space]]

            - [[CLM - Expert designers are solution-oriented]]

            - Iterative / accretive nature of ideation

                - designers may compose and iterate and recombine ideas, rather than sample points in a design space

                - cf. also [[CLM - Compression is necessary for synthesis]]

                - [[@sosaAccretionTheoryIdeation2019]]

                    - a similar idea is that of [[preinventive structures]]

            - use of generative strategies (vs. just search)

                - e.g., use of [[design heuristics]]

                - these seem like "meta-patterns" through the design space

        - Models

            - [[mComputational Model]]

                - [[THE - Search in Associative Memory (SIAM)]]

                - [[tmodelBVSR]]

                    - fun empirical demonstration in [[@simontonCreativeProcessPicasso2007]]

                        - seems contra to basic "hill climbing", but probably interaction with problem characteristics

                        - we see similar meandering back-and-forth dynamics in analysis of [[Darwin's notebooks]]

                - Good review of models based on [[mThink-aloud protocols]]

                - Another good review of process models across design and creativity (including [[John Gero]]

            - Other

                - [[@schonReflectivePractitionerHow1983]]

        - Constraints / interactions

            - Individual differences

                - [[working memory]]

                - expertise

                - [[latent inhibition]]

            - Arousal / [[attentional focus]]

                - [[@martindaleCreativityConnectionism1997]]

                - Some interesting evidence around alcohol's effects on creative exploration, albeit with artificial tasks [[@jaroszUncorkingMuseAlcohol2012]]

            - Limited [[working memory]]

                - [[@cowanMagicalNumberShortterm2000]]

                    - but can be circumvented somewhat by [[Chunking]]

            - Design problem characteristics

                - Routine vs. nonroutine

                - Well-defined vs ill-defined (how structured is the problem?)

                    - [[@reedStructureIllStructuredWellStructured2015]]

                        - builds on proposal by [[@simonStructureIllStructured1973]]

                - Wicked?

                    - [[@rittelDilemmasGeneralTheory1973]]

        - Generations / streams of research

            - Design [[mThink-aloud protocols]]

            - Case studies

            - Design experiments

            - Computational / cognitive models

            - Studies of insight and creative ideation

###### Discourse Context

- **Informed By::** [[EVD - Undergrads' drawings of imaginary animals frequently included typical features from earth animals, with occasional deviations - @wardStructuredImaginationRole1994]]
- **Informed By::** [[CLM - Compression is necessary for synthesis]]
- **Informed By::** [[CLM - Design proceeds by co-evolution of problem and solution space]]
- **Informed By::** [[CLM - Expert designers are solution-oriented]]
- **Informed By::** [[@ballCognitiveProcessesEngineering1994]]
- **Informed By::** [[@carsonDecreasedLatentInhibition2003]]
- **Informed By::** [[@simontonCreativeProcessPicasso2007]]
- **Informed By::** [[@ballProblemsolvingStrategiesExpertise1997]]
- **Informed By::** [[@campbellBlindVariationSelective1960]]
- **Informed By::** [[@cowanMagicalNumberShortterm2000]]
- **Informed By::** [[@rittelDilemmasGeneralTheory1973]]
- **Informed By::** [[@schonReflectivePractitionerHow1983]]
- **Informed By::** [[@gruberDarwinManPsychological1974]]
- **Informed By::** [[@howardDescribingCreativeDesign2008]]
- **Informed By::** [[@simonStructureIllStructured1973]]
- **Informed By::** [[@suttonBrainstormingGroupsContext1996]]
- **Informed By::** [[@fingerReviewResearchMechanical1989]]
- **Informed By::** [[@daviesCharacterizingProgramDesign1991]]
- **Informed By::** [[@wardStructuredImaginationRole1994]]
- **Informed By::** [[@finkeCreativeCognitionTheory1996]]
- **Informed By::** [[@nijstadHowGroupAffects2006]]
- **Informed By::** [[@jaroszUncorkingMuseAlcohol2012]]
- **Informed By::** [[@sosaAccretionTheoryIdeation2019]]
- **Informed By::** [[@reedStructureIllStructuredWellStructured2015]]
- **Informed By::** [[@simontonCreativityDiscoveryBlind2011a]]
- **Informed By::** [[@yilmazCreativityDesignHeuristics2011]]
- **Informed By::** [[@maherCoevolutionComputationalCognitive2003]]
- **Informed By::** [[@martindaleCreativityConnectionism1997]]
