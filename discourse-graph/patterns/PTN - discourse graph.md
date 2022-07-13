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

                    1. A minimal context snippet note is simply an unnamed excerpt, like a screenshot or quote from a source document. Like a [[sys/Hypothes.is]] [[annotation]], we can optionally add a note/description to this snippet to enrich it further.

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
- 

###### Discourse Context

- **Informed By::** [[@clarkMicropublicationsSemanticModel2014]]
- **Informed By::** [[@gruberDarwinManPsychological1974]]
- **Informed By::** [[@brushSEPIOSemanticModel2016]]

###### References

[[September 18th, 2020]]

- easiest to boostrap our [[[[PTN]] - discourse graph]], since they already have annotations built in with position markers, and [an annotation API](https://dev.mendeley.com/methods/#annotation-attributes), as well as mature groups infrastructure

    - bc it's a commercial compoany, the infrastructure is easier to get into - documentation, support, etc.

    - and a large existing userbase

    - [annotations](https://dev.mendeley.com/methods/#annotations) with position markers in data structure:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FEdcl5svSpj.png?alt=media&token=d011e77b-bfb5-42ef-a0b6-c3b79147dcb7)
[[February 7th, 2021]]

- Something for understanding whether [[[[PTN]] - discourse graph]] can be integrated into the messy reality of creative work

    - The shitpost-to-scholarship pipeline – drossbucket: https://drossbucket.com/2020/01/17/the-shitpost-to-scholarship-pipeline/
[[May 11th, 2021]]

- Piloting porting over all [[[[PTN]] - discourse graph]] observation notes for [[bet/prototype discourse graph for COVID and children + experiment can help us quantify the potential gains of discourse graphs for synthesis for effectiveness and efficacy]] into page format

    - Main motivation is to support both [[interoperability]] and start to move towards exploring [[findability]] and [[reusability]]

        - Use attributes (can be ported over into plain text markdown

            - try to use open schema standards for attributes

                - but only as needed

                - e.g., use https://schema.org/author for author

                - convention of camelCase for attributes

                - need to figure out shared ontology for evidence and propositions - [[open problem]]

                    - could use micropublications, relatively simple ontology: https://raw.githubusercontent.com/timclark001/mp/master/mp.owl

                    - or SEPIO (has mechanism for representing strength of evidence)

            - provenance metadata should ideally be "hidden" at the page level and automatically updated [[open problem]]

        - Refactor into (mostly) self-contained page

            - Put all context blocks associated with a given obs note in the same page - so page is self-contained if flattened export

            - Page name principles: compressed summary of key result/claim with citation at the end

                - Might be tough to name the page in a fully context-free manner - [[open problem]]

            - Draft template:

                - Synthesis: evidenceNote #[[roam/templates]]

            - Summary block is the same as we had before, but it's syntactic sugar for now - can write an exporter that strips them out in a plain text export if needed

            - Not 100% sure about section headers (e.g., summary, grounding context, discourse context, etc.)

    - 14:21 Did the first 5 of the top 10 papers so far, took about 1 hr, probably can do it much faster since we're figuring out as a we go

    - 17:18 Finished the remaining 5 in ~25 mins
[[February 3rd, 2021]]

- Second, to the extent that reuse of [[[[PTN]] - discourse graph]] is possible, the overhead of synthesis that comes from the need to create [[[[PTN]] - discourse graph]] from unstructured literature would be eliminated or greatly reduced.

    - Even if the \artifact{} elements themselves cannot be directly reused, they could be useful as a collection for understanding the overall structure of a conceptual space. This benefit of handoffs has been observed in studies of sensemaking handoffs, often in intelligence analysis. #[[Z]]

    - This is mainly because creating [[[[PTN]] - discourse graph]] is likely to be quite effortful, with a lower bound on cost.

        - Finally, studies of reuse in other settings suggests that [[[[CLM]] - Specifying context for future reuse is costly]],  in part because [[[[CLM]] - Specifying context for future reuse requires predicting trajectories of future reuse]], and [[[[CL]] - Predicting trajectories of future reuse of information objects is hard]] [[@ackermanOrganizationalMemoryObjects2004]], [[@andersonDataBaseMent2008]].

        - Research on sensemaking, for example, suggests that [imposing a schema on an unstructured collection of documents/materials is a major cost of sensemaking](They find that, for the cases they study, extracting data is the most costly step for [[🧱 sensemaking]] (p.273). ) [[@russellCostStructureSensemaking1993]]. #[[Z]]

        - Studies of systematic review practice, where the formality of data structures extracted from literature approximates [[[[PTN]] - discourse graph]], also have a similar phenomenology, with some studies documenting that this step of extracting data from papers feels like being "enslaved to the trapped data" [[@knightEnslavedTrappedData2019]].

            - cc [[[[CLM]] - Effective synthesis is hard]]
[[October 29th, 2020]]

- [Started work](https://lucid.app/lucidchart/72613594-d7ae-4cf5-a4e9-7b89bbbfca99/edit?page=0_0#?folder_id=home&browser=icon) on a slightly less horrendous version of horrendous first sketch for [[[[PTN]] - discourse graph]] - should keep working on this

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FqrlN3AaJ3G.png?alt=media&token=f4edc637-1d0e-4db4-b7b9-945545d8ad80)

    - Some key questions to think through on this

        - What is our best guess rn of the prevalence and "throughput" of existing social practices like journal clubs, seminars, lab meetings, and lit review milestones for papers in a lab?

            - These are places where structured, contextualized artifacts are *already* being created, and thrown away!

        - What is our best guess rn of the cost structure of creating something like our tripartite model?

            - Can test this with the [Roamify synthesis pilot](#idea Riffing on ((C28zKGT0h)), have interest from a few people in the Roam community to do a trial run of "Roam-ifying" the evidence and [[synthesis]] on mask usage!)

        - What is our best guess rn of the degree of gain for [[synthesis]] efficiency and effectiveness, with full access to our "grounded claims"?

            - I think this is paper 1! I don't know that we've ever done a study of how this kind of model (forget about system/authoring, just having access to this kind of "unit") impacts the synthesis process?

                - This is what we wanted to do with [[[[ART]] - Knowledge Compressor]], but we weren't ready yet, not just because we had a canvas as the space for "using" the grounded claims, but also because (I can see now), our data model wasn't *quite* right yet:

                    - At least for me, I was rushing from context snippets all the way to high level claims, actually doing lossy compression!!

    - Data model (and how it aligns with [[std/Micropublication]]s and [[std/SEPIO]] as initial test cases)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDTeOzqIN2I.png?alt=media&token=535e659d-df39-4ef4-b15b-b598c34af0de)

            - I like how this helps bring out the rich layers of context, and the stark contrast to what is typically available: the claims alone, and at best claims + pointers to the papers (from which you must then dig up the relevant context snippets and micropub(s)!)

    - How the parts fit together and overlay onto existing tools

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F4KO1rFp76z.png?alt=media&token=5818aee2-763f-44f5-bd96-1eba66b270d9)
[[December 18th, 2020]]

- saved entry points as good #example-of [[[[PTN]] - discourse graph]]

    - [skip-gram model](((4xz52frAQ))) with vanilla BOW contexts performed ~50% worse on verbs compared to nouns and adjectives in terms of predicting [human similarity judgments on SimLex999](((n3Xi0Tp0B)))

    - [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

    - [[[[QUE]] - How might domain distance modulate the effects of analogies on creative output?]]
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
[[February 14th, 2021]]

- spec out idea for question-driven p2p infrastructure (cc [[Ryan Muller]] and [[Matt Brockwell]], drawing on [[[[PTN]] - discourse graph]])

    - organize around questions

        - i'm curious about, expressed in `question notes`

        - this is what i'm learning, expressed in `fleeting notes` and eventually `synthesis notes`

            - these are personal, can be co-authored, forked

            - always in flux

            - based on `observation notes`

                - more stable

                - grows over time

                - copy-pasted, block-reffed

    - can map to policy

        - how might we x: problem statements expressed in `question notes`

            - subgroups form around common questions

        - i think we should do x, because this is what i'm learning, expressed in `fleeting notes` and eventually `synthesis notes`

            - based on `observation notes`
[[July 31st, 2021]]

- big uncertainty right now as we build the [synthesis extension]([[bet/[[D/Synthesis Infrastructure]]: it is possible to write close to prose but seamlessly translate to queryable, shareable discourse graph formalisms in the backend]]): [what direct value might accrue for people]([[[[QUE]] - How might a discourse graph provide direct value to researchers who author them?]]) (given realistic assumptions about variations in quality) from the elements of a [[[[PTN]] - discourse graph]]?

    - seems clearer that having some special marking and content of the **elements** is useful

    - what's less clear is what value we might get from the **relations**, especially given varying levels of quality.

        - i like the idea of [[[[PTN]] - representational talkback]] a lot as a design prompt

        - but i'm wondering if the value of the relation map is less for myself and more for others. which makes me nervous. but maybe it's not just others, but me and others: finding ways to collaborate and converge?

    - this is a classic [[riskiest risks]]. i think the thing to do is to use the extension right now as a probe, and schedule a bunch of interviews. best use of time i think.

        - {{[[DONE]]}} write up pitch and ask for interviews with academic roamers #next
[[April 26th, 2021]]

- Prototype of how to write an `observation note` for a formal result-by-proof for a [[[[PTN]] - discourse graph]]

    - [[@vanrooijIntractabilityUseHeuristics2012]]

        - "[[[[CL]] - intractable problems cannot be solved by a fixed number of parallel procedures - [[@vanrooijIntractabilityUseHeuristics2012]]]]"

            - [[@richHowHardCognitive2021]] cites [this result](if we assume that P != NP, and a function f is intractable, claiming that we have any polynomial-time procedure for solving f (by tractably choosing from a finite set of tractable heuristics) implies that P=NP ([[reductio ad absurdum]])) as support for this claim

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FdWJDK4jrnc.png?alt=media&token=e158d319-4e9b-42ef-9952-483ff916a359)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft0FUh8grSP.png?alt=media&token=86388358-8211-47b1-8d09-992a4e306837)

            - what's interesting is to think through the extent to which this kind of result-by-proof (which is a special case of logical argumentation) is similar or different to empirical argumentation, subject to uncertainty. what uncertainty or [[context]]uality exists here?

                - well, for one: the assumptions being made here, the biggest of which is P=NP, which... is an [open problem](https://en.wikipedia.org/wiki/P_versus_NP_problem) still?

            - [[SupportedBy]]

                - [[[[EVD]] - assuming that there is a polynomial-time procedure for choosing solutions for an intractable function implies that P=NP - [[@vanrooijIntractabilityUseHeuristics2012]]]]

        - there's a connection here (that [[Konrad Paul Kording]] himself made!) to the [microprocessor paper]([[@jonasCouldNeuroscientistUnderstand2017]])
[[March 18th, 2021]]

- #idea to help with [[[[PTN]] - discourse graph]] actual implementation: curate broader reading checklists similar to [[critical appraisal]] checklists like [[org/Oxford Center for Evidence-Based Medicine]].

    - could start in HCIL?

    - ha! already [hinted at this idea in the past](It will be high-leverage to return to the [[critical appraisal]] [stuff](((PwUqiYyQ4))) to develop templates, and then map the [[[[PTN]] - discourse graph]] schema onto that).
[[April 25th, 2022]]

- re-reading [[@starInstitutionalEcologyTranslations1989]] and recalling the [core motivation](per [[[[PTN]] - boundary object]]s, meant to strike a balance between the extremes of [too much](((L5b1tSbi2))) and [too little](((i0p-3Ud6n))) structure) of [[[[PTN]] - boundary object]]s for the [[[[PTN]] - discourse graph]]'s design; in particular, of the four types of boundary objects they identified in the Museum, the "ideal type" seems to fit the most:

    - > This is an object such as a diagram, atlas or other description which in fact does not accurately describe the details of any one locality or thing. It is abstracted from all domains, and maybe fairly vague. However, it is adaptable to a local site precisely because it is fairly vague; ^^it serves as a means of communicating and cooperating symbolically- a 'good enough' road map for all parties^^. An example of an ideal type is the species. This is a concept which in fact described no specimen, which incorporated both concrete and theoretical data and which served as a means of communicating across both worlds. Ideal types arise with differences in degree of abstraction. They result in the deletion of local contingencies from the common object and have the advantage of adaptability. ([[@starInstitutionalEcologyTranslations1989]], p. 410)

    - our field studies have made clear that people desire a lot more local control and fine-grained nuance in their local models. yet these distinctions may not always be relevant or understandable to others.

    - our core motivation is not just local, individual synthesis, but a protocol that can respect [[epistemological diversity]], and facilitate cross-talk and synthesis across disciplines

    - the "paper" is a good boundary object on some notes, but when translated locally begins to run afoul of a lot of the contextual requirements
[[November 19th, 2020]]

- Keep working on [[[[PTN]] - discourse graph]]

    - Prototyping something: I like the "[what does this buy us](What does this model buy us?)" bit: really helps to clarify what we're after.

        - We could flip it and frame the problem from the start.

        - For this to be true, we need a system that helps us

            - Achieve the right balance between compression/divergence/abstraction/theory and context/convergence/particulars/data

                - Because of the unit of analysis

            - Accrete insight over boundaries of time and projects/disciplines

                - We don't always have the luxury of being able to devote (funded) time and attention at an intense level for a given project. Often have multiple irons in the fire (good for creativity)

                - And we often want to [reuse stuff from the past](the scientists in both study groups needed to [[reuse]] articles from previous projects, but it was hard to do so) [[@blakeCollaborativeInformationSynthesis2006a]]

            - Distribute work across multiple people

                - There are just too many papers for any one person to absorb by themselves!

        - A future we want: a research group can confidently aim their sights at a complex, interdisciplinary problem area, and construct an effective synthesis together with minimal "busywork overhead", in part drawing on intermediate products of synthesis from their own past work and the work of others. The results of their synthesis work also provide a stronger foundation for themselves and others in the future to build on.

        - Here, we take aim at the "unit of work" (see [here]([[@qianITunesPapersRedefining2019a]]) and [here]([[[[CLM]] - Most scholarly communication infrastructure operates on the document as the base unit]])), and specify an alternative data model we believe can "buy" us these

        - The goals of this piece are to

            - Compare the efficacy of the current model to its closest [[SOTA]] variants, such as [[sys/NVIVO]] and [[[[ART]] - LiquidText]]

            - Demonstrate how it can be instantiated within [[sys/RoamResearch]]

            - Articulate the model here, at a level that is implementation-agnostic

            - Articulate dimensions of future improvement that are likely necessary for this model to be seamlessly adopted by more scientists

        - Painful situations for synthesis that are familar:

            - Too many papers!

            - Lose context over time, past notes almost useless

            - Ideas ossifying and hardening over time, leading to fixation

            - Difficulty going "deeper" than a superficial summary / rough clustering
[[February 16th, 2021]]

- [[sys/RoamResearch]] + [[[[PTN]] - discourse graph]] / [[sys/Zettelkasten]]

    - particularly excited about this one due to higher potential for powering a shared [[infrastructure]]
[[January 5th, 2021]]

- Taking a moment to write a brief memo on the various pilots going on for [[[[PTN]] - discourse graph]] for [[D/Synthesis Infrastructure]]

    - [[Matthew Akamatsu]]

    - Contacts via [[Alexander Briand]]

    - [[P/COVID and children synthesis pilot]]

        - Some interesting points of feedback from the first kickoff today:

            - Questions about where to think about paradigms and schools of thought (from economics research)

                - Could specify and make available at the paper level via the `#lit-context` block

            - Questions about where we typically find observation notes vs. synthesis notes (results vs. abstract/discussion)

            - Questions about high vs. low-level questions

        - A few people involved who aren't interested in the medical domain but want to learn the system

            - Lawyer

            - Two economics researchers

            - A few others, including [[Henry Finkelstein]]

    - Possible contacts with [[Joel Anderson]]?

    - Some other contacts also via Twitter thread on the model

        - Talking to [[William Gunn]] next week

        - [[Maarten van Doorn]] is interested in trying out

    - [[Henry Finkelstein]]'s giant synthesis project for thriving: https://docs.google.com/document/d/1N8sqL3J_EBUkT6XkVwOMhd6BRtYd4QNkabsWWQQij64/edit

    - #fieldnotes for [[P/PO study/dev for synthesis infrastructures]]
[[June 9th, 2021]]

- some emerging conventions related to [[[[PTN]] - discourse graph]] and [[bet/[[D/Synthesis Infrastructure]]: it is possible to write close to prose but seamlessly translate to queryable, shareable discourse graph formalisms in the backend]]]

    - now uses structure notes as multiple indices instead of a central master index - very reminiscent of [Maps of Content]]

    - has modified [[Beau Haan]]'s tripod to add more structure: argues for, argues against, examples, chronology, etc. (also for the connections to other "permanent notes" inside the "relevant notes" bucket), and does that tripod inside the page of a claim instead of in the daily notes
[[roamSOP]]

- ^^Micropub^^ blocks (see [[[[PTN]] - discourse graph]])

    - Contextualized

        - In past tense, with names of authors maybe?

        - Grounded in block references to context snippets
[[November 28th, 2020]]

- Insight that could integrate "systems" stuff into the [[[[PTN]] - discourse graph]]!!

    - per [[@galeyHowPrototypeArgues2010]], the artifact itself (a description of what it is, and what it was able to do, under those conditions), is a micropub

    - it *could* imply different higher level [[strong concepts]], but we need to study the usage of the artifact under different conditions to really get at that

    - the lower-level thing is still useful insofar as you are trying to do basically the same exact thing (under the exact same conditions) as what the artifact was able to do

    - but the higher-level claims are needed in order to generalize

    - e.g.,

        - lower level

            - AA built a model (that works like this) that was able to achieve 95% accuracy on GLUE, better than previous SOTA of 93%

        - higher level

            - transformer architectures can achieve higher accuracy with less data than Y under conditions Z

            - language modeling can approximate human-like structural comprehension, such as XYZ

            - each of these might be stronger or weaker with successive, diverse demonstrations of instantations of transformers

    - let's actually try it out! start with [[[[QUE]] - Can deep learning discover analogical representations?]]

        - see: [skip-gram model](((4xz52frAQ))) with vanilla BOW contexts performed ~50% worse on verbs compared to nouns and adjectives in terms of predicting [human similarity judgments on SimLex999](((n3Xi0Tp0B)))

            - this is an empirical NLP paper, but we should be able do basically the same thing with eval sections from good NLP systems papers

            - ultimately we don't care if an artifact just exists, or is "intended to do X": we only take notice if we have some reason to believe that it can in fact do X. then it tells us something about the way the world could be

            - note: this could also potentially be done through argumentation: we'd just want to make clear in the micropub (e.g., XYZ proposed design X, and argued that it can do X because of THEORY)
[[February 16th, 2021]]

- Design primitives (where might we instantiate and develop [[[[PTN]] - discourse graph]]?)

    - New

        - Note-writing ([[hypertext notebooks]])

            - hypertext linking (referencing, transclusion, embedding)

            - zoomable (e.g., expand/collapse, focus)

            - block-centric

            - connection-centric

            - multimodal

        - Reading (enhanced source readers)

            - annotations as portals

    - Old

        - Note-writing (e.g., Google Docs, OneNote, spreadsheets)

            - copy/paste

            - static

            - document-centric

            - category-centric

            - text OR visual-centric

        - Reading (standard PDF readers)

            - annotations as extractions

    - Comparison

        - annotations as portals vs. ((7_Ojs_TgT))

            - [[[[PTN]] - flexible compression]]

        - hypertext linking (referencing, transclusion, embedding) over ((09Yhi-c26))

            - [[[[PTN]] - flexible compression]]

        - zoomable (e.g., expand/collapse, focus) over ((8DKDk7khu)) interfaces

            - [[[[PTN]] - flexible compression]]

        - connection-centric vs. ((246YA2nTl)) structure

            - [[composability]]

        - block-centric vs. ((_1GsRim0s))

            - [[[[PTN]] - flexible compression]]

            - [[composability]]
[[October 16th, 2020]]

- Meta-reflections on [this exercise](Working on speccing out more of the [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]] stuff) for [[[[PTN]] - discourse graph]]:

    - Abstract is a reasonable starting point for a micropub

        - Can then alias block refs to contextualizing bits, for a more graceful way to implement [[[[PTN]] - flexible compression]]:

            - Highest level is something like a zettel: analogous still to the [[epistemic synthesis layer]]

            - These should be grounded by / composed of / mapped to stuff from the [[epistemic foundation layer]]

                - These will be sort of super-mini abstracts, but themselves grounded in [[context snapshots]] (which might be implemented in [[sys/Hypothes.is]] annotations: for now, we implement them as context blocks in Roam)

                - We can include them more naturally / informally / narratively at first via markdown aliases as well

        - Example:

            - #[[observation-notes]] [[far analogies]] increased the teams concept generation rate compared to baseline conditions.

    - Possible structure of a [higher level zettel]([[epistemic synthesis layer]]) that is focused on a more atomic statement / assertation / claim (feels pretty good atm)

        - 1: Explain the core idea

            - This is where we can have [[context queries]] related to examples, connections to other ideas, etc.

        - 2: Summarize the evidence for the idea

            - This is where we can connect most directly, with citations, to the [[epistemic foundation layer]]

        - 3: Summarize the "epistemic" status of the idea

            - This builds on stuff (more specifically [[context snapshots]], and other [[metaknowledge]] stuff) to justify a judgment of "epistemic" status

            - COuld be "I don't believe this at all, but I'm arguing against it, or "my best guess", etc.

            - Connects nicely here to the #idea 2: [[outline/2020-10 - supporting explicit reasoning over evidence context for claims (ASIST workshop)]] [*](#idea 2: [[outline/2020-10 - supporting explicit reasoning over evidence context for claims (ASIST workshop)]])

                - One connection here that I've been thinking about more: less about the algorithm and more about an *executable*?

                    - There's a [[LessWrong]] post about substituting "epistemic effort" for "epistemic status", to emphasize more of a "show your work", instead of a contextless judgment: https://www.lesswrong.com/posts/oDy27zfRf8uAbJR6M/epistemic-effort

                    - Some other examples of "epistemic status" here: https://www.lesswrong.com/posts/Hrm59GdN2yDPWbtrd/feature-idea-epistemic-status

                        - And also [[IVEO Matrix]] Empirical support score is essentially a qualitative binning thing with the algo mixed in

                    - [[I wonder]] how we can describe regularities/patterns in how this is expressed (if at all) in lit reviews in the wild? [[@holbrookLevelsSuccessUse2008]] would suggest that we actually might not see much of this at all :(

    - The whole exercise feels quite tedious, but I feel that the micropub is now wayyyyyyy more useful.

    - I also want to
[[May 9th, 2021]]

- could be useful for powering [[PDF parsing]] for [[context queries]] for [[[[PTN]] - discourse graph]]

    - [[[[QUE]] - What are effective ways to parse PDFs into usable structured data?]]
[[April 21st, 2021]]

- Devil-in-the-details for [[[[PTN]] - discourse graph]] rearing its head... pain points:

    - How to "keep track" of obs notes?

    - How to ensure that essential context for obs notes is never too far away?

        - Seems easiest to keep it "inside" the reference page

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FLA9LR_LZDO.png?alt=media&token=475c5b43-faa1-4fa7-a933-9caf0fb7e2df)

        - But... there's an [[ethnographic sneeze]] here... something isn't quite right
[[October 30th, 2020]]

- Let's do more prototyping of [the model]([[[[PTN]] - discourse graph]]), building on [yesterday's iteration]([Started work](https://lucid.app/lucidchart/72613594-d7ae-4cf5-a4e9-7b89bbbfca99/edit?page=0_0#?folder_id=home&browser=icon) on a slightly less horrendous version of ((qrpR4F9b1)) for [[[[PTN]] - discourse graph]] - should keep working on this)

    - Do the near vs. [[far analogies]] thing from the diss - relevant and useful for [[D/Computational Analogy]] and the [attribute stuff]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]).

        - --> [[[[QUE]] - How might domain distance modulate the effects of analogies on creative output?]]

            - Digging back into this was also substantively useful, for resurfacing the idea of "expertise mediation" as another spin on the [attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]): if I show you something from a far domain, and your understanding of that domain is shallow, it's not going to be very useful to you, probably even if it's quite thoroughly explained - what needs to happen is a fruitful iteration or co-evolution (a la [[@dorstCreativityDesignProcess2001]] and [[@helmsCompoundAnalogicalDesign2008]]) between your problem space and the other problem space

                - See these excerpts from the dissertation discussion on this point

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FopBJK2rVAv.png?alt=media&token=80011078-0c6b-475d-8160-4c3254e94409)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FT-C1RHKiE5.png?alt=media&token=fbbec25e-f1d6-4aca-823b-408595611b2b)

                        - [[@hargadonTechnologyBrokeringInnovation1997]]

                - A subtle variation of a "find collaborators" model might be a variation on Julie Hui's [[sys/IntroAssist]] [[@huiIntroAssistToolSupport2018]]

                    - Where might we test something like this? In ConservationX????

                    - What would we need to get started?

                        - Would be easiest with academic work, can leverage citation network.

                        - Just specify papers you've written, or ones you know really well, and those define your "network position"

                        - Then whenever we find analogical matches that overlap with your network position, we suggest an intro between you and the seeker
[[August 30th, 2020]]

- and [[[[PTN]] - discourse graph]]

    - this idea about recursive/iterative conversations with the primary evidence and its [[context]] (which is often "locked away" into PDFs) is identified (like us) as a central unmet need in existing tools and systems

        - https://twitter.com/LauraDeming/status/1299744199483432960

    - summarized in here: https://ldeming.posthaven.com/can-someone-build-roam-x-mathematica
[[December 4th, 2020]]

- game to try out [[[[PTN]] - discourse graph]] and maybe [[Z: Paths and workflows towards synthesis]]

    - solid knowldge base across disciplines to make good design decisions
[[January 25th, 2021]]

- Random thought on [[[[PTN]] - discourse graph]] for [[D/Synthesis Infrastructure]] and why we might want to favor discourse-centric representations (and only allow for concept-centric ones where it makes sense):

    - Classification into a binary/categorical "bin" (is this a gene? how about that?) is straightforward in rare cases: in most cases, the classification hides a really really complex underlying continuum and process/dynamic that is dangerous to "flatten"

        - MIght be ok if we only want to make things [legible]([[Legibility]]) for the state (cc [[Seeing Like a State]])

            - Whoa! [[Joel Gustafson]] actually made [this exact connection](![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FEvMFoPWnYw.png?alt=media&token=a9217719-3a6b-4b94-8b4e-0873845e1447)) in [[@gustafsonWhatDistributedKnowledge2020]]!

        - See also [[@bowkerSortingThingsOut2000]]

        - This is a deeper point than [[[[CLM]] - Knowledge is fundamentally contextual]], [[[[CLM]] - Universal Semantic Webs are neither feasible nor useful]], more about the distinction between a [[knowledge graph]] and a discourse graph

    - [[Legibility]] is a legit motivation. The problem comes when the compression is lossy.

        - It's ok I guess to classify, as long as the [[compression]] is [reversible]([[[[PTN]] - flexible compression]]). Otherwise, we forget that [[[[CLM]] - The map is not the territory]]

    - More, from the inimitable [[David Chapman]]:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FmnJY9eZ-ut.png?alt=media&token=1d1c53f7-40e1-461f-b7b2-539ae2b48226)

        - > "Ego depletion now seems to be mostly not a thing, but maybe somewhat a thing, but it's not clear what sort of a thing it is, probably a different sort of thing than people thought five years ago, or maybe it's several vaguely similar things, and anyway the hundreds of papers were all pretty much nonsense (probably?) because the thing that people thought it was mostly isn't one."

    - To connect back to [[[[PTN]] - boundary object]]s, [[knowledge graph]]s with atomic concepts as nodes feels closer to classical formal [[ontologies]], which make strong assumptions about what should be in/out of the model. This is a SPECIAL CASE of reality! THE MODAL case is ambiguity and variation: it is perhaps for this reason that (effective) [[[[PTN]] - boundary object]]s are weakly structured in common use, and only strongly structured in local use

        - See also:

            - Constant themes in [[ASIST 2020 Conceptual Modeling Workshop]] of how it's tricky to draw boundaries and say "these are the same" (e.g., [here](((r8R6A2mgd))) and [here](((1WmT_5umb))) and [here](((YY3Kk7zMj))) and [here](((l9FWWyIKt))) and [here](((NRC6L8-Zf)))), which is what we try to do with [[ontologies]] and formal models

            - "Meta-rationality treats all categories as inherently purpose-laden—including scientific categories. It rejects the rationalist ideal of perfectly disinterested Truth. Any useful categorization of solar system objects would group them according to a sub-discipline’s interests. Dynamicists and astrobiologists would naturally come up with different ones. Meta-rationality accepts, applies, and coordinates multiple ontologies for a single domain. There isn’t a great example in our solar system, but astrobiologists exploring other star systems might need to take dynamical considerations into account. Hopefully they would have no difficulty holding both classification schemes in their heads at once. Investigating the ruins of an ancient civilization on an unusual natural object in the Alpha Centauri system, they should not get sucked into arguments about whether it is “really” a planet."

    - All of this I think circles back to the forceful points that [[@scheelWhyHypothesisTesters2020]] make about what is necessary in order to get to a place where we're comfortable designing experiments, which implicitly or explicitly employ some kind of formalism or "map"/ [ontology]([[ontologies]])

        - one of the key things they prescribe as [part of theory-building](![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzlLsk8z23g.png?alt=media&token=9e7cd594-9fe8-443e-875d-afbfef05a9ac)) BEFORE we start worrying about preregistration and really precise, strong experiments, is precisely **concept formation**

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FGd7T8m_xsm.png?alt=media&token=f4ce8a6a-83d0-4586-b8d6-9ccfe8303d4a)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fp_yGedssnC.png?alt=media&token=ec7f4d52-c9d3-44cd-a162-baa69deaa58b) (pp. 3-4)
[[June 2nd, 2021]]

- with [[Victor Davila]] about [[[[PTN]] - discourse graph]]

    - about

        - want to use synthesis for writing research articles, and also translational article and conference papers/talks

        - assistant professor at OSU in anasthesiology

        - using [[sys/RemNote]]

        - has developed some text expander snippets (a bit of a [[Hackers]]?)

        - lots of similarities in our system

            - independently discovered daily notes paradigm, time stream - draft in DNP, move to pages if they are useful

                - e.g., started reading [[@chanKnowledgeSynthesisConceptual2020]] in DNP, then moved to area

            - just learnt and trying to adopt [[sys/PARA]]

    - hard to learn zettelkasten (which he thinks is a collection of a bunch of techniques: i tend to agree)

        - need examples, especially from our use case

        - how to take smart notes sucks

        - too much diversity in systems for [[sys/Zettelkasten]]

    - remindings

        - guy from u chicago does PhD stuff

        - `question notes` remind him of envelope method

    - problems

        - problem: where are the hubs?

            - [[sys/MOC]]: https://forum.obsidian.md/t/in-what-ways-can-we-form-useful-relationships-between-notes-long-read/702

        - problem: how to keep track of, develop early ideas?

    - feedback

        - 2 x 2 (both synthesis notes and observation notes are kinds of literature notes):

            - > I think that Literature notes could be either Observation notes or Synthesis notes depending on what the authors in the paper are doing.  To use your example from Darwin, the individual observations in a study he did could be observation notes. However, you may want to reference his conclusions; his synthesis of the data.  In that sense a specific note has two axis: the originator (you vs someone else ) and the nature ( synthesis vs observation).

        - really like the research kitchen idea

            - bets make a lot of sense!

            - research directions and questions are like areas in [[sys/PARA]], bets and milestones are like projects

            - in general really think there is demand for this sort of guide, with examples, for researchers - [[sys/PARA]] and [[GTD]] don't quite work
[[December 18th, 2020]]

- re: [[[[PTN]] - discourse graph]]

    - might need to think more carefully about tech implementation of context snippets

    - in modeling, there is distinction between "thing" and "role" - is context snippet a special role for an observation note?

        - not sure... obvious cases where we don't care to describe a context snippet: like screenshots of key figures or quotes

        - but in other cases we do want to describe them, like the fact that the inter-rater reliability of this scale was X, which is important for grounding an observation note, or that this paper has N citations

    - one proposal is to have only observation notes, but have some of these able to contextualize each other...?

    - need to think about this more and see more in practice before we make a final call

    - not crucial at this point: any design decisions we make should be able to walk back
[[January 9th, 2021]]

- Felt inspired to sketch this out tonight about the [[dialectic]] that is at the heart of the [[[[PTN]] - discourse graph]] and the idea of [[[[PTN]] - flexible compression]]

    - And I do like the phrase "[[disciplined imagination]]" as another shorthand way to talk about this [[dialectic]] [[dance between the theoretical and the evidential]], and the [[[[PTN]] - flexible compression]] required

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FLyzgySUC_d.png?alt=media&token=6cf535f5-8c47-44f3-9078-144aced62e14)

    - Also thinking about `question notes` as the "space" within which this dialectic can productively grow - the question notes help define the boundaries of the space, and provide a "hook" for material to be collected and to collide and grow

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Flj-He0l83s.png?alt=media&token=0d48b6c2-ab43-4e8a-8e95-9c3fe26faad3)

        - within this space, `observation notes` can fuel [[induction]] (this is x, maybe X are Y...) and [[deduction]] for theory development (if A, then x is z, but I see that x is y, therefore...) that shows up in `synthesis note` networks

        - and `synthesis note` development can also be done to do [[abduction]], to explain observations (thinking again of what [[Charles Darwin]] did)
[[February 7th, 2021]]

- To add to the intuition for why we want to have [[[[PTN]] - discourse graph]] with both claims and context, we can quote [[@gruberDarwinManPsychological1974]] describing the [[dance between the theoretical and the evidential]]

    - > The two kinds of task, theoretical and evidential, entail different activities, and in the long run they may yield distinguishable products for our consideration. But __in vivo__, in the life of the thinking person, they are thoroughly intertwined. The most speculative "castle in the air" is triggered by a simple observation or a friend's remark about his dog. Hard work amassing the facts on a special point is guided by a long theoretical argument with which it may have only a tenuous logical relationship: the theory does not absolutely depend on the facts, nor could the facts ever guarantee the theory. The relation of theory and evidence is not simply logical but psychological.
[[February 17th, 2022]]

- writing quickly for [[[[PTN]] - discourse graph]] authoring systems --> [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]]:

    - design principles

    - system components

        - grammar translation system addresses [integration](integrated into intrinsic work of synthesis, with minimal friction)
[[January 31st, 2022]]

- and on [[[[PTN]] - discourse graph]], we should support description of a rough **schema**

    - protocols can then describe how to pass discourse (sub-graphs) from different schemas to each other

    - the discourse graph extension is a building block for this vision, which has many risks, but the analogy here is similar: we make it easy for you to reuse your own shit, and thereby make it easier for others to do so as well, and you do that not after hte fact, but in the spec of your own

    - the key thing that is cool here too is the blockhub, where people are sharing individual blocks for reuse

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRVawHOypeQ.png?alt=media&token=b6ed4fbf-58fc-494b-89b9-de30fb21ac7d)

        - it's not the right level of abstraction for us, but something similar where the protocol spec links right to a portal of sharing hubs, is probably going to be important
[[February 5th, 2021]]

- For the third [RQ]([[Question]]): ^^**what enabling conditions are necessary for [[[[PTN]] - discourse graph]] to be successfully adopted/implemented?**^^

    - A final question concerns the enabling conditions that are necessary for [[[[PTN]] - discourse graph]] to be successful adopted or implemented. For example, might the compressed and claim-centric nature of [[[[PTN]] - discourse graph]] be more suitable for some fields than others? It is possible, for instance, that qualitative or historical work might be more difficult to compress into a set of context snippets and grounding observations. Another question might be one of motivation, or technological readiness.

    - This overarching question is critical for understanding whether/how these practices might generalize (or not) across scientists and domains, and to better understand what further work might need to be in place, should transformative benefits be observed, to better disseminate [[[[PTN]] - discourse graph]] across scientific practice.
[[June 7th, 2022]]

- maybe the base ontology for [[[[PTN]] - discourse graph]]s should be consistent with and inconsistent with!!! support, like explanation, is conditional on ruling out alternative explanations!! other types of edges are functions of these two base

    - this is probably due to [[Eirini Maliaraki]]'s approach to their graph
[[June 9th, 2021]]

- Problem for [[[[PTN]] - discourse graph]]: there is likely going to be some (not sure how much) refining of the *title* of a claim or evidence note

    - It's also likely to be a bit contextual, with some details and jargon left out/in (e.g., PD instead of participatory design)
[[January 26th, 2021]]

- Despite their promise, [[[[PTN]] - discourse graph]] remain largely untested in authentic usage \cite{kuhnBroadeningScopeNanopublications2013}. Consequently, we lack robust \textit{empirical} understanding of how [[[[PTN]] - discourse graph]] might deliver on their promise of accelerating knowledge synthesis, and whether these benefits could be obtained in a cost-effective manner (e.g., through reuse/sharing of [[[[PTN]] - discourse graph]]).

    - [[[[CLM]] - Effective individual synthesis systems (seem to mostly) exist (for a select few)]]
[[February 7th, 2021]]

- Somewhat of a #fieldnotes for [[P/PO study/dev for synthesis infrastructures]], or at least something that is likely to come up frequently in conversations: where might [[[[PTN]] - discourse graph]] fit into academic writing workflows? Or, generalizing, where might they fit into "compression" of ideas into a an argument suitable for consumption by others?

    - In the Roam graph, it is useful and helpful to have links, internal names, aliases, etc.

    - But many of these are not [interoperable]([[interoperability]]) with output spaces, like a manuscript in LaTeX, for example (which also has its own incompatibilities with Roam)

    - An [[example-of]] this is the term \artifacts{} in my grant manuscript, which remains open as a variable because the exact term I use will depend on what maximizes comprehension and resonance for that specific audience; it is useful for me to track that concept and idea throughout my writing on it in the graph, but I don't want it to be named that. It should be named something useful for me, which may or may not be comprehensible to others (although if they have access to the context of is use, this shouldn't really be that much of a problem)

        - related: how children are able to "understand" nonsense words through contextual usage (something like [[one-shot learning]]?), a super common paradigm in developmental research

    - So I think I need to settle for some friction now in the transition between the desk and the stage

        - cf. [[@ferrissJerrySeinfeldComedy]]: Another [[dialectic]]: between the [desk and the stage](((B4Q0IAWjm))), with an explicit analogy to scientific method: experiment!

    - It's possible that this could be automated at some point and in some way, but I'm not sure. The [friction]([[desirable difficulty]]) might not actually be something we want to remove: it might be generative in some interesting way.
[[December 18th, 2020]]

- talked a bit about [[[[PTN]] - discourse graph]]

    - [[Jason Larkin]] says makes sense
[[February 2nd, 2021]]

- We can think of this study as comparing [[[[PTN]] - discourse graph]] with various baselines that resemble the current state of practice: for example, how much quicker could a new PhD student get to a workable research idea if they started with a set of [[[[PTN]] - discourse graph]], rather than a reading list or annotated bibliography (if they're lucky enough for something like this to exist for their exact topic)? We will draw on the same materials as Experiment 2, but this time randomly assign participants to the best performing \arfifacts{} condition from Experiment 1, and one of N baseline conditions, such as a raw reading list or annotated bibliography. The task will be the same as Experiment 1, but the measures will now focus on two sets of metrics:

    - 1) What is the probability that the participants converge on a similar insight or question to the known insight for the given evidence collection, within the time limits of the experiment?

    - 2) What proportion of the time on task is given to "overhead" work (e.g., extracting and finding/retrieving context snippets) vs. "generative" work (constructing and refining explanations/arguments)?
[[May 2nd, 2021]]

- Thoughts about [[[[PTN]] - discourse graph]]:

    - Give space for [[context]] to live, rather than define specific "context entities".

        - For example, have the primary authoring interface be a blank page that is relatively unstructured, to give breathing room for context such as appraisal, uncertainty, discussions, etc.

        - And have a specific kind of discourse entity that incorporates a specific kind of **Context from "below"**

    - Yesterday's thought can be factored as a bet about how to implement [[[[PTN]] - incremental formalization]] to [bridge personal and shared discourse graphs]([[[[QUE]] - How can we best bridge private vs. public knowledge?]])
[[February 17th, 2022]]

- with [[Eirini Maliaraki]] and [[Dominic Falcao]] from [[org/Deep Science Ventures]], discussing [[[[PTN]] - discourse graph]], among others

    - want to identify regions of reasonable risk for ventures, but also "research-level" uncertainty, fund doctoral work

    - model is logic model about assumptions, constraints, etc., that they want to ground in evidence to inform their judgments of risk/uncertainty/opportunity - can absolutely sit on top of the d/graph

    - want to explore multiplayer more

    - will probably build export/write via API to Notion for the model layer from Roam (the d/graph layer) - i think this is probably going to be common model moving forward - an authoring layer, and a "use" layer
[[January 28th, 2022]]

- Have a random idea for how to finally merge synthesis and [[[[PTN]] - discourse graph]] with [[sys/lebeauzettel]]

    - The [[idea - synthesis-zettelkasten practice]]

    - Some reflections on [this idea](The [[idea - synthesis-zettelkasten practice]])

        - I think this resolves several open questions

            - Solves the [question of the index](The role of the index: one or many)

                - We decide to have one.

                    - [[Mise en place]]

                    - Maximize surface area of cross-disciplinary connection

                - Concept pages can serve the role of structure notes, analogous to [[sys/MOC]]s, as a complementary system of entry points, separate from the Zettel-index

            - Solves the [issue of timescale / pace / development over time](Timescale - can this really be done in a single session? e.g., ((aEi9V4vIQ)))

                - We can allow evidence notes to accumulate. When to stop and zettel from them is an art, but can be learnt and felt.

                - We can also create a queue, just like Beau does, of zettel tripods in incubation. This should be manual. And then just move it to DNP when it's "done"

            - Reinforces resolution of the [question of how to map the elements to each other](Mapping of the elements. e.g., ((mx1f2n5Dq)))

            - The [question of keywords](The keywords next to each entry in the index) is still unsolved, but I think that's ok.

        - We can definitely set up the discourse-graph grammar to capture durable typed relationships between EVD and CLM, and between CLMs and QUEs, playing nicely with block references

        - This is about infusing the zettelkasten with synthesis, not merging the two per se

            - Although one might think of this as filling the missing area in the synthesis loop [process diagram](![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F02Unj9yT4G.png?alt=media&token=5c8e514d-dc31-4498-95b0-a182ae282547))

        - There are still some uncertainties, but all seem straighforwardly resolvable

            - How this relates to theory-building.

                - This is an open question. My rough thought rn is that... it goes in stages, parallel to the zettel-ing process

                    - The theory can percolate in its latent, semi-stable [[ideasimals]] across fleeting notes, conversations and sketches, in parallel to the zettels

                    - It can also develop through particular exercises such as formal modeling, which will be all the stronger coming from my mind having zettel-ed, and we can refer to the zettel-index

                    - At some point, it may be reified enough that it makes sense to formally make the case against the zettel-index, and write it out

                    - This is then the thing that is shared with the community

            - Whether the evidence index is an index (where things live) or a queue (where things are stashed until they are processed)

                - Queue is simpler, because then there is only one index

                - But without a central index for evidence, they sort of... disappear a little. How often might I want to directly go from an evidence note or two to a new synthesis note? I can still access them easily through the discourse graph behind a CLM.

                - I think the index is the way to go for now (preserves optionality, and allows for the EVD-informs-QUE relation to hold).

            - What happens when new evidence comes in?

                - Well, it can corroborate or strengthen an existing synthesis note. If its essence remains unchanged, we could simply add it to the body of the note to reify that linkage

                - If it changes the synthesis note materially, or sparks a branching or refining, then I think it makes sense to do another zettel session

                    - What happens to the original synthesis note then? I suspect it will depend!

                        - If it is definitively refuted, I might in extreme cases *remove it* from my index, and maybe archive it under a "changed my mind" index :)

                        - Otherwise, I might just leave it in the index and live with the tension and nuance :)

            - How this plays out in tension with sharing

                - The evidence notes are still contentful, and shareable

                - But the CLM notes will sort of be contentless.

                - Well. Maybe not all of them! Some of them might be fleshed out in their body if we want to share them. And these will be good and meaty enough to be shared as essays or blog posts or something to be shared more widely. The contentless stuff can still be shared (along with their discourse context) with closer collaborators who can handle the mess.

            - I worry that progress will grind to a halt if everything needs to pass through this

                - It's a heavy duty practice

                - We want its benefits

                - But again, This is not everything.

                - There must be space for free-form speculation and free-floating fleeting notes. This is everything else in Roam. It is the chaos that only I can surf. And that is ok.

        - The design pattern of the central manual index and queue is beautiful its simplicity, and its manual, situated (one place) nature reminds me of... the humble [Starbucks coffee cup as a distributed cognition facilitator]([[[[EVD]] - Starbucks baristas used a paper cup to support complex coordination to reduce the cost structure of creating complex drinks in a tight, multi-tasking and interruption-intensive environment - [[@kirshMultitaskingCostStructure2005]]]])

            - The index and queue acts as a forcing function to not grow the inbox endlessly. Practice the discipline of letting go.

            - And it is very much inspired by [[Matt Clancy]]'s simple practice

        - This is not everything.

            - This won't be the only implementation of synthesis

            - I think the zettelkasten process is amazing for scaffolding the articulation of **what you really think** in conversation with the world and your own ideas, free from the externally imposed strictures of disciplines and topics, resulting in durable synthesis notes that are *yours*. This is tuned for transdisciplinary thinking over a lifetime. Not everyone needs to do this.

            - There is still a place for project-based, one-off synthesis work. And the discourse-graph plays nicely into that as well.

        - Therefore, I can migrate to this slowly over time

    - The sparks

        - The process of drafting sketches to specify process for a lit review for [[Connie Siebold]] and [[Ana Ndumu]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F4hX5V2xGE7.png?alt=media&token=ae6be487-3b87-4748-a530-a3154fcd112f)

        - And some threads from the past

            - I last tried to grapple with this here: Reflecting on similarities/differences between [[Beau Haan]]'s [implementation]([[sys/lebeauzettel]]) and mine

            - Some of the open questions were:

                - Mapping of the elements. e.g., where do `observation notes` fit in, in the tripod?

                    - I think this is basically solved.

                        - Permanent Note --> CLM

                        - Literature Note --> EVD (as a special case)

                        - Fleeting Notes --> not in synthesis, this is a [[sys/Zettelkasten]] thing

                        - The index --> Question page (but we should generalize this, I always feel like I want to expand it out from here)

                            - And [[Brother Spirit]] already showed that questions can easily be integrated into the central index

                - The keywords next to each entry in the index

                    - I'm not sure what role this plays, perhaps as a thumbnail. I'm not sure I want to force this for each one. We'll see. Makes sense for some, but not others.

                - The role of the index: one or many

                    - There is the MOC style as a separate thing. Which seems v useful. But I think.... these might be structure notes? I think there is still a place for these hubs. But I think they cannot replace a central index.

                    - But there is something very freeing about having a single index, and the surface area potential here is greatly multiplied

                - Timescale - can this really be done in a single session? e.g., can't develop permanent notes from a single source. too risky. but want them to stick around for development!

                    - Probably not.

            - And I wrestled with these ideas with him on [[April 8th, 2021]]: with [[Beau Haan]] re: democratizing [[[[PTN]] - discourse graph]] and [[sys/Zettelkasten]] in [[sys/RoamResearch]]

            - And I wrote some substantial thoughts out after listening to his podcast appearance on [[April 25th, 2021]]: Listening to [[Beau Haan]]'s [[RoamFM]] interview, some thoughts worth writing down in relation to [[[[PTN]] - discourse graph]]:

        - An [[ethnographic sneeze]] here this whole time during the [[[[EXP]] - [[D/Synthesis Infrastructure]] - Field study for discourse graph extension]]

            - But there **is** a point at which they get crystallized.

            - EVD notes seem straightforward, but CLM notes are.... not the same beast.

            - They seem very wild.

            - And... Idk. There is a sense in which we don't want to pin them down. Until they're forged properly. Leave them percolating.

            - I am reluctant to make them, and I sometimes feel like I made them too hastily, leading to [noise](i like this a lot. keeps me from "[polluting](((NgwvGD-AT)))" the central index unknowingly. everything in there should be [reasonably mature](((BS6GNRQFt))), and robustly challengable.).
[[January 27th, 2021]]

- Knowledge management (building your own repository): [[[[PTN]] - discourse graph]]

    - Roam demo
[[May 1st, 2021]]

- new idea for [[[[PTN]] - discourse graph]], for specifying [links](how to formally specify discourse graph links between objects?) and "[keeping track](((vYAhUPzml)))" --> [[bet/[[D/Synthesis Infrastructure]]: it is possible to write close to prose but seamlessly translate to queryable, shareable discourse graph formalisms in the backend]]

    - principle: remember, we're trying to lower the threshold for semantics, not impose it ont he user! have htem write prose and go back and forth and be as messy as they like, but take care of semantic relation specification (formal) as a recognize-fix task, rather than a manual user-specification task, so they can focus on the writing and thinking! they can sketch and write, and the system "talks back" to them re: the graph they are building

        - major inspiration: [[std/Argdown]]

    - super rough sketch

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FBbByHyKHbe.png?alt=media&token=06c237ae-1dbc-4d55-83e7-93a211d90e61)

    - basic idea:

        - parser output is written to discourse-centric [[RDF triple store]]. if desired, can also write relations in yaml or in the body of the note (under "relations"). goes both ways: user can also write these at the bottom to help the parser, but my hypothesis is that it's easiest and most natural to do it in the body of ht question note: closest to writing a regular argument/essay.

        - we write as usual in markdown. and we can reference "discourse entities" (questions, synthesis, and evidence).

        - we can then have a set of user-defined "keyphrases" the system can use to recognize possible discourse relations (e.g., support, inform, oppose) between these discourse entities (can be messy otherwise if we like!!!)

        - we can later refactor the evidence into a self-contained synthesis note if we like, but preserve the rdf relationships.

        - the key idea is that USING the synthesis and evidence in writing creates formal semantic links as a byproduct (that can be helpful for [[[[PTN]] - representational talkback]], but is not the primary task). in other words, authoring a discourse graph as a side effect of writing!

        - the triplestore can then be used to run [[std/SPARQL]] queries like:

            - find all related questions for this question

            - find all synthesis notes that inform this question (or similar)

            - find all evidence that can inform this question (or similar)

            - find all contradictory synthesis notes for this question

            - find all evidence for this synthesis note

            - find all counterarguments/evidence for this synthesis note

    - probably can hack a prototype for this in a weekend, leveraging the [[sys/Obsidian]] plugin API - talk to the Roam expats about this (esp. [[Rob Haisfield]] and [[Shawn Murphy]], maybe also [[RoamHacker]] and [[Paul Bauer]])

    - i think this can be done in roam as well, but it's a bit more complex bc of the possibiltiy of block-referencing, and the lack of ability to specify formal semantics (e.g., no yaml) or categories), so it's abit more brittle wrt convention

    - thinking in markdown (pages as primary units of references, yaml for metadata, folders for categorization) simplifies things i think because we don't have to overload the indentation for querying, and we don't have to worry about block references.
[[January 12th, 2021]]

- Not sure where to put this yet, but will start drafting here, the focusing research questions, methods, and plans for PO investigation of [[[[PTN]] - discourse graph]] and [[idea: multiplayer zettelkastens]] --> [[P/PO study/dev for synthesis infrastructures]]

    - What do I want to know? An initial sketch

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0Mzp85vxYO.png?alt=media&token=53c9b6b4-9f68-4f1f-b620-b624db0d8593)

    - Now we can draft something (moved to [here](What are the goals of this PO effort?))
[[February 11th, 2022]]

- with [[org/invisible college]], discussing grammar for results graph, overlap with [[[[PTN]] - discourse graph]]

    - key [prior art]([[discourse-graph-centric information models and platforms]]):

        - [[std/Micropublication]]

        - [[std/HypER]]

        - [[std/SEPIO]]

        - [[std/ScholOnto]]

        - [[std/Nanopublications]]

        - [[std/SWAN]]

    - overviews:

        - [[@clarkMicropublicationsSemanticModel2014]]

        - [[@deWaardProteinsFairytalesDirections2010]]

        - [[@dewaardHypothesesEvidenceRelationships2009]]

        - [[@brushSEPIOSemanticModel2016]]

        - [[@harsDesigningScientificKnowledge2001]]

    - prior threads

        - Ok so this is the first thing to do. Let's talk more specifically about which of the standards we want to highlight as basically what we want.

    - braidify
[[December 18th, 2020]]

- message to roam-medical folks for covid pilot of [[[[PTN]] - discourse graph]] / [[idea: multiplayer zettelkastens]]

    - Hi all!

    - About a month ago I posted something to gauge interest in doing a pilot of setting up a shared Roam for synthesizing medical knowledge. Alas, that was more than 10k messages ago, so context is all gone now!

    - To recap, I'm developing a conceptual and process model for how to do knowledge synthesis in Roam, in a way that is both more powerful for individuals, but also potentially amenable to collaboration and sharing.

    - It's written up (hot off the presses, first release) here: https://oasislab.pubpub.org/pub/54t0y9mk/release/2

    - The basic idea is to start with some key question notes and a bunch of sources, and systematically develop synthesis notes that are informed by / grounded in observation notes, that are themselves grounded in context snippets.

    - Here's an example of what that might look like for a question about COVID transmission in children:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FXaxZPtORnu.png?alt=media&token=6de0d4de-18f8-4b0c-bfe8-8f443fd0dd66)

    - And here's an example of how that particular synthesis note might be embedded in a larger network of synthesis notes to get a fuller picture on the question:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fqu_lUj1wBz.png?alt=media&token=c2c5d1d2-f08e-42e9-85fe-409ffe8ce87b)

    - I'm looking for people who might be interested in joining me to pilot how we might do some collaborative synthesis (using this conceptual/process model) for a medical research question. An initial test bed would be synthesizing literature on COVID and children (super relevant and also hard to get a good synthesis right now), sort of creating a Roam version of this: https://dontforgetthebubbles.com/evidence-summary-paediatric-covid-19-literature/

    - I know quite a few people expressed interest during my original post, but unfortunately I didn't have the foresight to save those messages. So my only memory right now is @mattbrockwell

    - If you're using Roam to do something like knowledge synthesis (whether you're an academic or not), you might be interested in joining to get a feel for whether this model might help your own process.

    - If this sounds interesting to you, please fill out this form so we can coordinate over email (including a possible kick-off call): https://forms.gle/ThE4vEquyvZ1oPHW9

    - #fieldnotes for [[P/PO study/dev for synthesis infrastructures]]
[[February 3rd, 2021]]

- First, the same affordances of [[[[PTN]] - discourse graph]] around compression and contextualizability that are hypothesized to augment individual synthesis should also **facilitate exploration and reuse** of an evidence collection that was created by someone else, or by oneself in the past.

    - Granular representation of scientific ideas at the claim level [matches the kinds of queries that you would want to ask of an evidence collection during synthesis]([[[[CLM]] - Scholarly argumentation operates on atomic statements and concepts as fundamental units]]), and exploration is enhanced through the networked structure.

        - This network structure is worth reemphasizing, since keyword-based search often fails when crossing knowledge boundaries: you often don't know what terms are relevant or the most fitting for search. Even when crossing relatively near knowledge boundaries, there can be idiosyncratic differences in the exact terms used. In these instances, network-based foraging through associative trails is superior to keyword search.

            - [[Z: Interdisciplinary synthesis is hard because you have to navigate multiple, sometimes competing epistemologies]]

            - [[[[CLM]] - In interdisciplinary domains, network-based foraging is more powerful than search-based foraging]]

    - The rich [[[[context]]ualizability]], too, of [[[[PTN]] - discourse graph]] should facilitate the deep engagement with context that is necessary to make sense of and appropriately and creatively integrate \artifact{} elements into your ongoing synthesis.

        - Thus, knowledge representations that are lossy with respect to context should be especially difficult to reuse across knowledge boundaries.

        - Here, as with compression and exploration, the benefits of contextualizability might be especially pronounced when crossing boundaries. Used in this way, [[[[PTN]] - discourse graph]] can be conceptualized as [[[[PTN]] - boundary object]]s, which are optimally weakly structured in common use (at the boundaries), but need to be strongly structured, with context added, for example, to be useful across boundaries.

    - But it could also be the case that the \artifact{} itself is epiphenomenal, and the act of constructing the \artifact{} is what enhances synthesis.

        - or that writing abstractions and functions while programming is beneficial because of the way it provokes systematic thinking through of the theory of the problem, not because the abstractions and functions themselves are really more useful to have around than just writing them anew.

        - This would be reminiscent of claims that note-taking and annotation are beneficial for their construction, not their reuse [[@marshallExploringRelationshipPersonal2004]]; #[[Z]]
[[outline2021-06-29 talk on knowledge management with orgProtocol Labs summer research associates]]

- Part 2: Practical concept: [[[[PTN]] - discourse graph]]

    - Beyond iTunes for papers

    - Preserve the mess!
[[August 16th, 2020]]

- also thinking more and more about the [[[[PTN]] - discourse graph]] in conjunction with [[@gruberDarwinManPsychological1974]], this [dance between the theoretical and the evidential](> The two kinds of task, theoretical and evidential, entail different activities, and in the long run they may yield distinguishable products for our consideration. But __in vivo__, in the life of the thinking person, they are thoroughly intertwined. The most speculative "castle in the air" is triggered by a simple observation or a friend's remark about his dog. Hard work amassing the facts on a special point is guided by a long theoretical argument with which it may have only a tenuous logical relationship: the theory does not absolutely depend on the facts, nor could the facts ever guarantee the theory. The relation of theory and evidence is not simply logical but psychological.) [[dance between the theoretical and the evidential]]

    - On the one hand, there seem to be useful distinctions between the two layers, and [[std/Micropublication]]s seem to be able to capture these nuances.

    - On the other hand, we want to be careful not to make the distinction between these two layers/tasks "hard" - more specifically, we don't want to make the mistaken assumption that data is "neutral" (cf. [[Z: Observation is theory-laden]])

        - I guess this would be an important reason for requiring there to be rich [[context]] attached to each "data" micropub

    - I am not sure that [[sys/Hypothes.is]] annotations are the best way to encode the [[epistemic foundation layer]]: they seem important, but maybe they should not be the main containers: maybe we have [[std/Micropublication]]s all the way through, but with a distinction between "evidence" and "hypothesis" ones?

        - this again would be similar to [[sys/Polyplexus]], although there isn't nearly enough [[context]] in the evidence micropubs, as far as I can tell
[[January 24th, 2022]]

- Quick note: reading [[@oulasvirtaHCIResearchProblemSolving2016]] quickly, and realizing that the [[[[PTN]] - discourse graph]] model struggles with kinds of contributions that are *conceptual*, at least as currently conceived.

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FI_h6m-Xaxn.png?alt=media&token=b4b3a487-b7df-4620-92f5-fa79aa2e3ba2) (p. 4958)
[[July 8th, 2021]]

- some good stuff on [[web 3.0]], and good case for things like [[sys/IPFS]] (I really want to try this out, and maybe have my [[[[PTN]] - discourse graph]] [[bet/[[D/Synthesis Infrastructure]]: it is possible to write close to prose but seamlessly translate to queryable, shareable discourse graph formalisms in the backend]] stuff be hosted on there?)

    - The Rotting Internet Is a Collective Hallucination - The Atlantic: https://www.theatlantic.com/technology/archive/2021/06/the-internet-is-a-collective-hallucination/619320/

    - Perma.cc | Docs: https://perma.cc/docs/accounts

    - ipfs/ipfs: Peer-to-peer hypermedia protocol: https://github.com/ipfs/ipfs

    - Browsers 3000: Building the decentralized browser we need, with web3 and P2P technologies. - Devpost: https://browsers3000.devpost.com/
[[October 25th, 2020]]

- Template for [[[[PTN]] - discourse graph]] integration into journal club discussion questions:

    - 3: What are the main implications of these findings/observations in this paper that we care about?

        - e.g., what major claims do these findings help us think through or develop?

        - these might become seedlings or zettels

        - this currently maps i think to "significance" in the current templates

    - 2: What are the main details we'd want to have on hand to interpret/contextualize the findings and what they mean later on?

        - e.g., Study details? Population? Setting? Specific effect sizes and measurements? Anything about the authors?

        - try to grab screenshots of things someone might look at later, alongside some description of them

        - these will go under a "lit-context" block in a paper entry, and be linked to the micropubs or zettels via block references. see #[[observation-notes]] examples in Joel's graph

        - e.g., any other papers that have similar/opposing findings?

        - these currently map to "methods" i think

    - 1: What were the main findings/observations we thought were interesting?

        - Try to phrase these in the past tense, and contextualized (e.g., "the model converged to y accuracy in n epochs with the xyz dataset", or "the measurements on the mouse were z")

        - These will become micropubs

            - Can write a methods block that is tied to a particular finding (e.g., measured XYZ with material A under conditions y; saw ABC); see #[[observation-notes]] examples in Joel's graph

            - idea here is to make these as contextual as possible, so we can carefully extrapolate and synthesize into zettels and higher level claims
[[January 26th, 2021]]

- Here we want to unpack much more **why** we think the design of epistemic models, like [[[[PTN]] - discourse graph]], could really boost synthesis, which really falls into two broad sets of ideas, following the [2nd paragraph in the 1-pager](Significant work across formal conceptual models of scholarly argumentation [[@deWaardProteinsFairytalesDirections2010]], [[@clarkMicropublicationsSemanticModel2014]], sensemaking [[@russellCostStructureSensemaking1993]], and knowledge management [[@ackermanSharingKnowledgeExpertise2013]] suggest that an optimal information model for supporting synthesis is the epistemic model: shareable collections of knowledge __claims__ (e.g., __children are less susceptible to COVID-19 infection, given equivalent exposure__) and their associated __context__ (e.g., \textit{was sampling symptom-based? Where was the study conducted? At what point in the locality's epidemic time course?}), \textit{connected} in a discourse graph (e.g., supporting other hypotheses/claims, corroborated/disputed by other claims). )

    - Fits interaction/cognitive requirements of synthesis [like a glove](These affordances are hypothesized to enable key process-level interactions with scholarly knowledge that are crucial for synthesis, such as a principled dialectic between context-rich observations (data) and creative and formal construction of models and hypotheses (theory). )

        - [[dance between the theoretical and the evidential]] / [[dialectic]]

        - [[[[CL]] - Compression and contextualizability are in tension]]

        - [[[[CLM]] - Context is necessary for reasoning under uncertainty]]

        - [[[[QUE]] - How can we support explicit contention with evidence when synthesizing knowledge claims?]]

        - [[[[CLM]] - Knowledge is fundamentally contextual]]

    - Enables [[reuse]] [across boundaries](These affordances may also enable more effective reuse and remixing of ideas across boundaries of time, projects, and even collaborators. ) of time, projects, and people

        - [[[[CLM]] - Knowledge must be recontextualized to be usefully reused]]

        - [[[[CLM]] - Most private annotations aren't useful to other people]]
[[January 18th, 2021]]

- this pairs nicely with [[@vanrooijTheoryTestHow2021]] in specifying heuristics and moves for theory-building, which... I think is a nice fit for [[[[PTN]] - discourse graph]] and [[context queries]]

    - how nice if we had tools and systems (with data!) that allowed us to explore these, in a somewhat analogous way to photoshop (exploring variants), simulations, statistical software, and other tools for thought.

    - what are the tools for synthesis?

        - as I've said in the past [[[[CLM]] - Effective individual synthesis systems (seem to mostly) exist (for a select few)]]

            - the critical problem, though is this: because they're so individual, everyone is effectively an island. what if you don't have?

            - a small exception, again, is sofware for [[systematic review]]s, but again, this doesn't solve our problem, bc so much [[synthesis]] that we want to do goes far beyond [[RCT]]s

                - plus, they're often, afaict, "use once", not really supporting [[interoperability]] [[@oconnorStillMovingAutomation2019]] and [[reuse]] [[@blakeCollaborativeInformationSynthesis2006a]]
[[January 15th, 2022]]

- similarly, rates of change for nodes in the [[[[PTN]] - discourse graph]] ontology are different in a systematic way

    - previously we had questions and claims as pages, and evidence as blocks. i think the reverse is better! [[technologies-in-practice]] reveals this in my own work, and i suspect in others as well

    - they vary by node type

        - questions - low (driving questions) to high (frontier questions)

        - claims - low (foundational, well-tested claims) to high (speculative)

        - evidence - low (mostly stable, only change if there is correction)
[[December 18th, 2020]]

- INhaling some discussion with another Roaman about potential applications of [[[[PTN]] - discourse graph]] #fieldnotes for [[P/PO study/dev for synthesis infrastructures]]

    - **[Henry Finkelstein](https://app.slack.com/team/U01CAM7HW81)**  [1:39 PM](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608230370031900)

    - [@Joel Chan](https://roamresearch.slack.com/team/USYSQ6K28) - I’m undertaking an ambitious project that is grounded, first and foremost, in current academic literature. My project kicks off in January in earnest, and I’m laying the foundations now to hit the ground running after the new year.It is my intuition that, before I delve deep into journals, I want to have a standardized rubric for how I grade the potential validity of any given article. There are enough scientists in my family for me to know that seemingly innocuous articles can easily be perverted by funding sources, PI agendas, predatory journals, or other (intentionally or unintentionally) limiting choices by the investigators.

    - [1:40](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608230430033100)

    - Do you have any resources that I can grok for how to train myself to critically read academic literature? I’d like to develop a 7-15 point rubric that I squeeze every article through to assign a “trustworthiness” score that then informs some of the synthesis aspects you discussed in the article you shared.

    - [1:42](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608230523034800)

    - For example, even if an article has very sound methods, analysis, and logical conclusions on the effects of white sugar being a godsend in the health and longevity of mice, I will heavily discount that study if I learn it was funded by Coca Cola and is often cited in their marketing materials. I simply do not trust the impartiality of the researchers based on the funding source, in this (perhaps hyperbolic) example (edited)

    - **[Joel Chan](https://app.slack.com/team/USYSQ6K28)**  [9:36 PM](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608258986036900)

    - ![:smile:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/google-medium/1f604@2x.png) i'm on here pretty often, just a bit nervous about doing substantive discussions here due to the Slack free plan message limit

    - [9:39](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608259155039500)

    - i like how you're thinking about this! i'm not sure it's feasible for this job to be done with a rubric: while parts of it could be -- e.g., an experiment with 10 participants total and a clear confounding variable should probably be downgraded -- many other times the judgment is more nuanced and in context (e.g., gains in trustworthiness for a set of claims if there is diversity in settings; or we might be a bit skeptical due to funding sources, but the data is open so we cautiously trust it and increase our trust if it is independently verified). but i'd be curious to see how far we can get with a rubric!

    - [9:39](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608259173039900)

    - is health/nutrition the domain you're thinking of?

    - [9:39](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608259189040300)

    - that woudl be a really rich domain for thinking through a rigorous process of synthesis!

    - Today____

    - **[Henry Finkelstein](https://app.slack.com/team/U01CAM7HW81)**  [11:45 AM](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608309932041500)

    - Thanks Joel, and your comments are well received. I’m intent on getting as far as possible with the rubric methodology, recognizing it’s inherent limitations and instituting a resurfacing system so that I can continuously upgrade / downgrade articles based on new awareness around investigators, data, etc

    - [11:48](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608310117045100)

    - My area of research is very broad (= human thriving) and I’m writing up a detailed (layman’s) research proposal that underscores exactly what I care to study. Should be done within the next week and I’ll share that with you so that we can begin to grok the best way to tackle that.To answer your question head on: physical health is the first leg of the stool and that’s where I’m starting. Physical health includes nutrition, movement, sleep, medicine (anything from sub-baseline to baseline), and enhancements (anything from baseline to above baseline).Within that domain, I’m starting with nutrition, then transitioning to sleep, then to movement, then to medicine, then to enhancements. I’m starting with nutrition because it’s a (relatively) straightforward domain of literature that is well studied and can act as a (relatively) simple entry point to this process and workflow. I only care to introduce more nuanced and complex topics as I get comfortable with the flow of parsing, digesting, and synthesizing academic literature. (edited)

    - ![:+1:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/google-small/1f44d@2x.png)1

    - ________

    - [11:53](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608310388049700)

    - And, as I get deeper into a rich academic study, I’ll be putting together a scientific advisory board to make sure my inherent cognitive biases are kept at bay, as much as possible. In seeking to bridge the academic and the lay population, I strive to be a multi-stylist - I want to uphold the absolute highest standards of academic rigor so that I can stand proud were I ever to be published in Nature or Science, and then to carefully engineer that awareness to be palatable and accessible to folks who would never conceive of ever picking up such a journal.To that end, I will compile an academic advisory board (to ensure academic rigor and pristine intellectual honesty) in parallel to a coaching / educator / writer / counselor advisory board (to ensure I can craft a message that resonates in the target populations). Certainly a lot of work to come, and I’ve never felt more inspired and empowered to follow that path.

    - ![](https://ca.slack-edge.com/TNEAEL9QW-USYSQ6K28-7dff9f6391dd-48)

    - **[Joel Chan](https://app.slack.com/team/USYSQ6K28)**  [10:26 PM](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608348381053700)

    - Wow, that's a really fascinating and ambitious project [@Henry Finkelstein](https://roamresearch.slack.com/team/U01CAM7HW81)! Would love to talk more about this.Looks like you've connected a bit with [@Chinarut](https://roamresearch.slack.com/team/U01E17XN0P3) who shares quite a bit of your goals.I'd be interested in talking more with you about how you want to set this up. You might be interested in this pilot I'm trying to get off the ground to try to apply a conceptual / process model for synthesis that I'm developing to medical research questions: https://roamresearch.slack.com/archives/C017K0BM5S6/p1608348125041500

    - ____

    - ![](https://ca.slack-edge.com/TNEAEL9QW-USYSQ6K28-7dff9f6391dd-24)**Joel Chan**

    - Hi all!About a month ago I posted something to gauge interest in doing a pilot of setting up a shared Roam for synthesizing medical knowledge. Alas, that was more than 10k messages ago, so context is all gone now!To recap, I'm developing a conceptual and process model for how to do knowledge synthesis in Roam, in a way that is both more powerful for individuals, but also potentially amenable to collaboration and sharing.

    - It's written up (hot off the presses, first release) here: https://oasislab.pubpub.org/pub/54t0y9mk/release/2The basic idea is to start with some key question notes and a bunch of sources, and systematically develop synthesis notes that are informed by / grounded in observati… Show more

    - 2 files ____

    - [![image.png](https://files.slack.com/files-tmb/TNEAEL9QW-F01HNKJ1HBK-65269b267e/image_720.png)](https://files.slack.com/files-pri/TNEAEL9QW-F01HNKJ1HBK/image.png)

    - [____](https://files.slack.com/files-pri/TNEAEL9QW-F01HNKJ1HBK/download/image.png)________

    - [![image.png](https://files.slack.com/files-tmb/TNEAEL9QW-F01HA71QP8T-56d5ab8839/image_480.png)](https://files.slack.com/files-pri/TNEAEL9QW-F01HA71QP8T/image.png)

    - [____](https://files.slack.com/files-pri/TNEAEL9QW-F01HA71QP8T/download/image.png)________

    - [Posted in #roam-medical](https://roamresearch.slack.com/archives/C017K0BM5S6/p1608348125041500) | [Today at 10:22 PM](https://roamresearch.slack.com/archives/C017K0BM5S6/p1608348125041500) | [View message](https://roamresearch.slack.com/archives/C017K0BM5S6/p1608348125041500)

    - **[Henry Finkelstein](https://app.slack.com/team/U01CAM7HW81)**  [1:29 PM](https://roamresearch.slack.com/archives/C011F6XNV0V/p1608229764029200)
[[September 1st, 2021]]

- [[Matt Clancy]] is building on some ideas around [[[[PTN]] - discourse graph]] to create the first (to my knowledge) public hypertext [[living literature review]]! https://www.newthingsunderthesun.com/

    - Announcement here: https://mattsclancy.substack.com/p/the-future-of-new-things-under-the?utm_medium=email&utm_campaign=cta

    - Publishing on [[sys/Pub-Pub]]!
[[February 25th, 2021]]

- Thinking through more of the infrastructure for sharing [[[[PTN]] - discourse graph]] (following from [yesterday](Feeling an [[ethnographic sneeze]] about how to jive the richly [flexibly compressed]([[[[PTN]] - flexible compression]]) of elements of the [[[[PTN]] - discourse graph]] into a shareable format that might go on something like [[sys/Ceramic]])), but also the more concrete instantiation of the various kinds of [[context]] (from below, beside, above) and [[[[PTN]] - flexible compression]] that is enabled by a block-and-page data structure

    - Here we have an `observation note`

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0SelwTIR2n.png?alt=media&token=8b632960-daeb-4111-a727-c8b813f858b4)

    - Let's consider how a `discourse graph` representation allows for rich contextualization of the `observation note`.

    - **Context from "below"**

        - The focal `observation note` has [[context]] from "below" through 1) a `context snippet` snapshot of the Table of results that is both indented under the observation note, and also hyperlinked into it, 2) methods details (also `observation notes`??) that live as blocks (which are themselves contextualized by `context snippets` through indentation and hyperlinking). This rich contextualizing information is available on-hover, as well as by clicking to unindent and reveal an indented block

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FTHTI4RtisW.png?alt=media&token=5fc50aba-5181-4173-88f9-de5429ee53c7)

        - Clicking through to a hyperlinked methods `observation note` also opens up a similar set of rich access to contextual information, through hyperlinking and indentation

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fx-H7CGmvbk.png?alt=media&token=a76d2a16-fe3c-477e-ae79-92172be3a816)

        - Importantly, the block/graph data structure also means that other contextual details from the same paper are accessible (and in principle queryable and computable for [[context queries]]) through their common parent (the paper page).

            - First, the screenshot shows how every block in the indentation "path" (every item between `>` symbols) is formally connected to the `observation note` in the underlying graph.

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fg72Hz3O9PS.png?alt=media&token=3cd2de47-385c-40a5-8b1d-aa0c08f4d8f7)

            - But every other block that is also a child of the parent page is also formally connected to the focal `observation note`, which means that details such as the procedure, experiment design, or metadata of the paper, such as authors, year, etc. are closely accessible for contextualizing the focal `observation note`.

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FGcwHwiAQWt.png?alt=media&token=669b3048-5443-4881-a3ba-a8985e990eb2)

            - Since every element is linkable, we can also explore details about the authors (through linked references of the author page) to help contextualize the focal `observation note`. For instance, you can ask questions like "where does this author tend to publish? What theoretical or disciplinary angles might this person be coming from?"

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FcoDg-EuN2I.png?alt=media&token=400b8a35-cb31-4ca5-a7cb-263d8a8f20f5)

    - **Context from above/beside**

        - The focal `observation note` also has [[context]] from "above" and "beside", through referencing in other pages or blocks. For instance, clicking on the `2` button on the right reveals two references to the focal `observation note`: 1) discussion of this result in a question note about whether/how people are efficient routes to useful cross-boundary information, and also 2) reference in a "sibling" `observation note` about a significant interaction effect between background similarity and face-to-face contact, which qualifies the original effect in an important way.

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FR84TnO96NK.png?alt=media&token=b33322e1-063e-4774-a53b-3f3ddf4c8122)

        - Seeing the focal `observation note` in its larger referenced/discourse context helps reveal also how having direct access to contextualizing information through hyperlinking can facilitate synthesis across `observation notes`. It might be crucial, for example, to know if there are any variations in effects by institution/prestige: is there some effect of "leeway" or resources that needs to be taken into account for face-to-face conversations to bear fruit?

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkZfDRnSyoO.png?alt=media&token=fee55a9e-88df-4b6e-a9ec-323e501916c3)
[[April 25th, 2021]]

- Listening to [[Beau Haan]]'s [[RoamFM]] interview, some thoughts worth writing down in relation to [[[[PTN]] - discourse graph]]:

    - The evidence for his system is VERY strong and worth attending to because it is not built on ideology or arm-chair theorizing, but from **practice**: really costly, honest signals from literally hundreds of people using it and finding that it "works" for them

    - His system is optimized for storytelling, going into the depths of who you are to draw from that and tell compelling stories

        - I think there is an elegant overlap between this and what we really really want to do in science: in the pursuit of truth, the uncertainty, the difficulty hearing yourself think (cf. [[Andy Matuschak]]: 17:45 is where [[Andy Matuschak]] starts talking about hearing himself think: "goddamnit, it's hard to hear yourself think!"), the [[ethnographic sneeze]]

        - The driving force of the story of Lydia is part of it

        - And so is his own story for why he really wanted to do it for himself

    - How does it work? I don't think I still quite understand it 100%

        - But I feel like there's something more. He keeps coming back to the idea of "relief".

        - I think, still, there is a strong element of [[context]] here. Our conversation about the central role of the fleeting notes here, the tripod.

        - There's simplicity too. This is what draws me in, when thinking about shared schemas for [bridging public and private knowledge]([[[[QUE]] - How can we best bridge private vs. public knowledge?]])

        - And deeper still... this idea of... really having it be a [representation of *you*](His system is optimized for storytelling, going into the depths of who you are to draw from that and tell compelling stories). What you really think. Not what you think you should think, what others think you should think... not what will persuade someone else. But... reality. Unvarnished and distilled. The *process* (not just the structure) pushes you to this level of honesty.

            - ~57:00 - this is what I think.

                - I think this is it.

                    - This resonates so much with what I'm thinking and feeling as the essence of creative courage that must drive true synthesis - an honest [[dance between the theoretical and the evidential]] - building knowledge that is *real*. that will last. not [[Cargo Cult Science]], but real shit.

                    - COURAGE. this takes courage. and creates, builds courage.

        - But also.. I'm not even sure I understand what constitutes the system.

            - The tripod... keeps coming up.

                - There are layers of [[context]] in there that can really help someone else [[reuse]] it (or yourself in the future)

                    - It's not all or nothing.

                    - The reference and literature notes at least feel like **Context from "below"**

                    - The fleeting notes I think is waht connects most clearly and elegantly with teh central insight of standpoint theory: measure the measurer. Make the observer transparent. No [[view from nowhere]]. This goes back to [[[[CL]] - People need information about authorship to reuse information]]

            - The index... feels like context from "above" (discourse context, or **Context from above/beside**)

            - The relevant notes space, and the tags... that I'm still not quite wrapping my head around. i think it serves the purpose of... scanning? entry points? idk. not sure yet. but my gut says this might be where we put placeholder names like standpoint theory or boundary objects, or... idk. pithy phrases like "survival of the fittest"? that are just beginning handles into deeper ideas?

    - The discomfort I have is still.. I think... is there a tension here between what gets written in here and sharing with others?

        - In the limit of open science, of openness and vulnerability, this isn't really an issue. And maybe that's not our problem to solve?

        - But one question is... if we "lop off" the personal bits, the fleeting notes... will the permanent notes even make sense? From a personal standpoint, it's definitely going lose some of its power? There is some connection and knitting together of the knowledge base that happens in that space. But maybe for fleeting notes, it's more important that it *did* happen, rather than it being useful as a resource to return to...

        - but also: if there is no real gain for individual synthesis, then everything is moot. forget it. so we figure out what will help the individual first, and figure out how to share it. i think it is solvable. there are different levels of sharing.

        - what might sharing look like?

            - you find a connection with a question or claim in my graph that interests you.

            - you then "graft" it into your own graph. my "citation" and context snippets go into your reference notes slot (the "material/world"). my observation note becomes the *starting point* for your literature note slot. you make sense of it in the fleeting notes and EDIT it as you see fit. even throw it away if you want to.

            - with this in mind: what might queries of others' graphs look like to support this?

    - There is still the set of [three problems](three problems (and solutions) in adapting the zettelkasten to [[synthesis]]:) we talked about, and a new problem of semantics: we have, as far as I can tell, basically all implicit relationships between the elements. i think the foundation is supports relationships? and then between the permanent notes we have... associative relationships? how to translate that to the basic primitives of [[synthesis]]? support/oppose/explains/moderates, etc.?

    - But it also speaks to the [[ethnographic sneeze]] I've been feeling... the perils of over-structuring, always trying to rear its ugly head... [[[[PTN]] - incremental formalization]]!!! writing a literature note in isolation, embedded in a decontextualized, "clean" way in the body of a reference note, feels.... like it goes against a fundamental idea that we have to keep coming back to: [[[[CLM]] - Knowledge is fundamentally contextual]]!
[[August 2nd, 2020]]

- [[[[PTN]] - discourse graph]] for [[D/Synthesis Infrastructure]] (quite similar in some ways to what [[sys/Polyplexus]] does with their evidence and conjecture [[std/Micropublication]]s), fleshing out for [[Grant proposal for Synthesis Infrastructure - NSF CHS / SOS 2020]]

    - putting it all together

        - for the [[epistemic foundation layer]]

            - each group uses zotero shared libraries, and people annotate in their favorite pdf reader

            - we build an extension (or maybe fork on [[sys/Zotfile]]) that extracts special annotations and dumps into a shared [[sys/Hypothes.is]] library into our special [[epistemic foundation layer]] format.

                - technically, extracting annotations shouldn't be that hard, there seems to be a stnadard representation of annotations across most PDF readers; [evidence of this is zotfile](https://remembereverything.org/manage-pdf-highlights-annotations/)

                    - depends on the pdf being OCR-ed, but most PDFs should be already by now, and can stop-gap with adobe acrobat

            - in the background we have a [[[[PTN]] - flexible compression]] module that parses the PDF to enable [[context queries]] at this pub level.

        - for the [[epistemic synthesis layer]]

            - we will likely support google docs to start with, since this is for teams.  are then available for autocomplete insertion into synthesis notes, similar to citation statements

                - feedback from [[August 4th, 2020]]:

                    - in the ((Ysk6dNrA4)), definitely lean into the diversity, not just a google docs add-on but also consider at least one or two more alternative representations, like a google spreadsheet or canvas, depending on what scholars are already doing;

                        - key strength of integrating into a [[sys/Hypothes.is]] or other existing [[standards]] is the ability to have it end up in different "endpoints"

            - we can maybe jerry-rig a [[sys/Google Docs]] extension to allow linking of individual statements into larger ones across different documents, similar to roam. and also support maybe a lighter, cleaner version of roam (maybe a front-end wrapper on top of [[sys/FoamBubble]] or similar?). the stuff that gets linked is important enough that people want to remember and probably has also gone through some peer review. whatever the case, we can tack onto these intrinsic motivations.

            - the tricky part here will be to somehow extract [[epistemic synthesis layer]] pubs from these notes into a collection.

            - people write summaries and higher-level notes in their favorite text editor. the key part here will be some kind of extension that supports interactions with the shared library of [[epistemic foundation layer]] pubs:

                - individual "autocomplete" insertion (similar affordances to a zotero extension) - insert into a citation statement, you get the citation, plus a [[sys/Hypothes.is]] link to the original grounding statement

                - [[context queries]], that enable the writer to start to sift through collections of pubs in a citation statement

        - at a high level then, if we can make it so that, from the user perspective, they're using zotero + their favorite PDF reader for reading, and google docs for synthesis notes (familiar and suitable for sharing), with a standard [[sys/Hypothes.is]] layer in the background, i think this could be quite promising from the POV of sociotechnical integration.

            - buzzword: make simple yet powerful modifications to familiar tools and workflows

        - this is way more concrete than what we had: more risks on the dev side, but i think if we scope it to a particular set of users, rather than aiing for generality to start with, knowing that were building on top of an ecosystem that is trasnferable (plugin system, api, [[sys/Hypothes.is]], etc.).

        - how does this design approach address concerns about sharing, etc.?

            - for one thing, the initial target of sharing is people you have shared cotnext with, likely not in direct compeittion (e.g., within your lab, reading group, department, cohort)

                - there are also natural opportunities and social infrastructure for peer review and synthesis and sharing;

                    - peopel email and slack each other all the time

                        - we could make [[sys/Hypothes.is]] or [[std/Micropublication]] integrations for slack, where you can @mention something to share

                        - maybe integrations into open-source forums like [[sys/Discourse]]?

                        - or maybe just a simpler chrome extensino that you can use to insert into a forum post?

            - and there is no need to change incentive structures (vs. say, making [[open data]] or [[open science]] practices or novel pubs like [[sys/distill.pub]] and [[std/Micropublication]]s part of APT or top-down imperatives from journals and funders) - in this way, it's more bottom-up and "growing" in flavor

        - what are the technical or research problems to be solved?

            - the stuff about [[[[PTN]] - flexible compression]] still apply.

                - context hooks and so on in the [[epistemic foundation layer]]

                - [[context queries]] in the [[epistemic synthesis layer]]

            - and we also want to enable some degree of [[composability]] in the google docs-ish plugin in the [[epistemic synthesis layer]]

            - conceptually too we can illuminate more of the [[synthesis]] workflows

            - and address / validate hypotheses about sharing

                - e.g.,

                    - x "note designs" will be sufficient for y benefits of sharing

                - we'll want to be quite precise about the levels of sharing - maybe just set a more precise "upper limit" (this could also be a conceptual hypothesis to test)

                    - cf. [[[[QUE]] - How can we best bridge private vs. public knowledge?]]

                    - and also [[Karen Wickett]]'s comments on our talk

                        - and [[Wayne Lutters]]'s response in email "I especially appreciated Karen W's comment about moving from the idiosyncratic individual to the group, but how unnatural that is and how you may not be able to step up from pair, to team, to community, to world, ... "The parts for sharing""

                    - feedback from [[August 4th, 2020]]: be careful about the dragons when crossing from 1 group to another; sharing within a group probably acceptable risk; maybeeeeeeeee sharing to another closely related group, say, int he same dept, but might want to scope out that risk entirely from the grant

        - could we sneak in some baseline comparisons to explore how this local approach might compare to a more centralized repo approach?

            - maybe start to explore this if we add (esp. if we're doing a medium or larger) attempted expansions beyond my local circle, and elucidate the sociotechnical challenges there

        - as a side note too, the prevalence of [[Explorers]] and [[Hackers]] tools suggests some initial feasibility and value of the core ideas around [[[[PTN]] - flexible compression]] (cf. [[[[CLM]] - Effective individual synthesis systems (seem to mostly) exist (for a select few)]]), but they haven't yet been empirically validated in a rigorous way, and also often really struggle to escape silos

    - terrible #sketch

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0rJuGaLbjJ.png?alt=media&token=815bfb6e-70b8-4291-a806-d7d613b84bf4)

        - reminds me: at both stages, things get a lot more interesting once things get going and you're no longer starting from scratch; the problem gets a bit easier, and hte value starts to accrue pretty quickly

        - in theg rant, we want to be a bit more concrete about hte potential palces for value that we see integerated into people's workflows and practices, and articualte how we intend to test these hunches

    - finally: some next steps:

        - one key dimension of risk we can control: is tehre any reaosn to believe that we can get perofrmance that is reaosnable enough to support valuable [[context queries]] operations (and [[[[PTN]] - flexible compression]]?)

            - need to identify sections

                - then within sections, identify things "likely to be answer for [[context]] query x"

                - doesn't need to be perfect (can prioritize recall over precision) bc we verify at [[context queries]] time

                    - also preioritize recall over precision bc [[[[CLM]] - Specifying context for future reuse requires predicting trajectories of future reuse]]

            - get SOTA code if we can for some major approaches

                - [[Jodi Schneider]]

                - [[Catherine Blake]]

                    - claim extraction is challenging, but we're not trying to solve that; that's the job of the reader! what we try to do is basically do some kind of specialized [[information extraction]]

                        - which is probably quite a bit easier

                            - things like author, affiliation, year, method used (lots of leverage if there is some maturity in field, as long as there is at least a methods textbook we have [[distant supervision]], at minimum we probably have some kind of methods section)

    - the two layers

        - ## [[epistemic foundation layer]]

            - past tense

            - observation

            - [[context]] grounded in methods, etc

                - maybe replication too?

                - and connections to second layer for “what it means”

            - formal [[composability]] relations in terms of support / detract from

            - mostly happening in reader

            - exported into [[sys/Hypothes.is]]

            - analogous to my lit-notes

            - maybe eah of these is a two-fer, at the level you might find in an abstract:

                - 1: authors did X (e.g., showe)

                - 2: authors then saw Y

        - ## [[epistemic synthesis layer]]

            - present tense? more like [[std/Nanopublications]] or zettels

            - [[context]] inherited from lower layer, and also emphasized from networked connections

            - formal [[composability]] relations in terms of discourse and causation (eg boundary condition, causes, explains, etc)

            - mostly happening in “notebook”

            - exported into [[std/Nanopublications]] or [[std/Micropublication]]

            - analogous to my zettels

            - where possible, can here (and in the lower level) impelement some knid of [[controlled natural language]] (a ala [[@kuhnBroadeningScopeNanopublications2013]], and some stuff [[sys/Hypothes.is]] is exploring), to get some kind of [[[[PTN]] - incremental formalization]]
[[February 11th, 2021]]

- name [[[[PTN]] - discourse graph]]?

    - used to be:
[[October 27th, 2020]]

- fact-finding mission for further specifying the technical infrastructure for [[[[PTN]] - discourse graph]]

    - digging into [[annotation]] [[standards]] that overlap with [[sys/Hypothes.is]] - specifically the [[std/W3C Web Annotation recommendations]]

        - Some key takeaways

            - The [[W3C]] working group is chaired by [[Paolo Ciccarese]], of [[std/Micropublication]] and [[std/SWAN]]! 100% need to get in touch with him - he also built and maintained [[sys/DOMEO]] for awhile, so would have hte most insider knowledge about its use and so on

            - Binding an annotation to a specific subregion of a PDF is technically feasible

                - This is specified in the [section on "fragment selectors"](https://www.w3.org/TR/annotation-model/#fragment-selector), where you can specify PDF sublocations with a combination of page numbers and bounding boxes

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FtPWffEfIBg.png?alt=media&token=44b82946-fe91-4b57-8546-ab7c32241add) (from [here](https://hyp.is/3YJxrBiaEeu0p49-SClxVQ/www.w3.org/TR/annotation-model/))

                - a screenshot can also be specified as an img in the "body" of the [[annotation]] (typically only given by text strings in [[sys/Hypothes.is]] annotations), but the model is definitely expressive enough to accommodate it

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUyYZwXwt3C.png?alt=media&token=beccce47-d448-499b-a34b-5b7ec814c7ce) (from [here](https://hyp.is/jryHqhibEeuY69Ph3CvSFw/www.w3.org/TR/annotation-model/))

    - also digging back from [[Xin Qian]]'s earlier prototype of the autograb stuff

        - one question is whether the [[sys/GROBID]] parser that breaks the PDF into classifiable units retains information about the page number and bounding box information, or whether that is lossily compressed! if the latter, then no go, i think: crucial for [[[[PTN]] - flexible compression]] to always tie back to the source location

            - edit: yes it does!

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0qdzFzZro7.png?alt=media&token=7a5bc75f-16d7-464a-b84d-0eb64757d127) (from [here](https://hyp.is/7ygKYhieEeu691sWdQf8og/grobid.readthedocs.io/en/latest/Coordinates-in-PDF/))

        - Links

            - annotated spreadsheet at https://github.com/xeniaqian94/lab/blob/master/python-service/output/reproducibility_sentence_output_to_annotate_021919_randomized-Xin.csv

            - Server to call sentence classification https://github.com/xeniaqian94/lab/blob/master/python-service/autograb-server.py

                - API that is later called for various things, including

                    - [[sys/GROBID]] for auto-grabbing metadata

                    - a component that models

            - classifier at https://github.com/xeniaqian94/lab/blob/master/python-service/reproducibility_classifier_train.py

                - Is how we train a model that we later do inference on for classifying "reproducibility" sentences

    - re-clarification: our goal in integrating into [[annotation]] [[standards]] like [[std/W3C Web Annotation recommendations]] is less to enhance the reading experience and engagement around a single *document*, so much as to enhance the richness of [[context]] that can be attached to [[std/Micropublication]]s that are at the "claim" level, to significantly enhance their [reusability]([[reuse]])

        - this is because these context snippets cannot feasibly be (and probably not even conceptually) be meaningfully pre-specified outside of a specific [context of reuse]([[context queries]])

        - that said, a context classifier could enhance the [[active reading]] process by providing potential context "bookmarks" for the reader to reify as they make sense of a document in the context of a specific reading goal

        - additionally, the integration into open [[standards]] allows for broader integration of [[annotation]]s about [[context]] (I think the proper term here then might be [[context annotations]]?) into the active reading experience

        - again, this "autograb" approach is substantiated in part by the findings of [[@blakeCollaborativeInformationSynthesis2006a]]: authors think that there is enough regularity in the types and locations of [[context]] information that we could build an automated system to extract htese bits of information, which would in turn enable exploration of a variety of hypothesis projections

    - horrendous first sketch

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FqrlN3AaJ3G.png?alt=media&token=f4edc637-1d0e-4db4-b7b9-945545d8ad80)
[[January 4th, 2022]]

- Thinking this is going to be needed to help [federate]([[federation]]) distributed [[[[PTN]] - discourse graph]]s for [[D/Synthesis Infrastructure]] - addresses a nagging [[ethnographic sneeze]] about how to join different

    - Also cool: they build on [[wikidata]]

        - [[Ivo]] already has a plugin for integrating with wikidata, could play nice with it
[[roamSOP]]

- ^^observation-note^^ blocks (see [[[[PTN]] - discourse graph]])

    - Contextualized

        - In past tense, with names of authors maybe?

        - Grounded in block references to context snippets
[[March 17th, 2021]]

- Thinking more about my adaptation of [[Beau Haan]]'s [process innovation]([[sys/lebeauzettel]]) (relevant insights for refining process model for [[[[PTN]] - discourse graph]])

    - There's still a missing primitive: "foraging" from others, like a lit review, theory paper, or something. But I think we can define it quite easily as a variant (generalization?) of `write-obs-note`

        - `write-lit-note`

            - for <what question/topic/synthesis/idea> ((one parent bullet per focal question/synthesis note))

                - from <which source> ((one parent bullet per source))

                    - lit-note ((blockref in the lit notes from the source page))

        - The templates make clear what is implicit in my brain: not just read with a pen in hand, but read with a question(s) in hand! We are bringing sources and observations into conversation with a question we have.

    - Key bits I like:

        - Writing sessions as git commits: writing microtasks! Header as commit message: summary of what was contributed to the conversation (if any)

            - Diff from his approach: doesn't have to be unique per session; can't be! ideas take longer to percolate than a few sessions

                - Levels of "zettel" maturity, heuristics driven by friction of use ([[desirable difficulty]]):

                    1. Just a text block (still very early stages, exploratory); accessible, but hard to reuse. that's good!

                    1. Inkling = block in question page, analogous to index; can reuse, but harder (can't autocomplete as easily; that's good!)

                    1. Mature = page with metadata ([[desirable difficulty]] to create this, but that's good!)

                - What i like about these levels:

                    - natural way to have the argument "talk back to me"

                        - can generalize these levels of desirable difficulty for questions and ideas too!

                        - really wnat to prototype this; can refactor any of my question pages into this :D

                        - can see where the argument is softer and harder quite naturally

                            - softer = just blocks of text

                            - a bit harder = blocks with references

                            - solid = page references The templates make clear what is implicit in my brain: not just read with a pen in hand, but read with a question(s) in hand! We are bringing sources and observations into conversation with a question we have.

                    - could also be a natural pruning function to help with the [noise problem](Thinking back to convo with [[Andy Matuschak]] about [noise](((Aq6nPUGWy))) in synthesis notes / [[sys/Evergreen Notes]]) that I've been talking about with [[Andy Matuschak]]

        - "Index" as larger discourse [[context]] for conversation

            - but i think our stuff should be more focused: need semantic annotation on the index, not just a navigational aid

            - i think questions/arguments are a good fit for this

        - Local structure with affordances that target a [[dialectic]]

            - I think the original was more progressive summarization?

            - But I really like representing / reifying the insight about the [[dance between the theoretical and the evidential]] right there in the structure of the template
[[February 3rd, 2021]]

- Studies of systematic review practice, where the formality of data structures extracted from literature approximates [[[[PTN]] - discourse graph]], also have a similar phenomenology, with some studies documenting that this step of extracting data from papers feels like being "enslaved to the trapped data" [[@knightEnslavedTrappedData2019]].

    - cc [[[[CLM]] - Effective synthesis is hard]]
[[October 22nd, 2021]]

- [[Joel Chan]] and [[Matthew Akamatsu]] for [[D/Synthesis Infrastructure]]: [[[[PTN]] - discourse graph]]s for experimental science

    - going big! want to partner with [[Allen Institute for Science]] to push for [[std/Micropublication]]s!

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

        - gotta talk to [[Adam Marblestone]] and others about crafting a focused proposal/project around this: create (infrastructure for) a discourse graph for biology

    - also eager to use [[[[ART]] - [[D/Synthesis Infrastructure]] Roam discourse graph extension]] for own lab

        - easy sell for supporting:

            - writing intro

            - mini lit reviews to choose next experiment

            - parameters for simulations/models

        - want to experiment with this!

        - [[Allen Institute for Science]] and others probably would be excited about this as well, along with folks in his department at [[University of Washington]]

    - Matt's notes here: https://roamresearch.com/#/app/teamcovid/page/8hevJKhTu
[[November 6th, 2020]]

- We propose to develop a **data model** ([*]([[[[PTN]] - discourse graph]])) to test that can be instantiated in various systems

    - We test in [[sys/RoamResearch]], and also explore generalization to another system set up

    - We draw on [[CSCW]] theories of [[reuse]] and [[[[PTN]] - boundary object]]s, and conceptual models of scholarly argumentation
[[April 6th, 2021]]

- Reflections on getting [[Tammie Nelson]] set up for a protoype lit review in Roam (cc [[[[PTN]] - discourse graph]]):

    - Finally clicked at two points:

        - First, Tammie said she was having trouble seeing how it all fit together (after we had imported a bunch of stuff and started working through the annotated bib). Clicked when I explained it as three buckets of documents (each can be thought of as Google Docs with more bells and whistles):

            - This framing lowers the barrier to entry, can map more easily to existing practices and tooling

                - More advanced stuff like daily notes pages, indices, may not be worth it at this point

            - The buckets

                1. __What to read and why?__ --> `annotatedbib`

                1. __What do the sources actually say?__ --> `references` pages (one per source)

                1. __What does it all mean for my questions?__ --> `question` pages

        - Second, when we did a worked example of what might go in the question page, and how it would relate to the reference pages, and I said "you can then refer to something more specific/granular than the whole paper", and this was the visible/audible aha moment.

            - #example-of [[[[CLM]] - Compression is necessary for synthesis]]

    - More generally, I'm thinking... it's time to get serious about tending to the garden. Some changes/friction points:

        - There is more to literature notes than observation notes. I/people "don't know what to do" with other stuff, like theories, assertions, and so on.

        - I need far, far, far fewer zettels.

        - I still don't feel like I have a good place to develop things over time
[[October 15th, 2021]]

- Re: denoting "epistemic status" or "credence" for claims in a [[[[PTN]] - discourse graph]]

    - Because [[[[CLM]] - Diversity in epistemology and methodology is critical for scientific progress]], we don't want to make a universal ontology of epistemic status, because that would require epistemic homogeneity

        - CC [[[[EVD]] - assuming that there is a polynomial-time procedure for choosing solutions for an intractable function implies that P=NP - [[@vanrooijIntractabilityUseHeuristics2012]]]]

        - CC [[[[CLM]] - Universal Semantic Webs are neither feasible nor useful]]

        - CC [[[[CLM]] - Context is necessary for reasoning under uncertainty]]

        - CC [[[[QUE]] - How can we support explicit contention with evidence when synthesizing knowledge claims?]]

    - This connects with things I've been wrestling with, as well as ideas from [[Maarten van Doorn]]

    - Related: [[Barath Raghavan]] mentioned this blog post by [[Terrence Tao]] that [[Wei-Wei Chi]] had [previously mentioned]([[Terrence Tao]] talks about the "three phases" of mathematics from) -> [[postrigorous and meta-rational]]

        - There’s more to mathematics than rigour and proofs | What's new: https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/

            - The core idea of stages, from pre-rigorous to rigorous to post-rigorous, was really evocative, reminiscent of our previous discussions about connections to [[David Chapman]]'s ideas around [[meta-rationality]] and [[Robert Kegan]]'s stages of human development - Barath finds this helpful for framing how to advise students at different stages

                - A bridge to meta-rationality vs. civilizational collapse | Meta-rationality: https://metarationality.com/stem-fluidity-bridge

        - Idea of "leap first, then backfill later to refine" from post-rigorous stage is particularly relevant to thinking about how to structure the process for [[outline/[[D/Synthesis Infrastructure]] [[NSF Germination program]] proposal]]

            - This also connects to important thoughts from my visit to [[CMU HCII]] about [how discourse graphs connect with abduction](Really hitting the theme of how important it is to have the informal live alongside the formal: asked about [[abduction]], and where that lives in here - my sense is that [[[[PTN]] - discourse graph]] don't represent abduction, but support it (by having something to talk back to); similar to [[Chinmay Kulkarni]]'s question about speculation)

            - I think this means we really need to generate ideas in the first phase. And use those to frame the analysis / "backfilling" - that is how we prioritize. And we don't search for disagreements for disagreements' sake. We look for complementarity and surprise!

                - Cross-disciplinarity and peers expand the diversity of the first phase, and also expand the depth of the second phase

            - Remind me also of [[@bergPrimalMarkHow2014]]: fun paper on anchoring of novelty vs. feasibility (authors use the weird language of "primal mark", but the idea is in anchoring/priming).

                - TL;DR, it was harder to increase novelty (and therefore lower ceiling on creativity) if we anchored in feasibility and infused with novelty later, than it was to start with novelty, then infuse feasibility later. reminds me very much of the pattern of intuitive leaps first, then backfilling later with more analytic thinking. #[[➰ breadcrumbs]]

    - Humorous example of the ridiculousness of universal ontologies: [[Celestial Emporium of Benevolent Knowledge]]: https://en.wikipedia.org/wiki/Celestial_Emporium_of_Benevolent_Knowledge
[[February 23rd, 2021]]

- What might it cost over the long-term to create and maintain "aggregators" of individual, local-first [[[[PTN]] - discourse graph]]?

    - "Where" might the infrastructure need to be?

        - One pointer: [[sys/Ceramic]] https://github.com/ceramicnetwork/ceramic/

            - Contact for this is [[Danny Zuckerman]], met from [[org/Ink and Switch]] talk

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkNJw2oF3lv.png?alt=media&token=a69eb7a7-44f7-4e0e-b11c-bb09ead112cc)

            - One click push to the Ceramic-powered blockchain?

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FTGyWSwD71f.png?alt=media&token=82763f86-3510-4197-b478-426eb8ffcd34)
[[April 8th, 2021]]

- with [[Beau Haan]] re: democratizing [[[[PTN]] - discourse graph]] and [[sys/Zettelkasten]] in [[sys/RoamResearch]]

    - what is a zettelkasten (for)???

        - conversation partner [[Niklas Luhmann]]

    - reflections:

        - three problems (and solutions) in adapting the zettelkasten to [[synthesis]]:

            1. where do `observation notes` fit in, in the tripod?

                1. option 1: reference notes, since they're reference material

                    1. but that's not quite right. what role does the `literature note` play then?

                1. option 2: special case of `literature note`

                    1. so everything that someone else is saying goes into literature notes, and synthesis notes are only things that i'm willing to claim and build on. i like that!

                    1. i think this is the thing to try out

                        1. one open q to keep in mind: is it bad that these observation notes aren't going to live in the reference page? should they?

                    1. this also solves my problem of [how to deal with notes from sources that... aren't literature notes](There is more to literature notes than observation notes. I/people "don't know what to do" with other stuff, like theories, assertions, and so on.).

                    1. context snippets go in reference notes, can block ref in.

                1. really need them for [[synthesis]]

            1. can't develop permanent notes from a single source. too risky. but want them to stick around for development!

                1. possible solution: intermediary notes (idea from [[Sönke Ahrens]]), but with exact same tripod structure

                    1. when ready, create new permanent note to add to zettelkasten, but build from intermediary note as reference, to preserve the linkage and provenance

                1. i like this a lot. keeps me from "[polluting](I need far, far, far fewer zettels.)" the central index unknowingly. everything in there should be [reasonably mature](((BS6GNRQFt))), and robustly challengable.

                1. i can now move all of my zettels to intermediary notes and start fresh.

            1. how to trace citations for when i'm writing?

                1. easy: each citation is a `reference notes` entry in the tripod

                1. if i really want to, i can crystallize a summary, maybe for different audiences, of a permanent/synthesis note in the body of hte page.

        - `fleeting notes` are essential, 1-to-1 relationship with a literature note: it's where the [[context]] from the note-writer comes in. crucial.

            - experienced the lack of this when others wrote the observation notes. why did they think it was important? in what way did they think it informed the question? where is the uncertainty, the appraisal?

            - also creates more "surface area" for the note to intermingle and converse with other ideas, creating more opportunities for synergy and serendipity

        - distinction between claims and `observation notes` again not obvious. resonated when explained in terms of two things that science articles "say": claims, and evidence/data.

            - need to keep the evidence distillations around, to be able to lay them out and feed the synthesis. can't just rely on memory or glancing at a table/screenshot/snippet only.

        - i think these will work for me, and if we can converge on this shared structure across a bunch of researchers, we can start experimenting with cross-graph sharing.

        - i am a bit worried, though, that the zettelkasten might still be too much overhead to adopt, too different from familiar academic practices.

            - to mitigate this, value proposition needs to be STRONG. clear and compelling.

                - establish this with early adopters first.

            - the structure is also simple, simple enough to be adopted by a wide range of users

            - not sure how I would do something [like what I did with Tammie](First, Tammie said she was having trouble seeing how it all fit together (after we had imported a bunch of stuff and started working through the annotated bib). Clicked when I explained it as three buckets of documents (each can be thought of as Google Docs with more bells and whistles):) in terms of simplication

    - recording:

        - {{[[video]]: https://www.youtube.com/watch?v=Xta7bv3KzkI}}
[[September 10th, 2020]]

- Scratch thoughts on [[[[PTN]] - discourse graph]]

    - [[sys/Hypothes.is]] is... kind of buggy.

        - URL for each annotation doesn't work for sharing unless the file is publicly hosted

        - Even then it doesn't go right to the spot in the PDF automatically

    - Similar to [[sys/Obsidian]], can use headers as parts of claims to link together?

        - https://developers.google.com/docs/api/reference/rest/v1/Header
[[December 8th, 2020]]

- Made substantial progress on the [draft writeup](https://oasislab.pubpub.org/pub/54t0y9mk/draft) for [[[[PTN]] - discourse graph]], should be ready to share by tomorrow, I think, with just a little more tweaking

    - Next step is to write up some brief examples for motivation around [[context]]

        - The children under vs. 10yo is a good one

        - Examples from my dissertation

        - Any others?

        - Saying something is not possible but it's contextualized

    - Sketches in today's entry in OneNote

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FqZ20GJ2K1A.png?alt=media&token=a5b68a65-0dc8-4796-a24d-3db0c5fd6dcc)
[[August 28th, 2021]]

- Permissionless is an emphasis of [[org/Protocol Labs]] - does this get towards openness? no need to gate. this resonates. with [[D/Synthesis Infrastructure]], i want to build an open and sustainable infrastructure for sharing humanity's knowledge, specifically around claims and evidence in a distributed and decentralized [[[[PTN]] - discourse graph]] - i want this to remain robust, so [[content-based addressing]] and [[Web3]], a la [[sys/IPFS]] is a big plus.

    - see also [[self-sovereign identity]]: https://www.windley.com/archives/2021/08/ephemeral_relationships.shtml (h/t [[Ward Cunningham]] on Twitter)

        - connects back to something that [[Geoffrey Litt]] mentioned in a talk (also floated around [[org/Ink and Switch]] Discord): https://0data.app/en

    - Protocol Labs is also an ideal lab to shepherd the development of [[interoperability]] (see this [recent evocative piece](https://subconscious.substack.com/p/composability-with-other-tools) by [[Gordon Brander]] on this, connecting back again to [[Geoffrey Litt]]), through a shared protocol that allows people to participate in the distributed, decentralized stream but with "bring your own app"
[[January 7th, 2022]]

- discuss problem: [[[[QUE]] - How can we best bridge private vs. public knowledge?]] re: [[[[PTN]] - discourse graph]]

    - metaphors and interaction patterns

    - subproblems:

        - rich history and context in personal notes, but frequently unnavigable to someone else: how to make dense personal context of notes available and navigable to someone else?

            - while respecting [privacy]([[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]])?

        - how to support reasoning about and mashing together of federated discourse graphs?

    - how would you start attacking this problem? what does this make you think of?

        - strategic intelligence graph from world economic forum: https://intelligence.weforum.org/

        - translational design

        - will this transform scholarly communication?
[[February 3rd, 2021]]

- The rich [[[[context]]ualizability]], too, of [[[[PTN]] - discourse graph]] should facilitate the deep engagement with context that is necessary to make sense of and appropriately and creatively integrate \artifact{} elements into your ongoing synthesis.

    - Thus, knowledge representations that are lossy with respect to context should be especially difficult to reuse across knowledge boundaries.

    - Here, as with compression and exploration, the benefits of contextualizability might be especially pronounced when crossing boundaries. Used in this way, [[[[PTN]] - discourse graph]] can be conceptualized as [[[[PTN]] - boundary object]]s, which are optimally weakly structured in common use (at the boundaries), but need to be strongly structured, with context added, for example, to be useful across boundaries.
[[➰ breadcrumbs]]

- important point here about the relationship between [[[[PTN]] - discourse graph]] and [[knowledge graph]]s: one might say that in the majority of instances, discourse determines entity resolution (resolving references for names). in some ways, that comes before any a priori attempt to define names in a vacuum (outside usage). so discourse graphs might be the more general architecture, with all of its useful [[ambiguity]], within which we can integrate formal knowledge graphs for specific applications, as appropriate.

    - this reminds me of the usefulness of [[[[PTN]] - boundary object]]s as connective tissue between disparate worlds: ill-structured in common use, strongly structured in local use

        - wrote about this on [[January 25th, 2021]]: To connect back to [[[[PTN]] - boundary object]]s, [[knowledge graph]]s with atomic concepts as nodes feels closer to classical formal [[ontologies]], which make strong assumptions about what should be in/out of the model. This is a SPECIAL CASE of reality! THE MODAL case is ambiguity and variation: it is perhaps for this reason that (effective) [[[[PTN]] - boundary object]]s are weakly structured in common use, and only strongly structured in local use
[[July 9th, 2021]]

- Connecting it to [[[[PTN]] - discourse graph]], we might formally model assumptions as `claims` with some pattern of properties:

    - "deep" in an argument chain, where if removed, large edit distance from current state

    - controversial or lower evidentiary support/coherence than warranted by distance
[[March 16th, 2021]]

- Reflecting more on process model for [[[[PTN]] - discourse graph]] x [[Beau Haan]]'s implementation x [[theoretically grounded workflow for synthesis]] / [[Z: Paths and workflows towards synthesis]]

    - Three primitives for writing sessions in Roam

        1. What's fun is that each of these could define new events to "watch" for in a [[roam/inter]] scenario (cc [[Stian Håklev]])

    - There's also ^^**writing-synthesis-argumentation**^^, but this isn't really a writing "microtask" - it sort of sits over everything

        - **when:** whenever! ongoing. but works best once there is critical mass of distilled synthesis notes to work off of. functions as another form of indexing and "weaving together" of key notes

        - **input**: everything!

        - **output**: proto-drafts and outlines to be used

            - design argument is one example

    - Can discuss with [[Lisa-Marie Cabrelli]]
[[February 16th, 2021]]

- Information model: [[[[PTN]] - discourse graph]]

    - Critical design move: from paper-centric to
[[August 4th, 2020]]

- [[[[PTN]] - discourse graph]] seems to resonate

    - be careful about the dragons when crossing from 1 group to another; sharing within a group probably acceptable risk; maybeeeeeeeee sharing to another closely related group, say, int he same dept, but might want to scope out that risk entirely from the grant

    - in the [[epistemic synthesis layer]], definitely lean into the diversity, not just a google docs add-on but also consider at least one or two more alternative representations, like a google spreadsheet or canvas, depending on what scholars are already doing;

        - key strength of integrating into a [[sys/Hypothes.is]] or other existing [[standards]] is the ability to have it end up in different "endpoints"
[[October 30th, 2020]]

- More intuition behind vision for [[D/Synthesis Infrastructure]] and the [[[[PTN]] - discourse graph]]

    - The graph isn't meant to be an "authoritative" source that we can do automated reasoning over, but rather a better source of *entry points* and *raw materials* that a human will still need to process. The difference is that this "processing" is no longer an extrinsic overhead task (e.g., fixing classification errors, formalizing things for some distant future), but the primary task of [[synthesis]] and [[🧱 sensemaking]]!
[[February 3rd, 2021]]

- This is mainly because creating [[[[PTN]] - discourse graph]] is likely to be quite effortful, with a lower bound on cost.

    - Finally, studies of reuse in other settings suggests that [[[[CLM]] - Specifying context for future reuse is costly]],  in part because [[[[CLM]] - Specifying context for future reuse requires predicting trajectories of future reuse]], and [[[[CL]] - Predicting trajectories of future reuse of information objects is hard]] [[@ackermanOrganizationalMemoryObjects2004]], [[@andersonDataBaseMent2008]].

    - Research on sensemaking, for example, suggests that [imposing a schema on an unstructured collection of documents/materials is a major cost of sensemaking](They find that, for the cases they study, extracting data is the most costly step for [[🧱 sensemaking]] (p.273). ) [[@russellCostStructureSensemaking1993]]. #[[Z]]

    - Studies of systematic review practice, where the formality of data structures extracted from literature approximates [[[[PTN]] - discourse graph]], also have a similar phenomenology, with some studies documenting that this step of extracting data from papers feels like being "enslaved to the trapped data" [[@knightEnslavedTrappedData2019]].

        - cc [[[[CLM]] - Effective synthesis is hard]]
[[December 19th, 2020]]

- Draft discussion of [[[[PTN]] - discourse graph]] with [[Rob Haisfield]]

    - {{[[youtube]]: https://www.youtube.com/watch?v=JoCjpTXCklw&feature=youtu.be}}

        - Timestamps

            - 4:07 Brief intro about myself

            - 8:37 On the benefits and challenges of user freedom in Roam

            - 10:25 Background on the synthesis model and goals of the chat

            - 12:10 Motivation for the model and document

            - 14:32 What is synthesis?

            - 16:55 Synthesis for decision-making and design

            - 21:49 A concrete example of synthesis using the model in Roam from my own work

            - 28:16 The conceptual model of synthesis behind this concrete example: overview, focusing more on synthesis notes and observation notes

            - 32:48 Sidebar: Being disciplined about distinctions between observation and synthesis notes, and retaining context, enables principled creativity (questioning of past knowledge)

            - 35:35 Back to the model: varieties of sources and observation notes, and the question note entity

            - 39:40 Concrete examples of question notes

            - 48:32 Sidebar: Indentation and querying in Roam

            - 53:56 Drafting a new synthesis note

            - 55:13 Why it's useful to have a synthesis note as a page vs. a block (the pattern of the "writing inbox" via linked references)

            - 56:58 Back to the model: context snippets

            - 1:00:00 Model implementation in Roam: Why write observation notes as blocks instead of pages?

            - 1:01:39 Opportunities for improvement (e.g., with automation, Smartblocks), tradeoffs with desirable difficulty

            - 1:06:03 Where is "speculation" in the model? Returning to the pattern of the writing inbox

            - 1:11:17 Model implementation in Roam: Advantages and disadvantages of page vs. block references

            - 1:16:40 Back to the model: the process of synthesis

            - 1:18:56 Using the model to support long-term reuse and collective intelligence

            - 1:23:23 Differentiating principles vs. implementation of the model

            - 1:30:53 Using the model to support long-term development of ideas

            - 1:02 Goals of the conversation

            - 1:32:35 Wrap-up / closing thoughts
[[January 8th, 2021]]

- we discussed some baseline designs to compare against [[[[PTN]] - discourse graph]] for interacting with heterogenous evidence collections (again, I think core problem is [tradeoff between context and compression]([[[[CLM]] - Compression and contextualizability are in tension]]))

    - high degree of [[compression]] that is lossy:

    - [[What Works ClearingHouse]] quant-focused, similar to [[Cochrane systematic reviews]] in terms of focusing on "scoring" quality of evidence: https://ies.ed.gov/ncee/wwc/Intervention/752

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0CBlfS_Vhk.png?alt=media&token=d159adc1-46a9-4872-a3ed-1ad3e20c77a5)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F26G7d_9_oJ.png?alt=media&token=f7aa909b-adc4-45f3-8877-dd08539cc84f)

        - Not totally lossy compression, since there is a link to an intervention report, which discusses the rationale behind (cf. [[outline/2020-10 - supporting explicit reasoning over evidence context for claims (ASIST workshop)]]): https://ies.ed.gov/ncee/wwc/Docs/InterventionReports/wwc_firststep_030612.pdf

    - [[org/LearnLab]] maintains a [[sys/Wiki]] focused on ideas around robust learning: https://learnlab.org/research/wiki/Main_Page - here the emphasis is less on evidence contention, and more on theoretical [[synthesis]] - references are cited in the usual way, so compression is quite lossy, although context is high in the sense of significance (since it's a kind of [[hypertext notebooks]])

    - [[Erik Harpstead]] made a "card deck" of learning science principles that is beautiful and very usable, but totally lossy in terms of [[compression]]

        - https://eharpste.github.io/interactive-principles/#/

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMdsFCEzKk_.png?alt=media&token=80484565-4b04-48ef-9608-7e01cc6b5a30)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FvitSRql8hN.png?alt=media&token=42f31e77-c12f-432c-bfd9-0b2a9bd21313)

        - since compression is totally lossy, you basically have to trust the source completely, both in terms of authorship, and timeliness
[[December 18th, 2020]]

- An update to the [[[[PTN]] - discourse graph]] (changing name from two layer to multi-layer :))

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUnIXnxGI3c.png?alt=media&token=82f5cfed-4466-4bb5-b1dd-0a8add393c18)

    - h/t [[Rob Haisfield]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FWx-Wl4b6PN.png?alt=media&token=fe2e2b94-a67a-44be-9a8a-32b088fa551a)

        - makes sense to me, and i think also highlights an evolution point from the original zettelkasten / evergreen note model that feels too... complete/polished to me?

        - also makes research questions a first-class object, which makes total sense from a creative knowledge work and research project perspective

            - probably a project starts with a high-level question (which is likely shared with other projects), then drills down through a set of synthesis notes to form an argument for a new research question that needs to be answered

            - mapping back to [[study design design process]] and [[Heilmeier Catechism]], the "however" points in the arguments would correspond to synthesis notes that are much more tentative

        - #fieldnotes for [[P/PO study/dev for synthesis infrastructures]]
[[February 7th, 2021]]

- Proposed solution 1: [[[[PTN]] - discourse graph]] as underlying [[infrastructure]]

    - Problem: sustainability

    - I'm Trying to transform this problem: [[scholar-powered model of semantic publishing]]

        - Make your own discourse graph, using [[hypertext notebooks]]

            - Example: [[Z: Improving B6 status increases immunocompetence in the elderly]]

        - Figure out a way to [federate]([[federation]]) or share them
[[April 22nd, 2022]]

- wondering about how to model "explains" (e.g., this theory explains this evidence) in terms of [[[[PTN]] - discourse graph]]s. it's a really rich and information dense move. this happens because... that would explain why...

    - [[@simonWhatExplanationBehavior1992]]

    - [[@vanrooijTheoryTestHow2021]]

    - digging into the philosophy of this more... https://plato.stanford.edu/archives/spr2009/entries/scientific-explanation/

        - it's friggin complicated man!!!

        - so many diff. models, none are fully satisfactory

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FoWo19EXcWn.png?alt=media&token=97b76076-38f9-4db9-804b-7829938c828f)

        - lots of auxiliary things that need to be in place to model this, which may be hidden or implicit

        - this goes back to our motivation to ground this in [[[[PTN]] - boundary object]]s

        - without access to these pieces, it's... unacceptably lossy to compress things down to the more precise view

        - we *could* model it in principle, i think, using a graph of propositions, but my intuition is that it would be ridiculously unwieldy. what we want instead i think is a way to **bridge** the intermediate discourse representation to more sophisticated formalisms, like tables (we do this), and syllogisms, and computational formal models (mathematical, programming), and knowledge graphs

        - may not even be possible or desirable to have a "explains" relation that works across diff. disciplines and ways of knowing! cc [[epistemological diversity]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FXy-lK03ssw.png?alt=media&token=b5b2e347-a170-40b7-9907-a8ce048b8fd1)

        - our driving goal is to facilitate [[synthesis]]: both across disciplines, but also within disciplines, across diverse sorts of evidence.
[[January 15th, 2021]]

- Let's do some reflection on the main points of feedback on [[@chanKnowledgeSynthesisConceptual2020]] / [[[[PTN]] - discourse graph]] so far, in somewhat decreasing order of salience/importance:

    - `questions` as a central organizing principle really really resonate

        - For [[Joel Anderson]], they are a good candidate for setting the necessary [[context]] for [[idea: multiplayer zettelkastens]]

            - see also: [[idea: zettelconversations]]

            - questions as fundamental bridging/organizing principles

        - [[Brandon Toner]]: helping to close some loops, like the emphasis on questions as first-class citizens

            - ○ https://twitter.com/brandontoner/status/1343586366995787778

            - ○ https://twitter.com/brandontoner/status/1344149286146207744

            - https://twitter.com/brandontoner/status/1344031373422718976

            - https://twitter.com/brandontoner/status/1349521718268854277

        - [[Nikki Huang]]:

        - [[Sönke Ahrens]] also [finds it useful](important to re-emphasize structure/hierarchy, not jettison it (might have overshot in book)) to think about it as a helpful "top-down" organizing principle or "index" as a balance to bottom-up, horizontal linking without hierarchy

    - how does this play out against "speculation"? where do "`fleeting notes`" go? how to develop over time in in the "real mess"?

        - [[Jason Griffing]] calls it "hunches"

            - https://twitter.com/jasongriffing/status/1348100386301775873

        - [[Rob Haisfield]] calls it "speculation"

            - https://twitter.com/JoelChan86/status/1348134623604318209

    - how does this play against "concepts"?

        - currently "missing" from the model, but might be the primary object in some lines of work, like philosophy (could also see this being the case for lots of sociotech work, like [[[[PTN]] - boundary object]])

        - [[Joel Anderson]] in his work on philosophy, focus on development of concepts

    - how might this work in settings with less emphasis on observation notes, such as philosophy? is it appropriate?

        - [[Sönke Ahrens]] isn't sure that the [[[[PTN]] - discourse graph]] would quite work for philosophical work (much less emphasis on observation notes)

    - takes time!

    - these are #fieldnotes for [[P/PO study/dev for synthesis infrastructures]]
[[February 5th, 2022]]

- connect CFT and [[hypertext notebooks]] with [[Cedric Chin]] obv with why a [[[[PTN]] - discourse graph]] might be personally useful, but also… the richness and privacy of concrete cases, for [[[[THE]] - interaction-oriented theory of creative inspiration from examples]]: a design pattern for (re)contextualizing for (re)modeling

    - readinglist: https://www.dropbox.com/sh/3wqb9t6lkb4k7hv/AABuyCg6LsI8c5r9tll1HpGba?dl=0

        - update: https://docs.google.com/document/d/1Q6LQlNmG0hEL44Oz0EJsYN9hWp0I0xIy0IqdQifi2ng/edit#heading=h.yey3aqibvijy
[[May 30th, 2021]]

- Galling #example-of why we need [[[[PTN]] - discourse graph]]!!!!!!

    - Result: significant association between genetic disposition to earlier sleep/rising and lower risk of depression

        - "Genetically proxied earlier diurnal preference was associated with a 23% lower risk of depression (odds ratio [OR] per 1-hour earlier sleep midpoint, 0.77 [95% CI, 0.63-0.94]; P = .01)."

        - The sleep timing measures were meant to contextualize the genetic variation!!!

    - Interpretation/theory: if you sleep earlier (REGARDLESS OF YOUR GENETICS), you might lower your risk of depression...?????
[[November 6th, 2020]]

- [[Katrina Fenlon]] highlights a good point of uncertainty about the [[[[PTN]] - discourse graph]]

    - some ontologies do make typed distinctions between entities/nodes (e.g., [[std/Micropublication]]s), but some do not
[[December 8th, 2020]]

- As I'm processing micropubs for [[@cattaniDeconstructingOutsiderPuzzle2017]], I'm noticing an [[ethnographic sneeze]] re: the distinction between micropubs and synthesis notes in [[[[PTN]] - discourse graph]]

    - For historical case studies, and claims of a historical nature, the synthesis notes are often already in the past tense, and do not necessarily need to be generalized. But yet I think they are still synthesis notes... is it the causal nature of those claims?

    - Here's the example:

        - Synthesis-like (though in past tense): George Graham and the Royal Society played an important role in legitimizing the outsider innovation of John Harrison.

        - Probably a better micropub (or component micropubs) that are less causal/inferential and more observational:

            - John Harrison progressed towards legitimacy more quickly after encountering George Graham and the Royal Society

            - The Royal Society wrote a

            - The Royal Society provided resources to [[John Harrison]] to start working on his initial prototype

            - The Royal Society supported [[John Harrison]]'s proposal to do a field trial of his initial prototype (H1) on the HMS __Centurion__

        - And other related micropubs:

            - Approximately 1/3 of Royal Society fellows in its early days were scientists, with the rest made up various "curious minds"

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FiDqb_jVUrQ.png?alt=media&token=ac02294c-ed5f-4dd4-b828-f2f44eba9bfa) (p. 974)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FywVWV7Gg6y.png?alt=media&token=8655b859-bf3f-4962-a240-63dc1dd11c20) (p. 975)

            - Thomas Hobbes ridiculed the experimentalists in the Royal Society by comparing them to "quacks", "mechanics", and "workmen"

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FSh9-DBAxA7.png?alt=media&token=39981c86-644f-4718-8184-cd5482ebe516)

    - This cannot be a hard distinction, however, since [[Z: Observation is theory-laden]].

        - It might seem obvious if we directly observed him inventing it: but what about counterclaims from others who had similar ideas at the same time? Invention is too complex a process to observe directly, and it also inherently a socially constructed judgment.

            - This is true to a certain extent even of seemingly "obvious" things like instrument readings. But arguably to a lesser extent.

            - More synthesis-note-like

                - Thomas Edison is the inventor of the lightbulb

                    - "inventor of" is a more fraught, socially constructed judgment that requires lots of backing statements (observation notes)

            - More observation-note-like:

                - Thomas Edison made a lightbulb

                - Society X formally credited Thomas Edison with the invention of the lightbulb

        - So the distinction here should be primarily **pragmatic**, not ontological.

            - When to distinguish synthesis notes and observation notes is guided pragmatically, by the extent to which distinctions help push you towards a richer and more effective [[synthesis]].

            - This means that one person's synthesis note might be another's observation note.

            - Or an observation note might be questioned as the field progresses and then "unpacked" (e.g. by being problematized) into a synthesis note

                - What to do then with the observation notes, and the web of connections it is a part of?

                    - Suspect we don't want to be too rigid about this.

        - Even something that seems "factual" like "Thomas Edison invented the lightbulb" can be contentious!

    - What to do with this then?

        - If your [[synthesis]] depends critically on particular ideas (they are core to your argument or model), then you want to tend towards preserving as much [[context]] as possible, which means not "hiding" potentially contentious ideas or claims as observation notes

        - For other ideas that may be less core, you can probably afford to make less fine distinctions.

            - Hopefully this is ok because of these fallbacks:

                - But also: hopefully what you gloss over, others might need to make fine distinctions because it is central to their argument or synthesis, and you can retrieve them from the P2P commons

                - Your observation notes are also never lossily compressed, because they are at least minimally tied to a context snippet, that allows you to start [[recontextualization]] if you need to make finer distinctions later
[[March 1st, 2021]]

- Maybe what we need is not "friction" for moving between spaces (e.g., thinking spots, but also "[note types]([[[[PTN]] - discourse graph]])"), but simply a boundary between the spaces, such that it is clear when you are moving from one to the other.

    - cf. our musings about [[desirable difficulty]] in [[@qianOpeningBlackBox2020]] and other places

    - Sparked by this thread on the [[org/Ink and Switch]] server on the idea of "[[all fork and no merge]]" (seems like a variant deficiency in opposition to [[dance between the theoretical and the evidential]]):

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FIM24ZtXEYu.png?alt=media&token=c68103bb-6c50-4293-b067-d349037630c7)
[[November 22nd, 2021]]

- Choice of data structure: base grammar of [[[[PTN]] - discourse graph]] that is extendable (^^++ fundamental technical contribution^^)

    - Inspired by [[[[PTN]] - boundary object]]s
[[February 8th, 2022]]

- Quick sketch of a plan for multiplayer test of [[[[PTN]] - discourse graph]]s - [[[[EXP]] - [[D/Synthesis Infrastructure]] - Roam Journal Club pilot]]: cc [[Jason Ding]]

    - We will run a series of pilots where people will be individually creating discourse graph notes on a shared reading list over a set period of time, and exchanging/interacting these notes with others in the same group.

        - Each week, rather than each person presenting the paper verbally only or with slides, they share and talk about the discourse graph notes they took, which will be in a shared graph. Then, others can use / build on these notes, through discussion or writing (synthesis) prompts.

        - Roughly, it will run for 4-5 weeks, like a journal club, but where readings are more tightly connected around a central set of questions.

    - We want to understand:

        - **Utility / preconditions for successful sharing**: Under what conditions discourse graph notes are intelligible and/or useful to others: e.g., what types of notes, for what purposes, with what modifications, etc.

        - **Privacy/utility tradeoffs and tensions**: Under what conditions might people want to bring in their own notes into a shared space, how much of their own notes would they want to share with others, how might this conflict with the context that is needed to really make use of others' discourse graph notes.

    - I think a diary study deployed over the course of the pilot might make a lot of sense, as a complement to semi-structured interviews and participatory observation!
[[November 17th, 2020]]

- Always find it helpful to start in Daily Notes :) I'm wanting to work on fleshing out the [[[[PTN]] - discourse graph]]. If I like it enough, I'll transfer to the note itself.

    - Come back to this [[November 18th, 2020]]
[[May 18th, 2021]]

- Realllllllly important #example-of the need for [[context]] and the need for [[[[PTN]] - discourse graph]]

    - [[@molteni60YearOldScientificScrewup]]: Title: The 60-Year-Old Scientific Screwup That Helped Covid Kill

        - this is about how we got to the misunderstanding about the 5 micron rule for aerosols and the resistance to recognizing that COVID is airborne, because of [bad citation practices]([[[[CLM]] - Citation practices in science are far from optimal]]) and dogma

            - related: [[@clausetDatadrivenPredictionsScience2017]] has lots of important notes about this
[[November 15th, 2020]]

- Stray thought: for [[[[PTN]] - discourse graph]], it's important to specify that the "claims" layer really admits far more than simply assertions.

    - Per my sense of [[Z: Paths and workflows towards synthesis]], we have questions, zettels, maybe even outlines, drawing richly from [[sys/Zettelkasten]], and also [[@harsDesigningScientificKnowledge2001]] [ideas about different "atoms" in scholarly argumentation and discourse](Four [[Positivist]] epistemological models of scientific knowledge from philosophy of science [[@popperLogicScientificDiscovery1959]] [[@nagelStructureScienceProblems1979]] [[@dubinTheoryBuilding1978]] [[@bungePhilosophyScience1998]] agree that scientists build __theories__ as systems of scientific __statements__, which are composed of relationships between __concepts__ (p. 70) #[[📝 lit-notes]] #Atomicity #compositionality)
[[May 20th, 2021]]

- of special interest to [[[[PTN]] - discourse graph]] - the machine-readable hypothesis could easily become

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft7feByzYV9.png?alt=media&token=494ce55e-1db9-4c0e-99eb-608bca839646)
[[November 3rd, 2020]]

- framed in this way, both [[analogy]] and our [[[[PTN]] - discourse graph]] stuff can be seen as quite distinct from "raw materials" (in the sense of being raw inputs into some combination process), and more as [[[[PTN]] - boundary object]]s that facilitate coordination and collaboration for [interdisciplinary]([[interdisciplinarity]]) work

    - this implies a quite expansive view of "how do we measure success", beyond the scope of an individual writing session or project, even, but examining broader impacts on navigating the network, professional identity and emotion, and so on

        - [[@palmerWorkBoundariesScience2001]]'s concept of [[leeway]] helps us see the broader picture
[[April 29th, 2021]]

- [[ethnographic sneeze]]s for [[[[PTN]] - discourse graph]] as I chip away at {{[[DONE]]}} [[Joel Chan]] Get to ~10-20 papers each that support/oppose children < adults #next

    - why are these questions important?

        - thinking about [how to organize reading](how to organize reading/processing? makes sense to have some kind of strategy i think?) has implications for [[context queries]]

        - specifying [links](how to formally specify discourse graph links between objects?) and "[keeping track](((vYAhUPzml)))" are important for thinking through mechanics of retrieving/finding (which is hypothesized to be better than just searching over papers... right???)

        - these all become especially important at scale... even once you get past low 10s!

    - questions

        - how to formally specify discourse graph links between objects?

            - obs --> question

                - options:

                    - manually ref into annotated bib

                    - indent under obs note as attribute

                    - manually ref into question page

            - obs --> synthesis note

                - difficulty: synthesis notes not always known ahead of time; actually, in cases where we most want to do synthesis, they are rarely known ahead of time

                - options:

                    - manually ref into synthesis note page

                    - indent under page ref in question page

            - synthesis note --> question note seems... easier

            - this might be a case where yaml  or some kind of semantic relational markup (e.g., attributes) is needed, and roam doesn't currently have hte right firepower for

        - how to "keep track of" observation notes?

            - keep track of the ones that exist

            - but also usage: how do i ensure i've "used" it in my synthesis?

                - feel like disciplined use of block refs might do it, but...

        - how to organize reading/processing? makes sense to have some kind of strategy i think?

            - rough first by "type" of study

                - e.g., epi, sero, case, contact tracing, modeling

            - then by various contexts to explore why

                - e.g., for covid and children: region, time in pandemic, mitigation

            - then by "evidence strength" - what does our "best evidence" say?
[[➰ breadcrumbs]]

- Keep digging into this thread, building out micropubs and zettels for [[D/Computational Analogy]], and external pressure to add to [[threadapalooza2020]], but also lay stronger foundation for students and others (while also prototyping [[[[PTN]] - discourse graph]] more concretely) [[[[interval]]:48.4]] [[[[factor]]:2.20]] [[May 13th, 2021]]

    - picking up thread again on [[@janssonDesignFixation1991]]'s [scite thread](((PwrlO3c1f)))

    - Investigating the Effect of Mental Set on Insight Problem Solving - [[[scite report]]]: https://scite.ai/reports/investigating-the-effect-of-mental-VdeM4J?mentioning=false&page=1&supporting=false

    - Design fixation - [[[scite report]]]: https://scite.ai/reports/design-fixation-KKjElG?contradicting=true&mentioning=false&page=1&supporting=true&utm_campaign=badge_generic&utm_medium=plugin&utm_source=generic

    - The Impact of Technology on Creativity in Design: An Enhancement? - Bonnardel - 2010 - Creativity and Innovation Management - Wiley Online Library: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1467-8691.2010.00560.x?casa_token=6YvOLBJlNnsAAAAA%3AuTAU1lipMlF4n_jR3kd5uw6Nx8kRD0oI229C5Bre6cDo-SbGxxCSI0bV5vbCIpA1YvpkVrAQ1kje2bik

    - The Impact of Technology on Creativity in Design: An Enhancement? - [[[scite report]]]: https://scite.ai/reports/the-impact-of-technology-on-8rMbeY?contradicting=false&mentioning=false&page=1&supporting=true&utm_campaign=badge_generic&utm_medium=plugin&utm_source=generic

    - The Impact of Type of Examples on Originality: Explaining Fixation and Stimulation Effects - [[[scite report]]]: https://scite.ai/reports/the-impact-of-type-of-QbPKyX?mentioning=false&page=1

    - Inspiration and fixation: Questions, methods, findings, and challenges - [[[scite report]]]: https://scite.ai/reports/inspiration-and-fixation-questions-methods-0RGPG9?contradicting=false&mentioning=true&page=1&supporting=false

    - Methodological diversity and theoretical integration: Research in design fixation as an example of fixation in research design?: https://www.repository.cam.ac.uk/handle/1810/298043
[[roamSOP]]

- ^^observation-note^^ blocks (see [[[[PTN]] - discourse graph]])

    - Contextualized

        - In past tense, with names of authors maybe?

        - Grounded in block references to context snippets
[[March 5th, 2021]]

- [[@[[AJ Rudd Jr]]]] re: [Grudin article]([[~[[Joel Chan]]]] The [Grudin article](https://sci-hub.do/https://www.tandfonline.com/doi/abs/10.1207/s15327051hci0602_3) from the Kujala paper so far isn't a study of any sort. It is just effectively an opinion article about some consequences of not involving users(so far). Is there a special way to do this article because my understanding is that you were looking for more concrete observations. I could totally be wrong just wanted to check before I get into this paper in detail): looks like just opinion, should we write `observation notes` from it? (relevant for developing [[[[PTN]] - discourse graph]])

    - We get to decide!

    - It would at least be useful as a source of possible synthesis notes.

    - But if the author is speaking from some kind of specific, unique experience (e.g., many years of experience running co-design sessions), it could count as an observation note.

    - One clue as to the degree to which this is an `observation note` is the extent to which we can judge something like the following:

        - > this is the basis on which the author is contributing this observation (ideally also how we might reproduce it"

        - This is still a work in progress, but the general direction of the heuristic is sound, I think.

        - In the specific case of this article, let's look at some cues:

            - more insight at the end of the intro for the [question of basis](> this is the basis on which the author is contributing this observation (ideally also how we might reproduce it"): we can think of this solo-authored article as sort of an extended transcript of an interview with a very knowledgeable expert sharing their beliefs

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FhKP-5bqguo.png?alt=media&token=16ddddd7-8db1-4699-9530-9d9d3c69be5d)

            - abstract signals some clues about the [question of basis](> this is the basis on which the author is contributing this observation (ideally also how we might reproduce it"): "examples and logical argument"

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fy0yx8n9Xue.png?alt=media&token=014351eb-c4b6-4050-8ddd-c59d93c9ce14) (from abstract)

                - suspect **logical argument** here is less formal than a. in any case, it's not empirical in a reproducible sense, so that alone wouldn't make the claims observation notes.

                - the **examples** might be observation notes if they are sufficiently richly described

    - Based on [this quick analysis](In the specific case of this article, let's look at some cues:), I think it would be reasonable in this case to make `observation notes` from this paper.
[[outlineDSynthesis Infrastructure - discourse graphs paper]]

- The data model: a [[[[PTN]] - discourse graph]], synthesized from prior efforts, and tested through iterative formative design of the model, separate from a computational system

    - see [[@chanKnowledgeSynthesisConceptual2020]]

    - per [[[[PTN]] - boundary object]]s, meant to strike a balance between the extremes of [too much](Runs afoul of [[[[PTN]] - boundary object]]s, but also [[[[CLM]] - Knowledge is fundamentally contextual]]) and [too little](((i0p-3Ud6n))) structure

    - [[[[PTN]] - flexible compression]]
[[February 24th, 2021]]

- Feeling an [[ethnographic sneeze]] about how to jive the richly [flexibly compressed]([[[[PTN]] - flexible compression]]) of elements of the [[[[PTN]] - discourse graph]] into a shareable format that might go on something like [[sys/Ceramic]]

    - To put it down into words and pictures:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FqAyKkG4F4S.png?alt=media&token=df828843-d940-4f77-aa88-c87daf687a91)

        - Probably the thing that makes the most sense to share is `observation-notes`

            - Reuser sees the bare obs note

            - Can explore "downwards" to [recontextualize]([[recontextualization]]) in terms of production context (e.g., methods, metadata)

            - Can explore "sideways" contextualize in terms of discourse context provided by other observation notes

                - Still fuzzy what to do with the "context notes" - doesn't make sense to make hard a prior distinctions between these notes and observation notes: they're all observations!

            - Can also explore "upwards" to contextualize in terms of synthesis/question notes

        - Note: from a modeling standpoint, we have three kinds of things:

            - {{table}}

                - **question/synthesis notes**

                    - yes

                        - yes

                            - yes

                                - wiki pages

                - type

                    - URI

                        - title

                            - body

                                - current status quo analog

                - **observation notes**

                    - yes

                        - no

                            - yes

                                - comments??

                - **context snippets**

                    - not sure

                        - no

                            - yes

                                - annotations

            - Am thinking that we want our little notes about methods, etc. to be observation notes

            - Start with **past-tense verbs**, something like "reported that...", but also "sampled <who> by..." or "measured  <x>" or "manipulated <y>", or "conducted...."

                - Leave indelible marker that this is a contextualized observation - must fill out the subject, and also note that it was done at a certain time and place

                - The latter kinds are currently

                - This makes sense from a modeling standpoint: but the question arises: how do we find the observation notes that are "findings"?

                - Also not sure how to think about observations that *we* the reader make, not necessarily one that is highlighted by the author. I guess technically they did report it if we are reading it from a graph or table!

            - This structure makes it clear what is missing from public discourse, and from page-centric workflows - we get a huge gulf or gap in [[context]], between a synthesis note all the way down to a source document

        - A possible workflow for sharing:

            - We have communities oriented around questions

            - Every time a new observation note gets added to a question, people who care about that question can get notified and are able to pull that note into their own space

                - This is the first step in distributed synthesis: you can aggregate across ^^"what raw grist have other people found helpful (optionally clustered by the synthesis notes, which you can take or leave) for answering this question i also care about?"^^

            - (optionally), when the observation note gets referenced or used in some way, that is recorded on the shared ledger
[[July 8th, 2021]]

- Therefore we contribute a [discourse graph]([[[[PTN]] - discourse graph]]) authoring system that integrates into an informal notebook (for now, hypertext) that includes DG-like conventions

    - There are three main components:

        - An authoring subsystem that interacts with and smoothens DG and local notebook conventions to assist in generating *draft* DG that the user can see and edit

            - This component should be flexible enough to accommodate variations in local conventions for notebooks, since people vary quite a bit in how they like to set up their notebooks (both between and within people).

                - So it should depend on a protocol/spec that is minimal/flexible enough to be instantiated in a variety of local conventions.

        - A querying/synthesis system that makes the DG deliver immediate value to themselves in the process of synthesis

            - This component should deliver noticeably and excitingly more value to the user's synthesis compared to not having the DG (extension)

                - use cases:

        - A sharing system that makes the DG deliver immediate value to visible others

            - use cases:

                - others visit my graph and download subsets of my DG that they like

                - i quickly assemble/bundle seed packs for collaborators and students
