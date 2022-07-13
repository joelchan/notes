---
title: @shipmanFormalityConsideredHarmful1999
url: https://roamresearch.com/#/app/megacoglab/page/4ZULLd46a
author: Joel Chan
date: Tue Feb 11 2020 15:53:20 GMT-0500 (Eastern Standard Time)
---

- #references

    - Title: Formality Considered Harmful: Experiences, Emerging Themes, and Directions on the Use of Formal Representations in Interactive Systems

    - Meta

        - Tags:: #[[D/Synthesis Infrastructure]]

        - Authored by:: [[Frank Shipman]] ,  [[Catherine C. Marshall]]

        - Year: [[1999]]

        - Publication: Computer Supported Cooperative Work (CSCW)

    - Context

        - #canonical paper in lab

    - #[[📝 lit-notes]]

        - Four problems with / created by formalization: 1) cognitive overhead, 2) tacit knowledge, 3) premature structure, and 4) situational structure

            - Cognitive overhead (aka [[Cognitive Load]]): often the task of specifying formalism is extraneous to the primary task, or is just plain annoying to do

            - [[tacit knowledge]]: if relevant info for developing formalism is tacit, asking people to formalize it will interrupt the task, with serious consequences for the quality of the work

            - [[Enforcing Premature Structure]]: people don't want to commit until they're sure what formalism is actually useful for their task (and what's extraneous and only annoying)

            - [[Situational Structure]]: Useful structures and formalisms vary significantly across people, situations, and tasks

        - [[[[PTN]] - incremental formalization]] can mitigate costs/risks of [[formality]] in interactive systems (section 4.3, p. 347-438)

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

###### Discourse Context

- **Informs::** [[CLM - (premature) formalism considered harmful]]
- **Informs::** [[CLM - Gracefully integrating formalism into interactive systems is hard]]
- **Informs::** [[CLM - PTN - incremental formalization can mitigate risks of formalism in interactive systems]]
- **Informs::** [[CLM - Distinction between neat vs scruffy in Semantic Web engineering]]
- **Informs::** [[QUE - How might we conceptualize and measure synthesis quality]]

###### References

[[CLM - Gracefully integrating formalism into interactive systems is hard]]

- These problems are well-documented in the classic "Formality Considered Harmful: Experiences, Emerging Themes, and Directions on the Use of Formal Representations in Interactive Systems" [[@shipmanFormalityConsideredHarmful1999]]. In brief, this paper identifies four classes of difficulties:

    1. Cognitive overhead (aka [[Cognitive Load]]): often the task of specifying formalism is extraneous to the primary task, or is just plain annoying to do

    1. [[tacit knowledge]]: if relevant info for developing formalism is tacit, asking people to formalize it will interrupt the task, with serious consequences for the quality of the work

    1. [[Enforcing Premature Structure]]: people don't want to commit until they're sure what formalism is actually useful for their task (and what's extraneous and only annoying)

    1. [[Situational Structure]]: ((LhqpJ_jeV))
[[Research proposal for P COVID-19 treatment search]]

- Follow citation thread from [[@shipmanFormalityConsideredHarmful1999]] to see what we've done already ont his integration question. NOT tool development only, or description only, but studies of how we can __integrate__ standards and [[formality]] into existing workflows (and if not, how to sustainably change them)

    - Cc [[[[QUE]] - Do scholarly synthesis infrastructures already exist?]]: [[Scholarly Ontologies Project]] is one extremely relevant prior art on this.

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft5dI7cHi6j.png?alt=media&token=4cbfae55-c940-40a2-8382-872f9e11addb)

        - #> from [[@urenSensemakingToolsUnderstanding2006]]

    - in zotero
[[CLM - PTN - incremental formalization can mitigate risks of formalism in interactive systems]]

- Here I note a few examples from [[@shipmanFormalityConsideredHarmful1999]] to help flesh out the concept (these are all older systems, mostly research systems, so unfortunately they're not available to play with):

    1. In the [[sys/Hyper-Object Substrate (HOS) system]], users enter mostly informal text initially, and the system recognizes patterns in the textual information to suggest possible formal attributes or relations for the underlying knowledge base, which the user can then accept/modify/reject as they wish (p. 347).

    1. Infoscope is a news reader system that suggests filters based on users' reading patterns; this helps them make their goals explicit which can facilitate formalization after it emerges from their task behaviors (p. 347-348)

    1. VIKI is a spatial hypertext system that includes heuristic algorithms to find recurring visual/spatial patterns in layout of objects; users can use these to specify schemas if they wish
[[Brain dump from Wayne Lutters about DSynthesis Infrastructure on February 18th, 2020]]

- [[Gerhard Fischer]] did some really nice stuff that's counter to formality considered harmful [[@shipmanFormalityConsideredHarmful1999]] for community deliberation - what's the lightweight [[sys/IBIS]] experience?

    - Not sure where it is now

    - Showed up in the "I-Know" conference in Austria (https://twitter.com/iknowconf?lang=en)

        - Non-archival conference

        - Anti-[[MIS]] crowd

    - Tabletops were involved; possible seed: [[@fischerCollaborativeDesignRationale2013]]
[[CLM - PTN - incremental formalization can mitigate risks of formalism in interactive systems]]

- The basic intuition is described well by [[@shipmanFormalityConsideredHarmful1999]]: user enter information in a mostly informal fashion, and then formalize only later in the task when appropriate formalisms become clear and also (more) immediately useful.

    - Basic idea: (mostly) informal entry of information, then defer formalization until later in the task when it is useful
[[#AnnotatedBib for Synthesis Infrastructures]]

- [[@shipmanFormalityConsideredHarmful1999]]

    - Gets at the problem of formalism and introduces the idea of [[[[PTN]] - incremental formalization]]
