---
title: [[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?
url: https://roamresearch.com/#/app/megacoglab/page/U8F4kbPuu
author: Joel Chan
date: Wed Aug 19 2020 10:34:39 GMT-0400 (Eastern Daylight Time)
---

- #[[🌲 zettels]] #[[Question]]

    - Tags: #[[D/Solution-Diversity]] #[[Fundamental Theories of Creativity]]

    - Description

        - Goal: We would like to choose one or more optimizers for [[D/Solution-Diversity]] that have psychological plausibility.

        - Working synthesis of principles (lots of #[[Z]] here)

            - **Limited memory**

                - cf. [[[[THE]] - Search in Associative Memory (SIAM)]]

                - Optimization algorithms that require significant "working memory" are psychologically implausible, since people have Limited [[working memory]]

                - Similarly, psychologically plausible optimization algorithms should have limited lookahead or function approximation (cf. [[tmodel/BVSR]]), except if designer is expert in problem area, or problem is routine)

            - **Problem dependency**

                - A range of optimizers may be psychologically plausible, since information-processing principles apply to all problems but apply differently as problems become more ill structured [[@reedStructureIllStructuredWellStructured2015]]

            - **Expertise dependency**

                - Lots of studies showing that experts and novices have different processes

                - Might be a different way of saying problem dependency: for experts, many problems are routine; when they tackle nonroutine problems, they might start to look like novices (this is a point that [[Herbert Simon]] makes about "strong" and "weak" strategies)

            - **Satisficing over optimizing**

                - This comes again in part from **Limited memory**, and also from general models and phenomena around [[decision-making]]: the basic idea is that people tend not to optimize in the sense of considering as many options as possible and exhaustively and precisely evaluating them to find the best option

                    - A possible implication of this for modeling is that we should only study up to a short number of runs, not necessarily to convergence

            - **Depth first and opportunistic**

                - Relatedly, there is a general tendency to explore deeper down (the specification hierarchy) of a solution angle, rather than exploring many different solution angles in parallel, in part due to **Limited memory**

                    - There is some evidence (again cf. **Expertise dependency**) that a depth-frist orientation might be more characteristic of novices (see, e.g., [[@ballProblemsolvingStrategiesExpertise1997]], [[@ballCognitiveProcessesEngineering1994]])

            - **Nonrandomness in sampling**

                - It should be possible to "bias" the algorithm (cf. [[🧱 fixation]] - nonrandom starting positions in design space; influenced by various things in the past)

                    - So "memoryless" functions are a bad fit

                - People are bad at randomness

                - And often use some kind of [[design heuristics]]

                - Search is also often in __lower dimensional space__ (e.g., [[Chunking]]), in part due to **Limited memory**

                    - A variant of this is that designers may compose and iterate and recombine ideas, rather than sample points in a design space

            - **Co-evolving problem and solution space**

                - Skilled designers rarely take the design space as "given"; instead, they actively reformulate the problem in conjunction with making design moves.

                    - More in [[[[CLM]] - Design proceeds by co-evolution of problem and solution space]]

            - **Has the capacity for "high temperature" search**

                - cf. [[tmodel/BVSR]], and explore/exploit models

            - [[serial order effect]]

                - roughly: ideas can get better over time

                    - although there are later models that dispute this based on protocol studies. important to think carefully about the difference, since there seems to be a systematic difference by methodology

                        - reminiscent of the arguments about [[nominal groups]] (see, e.g., [[@suttonBrainstormingGroupsContext1996]])

                - indicating a role for [[executive function]]

        - "Handles" for optimizers

        - Phenomena

            - Explore vs. exploit

                - Related to [[🧱 fixation]] - nonrandom starting positions in design space; influenced by various things in the past

            - Top-down vs. bottom-up

                - Designers frequently deviate from a normative top-down, structured design approach [[@ballProblemsolvingStrategiesExpertise1997]][[@daviesCharacterizingProgramDesign1991]]

            - [[🧱 fixation]] - nonrandom starting positions in design space; influenced by various things in the past

                - [[structured imagination]] [[[[EVD]] - Undergrads' drawings of imaginary animals frequently included typical features from earth animals, with occasional deviations - [[@wardStructuredImaginationRole1994]]]]

            - [[[[CLM]] - Design proceeds by co-evolution of problem and solution space]]

            - [[[[CLM]] - Expert designers are solution-oriented]]

            - Iterative / accretive nature of ideation

                - designers may compose and iterate and recombine ideas, rather than sample points in a design space

                - cf. also [[[[CLM]] - Compression is necessary for synthesis]]

                - [[@sosaAccretionTheoryIdeation2019]]

                    - a similar idea is that of [[preinventive structures]] from the [[creative cognition approach]] of [[@finkeCreativeCognitionTheory1996]]

            - use of generative strategies (vs. just search)

                - e.g., use of [[design heuristics]] (not to be confused with the [[Daniel Kahneman]] kind of heuristics) - more like meta-patterns or schemas (similar to [[sys/TRIZ]] or [[sys/SCAMPER]]) [[@yilmazCreativityDesignHeuristics2011]]

                - these seem like "meta-patterns" through the design space

        - Models

            - [[m/Computational Model]] / cognitive

                - [[[[THE]] - Search in Associative Memory (SIAM)]] [[@nijstadHowGroupAffects2006]] for brainstorming / generic ideation

                - [[tmodel/BVSR]] [[@campbellBlindVariationSelective1960]], later popularized and revisited by [[Dean Simonton]] (e.g., [[@simontonCreativityDiscoveryBlind2011a]])

                    - fun empirical demonstration in [[@simontonCreativeProcessPicasso2007]]: sequence of Picasso's sketches of Guernica was nonmonotonic in terms of progression towards final painting

                        - seems contra to basic "hill climbing", but probably interaction with problem characteristics

                        - we see similar meandering back-and-forth dynamics in analysis of [[Darwin's notebooks]] [[@gruberDarwinManPsychological1974]]

                - Good review of models based on [[m/Think-aloud protocols]] and [[m/Case study]] work in the early days of design research by [[@fingerReviewResearchMechanical1989]] / see also [[@maherCoevolutionComputationalCognitive2003]]

                - Another good review of process models across design and creativity (including [[John Gero]]'s [[tmodel/FBS]]] [[@howardDescribingCreativeDesign2008]])

            - Other

                - [[@schonReflectivePractitionerHow1983]]: reflective conversation with design problem / material: iterative, see-move-see --> frequent updating?

        - Constraints / interactions

            - Individual differences

                - [[working memory]]

                - expertise

                - [[latent inhibition]] [[@carsonDecreasedLatentInhibition2003]]

            - Arousal / [[attentional focus]]

                - [[@martindaleCreativityConnectionism1997]]

                - Some interesting evidence around alcohol's effects on creative exploration, albeit with artificial tasks [[@jaroszUncorkingMuseAlcohol2012]]

            - Limited [[working memory]]

                - [[@cowanMagicalNumberShortterm2000]]

                    - but can be circumvented somewhat by [[Chunking]]

            - Design problem characteristics

                - Routine vs. nonroutine

                - Well-defined vs ill-defined (how structured is the problem?)

                    - [[@reedStructureIllStructuredWellStructured2015]] information-processing principles apply to all problems but apply differently as problems become more ill structured

                        - builds on proposal by [[@simonStructureIllStructured1973]]

                - Wicked?

                    - [[@rittelDilemmasGeneralTheory1973]]

        - Generations / streams of research

            - Design [[m/Think-aloud protocols]] (around 1990's and before)

            - Case studies

            - Design experiments

            - Computational / cognitive models

            - Studies of insight and creative ideation

###### References

[[June 18th, 2020]]

- In response to query by [[Matt Erhart]] on Slack about [[D/Solution-Diversity]] (cc [[[[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?]])

    - query "expert design" also a very rich one in my library

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FhacKKaDVgx.png?alt=media&token=e4c66374-625a-400a-8436-382f8ca59a79)

    - [[Joel Chan]]: way late, but yes, there's a fair amount of work on this. what comes to mind immediately is this stuff looking at breadth-first vs. depth-first (or combo) strategies for experts vs. novices. although apparently it's not super relevant, since i wrote a note on this paper "i think breadth vs depth here has to do with the sequence in which *goals* (requirements, subgoals) are tackled, and doesn't really say anything about the breadth/depth of search among alternatives *within* certain solution spaces (e.g., for subgoal 2, or combination of 8 and 9 in figure c). From a cognitive perspective, the question of top-down development vs opportunism seems to be more of a question about cognitive control rather than search *patterns* among solution alternatives)"

        - [[@ballProblemsolvingStrategiesExpertise1997]]

    - there's also some interesting work on the differences between a "designer" approach vs. a "scientist" approach to problems, with the former more likely to try to jump into a particular solution sooner.

        - [[@crossExpertiseDesignOverview2004]]

    - Matt: I was just realizing that there's probably been a lot of work on how designers currently explore design spaces. What are the main factors that kind of research has looked at? I can only think of parallel prototyping: designers/humans struggle with sunk cost, so force them to branch out early. And early convergence: ideators typically don't explore enough [unknown citation].
[[🌱🌾 Research Garden]]

- [[[[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?]]

    - [[[[CLM]] - Design proceeds by co-evolution of problem and solution space]]
[[March 11th, 2022]]

- [[[[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?]]

    - Solution space

        - [[@siangliulueIdeaHoundImprovingLargescale2016]]

        - [[@xuIdeateRelateExamplesGallery2021]]

        - many designers have adopted a practice where they explore prior examples throughout the process: [[@herringGettingInspiredUnderstanding2009]], [[@kulkarniEarlyRepeatedExposure2012]]

        - Ideas by others can create fixation effects on designers [[@leahyDesignFixationInitial2020]]

        - [[@chanBestDesignIdeas2015]]

        - Researchers have explored the possibility of modeling and illustrating the conceptual distance between ideas to help designers compare and assess novelty: Crowdsourcing inspiration: Using crowd generated inspirational stimuli to support designer ideation; The cognitive neuroscience of creativity

        - [[@changRecipeScapeInteractiveTool2018]]

    - Problem space

        - [[@macneilProbMapAutomaticallyConstructing2021]]
[[August 21st, 2020]]

- Example: [[[[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?]] (ongoing)

    - Can show how to get stuff into Roam
[[@changRecipeScapeInteractiveTool2018]]

- [[Jason Ding]] for [[[[QUE]] - What are some major phenomena around designers' exploration of design spaces and how might these map to characteristics of optimizers?]] | __<summary of what was learned in this session (fill this out later)>__

    - ## results of interest and discussion

        - __One block for each result of interest. we'll refactor this together into EVD notes__

            - __also discuss possible critiques/claims. create source CLM notes for author conclusions (if you like), or reference other CLMs that we have that engage with this__

            - ### summary

                - A scatterplot-like visualization (RecipeMap) is more helpful for initial (novel) exploration than in-depth histograms (RecipeStat).

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FwRMqb9CG-2.png?alt=media&token=e83c6500-05bf-4b88-abd5-c9f0f0cedd69) page 9

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDgQA0v8w17.png?alt=media&token=5eee8f29-cc51-4998-832e-657a99a0eaee)

                - Examples might help stimulate and reinterpret/repurpose (?)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FIgwcJrQfGY.png?alt=media&token=0abc46d6-da16-46e4-812d-13f47c139920)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FffGoC0mSFp.png?alt=media&token=cb9e300f-ea89-49bd-ab9e-878476a89adc)

            - ### grounding context

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F4xTHJc0gd_.png?alt=media&token=7f338e3b-43c7-4df7-8d2a-200b8dc7dca3) page 8

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FI7t4RoWOkN.png?alt=media&token=e92191d0-ee9d-4fe1-a396-5fdafde1429a) page 9

        - __Also can discuss meta-results (combinations of results) in a similar template.____

    - ## side notes

        - __Where are the authors coming from? Are there any useful "breadcrumbs" (e.g., other theoretical frameworks, authors, papers) we can follow up on?__
