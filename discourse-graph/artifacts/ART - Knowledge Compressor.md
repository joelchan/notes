---
title: [[ART]] - Knowledge Compressor
url: https://roamresearch.com/#/app/megacoglab/page/fWbx35a-N
author: Joel Chan
date: Tue Apr 28 2020 11:51:16 GMT-0400 (Eastern Daylight Time)
---

- Example:

    - Processing 20 papers in [[[[ART]] - Knowledge Compressor]] around August [[2019]]

        - {{youtube: https://www.youtube.com/watch?v=h72JzSKPZ3Q&t=3215s}}

###### Discourse Context

- **Uses::** [[PTN - flexible compression]]

###### References

[[May 30th, 2020]]

- Processing 20 papers in [[[[ART]] - Knowledge Compressor]] around August [[2019]]

    - {{youtube: https://www.youtube.com/watch?v=h72JzSKPZ3Q&t=3215s}}
[[July 7th, 2020]]

- This is the direct design precursor to the [[[[ART]] - Knowledge Compressor]] in our OneNote "fast context capture" page in the "improving lit reviewing" section of the "KnowledgeCollider" notebook

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F31ikE3uJ7p.png?alt=media&token=d28c7d4b-5289-42c6-b503-db2fdd1d7223)
[[February 16th, 2021]]

- [[[[ART]] - Knowledge Compressor]]

    - what did we learn?

        - again, still lacking on the information model

        - getting warmer with the information model but still not quite there yet

            - good:

                - context snippets

                - claims and context = [[grounded claim]]s [[@qianITunesPapersRedefining2019a]]

    - Processing 20 papers in [[[[ART]] - Knowledge Compressor]] around August [[2019]]
[[June 9th, 2020]]

- Revisiting all the hard work that [[Matt Erhart]] did on the PDF side of things, first with [[sys/Active Science Reader]], and then with [[[[ART]] - Knowledge Compressor]]

    - IIRC, our conversion was definitely not perfect. It was very close, but not perfect. The goal of having some kind of UI for fixing the "last mile" is still an open problem. Not particularly glamorous for HCI, but really important, nonetheless.

        - Recognizing all text in PDF - fairly easy

        - Recognizing all text in PDF while preserving semantics (row/column, section, etc.) - HARD

    - Ok digging back through what we've done

        - [[Matt Erhart]] [wrote up a whole thing](https://docs.google.com/document/d/1IBGayrHXkHNeKQRsdus5JBTBUzuMC6SVKVKSCJfK6bY/edit) about a [[Mixed-Initiative]] approach, discussed with [[Aniket Kittur]] but didn't gain traction because wasn't priority for [[sys/Fuse]]

    - What resources are potentially available?

        - There were productive conversations with [[Jonathan Lazar]] back in Fall of [[2019]]. I think they are still motivated. Can work with [[TRACE Center]] to get funding, maybe? There is a very strong overlap in shared goals. Not sure if the closed-source IBM stuff will completely fly, but we could potentially figure out an abstraction over it (e.g., foundation funding)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQqGWY6g-ji.png?alt=media&token=d4739f48-4ad5-40f1-9705-b01d81788123)

            - Didn't work out, in part because we ran out of money and because the potential partner ([[sys/PAVE]]) couldn't work out a licensing thing

        - [[sys/IBM Corpus Conversion Service]]

            - [Corpus Conversion Service Makes PDF Content Discoverable | IBM Research Blog](https://www.ibm.com/blogs/research/2018/08/corpus-conversion-service/)

                - System described in #[[@staarCorpusConversionService2018]]

                    - Love the key insight here: A key element is that we designed the human-computer interaction in the system to allow very fast and massive annotation without any computer science knowledge.

                - This ([[PDF parsing]]) [problem]([[[[QUE]] - What are effective ways to parse PDFs into usable structured data?]]) was and remains a huge bottleneck. Without some kind of semantics behind it, we continue to have the problem of [[Disembeddedness]] with annotations and lossy [[compression]]. I'm thinking of basically all [[annotation]] approaches now, including [[sys/Hypothes.is]], which completely strip the excerpt from its [[context]]

                    - the [[IBM Research]] folks have followed up on this work quite well, see, e.g., #[[@gentilePersonalizedKnowledgeGraphs2019]]

                - #>

                    - Our AI-based cloud system can ingest 100,000 PDF pages per day (even of scanned documents) on a single blade server with accuracy above 97 percent—and then train and apply advanced machine learning models that extract the content from these documents at a scale never achieved before.

                    - A key element is that we designed the human-computer interaction in the system to allow very fast and massive annotation without any computer science knowledge.

                    - we have developed a unique technology that is fully customizable where the AI model can be trained with minimal effort. In fact, we report in [our paper](https://arxiv.org/abs/1805.09687) that an average person can annotate 20 pages per minute. Once several dozen PDFs have been annotated, the machine learning takes over—you can just sit back and watch in awe.

                - Learned about this stuff from the [[AAAI TACOS symposium 2019]]

                    - Side note: let's ingest the notes from that from Evernote too! [[Notes from [[AAAI TACOS symposium 2019]]]]

    - What to do next?

        - {{[[TODO]]}} Talk to [[Jonathan Lazar]]. Need advice on how to get resources, how to proceed.

        - {{[[TODO]]}} Try to get researcher access to the [[sys/IBM Corpus Conversion Service]]. I sent an email to [[Peter Staar]] back in May of [[2019]], but never heard back. Shoudl revive that.

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FGsXh6osadt.png?alt=media&token=f161ae4f-a7fe-4af8-aff9-1f1af55ea133)

        - The basic sketch of the idea is three layers:

            - 1. Alternative PDF reader, powered by

                - [[sys/IBM Corpus Conversion Service]] in the backend: solves [[PDF parsing]] problem

                - This PDF reader creates [[annotation]]s with [[[[PTN]] - flexible compression]]

            - 3. [[Digital Garden]] layer

                - Take various outputs from [[hypertext notebooks]] and make them "shareable". Doesn't have to polished, but it's more of an [[API]] on top of that

                    - e.g., [[sys/Federated Wikis]], [[std/WebMention]], etc.

                - From this layer we can then create a substrate that enables far more powerful and sophisticated mechanisms of [[D/Computational Analogy]]

                    - Not just matching on single purposes and mechanisms (e.g., [[@chanSOLVENTMixedInitiative2018]]), but matching on partial structures of arguments, etc.

            - 2. Personal [[hypertext notebooks]] to create initial synthesis

                - These [[annotation]]s can then be imported into a [[hypertext notebooks]] like [[sys/RoamResearch]] for downstream [[synthesis]].

    - What's exciting about this is that it targets one of the key weaknesses of our [[Grant proposal for Synthesis Infrastructure - NSF CHS Small 2019]] from Fall [[2019]]: it's a key building block that we don't actually want to solve directly, but without it, we are sort of stuck at square one.

    - Side note: ingesting [[Matt Erhart's notes on Compression from June 17th, 2019]]
[[July 11th, 2020]]

- Thinking back again to how we can best write extensions and prototype the piece about [[context]] for [[D/Synthesis Infrastructure]] (building on [[[[ART]] - Knowledge Compressor]]), building stronger, richer links between "source text" and "my thoughts".

    - There is a draw to building on [[sys/Visual Studio Code]]: it's a very mature implementation, with very wide adoption by programmers, who repurpose it for writing notes (just like [[sys/org-mode]] in a way).

        - But adoption of our systems will be limited to the [[Hackers]]

        - Still, we could demonstrate and debug and develop the ideas for the core functionality here first, especially since the "users" can be involved in development as well, and then once we've understood it well, work to transition it "down" the gradient to [[Explorers]] and eventually [[Virtuosos]]

        - In some ways, systems like [[sys/Obsidian]] and [[sys/RoamResearch]] are ideal bridges between the hardcore [[Hackers]] and the [[Explorers]]

            - It can go down further the gradient to [[sys/Notion]] and [[sys/Workflowy]] and [[sys/Dynalist]]

            - And they could adopt these as extensions or driven to development via user demand. And that user demand could come from, just like [[backlinks]] / [[bi-directional links]]

    - But [[sys/Hypothes.is]] already exists. I like the idea of exporting from my own annotations in my favorite PDF software or whatever, into [[sys/Hypothes.is]] as a standard, which then makes it available for integration into other tools for thought, even Google Docs, for example.
[[January 3rd, 2022]]

- In a sense this seems to recapitulate the error from [[[[ART]] - Knowledge Compressor]], and the more general need to allow for rich gradations of [incremental structure]([[[[PTN]] - incremental formalization]]) from very informal, flexible, to progressively formal and structured representations. One hypothesis is that ^^**core friction points in systems for creative work are at these transition seams, the "liminal spaces"**^^.

    - See also headers and memos as [[[[PTN]] - incremental formalization]]

    - This reminds me
[[Research proposal for P COVID-19 treatment search]]

- Remix of the [[[[ART]] - Knowledge Compressor]] to

    - Similar to previous idea around #idea Make a [[grounded claim]] ([[[[PTN]] - flexible compression]]) embed for [[sys/RoamResearch]] (or other [[sys/Zettelkasten]] systems)

    - Basic idea: just change the PDF reader (probably in-browser is best), and send "highlights" to a [[[[PTN]] - flexible compression]] module
[[October 29th, 2020]]

- This is what we wanted to do with [[[[ART]] - Knowledge Compressor]], but we weren't ready yet, not just because we had a canvas as the space for "using" the grounded claims, but also because (I can see now), our data model wasn't *quite* right yet:

    - At least for me, I was rushing from context snippets all the way to high level claims, actually doing lossy compression!!
[[May 23rd, 2019]]

- with [[HCIL]] BBL - discussion and feedback on [[[[ART]] - Knowledge Compressor]]

    - # Outside of session

        - Ge:

            - Transition from map in [[sys/NVIVO]] to writing is always a bit rough

                - would be great to be able to make “submaps”

                - gets hard to manage a very large map

        - Tom Hurst:

            - Can’t wait to

    - # During demo feedback session

        - ## **Conceptual feedback / comments**

            - Do you have a way of **subsetting **or making a **visual background with axes or areas**, so you’re **literally building a map**? (would be killer feature) -- Eric (10:49)

            - I’m **building an argument**, would want to “drop” stuff in there -- Yla (13:11)

            - Other objects on the canvas, can we **“tag” areas of the collection?** -- Tammie (13:11)

            - **Create stuff other than claims **directly tied to PDFs? -- Tammie (13:23)

            - Would want to **make the notes we write different from the claims -- **Eric (13:51) :

            - Killer feature would probably be how do we **take what we have and generate almost a draft of your lit review -- **Catherine (14:00)

            - **What’s the starting point? **A collection? Network? How do you get the starting collection? Collected one at a time? Or search results? -- Ben (15:25)

            - Literature reviewing is painful? But I *like* literature reviewing! --- Ben (16:30):

            - Have trouble with the idea of reducing a scientific paper into a “bit”. It’s **more like a story** for me with a set of personalities and characters. Lots of literature on writing emphasizes the story; should not be a set of bits; beginning, end, sense of drama --- Ben (17:00):

                - --> [[[[CLM]] - Requirements for sensemaking come from the particulars of the work task]]

            - Why are things like **concept maps** insufficient? --- Ben (18:00):

            - Are we reducing the right costs? **Some costs are productive **--- Ben (19:00):

            - This probably requires a lot of screen space! --- Ben (19:43):

            - I use Mendeley comments, and when I go back and look at what I wrote I find them to be completely useless? Can we **support users to actually write useful notes**? If I were the user I would need a lot more guidance, because clearly I’m very bad at it doing this for myself --- Yla (20:30):

            - The story I tell about aging research in HCI is like my own story and how **other people have different stories** about it --- Amanda (22:35)

            - There are **some things I write that I don’t want other people to see **--- Amanda (23:00):

                - [[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]]

            - If somebody shares something with me** I might take much more time to figure out what they’re trying to tell me rather than read the paper from scratch**, especially **if their mental model does not match mine **--- Hernisa (24:00)

            - Would be so interesting to **compare with existing literature reviews** into our map (that’s one way we build off other people’s conceptual models) - is that more useful right now as text, or is it more useful as a concept map? Someone reads a literature review, how much do they get out of it, vs. reading our concept map? --- Yla (25:47)

            - What’s your aspiration **range for number of papers**? --- Ben (32:01)

            - How will we **measure and evaluate the efficacy**? --- Ben (32:32)

            - Do you have a **theory about the content of literature reviews**? Naive is laying out temporal sequence. Forming groups that address particular sub issues and then showing one’s positive and one’s negative on this issue. We had quite an elaborate taxonomy once. Do you believe in taxonomies? Or maps? Or networks? Have you looked at 1000 literature reviews to get a taxonomy of literature reviews? --- Ben (34:15)

            - I almost want to **go from a loose map here to a sort of storyboard**, organize what the story of this lit review is --- Scott (36:27)

            - Well it’s a very ambitious challenge you’ve taken on, and **others have struggled with it** --- Ben (38:11)

            - You’re not just doing a study but **also trying to build a real open source tool that people can use, and OMG that’s really hard.  **--- Catherine (39:11)

            - Are there **other open source tools you can build on**? There are many prototypes that people have in **intelligence and analytics** Sandbox for Oculus (link each little bit to a hypothesis, supporting, etc.) VAST project --- Catherine (40:24)

            - Similar to Argupedia, tying back to evidence. What we’ve found is that **the argument itself is the fun part, building out connections to the evidence is really painful and nobody wants to do it**, labeling it and writing all the details. To do it well** it’s tedious **--- Yla (41:00)

            - Would it be helpful to focus on an area that’s a little bit more formal, like FMRI? Where people have more of a structured shared understanding of how they build these out? Like parts of the brain, physical locations, shared methods? A bit of a cleaner starting point, but might hurt you because it’s too clean --- Yla (43:25)

            - How many people use a reference manager? Does that give you enough support for what you want to do? What’s missing? Yla: No! **Forming the higher level structure and the reuse**. Recording those details that are useful, giving that context that you want to go back to is hard. Doesn’t have any support for higher level concepts --- Ben (44:26)

            - __Responded positively (“that’s a good point”) to the idea of Mendeley being bad because it’s just “Itunes for papers” (wrong unit of analysis) __--- Ben (46:23)

            - Possibly interesting connection to **tools in legal analysis** from Westlaw publishing --- Ben (47:30)

            - There’s a whole industry of people trying to summarize and help you analyze things for money: but we don’t have a whole industry of HCI study guides, cram guides, etc., helping you pass the bar, etc. you can pay people to do grunt work you don’t want to do --- Jonathan Lazar (47:50)

        - ## **Bugs / issues**

            - Security (e.g., Windows protected your PC)

    - Doc: https://docs.google.com/document/d/166DJIXqml_vQDn4tMVwOsTYILtJzfHx640zBwnxThcQ/edit#heading=h.aggx94on4ysj

    - Recording

        - {{[[youtube]]: https://www.youtube.com/watch?v=08Ost65rB8c}}
