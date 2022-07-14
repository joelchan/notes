---
title: [[PTN]] - discourse graph
url: https://roamresearch.com/#/app/megacoglab/page/Yd_CaihTg
author: Joel Chan
date: Tue Aug 04 2020 13:33:54 GMT-0400 (Eastern Daylight Time)
---

- #idea for [[D/Synthesis Infrastructure]], specifically for [[Grant proposal for Synthesis Infrastructure - NSF CHS / SOS 2020]] and beyond
- Diagram in: https://lucid.app/lucidchart/72613594-d7ae-4cf5-a4e9-7b89bbbfca99/edit?page=0_0#?folder_id=home&browser=icon
- Draft writeup here: https://oasislab.pubpub.org/pub/54t0y9mk/draft
- # Draft

    - ## Basic idea

        - ### Structure

            - In this model, we create and update three basic kinds of artifacts in the [[synthesis]] process:

                1. **SYNTHESIS** notes

                    1. This is where questions, claims, and evergreen notes / zettels live. These are meant to be generalizations, arguments, etc. This is where theories will be developed.

                    1. Synthesis notes should be "compressed" in the sense that it should be focused as much as possible on a single idea/question. That being said, each synthesis note can and should be richly connected to other notes.

                    1. We can roughly map this to the "topics/concepts" column in [[synthesis matrix]], and codes in [[sys/NVIVO]], or "hypotheses" in [[sys/ACH]]

                1. **OBSERVATION** notes

                    1. These notes are highly contextualized observations. Like **SYNTHESIS** notes, they're meant also to be "compressed", in the sense that it should be focused as much as possible on a single idea (in this case, a single "result")

                    1. When we say these should be contextualized, we mean it in as expansive a sense as possible: by convention, we write them in the past tense (to ground them in time), bind them to an author (to ground them in the standpoint of the observer), and avoid high levels of abstraction/generalization (e.g., Mount Prospect volunteer librarians, vs. librarians).

                    1. In this way, they are meant to be as close to "the data" as possible (think of what is reported directly in results sections, rather than the "implications" of the observations, or a rich case or anecdote in a qualitative study).

                1. **CONTEXT SNIPPET** notes

                    1. These are contextual details (e.g., author, a graph, details about participants/setting) that ground the **OBSERVATION** notes

                    1. A minimal context snippet note is simply an unnamed excerpt, like a screenshot or quote from a source document. Like a [[[[ART]] - Hypothes.is]] [[annotation]], we can optionally add a note/description to this snippet to enrich it further.

            - Conceptually, the three kinds of artifacts relate to each other like this:

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FNO0Klo46TA.png?alt=media&token=cd082e98-a461-4399-8017-e7f087fc9fa6)

                - Consider first the ordering of the artifacts: there is a hierarchical relationship between the artifacts: **SYNTHESIS** notes (at the top "layer") are ^^supported/opposed by^^ one or more ((QZlhwWCmB)) (at the middle "layer"), which are ^^substantiated/contextualized by^^ one or more ((epmLwtUy0)) (at the bottom "layer").

                - Next, consider the relationship that **SYNTHESIS** notes can have with artifacts of the same type: this expresses the idea that ((3FmhPV1OM)) can be ^^composed^^ into more complex structures (such as arguments or theories or models) through relations that vary in complexity from simple "relates to", to implication/explanation and support/opposition.

                - From a practical standpoint, our [current]([[November 18th, 2020]]) belief is that the typed distinction between entities (artifacts) is the most important to get right: typed distinctions between relations could significantly enhance the system's ability to augment human [[synthesis]], but significant boosts in [[synthesis]] will likely accrue with implementation of only the three distinct artifacts (without explicit typed distinctions between relations). Thus, a minimal model will include implementation of the three distinct artifacts, and explicit (untyped) links between them.

            - {{[[TODO]]}} Let's consider a few concrete examples of these artifacts and how they fit together.

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMLQyD7AK2p.png?alt=media&token=7ad0cd24-1a49-4437-b92b-043a6d582c36)

        - ### Process

            - Always approach papers with some **SYNTHESIS** notes in mind: in the early stages of inquiry, these will be relatively broad questions, or a claim that you want to investigate. The point is that ((QZlhwWCmB)) should be answers to (or information for) questions that you have.

                - This is distinct contrast to the idea of reading papers and writing "the summary" of them in a vacuum.

                - This also means that papers are never "read": they are only read with respect to particular questions, if they have yielded some **OBSERVATION** notes for those questions. It should be natural to return to papers with different questions in mind, which would then likely yield different ((QZlhwWCmB)).

    - ## What does this model buy us?

        - ### Facilitating [[synthesis]] aka "disciplined imagination

            - This model allows for rich layers of [[context]] to [aid synthesis]([[[[CLM]] - Contextualizability is necessary for synthesis]]): it avoids [rushing too quickly to generalizations]([[[[CLM]] - Compression and contextualizability are in tension]]), and allows for careful, nuanced questioning of past claims (e.g., does X really not work?), and consideration of possible syntheses between opposing claims.

            - In addition to [[context]] from "below" (in the sense of micropubs and context snippets "grounding" the claims and syntheses), we also get [[context]] from "above" (the other direction of the "dance": where theories inform the significance of individual observations)

            - Beautiful example of the "dance" in [[@gruberDarwinManPsychological1974]]

            - {{[[TODO]]}} EXAMPLES:

        - ### Long(er)-term [reusability]([[reuse]]) of ideas

            - Reduce overhead for self in future, and possibly for others

            - For shorter-term or one-off cases, a lightweight version like a [[synthesis matrix]] is probably ok

                - Should you use Excel or Google Sheets for your literature review? | Citavi - Reference Management and Knowledge Organization: https://www.citavi.com/en/planned-accidents/articles/excel-literature-review

                - Microsoft Word - synthesis matrix.doc: https://guides.library.vcu.edu/ld.php?content_id=1720465

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMxQl1VhPCN.png?alt=media&token=6858616f-a693-4385-a49d-1bd1a7e96d67)

            - Together with the previous point, the intuition here is that "[the devil/diamond is in the details]([[[[PTN]] - The devil/diamond is in the details]])", and "details fade over time". Therefore, notes that omit details (or at least make it hard to access details) have a much shorter half-life.

            - EXAMPLES:

        - ### Ability to distribute synthesis

            - In part due to directly enabling [[reuse]], it is then possible for teams to distribute the work of "notetaking", knowing that we will never have ["lossy compression"]([[[[CLM]] - Compression and contextualizability are in tension]])

                - The middle and upper layers can be shared, index, etc., either in isolation (but retaining connections to their [[context]]) or as collections/bundles.

                    - {{[[TODO]]}} EXAMPLES

                - This might be a way to counter the problem that [[[[CLM]] - Most private annotations aren't useful to other people]]: here we specify *what* will be shared, and ensure that when it is shared, it can be reused

            - And the lower layers in particular can be disaggregated, and handed off to, say, algorithms, human-AI teams, or apprentices doing [[legitimate peripheral participation]]

    - ## Implementation in Roam

    - ## Conceptual and technical roots

        - Rooted in theories of [[🧱 sensemaking]], scholarly discourse, and [[reuse]]

        - Strongly shaped by past work on conceptual / formal modeling of scientific discourse and argumentation. Chief inspirations (that directly address the distinction between "claims" and "evidence") are the [[std/Micropublication]] model from [[@clarkMicropublicationsSemanticModel2014]], and the [[std/SEPIO]] model from [[@brushSEPIOSemanticModel2016]]

    - ## Future directions
- UsedIn:: [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]

###### Discourse Context

- **UsedIn::** [[ART - DSynthesis Infrastructure Roam discourse graph extension]]
- **Informed By::** [[@clarkMicropublicationsSemanticModel2014]]
- **Informed By::** [[@gruberDarwinManPsychological1974]]
- **Informed By::** [[@brushSEPIOSemanticModel2016]]
