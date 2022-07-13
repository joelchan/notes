---
title: [[CLM]] - Composability is necessary for synthesis
url: https://roamresearch.com/#/app/megacoglab/page/AEmIaBKbs
author: Joel Chan
date: Sat Mar 07 2020 17:22:46 GMT-0500 (Eastern Standard Time)
---

- #[[🌲 zettels]]

    - Tags: #[[D/Synthesis Infrastructure]] #compositionality #[[Z]]

        - [[Joel Chan]] #TaskWrite #TaskNext Flesh out idea of levels of compositionality related to levels of synthesis. Probably want ot flesh out reading notes from source papers first, e.g., #[[@holbrookLevelsSuccessUse2008]], etc.

    - Description

        - Basic intuition: #[[[[CLM]] - Synthesis is creating a new whole out of component parts]]

        - There are levels of compositionality

            - #Claim Some types of [[synthesis]] are simpler to produce than others (p. 355-356)

            - Assemblage / quasi-synthesis

                - Weighing the bulk of the evidence (aka meta-analysis / [[systematic review]])

                - #Thought-Fragment Additionally, the [[IVEO Matrix]] isn't quite where we want it to be yet: it's more of a meta-analysis or [[systematic review]], rather than a coherent new whole. There is no causal model or graph that ties it all together to support sophisticated reasoning and decision-making

            - Levels of composability (cf. #[[[[CL]] - People process complex information in multiple levels and stages of processing]])

                - Bare minimum: can "affinity" group things

                    - Collections and tags can __kind of__ do this; but the upper limit on [[synthesis]] will be quite restrictive

                - Better: can connect things

                - Even better: can formalize things, typed relationships (e.g., contradiction, warrant, etc.)

                    - Cf. Principle #10: Save contradictory ideas

        - Synthesis is impaired in xyz way when we don't have sufficient compositionality

            - Classic example: affinity diagram?

            - Classic undifferentiated list, as noted in #[[@holbrookLevelsSuccessUse2008]] and others.

                - So, idea of "parts, not whole"? Assemblage? Can't transcend the sum of the parts. Or might not even have the sum.

                - The idea of a conceptually new whole construction is in contrast with what we often see in related work sections and literature reviews, which are much more about assemblage, often listing in chronological or author-order, what things have been done, what topics have been covered, with little to no synthesis into a coherent new whole.

                    - In this vein, [[systematic review]]s can be construed as a narrow subset of [[synthesis]] (and literature reviewing)

                        - It's not just that they're more easily done in well-structured domains where we have a bit more agreement.

                        - It's also that these [[systematic review]]s and meta-analyses are often laser-focused on just one edge in a causal model!

                            - Granted, good reviews (especially [[m/meta-analysis]]) might try to estimate some of the variability, but they're rarely focused on explicating a causal model or larger whole.

                                - Especially in medicine (e.g., [[Cochrane systematic reviews]]), the goal is more about getting a really good handle on what the evidence can say about a very narrowly defined question.

                    - #Thought-Fragment Additionally, the [[IVEO Matrix]] isn't quite where we want it to be yet: it's more of a meta-analysis or [[systematic review]], rather than a coherent new whole. There is no causal model or graph that ties it all together to support sophisticated reasoning and decision-making

        - [[[[CLM]] - Some degree of formalism is necessary for compositionality]]

        - Unfortunately, [[[[CLM]] - Gracefully integrating formalism into interactive systems is hard]]

    - R-Sources

        - Four [[Positivist]] epistemological models of scientific knowledge from philosophy of science [[@popperLogicScientificDiscovery1959]] [[@nagelStructureScienceProblems1979]] [[@dubinTheoryBuilding1978]] [[@bungePhilosophyScience1998]] agree that scientists build __theories__ as systems of scientific __statements__, which are composed of relationships between __concepts__ (p. 70) #[[📝 lit-notes]] #Atomicity #compositionality [[@harsDesigningScientificKnowledge2001]]

        - Introduces the [[Learning Loop Complex]] and idea of [[encodon]] as bridge between data and representations ([[Schema]]s)that are then used for downstream tasks during [[🧱 sensemaking]] (p. 271) [[@russellCostStructureSensemaking1993]]

        - [[Notional Model of Sensemaking]] in intelligence analysis has a looping structure that loops both between and within foraging and sensemaking loops, and progressively increases in both structure and effort, starting from raw data sources and culminating in a synthesized set of hypotheses #[[📝 lit-notes]] (p3) [[@pirolliSensemakingProcessLeverage2005]]

    - Status: #[[Z]]

###### Discourse Context

- **Informed By::** [[@holbrookLevelsSuccessUse2008]]
- **Informed By::** [[@harsDesigningScientificKnowledge2001]]
- **Informed By::** [[@russellCostStructureSensemaking1993]]
- **Informed By::** [[@pirolliSensemakingProcessLeverage2005]]

###### References

[[WP TOCHI Requirements framework for synthesis systems]]

- [[[[CLM]] - Composability is necessary for synthesis]]

    - Different word maybe? Formalism challenge, making it formality, need to have some formal structure e.g. Shipman paper Have to have some explicit representation
[[WP TOCHI Requirements framework for synthesis systems]]

- [[compositionality]] (which [[Katrina Fenlon]] thinks, and I think is worth considering, should be renamed to [[composability]]) #[[[[CLM]] - Composability is necessary for synthesis]]

    - Synthesizers should be able to ^^put ideas together^^ into more complex compositions. These compositions shouldn't be limited to simple clustering or aggregation, but should afford richer compositions like graphs, causal models, theories, arguments, facets, timelines, and so on.

        - cf. #[[@faisalClassificationSensemakingRepresentations2009]]
[[@halfordDigitalFuturesSociological2013]]

- This has significant implications for how we think about precisely in what sense [[[[CLM]] - Composability is necessary for synthesis]], and how [[formality]] plays into it

    - #[[Z: [[context]] and [[formality]] are in tension]]
[[May 30th, 2020]]

- Processing a real paper [[@liuOntologyFolksonomyStudy2008]] (actually really relevant to [[[[CLM]] - Composability is necessary for synthesis]])(there are others too)

    - {{youtube: https://www.youtube.com/watch?v=y65psAw-h4o&t=668s}}

    - also sparked citation thread to find this paper on multiple viewpoint [[ontologies]]: [[@zhitomirsky-geffetMultiviewpointOntologyConstruction2017]]
[[WP Synthesis requirements Theory and practice blog post series]]

- the **system **needs to enable you to [compose these units into various larger representations]([[[[CLM]] - Composability is necessary for synthesis]])

    - examples:

        - evergreen note structures

        - comparison tables

        - hierarchies (a la [[sys/NVIVO]] et al)

        - outlines and arguments

    - we can also potentially see how making the units compressable and contextualizable can aid in composability

    - the core idea here is of system affordances for **explicitly** composing/linking items

        - so [[bi-directional links]] help

        - spatial proximity is a nice start, but has limits

        - [[formality]] can help support richer composition motifs, but needs to be approached with caution (e.g., make sure it doesn't [destroy contextualizability]([[Z: [[context]] and [[formality]] are in tension]]), or [mess too much with multiplicity]([[Z: [[Multiplicity]] and [[Composability]] are in tension]]))

            - it may also be less necessary now that AI/ML can help us do more approximate similarity, perhaps in a more "scruffy" way, than relying on trustworthy, ontological sameness to do reasoning
[[October 22nd, 2021]]

- Structured: (composable): [[[[CLM]] - Composability is necessary for synthesis]]

    - so we can query it, and use computational support to help find new ideas (graph merge) as well as test and iterate on and develop ideas (synthesis queries)
