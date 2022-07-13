---
title: [[QUE]] - Do scholarly synthesis infrastructures already exist?
url: https://roamresearch.com/#/app/megacoglab/page/qno57yQ4G
author: Joel Chan
date: Mon May 11 2020 22:00:11 GMT-0400 (Eastern Daylight Time)
---

- #[[Question]]

    - Tags: #[[D/Synthesis Infrastructure]]

    - Description

        - [[[[CLM]] - Effective individual synthesis systems (seem to mostly) exist (for a select few)]]. But what about the collaborative/collective case?

        - The history of attempts at synthesis infrastructures is vast.

        - We have a thriving space of [[standards]] for underpinning [[infrastructure]] for [[synthesis]]

            - [[compression]] resembles the core concerns of standards like [[std/Micropublication]]s [[@clarkMicropublicationsSemanticModel2014]] and [[std/Nanopublications]] [[@grothAnatomyNanopublication2010]], which were developed in part to enable reasoning over more granular units of knowledge.

            - The property of [[context]] resembles the goal of representing evidence [[@brushSEPIOSemanticModel2016]], [[uncertainty]] [[@dewaardFormalisingUncertaintyOntology2012]], and [[provenance]] of publications [[@grothAnatomyNanopublication2010]].

            - The idea of formal semantics and [[composability]] connect well to the core vision of enabling machine assisted-reasoning and higher-level synthesis in the [[Semantic Web]] [[@kuhnGenuineSemanticPublishing2017]], [[@berners-leePublishingSemanticWeb2001]]

        - The history of *successful* attempts is... unclear? It's certainly not mainstream yet, at least in my experience. That is what we mean by infrastructure. No one "inherits" an infrastructure yet, at least to my knowledge.

        - Let's look at some examples.

            - The earliest ones in the computing era:

                - [[sys/Memex]]

                - [[sys/Xanadu]]

            - Within the sciences / scholarship, led by bioinformatics, best are under the rubric of "genuine" [[semantic publishing]] (term I've seen from #[[@kuhnGenuineSemanticPublishing2017]])

                - [[std/Nanopublications]]

                - [[std/Micropublication]]

                - [[std/BEL]]

                - [[std/SWAN]]

                - [[Scholarly HTML]]

                - [[Structured Digital Abstracts]]

                - [[digital libraries]]

                - [[standard/Claims]]

                - [[sys/Compendium]]

                    - More generally, there is a set of projects in this space around the orbit of the [[Knowledge Media Institute]], led for a time by [[Simon Buckingham Shum]]

                        - [[Jack Park]] is related to this thread, and now in the Telegram group for [[Digital Garden]]ing

                            - See, e.g., [[@parkKnowledgeGardeningKnowledge2009]]

                - [[std/Research Objects]]

                - [[Enhanced Publications]]

            - Other more recent ones

        - important to think through more carefully why [[sys/Xanadu]] and the many [[Semantic Web]] and [[std/Hypertext]] or [[sys/Memex]] related projects have “failed”.

        - What we see now is not infrastructure for synthesis. Instead, we see people either resort to all sorts of "hacks" and workarounds, or put in a substantial amount of work to "mine" publications for what they need (for an evocative example of this, see [[@knightEnslavedTrappedData2019]]). We have a whole cottage industry that is dedicated to fueling workarounds of this sort, for systematic reviewing. While these hacks often work well enough for the task at hand, they are rarely transferred in systematic ways across projects and people, violating the dimensions of "reach or scope" and "embodiment of standards", laid out by [[@starStepsEcologyInfrastructure1996]].

        - Conversely, we see the infrastructure that people do rely on (e.g., Google Scholar, Web of Science, and so on) consistently breaking down and thereby becoming visible when people try to use it for difficult [[synthesis]] tasks, especially across disciplines. They also often cannot really transfer their [[bricolage]] solutions from previous tasks or projects to these new domains they have to navigate.

        - It's important to recognize that these are not "one-time" costs either: scientific problems will require many such queries, and likely spawn new queries as projects evolve and more is learned. We would like for there to not be a disincentive to explore new directions and perspectives on your work as it evolves, simply because it is so arduous to find what is known about it.

        - It's not that we have made no progress! Indeed, the [[semantic publishing]] revolution is indeed underway! We see encouraging developments, in [[bioinformatics]] and [[archeology]], for example.

        - Yet, on the whole, we're not seeing nearly as much of this transformation as we'd like. [[[[CLM]] - Sustaining authorship for [[semantic publishing]] is hard]]

        - see: [[discourse-graph-centric information models and platforms]]

    - R-Sources

        - [[@miles-boardHypertextSemanticWeb2001]]

        - #[[@kuhnGenuineSemanticPublishing2017]]

        - #[[@kuhnBroadeningScopeNanopublications2013]] Includes history of attempts, ranging from [[std/Research Objects]] to [[Structured Digital Abstracts]] to [[std/Micropublication]] and [[std/Nanopublications]], and [[Scholarly HTML]] (p. 142-145)

        - "failure" documented extensively in this Wired article: #[[@wolfCurseXanadu1995]]

        - #[[@clarkMicropublicationsSemanticModel2014]]

###### References

[[August 24th, 2021]]

- [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - see especially thoughts about massive graveyard of CI tools like [[sys/Xanadu]]: important to think through more carefully why [[sys/Xanadu]] and the many [[Semantic Web]] and [[std/Hypertext]] or [[sys/Memex]] related projects have “failed”.
[[May 11th, 2020]]

- Ok did about an hour of prototyping [[[[CLM]] - The central bottleneck to synthesis infrastructures is authoring]], spawned uncertainty about [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - There are some very basic numbers I want to have in my head to think through things.

        - What is the coverage of major [[Semantic Web]]-style approaches for scholarly [[synthesis]] [[infrastructure]]?

            - A starting point is #[[@kuhnNanopublicationsGrowingResource2018]], which reports around 10 million [[std/Nanopublications]] published at the time of writing, albeit almost all within bioinformatics, and overwhelmingly dominated by a small (N=41!!) set of authors

            - Good question for [[Katrina Fenlon]]

        - What is the scale at which scientists are producing annotations and notes? In other words, what is the untapped opportunity here? What is the "drag coefficient"? How much energy is being "wasted'?

            - Analogy here to the [[cognitive surplus]] argument for crowdsourcing

    - Also need to be very precise about what I mean by [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

        - [[std/Research Objects]] actually may not count, at least according to [[@kuhnGenuineSemanticPublishing2017]]

        - We need to go back and forth between the question of existence and the question of standards.

    - Important caution: even if the answer to the existence question is negative, it does not follow that the [[Authorship Bottleneck]] is the main thing in the sense that we are thinking of (e.g., it may not actually be *that* tedious; it's just that nobody is incentivized sufficiently to do it; that still would connect with the idea of [[[[PTN]] - Integrated crowdsourcing]] though)
[[February 6th, 2021]]

- [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - I'm not sure that we want to say that epistemic models are already a thing that are suggested across disciplines. That's not really true in a literal sense. Standards like [[std/Micropublication]]s and [[std/SEPIO]] and [[std/SWAN]] (and systems like [[sys/Zettelkasten]], but we can leave that out for now), indeed are *basically* what we mean by epistemic models.

        - Then the truth is that these models have *significant* theoretical support

        - So we can first articulate these literal standards

        - Then give intuition for why they might help

        - Then show how these intuitions join with compelling theoretical justification to predict significant benefits for synthesis

        - And then set up the "they haven't really been tested".

    - Ok so this is the first thing to do. Let's talk more specifically about which of the standards we want to highlight as basically what we want.

        - [[std/Micropublication]]s from [[@clarkMicropublicationsSemanticModel2014]] comes immediately to mind as the clearest example

            - articulates the addition of richer [[context]] (through direct representation of empirical evidence), and [[composability]] (through the representation of claim networks) as a key advance over [[std/SWAN]], [[std/Nanopublications]], and [[std/BEL]] (the latter two in addition are limited by their requirements that statements be in formal language, although [[@kuhnBroadeningScopeNanopublications2013]] did modify the standard to support natural-language statements)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F5vRbtoadZU.png?alt=media&token=75c0d383-7499-4afd-aa57-6e2bea5f4aec) (p. 3)

            - note their strong grounding in argument theory, building on [[@toulminUsesArgument2003]], but going beyond it to think more deeply about [[context]], which, like what we [have been saying]([[[[QUE]] - What is context for the purposes of scholarly synthesis?]]), can be roughly divided into "data" (the thing we nest under the `observation note`: a figure/table/quote, etc.), the `context snippets` (typically methodological details that help us understand how the data was produced), and the discourse context of the claim

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F__UTLi_BlT.png?alt=media&token=f4559a05-ab2a-473d-b9a7-5f8d3dfdc48e)

            - [[std/Micropublication]]s [[@clarkMicropublicationsSemanticModel2014]] seems like the right model with an explicit emphasis on grounding in "lower-level" evidence and grounding in [[Stephen E. Toulmin]]'s model of [[defeasible argumentation]] [[@toulminUsesArgument2003]] and [[@verheijEvaluatingArgumentsBased2005]]

        - the next is [[std/SWAN]] [[@ciccareseSWANBiomedicalDiscourse2008]], which is a direct predecessor of [[std/Micropublication]]s (same key authors: [[Tim Clark]] and [[Paolo Ciccarese]])

            - [[discourse elements]] are at the heart of the ontology: they are composed of research questions, hypotheses, claims, and evidence

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_ulWmpVLzq.png?alt=media&token=933aee12-8247-40ff-b5b8-2dc534bb6cb6) (p. 745)

            - here is an example in actual use, focusing on arbitration of conflicting claims

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyV6OUclhOy.png?alt=media&token=0248ed0f-2489-4d1e-8b2c-2166c82f25de)

            - the key improvement of [[std/Micropublication]]s and [[std/SEPIO]] over this model is that **evidence is made a first-class object, alongside generalized claims**, rather than "bottoming out" in a citation (see also the importance of `observation notes` and `context snippets` in my model)

            - [[std/SWAN]] was actually instantiated in a working system, and was supposed to connect to [[sys/Alzforum]] (see [[@clarkAlzforumSWANPresent2007]])

                - But... I can't see a trace of it in the current [[sys/Alzforum]] website (e.g., would expect it to be listed somehow in their [list of databases](https://www.alzforum.org/databases), but it's not), even though it's still active, and there is active sharing and discussion of papers. What gives?

                - As far as I can tell, they did implement it

                    - See, e.g., this screenshot of the pilot interface

                        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FVY8pcT8UgN.png?alt=media&token=d4dbaef1-7e28-4af5-b99f-65c0e145bcca) (p. 167)

                - The motivation is remarkably similar to what we are talking about: retaining the [[context]] of sensemaking, zeroing on the things we actually care about (the **semantics**)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FnGkLDW_Yh9.png?alt=media&token=5d71f264-245a-47e1-97d4-0ec8b5f77660) (p. 168)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FGbKml2aUJk.png?alt=media&token=b2600e5c-140c-438a-96d2-1b5b47333d00) (p. 169)

                - They even think about a [[federation]] approach!!!!!! MySWAN, connecting together into a community SWAN!!!!!

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FvoyvdQxvo7.png?alt=media&token=9e00409e-aec0-4c03-b234-52dec65e828b) (p. 170)

        - a version of what we are doing is happening on

        - [[std/ScholOnto]]
[[July 14th, 2021]]

- Circling back to [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]], I think it's useful to ask and generate [[Notable examples of discourse graphs]]

    - https://twitter.com/JoelChan86/status/1415365121258446848
[[June 17th, 2020]]

- Maybe some good sources in here for understanding #[[[[CLM]] - The central bottleneck to synthesis infrastructures is authoring]] and #[[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]: #[[@peroniSemanticPublishingIssues2012]]

    - talks about the lack of effective user interfaces as a major bottleneck for [[semantic publishing]]
[[about these notes]]

- [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - [[[[CLM]] - Effective individual synthesis systems (seem to mostly) exist (for a select few)]]

    - [[[[QUE]] - What is synthesis?]]

    - [[[[CLM]] - Effective synthesis is hard]]

    - [[[[CLM]] - Effective synthesis is rare]]
[[June 17th, 2020]]

- relevant for [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - should do a run through of [[CORD-19 demos and resources]] and record it.

        - But the ability to sift through connections and literature at the claim level is sorely lacking. i got excited by a [[Question-Answering]] thing here [CORD-19 Search 5](https://cord19.aws/): Leverage this AWS tool to query the COVID-19 Open Research Dataset (CORD-19), with natural language questions and answers from Amazon Kendra. CORD-19 Search includes data from CORD-19 which has been processed using Amazon Comprehend Medical., but it turned out to be just a (basically keyword-based) search engine.

        - my current impression after testing a few is that #[[SOTA]] is support for concept-based search (with ontologies integrated), and these are really powerful!! My favorite was [DOC Search 44](https://covid-search.doctorevidence.com/): the ontology is really powerful, found immediate value from it.

        - can help with the problem that quite possible/likely that some good progress is being made behind closed doors, under license, at [[Elsevier]] and the like, not making its way to the published literature yet.

    - Another (free and [[open-source]]!!) tool for [[computer-aided model of semantic publishing]] for [[systematic review]]s:  [[sys/ASReviews]] - more focused on screening, using [[active learning]], rather than extracting [[PICO frames]] or similar, like [[sys/RobotReviewer]]

    - Maybe some good sources in here for understanding #[[[[CLM]] - The central bottleneck to synthesis infrastructures is authoring]] and #[[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]: #[[@peroniSemanticPublishingIssues2012]]

        - talks about the lack of effective user interfaces as a major bottleneck for [[semantic publishing]]

    - back to what i couldn't remember for synth infra meeting [[June 16th, 2020]] : [[sys/Meta]] from the [[Chan-Zuckerberg Initiative]].

        - I misremembered, too: looks like [[Andrew McCallum]] is involved not with [[sys/Meta]] directly (not sure), but on the newer [[Computable Knowledge Project]], which I'm not sure is actually running rn?

    - more stuff from [[Tudor Groza]], about enabling [[context]] #[[@grozaAddingProvenanceEvolution2008]]

    - bit of a critical review by [[Anita de Waard]] about [[semantic publishing]] ca. [[2010]]: #[[@deWaardProteinsFairytalesDirections2010]] #> "The column mentions different types of projects, including efforts focusing on entity enrichment and projects that involve triple markup of documents (subject-predicate-object expressions). However, such approaches are not enough. They help us find information, but they don't help us understand it. The author argues that we need to incorporate a better understanding of how language encodes meaning into our systems, so that we can develop a richer scientific knowledge representation"

        - very similar vision to what we're arguing for, in tandem with [[@kuhnGenuineSemanticPublishing2017]], for moving beyond [[ontologies]] to modeling claims and [[discourse]]

    - another example of the [[text mining model of semantic publishing]] - #[[@sateliSemanticRepresentationScientific2015]]

    - Found the [[std/Research Objects]] paper: #[[@bechhoferWhyLinkedData2013]]

    - #[[@vosBioHackathon2015Semantics2020]] reports on [[BioHackathon 2015]], which includes lots of cutting edge, industry [[semantic publishing]] efforts
[[June 23rd, 2020]]

- relevant analogous data for #[[[[CLM]] - The central bottleneck to synthesis infrastructures is authoring]] and #[[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - [COVID-19 pandemic reveals the peril of ignoring metadata standards](https://www.nature.com/articles/s41597-020-0524-5)
[[May 11th, 2020]]

- Also need to be very precise about what I mean by [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - [[std/Research Objects]] actually may not count, at least according to [[@kuhnGenuineSemanticPublishing2017]]

    - We need to go back and forth between the question of existence and the question of standards.
[[October 21st, 2020]]

- super important [[SOTA]] and related work for [[D/Synthesis Infrastructure]]: the [[sys/Open Research Knowledge Graph]] --> [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - h/t this blog post: [More cutting edge — Research tools for researchers — Oct 2020 by Aaron Tay](https://medium.com/@aarontay/more-cutting-edge-research-tools-for-researchers-oct-2020-by-aaron-tay-b90b56f3dfbd)

        - also relevant [systems for]([[system-for]]) for [[[[CLM]] - In interdisciplinary domains, network-based foraging is more powerful than search-based foraging]]

            - [More research/literature mapping tools - Connected Papers and CoCites](https://musingsaboutlibrarianship.blogspot.com/2020/06/more-researchliterature-mapping-tools_16.html)
[[Week of December 6th, 2021]]

- h/t [[Matt Clancy]], going to discuss with [[Protocol Labs Metaresearch Journal Club]], super relevant for [[D/Synthesis Infrastructure]] [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - > TL;DR: I worked on biomedical literature search, discovery and recommender web applications for many months and concluded that extracting, structuring or synthesizing "insights" from academic publications (papers) or building knowledge bases from a domain corpus of literature has negligible value in industry. Close to nothing of what makes science actually work is published as text on the web.
[[Week of January 17th, 2022]]

- Pulling on thread from [[@starStepsEcologyInfrastructure1996]], uncovering more explorations relevant for [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces - [[[scite report]]]: https://scite.ai/reports/steps-toward-an-ecology-of-gyan0A?contradicting=false&mentioning=false&page=1&unclassified=false&utm_campaign=plugin&utm_medium=plugin&utm_source=generic

    - Science Friction: Data, Metadata, and Collaboration - [[[scite report]]]: https://scite.ai/reports/science-friction-data-metadata-and-89g5RG?mentioning=false&page=1&unclassified=false

    - Exploring visual representations to support data re‐use for interdisciplinary science - Wiggins - 2018 - Proceedings of the Association for Information Science and Technology - Wiley Online Library: https://asistdl.onlinelibrary.wiley.com/doi/10.1002/pra2.2018.14505501060
[[🌱🌾 Research Garden]]

- [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - [[[[CLM]] - Sustaining authorship for [[semantic publishing]] is hard]]

    - [[[[QUE]] - What is the user experience of semantic authoring within regular scholarly workflows?]]
[[May 12th, 2020]]

- Split communities, diff. ways to think about [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - Knowledge representation / semantic web / tex mining

    - Semantic publishing (focuse don publishing athte point fo completion)
[[slipbox]]

- [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - [[[[CLM]] - Effective individual synthesis systems (seem to mostly) exist (for a select few)]]

    - [[[[QUE]] - What are the most efficient routes to useful cross-boundary knowledge?]]
[[Research proposal for P COVID-19 treatment search]]

- Cc [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]: [[Scholarly Ontologies Project]] is one extremely relevant prior art on this.

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft5dI7cHi6j.png?alt=media&token=4cbfae55-c940-40a2-8382-872f9e11addb)

    - #> from [[@urenSensemakingToolsUnderstanding2006]]
[[@cambrosioOvercomingBottleneckKnowledge2020]]

- for [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]

    - #inspectionalread on [[March 15th, 2022]]

        - it's a bit of an odd paper - it's not really a formal study (no methods section, no sense of field site, analysis method), though it contains numerous quotes from participants, but also many quotes from other sources (papers). i'm... not really sure what to do with it, other htan to take some light "claim" notes. things to follow up on.

        - seems to be drawing from the perspectives and lines of works like [[@suchmanPlansSituatedActions1987]], but is deeply situated in the general area of [[precision medicine]]

            - draws on suchman to talk about why knowledgebases are inherently going to be contextual and situated

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FZoIfp6s_wK.png?alt=media&token=b23da09e-7769-47bb-82c8-18fd1e938d81) (p. 310)

        - key thing is trying to figure out "what are these things"? distinction between databases and knowledgebases that they notice as 'actor categories' (not necessarily ontological distinctions)

        - section 1 introduces the context, section 2 is about "why we want x-bases"

        - section 3 starts to get at the heart of the hypothesized distinction between databases and knowledgebases - is this the key distinctino being made here between [[sys/CIViC]] and [[sys/OncoKB]]?

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FAaRtdype4X.png?alt=media&token=9e46e8a0-4d5c-47a3-87aa-00b1ed9871f1) (p. 310)

        - should pull out the databases and knowledgebases mentioned in this paper

            - caBIG

            - oncology kbs

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FESsrh09t1s.png?alt=media&token=8ead184d-ac33-4903-9f57-d51e7800430f) (p. 311-312)

        - sections 6-10 then digs into kbs

            - section 6 asks why the kbs were developed, from the practitioners' standpoint

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FYTAIXCUgAg.png?alt=media&token=48d33d80-e27b-4cef-b713-05ba70309dd3) (p. 315)

            - section 7 discusses how the curation/creation process differs across kbs

            - section 8 digs into issues of trust and transparency and how this is handled/manifested differently across kbs

            - section 9 digs into interpretation, levels of evidence, and how this is done across kbs

                - very relevant to [[[[QUE]] - How can we support explicit contention with evidence when synthesizing knowledge claims?]]

            - section 10 digs into how kbs differ at a fundamental level in terms of what they contain, their structure, etc.

                - this is what i'm most interested in atm

        - so i think each section is going to contribute something of its own.
[[My-Inbox]]

- This example again makes me wonder how far we actually are from SOTA for synthesis tools (cf. [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]), and if we're close, why these tools aren't mainstream yet. One simple explanation comes from [[diffusion of innovation]] theory, possibly also marketing - simply put, it's not that the tools aren't good enough, it's that their system lost out in the comm/marketing wars

    - However, the [[[[CLM]] - (premature) formalism considered harmful]] paper actually does review systems like the [[sys/Knowledge Forum]] - one important condition might be the much higher level of scaffolding (and perhaps compulsion) in ed settings, where the system is imposed, and perhaps also the level of complexity involved, such that the tradeoff between authoring costs and payoffs become much less favorable (maybe also after factoring in opportunity costs, pressures, etc.)
