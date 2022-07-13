---
title: [[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension
url: https://roamresearch.com/#/app/megacoglab/page/d9YXVjPSm
author: Joel Chan
date: Fri Aug 13 2021 09:54:09 GMT-0400 (Eastern Daylight Time)
---

- instantiates::

    - [[bet/[[D/Synthesis Infrastructure]]: it is possible to write close to prose but seamlessly translate to queryable, shareable discourse graph formalisms in the backend]]

    - [[bet/[[D/Synthesis Infrastructure]]: it is possible to enumerate and design for implicit authoring patterns for formal discourse graphs that can be shared across people]]
- addresses::

    - [[[[QUE]] - How can we best bridge private vs. public knowledge?]]

    - [[[[QUE]] - How can we design sustainable infrastructures for supporting interdisciplinary scholarly synthesis?]]
- Working with [[David Vargas]] on this here: https://roamresearch.com/#/app/roam-synthesis

    - https://roamjs.com/extensions/discourse-graph

    - With funding from [[org/Protocol Labs]]

        - Open Source Software Grant Agreement - Google Docs: https://docs.google.com/document/d/1lHsLN7S4Oyff4msTeb9sVtdA-xdkkOQNL-v2Fk8OYKw/edit

    - documentation: https://app.gitbook.com/o/2kiy4lcgby4uyFTgiAn6/s/VpoqQNZpk4qG2nMcQUaw/

    - repo: https://github.com/dvargas92495/roamjs-discourse-graph

###### Discourse Context

- **Uses::** [[PTN - flexible compression]]

###### References

[[January 15th, 2022]]

- what does this mean for the sharing paradigm of [[[[PTN]] - discourse graph]]s and [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]?

    - what paradigms do we need to have to ensure successful facilitated construction of knowledge?

    - how does this change the cost function?

        - clear that the naive (i will just use x from others instead of reading y papers) is naive. not gonna work

        - but does the alternative work better?

            - i think so still

                - easier to search

                - easier to contextualize, reassemble, manipulate

        - i think this means they shouldn't be super formal pubs

            - change and forking is the normal state, not stable reuse

    - synchronization for multiplayer feels... wrong. or not quite the right task. mismatches are not problems to be solved; change is the norm. what we want is some way to know that things are... simlar? but not *The Same Thing* (as in UID). that is one way to do retrieval and aggregation, but... idk.

        - cc [[[[CLM]] - Universal Semantic Webs are neither feasible nor useful]]
[[EXP - DSynthesis Infrastructure - Field study for discourse graph extension]]

- We have built a ^^**prototype probe**^^ (the [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]).

    - The prototype has core stable features that are designed to:

        - seamlessly integrate authoring of a formal discourse graph into people's informal notes in a way that is personally tailorable

        - provide immediate direct value from the discourse graph, through enhanced exploration and querying capabilities

        - support export of (subsets of) the discourse graph to others in Roam-friendly as well as interoperable formats

    - The prototype also has experimental features to probe further into reuse and distributed synthesis scenarios, including:

        - A UI for subscriptions, to support needfinding around conditions under which people might want to "pull" discourse graph elements from others they aren't directly collaborating with

        - A UI placeholder for inter-graph translation, to support needfinding around needed interactions for translating discourse graph conventions between graphs (e.g., through a common stream, or peer-to-peer)
[[March 25th, 2022]]

- Problem Statement, OKRs, and Evaluation Points for [[org/Protocol Labs]] funding for Phase III of [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - ## Evaluation points

        - In the current phase, the key objectives will center on designing, building, and testing capacity for collaborative and distributed usage of discourse graphs.

            - **Federation (schemas)**: managing and aligning differences in schemas between different discourse graphs

            - **Federation (content)**: if users are to share with others beyond copy/paste, what mechanics might we need to support, such as forking, synchronization, notifications/updates, etc.?

            - **Sharing management**: how to enable people to reason about and manage what they share atomically from their d/graph while preserving privacy?

        - Finally, we will also allocate a small fraction of development time on stability/refinements of existing core "single-player" infrastructure, including optimizing query speed for usability, as well as enabling more sophisticated discourse graph relations built on inference rules over discourse graph relations (e.g., "evidence A indirectly supports claim B if {claim A supports claim B and evidence A supports claim A}), which have been requested by users to support more structured reasoning over their discourse graphs.

        - We will also allocate a portion of development time to explore extending/interoperating with discourse graph authoring and sharing in other hypertext notebooks, such as Logseq and Obsidian.

    - ## Problem Statement

        - Claim: The need to sift through scientific papers — the standard form of scholarly communication — in order to understand the current state of the knowledge frontier imposes a great deal of unnecessary overhead on researchers, especially early-stage researchers. This project intends to reduce that burden, enabling researchers to start with a smaller, more tractable unit of knowledge: the idea, so that they can more rapidly begin to develop new research directions and questions from available claims, suppositions, and data.

        - These goals are aligned with PL Research’s interest in knowledge engineering and meta research.

        - The aim of this project is to __develop integrated authoring tools for shareable discourse graphs of scientific literature__.

        - Foundational research across information science and science informatics has clearly diagnosed the central obstacle: our current scholarly communication infrastructure privileges papers, authors, and coarse citations as the primary units, creating a mismatch between the available queries and the queries that facilitate synthesis. This line of research has also converged around a new information model for scholarly communication infrastructures: a discourse graph model. A discourse graph is a graph model in which the nodes are discourse elements (questions, claims, evidence, and concepts) and the edges are discourse relations (support, opposition, consistency, explanation).

        - Though discourse graphs present a powerful and elegant solution, there is one formidable obstacle: how to sustainably get data into this discourse graph model. Expensive manual (volunteer, or paid) labor is the only reliable way we know how to get information into such a model, and sustainability (especially after funding ends) remains a core open challenge. AI alone is not a viable solution; natural language understanding has made great strides, but the task of reliably converting messy unstructured, jargon-filled, and imprecise natural language scientific texts into accurate discourse graphs remains a challenging open problem.

        - While this problem may seem intractable, it is important to note that scientists are __already__ doing most of the authorship labor. Indeed, the discourse graph model matches the intuitive ways that scientists make sense of the research literature and design and interpret the results of their own studies. Thus, scientists themselves could solve the authorship problem if there were a way to seamlessly integrate authorship of the discourse graph into the intrinsically motivating work that scientists already do.

        - This project therefore investigates how to design a sustainable authorship model for discourse graphs. The goal is to design an effective and user-friendly authoring system that enables scientists to transfer the results of their research and literature reviews (e.g. findings that support or oppose a given hypothesis) to a more legible and shareable form (i.e. input into a shared discourse graph). The system would be interoperable with their existing tools and workflows, in ways that improve their own synthesis and unlocks new capacities to deeply collaborate on synthesis work within and across research groups. We approach this as a sociotechnical HCI research problem, given that the key issues will be efficacy, motivation and user experience.

        - 2-pager [here](https://docs.google.com/document/d/17McXPvxlplXC7-6_KJSchzCHw0Vg-iViv7Fs3l03k9c/edit)

    - ## OKRs

        - Alongside this development work, field studies with the existing user base (at least 800 “Roamans” working with this software to create and share discourse graphs) have provided sufficient validation of the core hypothesis that discourse graph authoring can be integrated seamlessly into the natural synthesis workflows of scientists.

        - Joel used a previous award of $9k to engage a developer, David Vargas, to extend the working prototype of the discourse graph extension for RoamResearch (which, prior to the award, had a proof-of-concept capability to construct a formal discourse graph as a byproduct of writing/outlining, explore/query the graph in basic ways, and export/backup parts of the graph in basic interoperable formats) along three key dimensions:

            - **Extend and personalize a discourse graph translation grammar** (which reifies discourse graph nodes and relations that are latent in users’ writing practices) to more seamlessly integrate with their personalized note-taking and writing practices. This is a key enabler of adoption to drive virtuous cycles of a shared discourse graph commons. Key features developed include the ability to document and "fork/duplicate" relation patterns that map writing/outlining patterns to discourse graph relations.

            - **Leverage a discourse graph data structure to overcome key bottlenecks in synthesis workflows**, such as leveraging discourse graph metadata and queries like “find all claims that are both heavily referenced and mixed in terms of supporting/opposing evidence” to manage and develop important new ideas over time. This is another key enabler of adoption. Key features developed include the ability to overlay discourse context information (e.g., ratio of discourse relations vs. raw mentions) for any given discourse node (e.g., question, claim, evidence) being used in an outline, to enhance the synthesis process, and powerful upgrades to the querying engine to enable incrementally structured comparisons and analyses of evidence, such as "find all evidence that inform a question, and group by a study attribute, such as location or measurement approach", or filtering/sorting of claims based on evidentiary support.

            - **Selectively and seamlessly share elements of their discourse graph with others (and subscribe to queries from others’ discourse graphs)** in a peer-to-peer infrastructure. This is a key building block towards moving from individual discourse graphs to a shared commons. A key feature developed was the ability to connect to other graphs via peer to peer and "push/pull" discourse graph nodes, as well as incrementally request nodes, while preserving provenance information of each node (transcluding rather than copying content to a peer's graph).

        - The core functionality of the extension has stabilized sufficiently to allow for a more mature and stable documentation to be drafted: https://oasis-lab.gitbook.io/roamresearch-discourse-graph-extension/
[[October 22nd, 2021]]

- would love to see if htis could hook up with [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - create different "evidence node" that we can use to inform our own thinking (before publishing), and then just seamlessly publish just *that* thing, and later stitch together into a traditional pub if we want

        - need buyin from publishers

            - maybe [[William Gunn]] has connections?

            - [[Anita De Waard]] via [[Simon Buckingham Shum]]?

            - Michael Eisen

        - and technical infrastructure

            - [[sys/Ceramic]] for these streams, and hosting

                - maybe large nonprofits and networks of labs like [[Allen Institute for Science]] could host these repos?

                    - decentralized?

            - [[org/Protocol Labs]] - [[Alan (Red) Ransil]] was talking about permissionless DOIs, as part of the
[[August 20th, 2021]]

- with [[Lisa-Marie Cabrelli]] and her students for [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - about 28 people on the call (more couldn't make it, asked for recording)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6C-lo93P99.png?alt=media&token=82c65415-4b24-48c3-b48b-831ba3bd6e0f)

    - key feedback for improvements: would really like to be able to access nested blocks (in specific format according to Lisa's structure) easily. this probably makes sense as a configurable thing.
[[March 2nd, 2022]]

- [[@heerAgencyAutomationDesigning2019]] coming back into orbit, core idea of [[shared representations]] for human-AI interaction - idea of [[domain-specific language (DSL)]], which is how the relation grammar works for [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRIqxE5NtkE.png?alt=media&token=117c9b43-02d9-461e-bcca-2e232d397338) 
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FoGo7FIGX1j.png?alt=media&token=ff614468-2bb1-407e-983f-5682ceaa7afb)(pp. 1848-1849)

    - cc [[Robert Haisfield]] [[Brendan Langen]]
[[October 16th, 2021]]

- Thinking about [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - Principle of "[[minimum benefit distance]]" as a way to capture our decision process in imposing structure. Only impose structure that is maximally helpful in the closest possible proximity to users' intrinsic goals.

        - As a user I want to [intrinsic goal], and [structure] can help me by [functionality]; therefore, the extension smooths the process of creating [structure]

    - Another principle: something deeper than [[interoperability]], but really leaning into the concept of [[[[PTN]] - boundary object]]s: weak structure in common use, but strong (and variable) structure in local use

        - Also related:

            - [[[[CLM]] - [[[[PTN]] - incremental formalization]] can mitigate risks of formalism in interactive systems]]

            - [[[[QUE]] - How can we best bridge private vs. public knowledge?]]

            - [[[[QUE]] - Under what conditions is it possible to transfer expertise from one person to another?]]
[[August 21st, 2021]]

- Testing out new generalized query drawer for [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - Now let's go to [[Playground: Analogy domain distance]]
[[August 19th, 2021]]

- with [[Lisa-Marie Cabrelli]] re: [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - "magical
[[February 17th, 2022]]

- writing quickly for [[[[PTN]] - discourse graph]] authoring systems --> [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]:

    - design principles

    - system components

        - grammar translation system addresses [integration](integrated into intrinsic work of synthesis, with minimal friction)
[[August 17th, 2021]]

- Looking at the screenshot from an old interface ([[sys/Hyperties]]), and realizing some major difference and innovation with what we're doing with [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] and [[hypertext notebooks]] in general for synthesis

    - 1: we are joining the idea of [[[[PTN]] - discourse graph]] with the technical affordances of [[hypertext notebooks]]. In contrast to the usual situation in hypertext and [[sys/Wiki]]s, where the nodes and pages are *entitities* (mostly nouns/concepts), the nodes in a [[sys/Zettelkasten]] or [[sys/Evergreen Notes]] system are *statements*. This is new and significant!

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_UpktpbxXJ.png?alt=media&token=64d32fa7-f2be-4ad1-9325-f93d8fc05caa)

    - 2: we are also focusing more on the authoring process, or at least where the author and the consumer are the same, and where the hypertext is being written for generative purposes, not merely for reference material
[[April 12th, 2022]]

- The most important next right thing for [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] is to do a proper walkthrough demo, like a real one, of the workflow from start to finish.

    - We already have [[outline/[[D/Synthesis Infrastructure]] - discourse graphs paper]]
[[October 22nd, 2021]]

- also eager to use [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] for own lab

    - easy sell for supporting:

        - writing intro

        - mini lit reviews to choose next experiment

        - parameters for simulations/models

    - want to experiment with this!

    - [[Allen Institute for Science]] and others probably would be excited about this as well, along with folks in his department at [[University of Washington]]
[[August 13th, 2021]]

- Demo some new stuff for [[Lukas Kawerau]] from [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - Playground!

    - Grammar preview!

    - Subscriptions proof-of-concept!
[[May 23rd, 2022]]

- Prep for tour draft of [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] with [[Rob Haisfield]]: how does the d/graph integrate into my synthesis workflow?

    - Overview of the flow??? (probably too much)

        - In Roam/synthesis/demo

    - What it looks like in my graph

        - Mechanics: what does it look like in the day to day?

            - Examples of how the discourse relations are instantiated? This is how this relationship gets populated

        - Benefits: Two key things to convey:

            - The experience of having things "at hand"

                - Better notes

                - Better discussions with others -

                    - really tough to kind of... push things through a straw (speaking), and really ineffective and inefficient to try to push through writing. can get alignment through shared sketching. but what about all that context?

                    - [[[[EVD]] - Technical design knowledge at IDEO that was used for analogical inspiration resided in a mix of artifacts, prototypes, and designers' memories, and was actively maintained through routines of access in design work - [[@hargadonTechnologyBrokeringInnovation1997]]]]

                - While thinking/outlining/gathering / quicker first pass based on claims and questions

                    - **Design Argument** for [[idea: sociotechnical analogical connector]]

                    - thinking through [[[[QUE]] - What is a model of the problem space?]]

                    - thinking through connections: a collaboration opportunity

                - Talkback with the discourse overlay's discourse attributes: better linked references - tell how developed an idea is by looking at the numbers

                    - [[[[THE]] - interaction-oriented theory of creative inspiration from examples]]

                    - [[outline/[[D/Synthesis Infrastructure]] - discourse graphs paper]]

                - In meetings with others, "bringing it to the table instead of a mere mention"

                    - regular lab meeting, brainstorming new tasks: [[[[CLM]] - Expert designers are solution-oriented]]

                    - ad-hoc discussion of a research idea with someone: really interested in chaining multiple analogies, 2nd order effects, fine-grained "motifs".

                    - brought this into meeting more than 2 months later to scaffold discussion: some musings from [[March 3rd, 2022]] on [[[[QUE]] - What is a model of the problem space?]]

        - Context

            - What are the relationships I've created

    - Considerations

        - Change the Zs to CLMs

    - My goals/audience

        - Goal: help onboard people

            - Convey what is possible, really, with the extension, not hypothetical

            - Show possibility of fitting diff. workflows (maybe RJC)

        - Audience

            - Not Roam-naive

            - Initial audience is researchers
[[March 24th, 2022]]

- this highlighter thing is key analog to what makes [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] tick: structure only when ready ([[[[PTN]] - incremental formalization]])

    - also the grammar
[[August 14th, 2021]]

- Watching [[Lukas Kawerau]] first look at the [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] from [[August 12th, 2021]]

    - Thoughts/responses:

        - Distinction between claims and evidence in my view is absolutely crucial, and often gets lost.

            - My hope is that this extension makes that distinction more explicit and easier to put into practice!

            - Many of my students struggle with this in practice, but not in concept; for some reason we are trained as academics to conflate these, despite the central importance of the [[dance between the theoretical and the evidential]] for [[synthesis]]!!!

            - If we don't distinguish them, the risk of [[🧱 fixation]] from prior work is very high: we won't be able to effectively clarify (not obscure) and productively attempt powerful resolutions to inconsistencies in past work ([a central requirement for effective synthesis](> A quality [[synthesis]] will clarify and resolve, rather than obscure inconsistencies or tensions between material synthesized)), and do powerful things like [[Hegelian dialectic]] and [[🧱 conceptual combination]]

        - Extension now has preview of what different relation patterns look like!

            - Defining user-friendly ways to construct patterns is an important open question: for now, the bet is that some subset will be comfortable enough with the block-based grammar to extend the set of user-defined patterns and share them on an exchange (similar to [[roam42]] SmartBlocks store), while others will be able to understand which patterns would fit in their own graph and working patterns based on the previews

        - Missing discourse context from CLM page to EVD has easy fix: need to define "complement" (if A supports B, then B is supported by A)

        - Response to Q from Shana Tote: Export is strongly influenced by value of interoperability: for now it exports to [[std/neo4j]] compatible CSV, as well as a zipped folder of markdown files are plain text (with resolved blockrefs) so they basically work anywhere

        - #idea - the way you explained export (almost like exporting from playground) goes beyond current functionality, but could easily be folded into it, I think! I'll make that a milestone to shoot for bc I can clearly see myself using it too.

        - didn't realize that the node menu makes it easier to migrate! :) love the way you explained it

    - Good to know

        - backslash conflicts with random quote extension: also i cant use backslash in roam anymore :P
[[October 21st, 2021]]

- really great discussion with [[Lukas Kawerau]] and [[Cite-to-Write]] crew about [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]:

    - some highlights

        - warrants: super important, but unclear how to represent in text/prose in a seamless way.

            - one quick idea:

                - for early stage stuff, can do the basic CLM-SupportedBy-EVD pattern

                - but as we think more carefully about things, we can "annotate" a support relationship in the following ways:

                    - single warrant for single evd

                        - CLM

                            - `SupportedBy` EVD `Because` CLM (acting as warrant)

                    - shared warrant

                        - CLM

                            - `SupportedBy` `Because` CLM (acting as warrant for a group of evidence with the same warrant)

                                - EVD

                                - EVD

                    - we'd need to then also annotate the edges in the end

                        - we might need to bust out the

        - distinction between evidence as role vs. evidence as thing - maybe a confusion of terms?

            - suggestion that "data" might be clearer?

            - questino was from law prof, focus on legal arguments

        - scale?

        - how to claims emerge from evidence?

        - qce changing the way reading happens: multiple passes expected
[[August 27th, 2021]]

- Thinking about [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] and publishing

    - Question that I think [[org/Protocol Labs]] can help with (maybe post on their Slack). pros and cons of publishing to [[org/TheGraph]] vs. [[sys/Ceramic]]?
[[August 25th, 2021]]

- with [[Danny Zuckerman]] from [[sys/Ceramic]] discussing [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

    - pre-writing some thoughts/questions:

        - focusing mostly on the individual and P2P/collaborative case for now, but want to make sure I'm not unduly narrowing the design space

        - broader vision of my work is a decentralized infrastructure for synthesis (via discourse graphs as the general infrastructure, and maybe connected to more granular knowledge graphs like domain ontologies)

            - requirements/issues:

                - federation/multiplicity - allow for multiple ways of saying things, no single canonical graph join

                    - not sure how this interfaces with content-based addressing

                - robust decentralization

                - change is central, and may be rapid!

    - notes:

        - can use [[sys/Ceramic]] to stream between graphs

        - interesting issue of how to represent changes over time - could get expensive to have each question/claim/evidence be its own stream

        - can subscribe to streams
[[December 18th, 2021]]

- In [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]], the grammar does this

    - So I think a milestone that dovetails into sharing, is some way to better document the grammar, and also make sure json exports include that documentation

    - Could also maybe put some brakes on grammar expansion creep - are you sure you want to make this distinction?
