---
title: [[PTN]] - incremental formalization
url: https://roamresearch.com/#/app/megacoglab/page/uqjCEC29Z
author: Joel Chan
date: Sat Nov 30 2019 01:49:56 GMT-0500 (Eastern Standard Time)
---

- #[[🔨designpatterns]]
- Basic idea: (mostly) informal entry of information, then defer formalization until later in the task when it is useful
- Key advantages:

    - Reduce initial overhead of entering information

    - Reduce risk of harm from prematurely committing to the "wrong" structure
- Examples of incremental formalization

    - In the [[sys/Hyper-Object Substrate (HOS) system]], users enter mostly informal text initially, and the system recognizes patterns in the textual information to suggest possible formal attributes or relations for the underlying knowledge base, which the user can then accept/modify/reject as they wish (p. 347).

        - example-of:: [[[[PTN]] - incremental formalization]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fnv5jGR2KtA?alt=media&token=7ab4cc41-116f-41d5-a440-d75b3a6d6741)

        - Original cite is [[@shipmanSupportingKnowledgebaseEvolution1994]]

    - Infoscope is a news reader system that suggests filters based on users' reading patterns; this helps them make their goals explicit which can facilitate formalization after it emerges from their task behaviors (p. 347-348)

        - example-of:: [[[[PTN]] - incremental formalization]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fts6VgCsUgF?alt=media&token=a90690af-947d-4767-922d-ca32ed3a7282)

    - VIKI is a spatial hypertext system that includes heuristic algorithms to find recurring visual/spatial patterns in layout of objects; users can use these to specify schemas if they wish

        - example-of:: [[[[PTN]] - incremental formalization]]

        - [[@marshallVIKISpatialHypertext1994]]

###### Discourse Context

- **Informed By::** [[@marshallVIKISpatialHypertext1994]]

###### References

[[July 11th, 2020]]

- No support for [renaming](https://foambubble.github.io/foam/renaming-files) files, or otherwise "[janitor](https://foambubble.github.io/foam/workspace-janitor)" tasks that are essential for [[[[PTN]] - incremental formalization]]

    - Interesting that the idea here builds on what [[Andy Matuschak]] did with his [[sys/note-link-janitor]] system
[[@furnasRepresentationalChangeSensemaking2008]]

- Discusses (introduces?) idea of [[Proto-Representations]], which reminds me of [[[[PTN]] - incremental formalization]] and our identification of intermediate synthesis products in [[WP: Synthesis empirical paper]] (p.4)

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FjX7yCM9xus?alt=media&token=c46752d6-145a-4d75-886a-7eb05e593cf9)

    - cf. also #[[[[CLM]] - Composability is necessary for synthesis]]
[[Blog post about PTN - incremental formalization for RoamBrain]]

- ### Features that enable [[[[PTN]] - incremental formalization]]

    - **Unlinked references** and **Frictionless creation of pages**: initially write informally before you know a term is important, later turn into a formal link to a page via unlinked references, or just double-bracketing when appropriate.

    - **Easily updated pages**: don't worry about precisely naming something at first, let the meaning emerge over time and easily change it (propagating through all references)

        - cf. [[Andy Matuschak]]'s comments about [[context]]ual backlinks bootstrapping new concepts before explicit definitions come into play

    - More generally, in Roam, **text is mixed with code** (similar to [[literate programming]], the paradigm from which Jupyter and other code-notebook systems have been inspired), but with a much deeper potential integration than simply interspersing text and code: each block is computable from the start. A simple example of this is the `calc` command, which grabs numbers from a block and makes them available for computation.
[[July 16th, 2021]]

- [[Wayne Lutters]]: idea of [[[[PTN]] - incremental formalization]] really resonates here

    - bit about being able to write and formalize later is really really important, particularly for the later ontology stuff
[[@gruberDarwinManPsychological1974]]

- Seems like we can see [[[[PTN]] - incremental formalization]] at work there: lots of intermingling, not much indexing a priori, lots of it after the fact

    - Key quote

        - > "Keeping notes, then was not simply a matter of recording observations. It was the expression of a broad philosophical point of view, and an opportunity for deepening thought and strengthening command of one's personal knowledge" (p. 22)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRJnCbtcJpg.png?alt=media&token=1df7e9fa-3a2a-4109-b847-69ef292b5871)
[[Review of existing synthesis tools]]

- [[[[PTN]] - incremental formalization]]

    - We repeatedly see people to many / multiple / repeated passes over things in various ways, from [[strategic reading]] to [[skimming]] to [[active reading]]

        - crossing the boundary from reading/annotating in the early stages, to the knowledge management / synthesis you might do later on. One example: in E's protocol/process, we see a separation from early stage highlighting/underlining, to mid-stage claim-writing in a notebook, to later-stage synthesis in a concept map. There is a manual linkage between them that might be lossy. Another example is [[Beck Tench]] 's process of reading stuff in a bunch of different forms, bullet-journaling, and then ultimately putting things into Tinderbox to synthesize over time. An important question is where our tool might fit in and plug into a larger infrastructure. THis is related to the idea of incremental formalism and the iterative nature of sensemaking, but can also be connected to lay advice about reading in multiple passes, and research on active reading.

        - One entry point into this is now: [[[[CL]] - People process complex information in multiple levels and stages of processing]]
[[@horn2002visual]]

- Similar to  #idea from [[March 16th, 2020]] around [[Mixed-Initiative]]-powered [[[[PTN]] - incremental formalization]]

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F5RJ73ObzKj?alt=media&token=89abf34c-7f32-47a8-91a0-6fb89a78845a)
[[Research proposal for P COVID-19 treatment search]]

- System: What can we (co-design) with the team to speed up the process? Where might ML, [[[[PTN]] - incremental formalization]], [[[[PTN]] - flexible compression]], etc. come in?

    - Experimenting with a collaboration system that implements [[[[PTN]] - incremental formalization]], among other things - division between domain scientists and synthesis assistants

        - Side note: new form of knowledge work? Connections to librarianship?

        - #idea What would librarianship of community [[sys/Zettelkasten]]s look like?

    - Tools for [[[[PTN]] - incremental formalization]] and [[[[PTN]] - flexible compression]] would really come in handy, integrated into the synthesis process

        - Slackbots to monitor Slack convo and extract stuff for synthesis

        - Remix of the [[[[ART]] - Knowledge Compressor]] to

            - Similar to previous idea around #idea Make a [[grounded claim]] ([[[[PTN]] - flexible compression]]) embed for [[sys/RoamResearch]] (or other [[sys/Zettelkasten]] systems)

            - Basic idea: just change the PDF reader (probably in-browser is best), and send "highlights" to a [[[[PTN]] - flexible compression]] module

    - In a [[Participatory Design]] vein, we'd want to document, in detail:

        - "Friction moments" or catalysts, (maybe also cf. [[[[CLM]] - Infrastructure is invisible until it fails]])
[[Research proposal for P COVID-19 treatment search]]

- Tools for [[[[PTN]] - incremental formalization]] and [[[[PTN]] - flexible compression]] would really come in handy, integrated into the synthesis process

    - Slackbots to monitor Slack convo and extract stuff for synthesis

    - Remix of the [[[[ART]] - Knowledge Compressor]] to

        - Similar to previous idea around #idea Make a [[grounded claim]] ([[[[PTN]] - flexible compression]]) embed for [[sys/RoamResearch]] (or other [[sys/Zettelkasten]] systems)

        - Basic idea: just change the PDF reader (probably in-browser is best), and send "highlights" to a [[[[PTN]] - flexible compression]] module
[[April 12th, 2021]]

- [[Anna Noel-Storr]] need for [[[[PTN]] - incremental formalization]]: get your schemas in place for modeling, but then this is tough because what's interesting/important changes rapidly, making your schemas obsolete quite quickly

    - also nervous about ongoing perforamnce of classifiers bc they were trained on early data
[[August 1st, 2020]]

- Thinking now also that it might be high value to, in addition to having "zettels", "questions", and so on, having #[[🔨designpatterns]] would be really useful on the system side. One obvious one is [[[[PTN]] - incremental formalization]], but there are others too.

    - Connecting to [[strong concepts]] [[@hookStrongConceptsIntermediatelevel2012]], as a complement to [[sys/Claim]]s

    - Other examples of this:

        - [[[[PTN]] - Integrated crowdsourcing]]

        - [[human-in-the-loop]]

        - [[[[PTN]] - Prefer to accrete new infrastructures on top of existing ones]]
[[January 3rd, 2022]]

- In a sense this seems to recapitulate the error from [[[[ART]] - Knowledge Compressor]], and the more general need to allow for rich gradations of [incremental structure]([[[[PTN]] - incremental formalization]]) from very informal, flexible, to progressively formal and structured representations. One hypothesis is that ^^**core friction points in systems for creative work are at these transition seams, the "liminal spaces"**^^.

    - See also headers and memos as [[[[PTN]] - incremental formalization]]

    - This reminds me
[[August 22nd, 2020]]

- [[sys/RoamResearch]] does allow for a [[dialectic]] between the formal and the informal, smoothly deploying various mechanisms of [[[[PTN]] - incremental formalization]] to fluidly move between them, from daily notes to zettels, post-hoc block creation and references, unlinked references and so on.

    - but it's, as I wrote previously, and discussed with [[Sue Borchardt]], [seriously limited on the dialectic between the verbal and the nonverbal](A serious limitation of [[sys/RoamResearch]] is the friction of moving to nonverbal / visual modalities of exploration. While [[[[CL]] - Visual thinking interfaces are tricky to get right]], most serious work probably has to move between verbal and nonverbal (less propositional?) modalities of representation: the holy grail is being able to move between the two (incidentally this is what [[sys/Liquid:Author]] can do, and is anticipated by the idea of [[[[PTN]] - representational talkback]] introduced in [[@yamamotoRepresentationalTalkbackApproach1998]]), and strongly related to this idea of [[Reflective Conversation with the Design Material]] and [co-evolution of design and problem space]( [[[[CLM]] - Design proceeds by co-evolution of problem and solution space]]))
[[Research proposal for P COVID-19 treatment search]]

- Experimenting with a collaboration system that implements [[[[PTN]] - incremental formalization]], among other things - division between domain scientists and synthesis assistants

    - Side note: new form of knowledge work? Connections to librarianship?

    - #idea What would librarianship of community [[sys/Zettelkasten]]s look like?
[[March 24th, 2022]]

- this highlighter thing is key analog to what makes [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] tick: structure only when ready ([[[[PTN]] - incremental formalization]])

    - also the grammar
[[@shipmanFormalityConsideredHarmful1999]]

- [[[[PTN]] - incremental formalization]] can mitigate costs/risks of [[formality]] in interactive systems (section 4.3, p. 347-438)

    - Basic idea: (mostly) informal entry of information, then defer formalization until later in the task when it is useful

    - Key advantages:

        - Reduce initial overhead of entering information

        - Reduce risk of harm from prematurely committing to the "wrong" structure

    - Examples of incremental formalization

        - VIKI is a spatial hypertext system that includes heuristic algorithms to find recurring visual/spatial patterns in layout of objects; users can use these to specify schemas if they wish

            - example-of:: [[[[PTN]] - incremental formalization]]

        - Infoscope is a news reader system that suggests filters based on users' reading patterns; this helps them make their goals explicit which can facilitate formalization after it emerges from their task behaviors (p. 347-348)

            - example-of:: [[[[PTN]] - incremental formalization]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fts6VgCsUgF?alt=media&token=a90690af-947d-4767-922d-ca32ed3a7282)

        - In the [[sys/Hyper-Object Substrate (HOS) system]], users enter mostly informal text initially, and the system recognizes patterns in the textual information to suggest possible formal attributes or relations for the underlying knowledge base, which the user can then accept/modify/reject as they wish (p. 347).

            - example-of:: [[[[PTN]] - incremental formalization]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fnv5jGR2KtA?alt=media&token=7ab4cc41-116f-41d5-a440-d75b3a6d6741)

            - Original cite is [[@shipmanSupportingKnowledgebaseEvolution1994]]
[[Blog post about PTN - incremental formalization for RoamBrain]]

- As another example, adding in page tags (or adding them later via unlinked references) to claim blocks can enable powerful structured aggregation of queries not just by association but involving particular kinds of relationships. Importantly, these can be added later! [[[[PTN]] - incremental formalization]] for the win!

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRZJCZHfR34?alt=media&token=c0cbd429-eefa-4af0-81fd-1988313149b9)
[[December 20th, 2020]]

- Ok let's collect some ideas around [[[[PTN]] - incremental formalization]] to add to #threadapalooza2020

    - 12345

        - {{character-count}}

            - One important thread of this problem is the impact of information organization/architecture. To solve a problem, you want to have the "right" (i.e., sparks useful / creative thoughts)) information at hand, and the "wrong" (i.e., blocks creative thought) far away.

        - {{character-count}}

            - One helpful [[Mise en place]]

        - {{character-count}}

            - What is "the same"? What is "helpful"? We can manually set this up, and often this relies on an unspoken model of our ideas. We could also have our tools help with this, and for that we would need a more explicit model.

        - {{character-count}}

            - We model things so we can find, exclude, link/assemble ideas into larger wholes. This is why some kind of formality is helpful for synthesis

        - {{character-count}}

            - Formality in a particular sense (expressed in machine-readable terms) is also very helpful for enabling computational support for our thinking.

        - {{character-count}}

            - So far so good: to be prepared for creative work, we want everything in place: useful ideas "here", harmful ideas "there". To do this ourselves or w/ computational support, we need a model of ideas. So what's the problem? Why did Shipman write "Formality considered harmful?"

        - {{character-count}}

            - Probably most powerful heuristic is adopting an organizational scheme from someone with similar goals.

        - {{character-count}}

            - Another exciting class of solutions is mixed-initiative systems, where computers and humans work together
[[Grant proposal for Synthesis Infrastructure - NSF CHS  SOS 2020]]

- [[[[PTN]] - incremental formalization]] for [[composability]] is probably focused on the wrong level of analysis (shuld be more about [[discourse]])

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_Bg6le9PIP.png?alt=media&token=b44a7c8d-8862-451e-991e-34fa15da2a97)
[[March 5th, 2021]]

- This feels similar to [[[[PTN]] - incremental formalization]]

    - Seen in this way, the problem of "bubbling up" structure from the beautiful chaos of synchronous conversation is analogous to (or maybe a special case of?) the more general problem of how to join the chaos stream / magical junkyard of fleeting notes with the [[disciplined imagination]] of other spaces?
[[April 11th, 2022]]

- [[[[CLM]] - [[[[PTN]] - incremental formalization]] can mitigate risks of formalism in interactive systems]]

    - #SupportedBy

    - PTN

        - addresses

            - OBST

                - for STAKEHOLDER

                    - in CONTEXT

        - OBST blocks GOAL for STAKEHOLDER in CONTEXT

            - OBST for STAKEHOLDER

                - complement: STAKEHOLDER faces OBST

            - STAKEHOLDER in CONTEXT

                - complement: CONTEXT contains STAKEHOLDER

            - STAKEHOLDER has GOAL

                - CLM

                    - EVD

            - OBST blocks GOAL

    - find all CLM where

        - and

            - OBST is part of CLM

            - OBST for STAKEHOLDER

            - STAKEHOLDER in CONTEXT

    - PTN

        - is-variant-of

            - PTN
[[July 12th, 2020]]

- experimenting with [[sys/Mermaid diagrams]], which is a potential #system-for and #example-of [[[[PTN]] - incremental formalization]]

    - [[Another paper on face masks]](https://www.sciencedirect.com/science/article/pii/S0021850220301063#bib48)

    - Then, model

        - {{mermaid}}

            - graph LR

                - cloth_masks --> |reduces| droplet_volume

                - humidity --> |reduces| evaporation_rate

                - droplet_volume --> |increases|transmission_risk

                - evaporation_rate --> |reduces| droplet_volume

                - air_circulation-rate -->|reduces| droplet_volume

                - vocalization_intensity -->|increases|droplet_volume

    - First, some notes from [[Fundamental protective mechanisms of face masks against droplet infections]]

    - Video idea here (need to do a better one)

        - {{[[youtube]]: https://youtu.be/0ZchzFnX_YM}}
