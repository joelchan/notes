---
title: [[EVD]] - People added substantial structure in their usage of spatial hypertext systems that were not explicitly encoded by the systems' data structure. - [[@marshallSearchingMissingLink1993]]
url: https://roamresearch.com/#/app/megacoglab/page/2C7oZuy3T
author: Brendan Langen
date: Thu Jan 20 2022 16:14:14 GMT-0500 (Eastern Standard Time)
---

- # Summary

    - Users added three forms of implicit structure in spatial hypertext systems for long-term information management and analysis tasks:

        - Layout-based (proximity in aggregates and lists)

        - Layout- and Type-based (taxonomies and composites)

        - Reference-based (notations and recurrence)

        - > In spatialized text, a reader/author can perceive the intended structures in space, just by noticing their geometrical relationships (“if this text is close to that text, then the two must be related”), visual characteristics (“if this text is in a twelve-point italicized serif font, it must fill an annotative role similar to the other twelve-point italicized text that’s an annotation”), and recurrence (“this segment of text means something completely different when I read it over here”). If this structure is perceived by heuristic algorithms, it can then fill the same function as explicitly represented structure. (pg. 219)

    - Spatialized text helps organize information, reduce representational problems, help others grasp content, and maintain consistency in information.

        - > The ability to find and use implicit structures can support authors and readers in a system that extends the node-link model with spatial hypertext. As we noted in our discussion of reasons to recognize implicit structure, this kind of found structure can be used as a basis for supporting information management, as a straightforward way of promoting knowledge-base evolution, as a way of solving representational problems endemic to many hypertext systems, or as a basis for collaboration or interaction. (pg. 227)

    - Automatic parsing of text into spatial structures is possible and enables easier interpretation in the future.

        - > From this automatic heuristic parsing experiment we can conclude that (1) such parsing is feasible; (2) interaction will be important in guiding this kind of recognition (especially since the structures can be both idiosyncratic and ambiguous); and (3) that the hypertext system can provide facilities for spatialization that will render later systematic interpretation much easier. (pg. 226)
- # Grounding Context

    - Methods

        - The sample: 8 datasets gathered from 3 tools. Each sample is the result of a long-term information management or analysis task (pg. 219)

            - > To explore how people have spatialized text in hypertext systems -- sometimes in creative ways at cross-purposes to developers’ hopes -- we gathered data about the textual objects appearing in layouts created in three different systems, NoteCards, the Virtual Notebook System (VNS), and Aquanet. Eight samples were selected, each the result of a long-term information management or analysis task.

            - The tools

                - NoteCards, the Virtual Notebook System (VNS), and Aquanet

                    - > We gathered data about the textual objects appearing in layouts created in three different systems, NoteCards, the Virtual Notebook System (VNS), and Aquanet. Eight samples were selected, each the result of a long-term information management or analysis task.

                        - [[[[CLM]] - Requirements for sensemaking come from the particulars of the work task]]

            - The datasets - some data analysis, some bug tracking, some topic organization for a paper.

                - NoteCards (pg. 220) - example: anthropological data analysis task. 35 individual pieces of text

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FbalOS%2FT19RU-SI3e.png?alt=media&token=73713c73-c7a3-4b4e-b595-612317526bfa)

                    - > Figure 1 shows a schematized version of one of his NoteCards sketches; text has been replaced by boxes that cover the same area as the text. Shading indicates whether the text was bold, italic, or plain. Graphical notations have been preserved.

                    - > So in our first example, structures using layout constraints, reference, and type constraints are all created outside the hypertextual framework provided by NoteCards.

                - VNS (pg. 221) - example: bug tracking with 7 or 8 collaborators. 63 total objects - 28 text/icon link markers, 10 images, miscellaneous text + link markers

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FbalOS%2F9o5sRxI1XA.png?alt=media&token=01bd5683-f3a7-494b-867a-6b9b623be8aa)

                        - > In our VNS example, 7 or 8 collaborators used the system’s hypermedia capabilities to track system bugs; Figure 2 shows an encoded’ version of the page. The page contains 28 textual/iconic link markers showing links to other VNS pages, 10 image objects that implement a tabular layout, column headings that area composite of numbers and text, and miscellaneous blocks of text and link markers (near the top of the schematized version shown in Figure 2). A total of 63 objects were arranged on the page when we collected this data, after six months of use. We could perceive six distinct types.

                        - > So in our second example, reference is still done hypertextually, but structures are composed through spatial layout and graphical notation.

                - Aquanet (pgs. 222, 227) - examples: bug tracking, a Spanish-English translation machine translation, and organizing topics for a paper. 16 composite structures.

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FbalOS%2FDGytGgXpcI.png?alt=media&token=5d647f04-669d-4eb0-b756-1d0b52844fb8)

                        - > So in our third example of spatialized text, typing and reference are done within the framework Aquanet provides; constraints on spatial layout are enforced informally, by the user.

                        - > Two of the four Aquanet examples had the unique property of having grown large enough to have distinct structural regions and many complex higher-level structures (structures formed of other structures). Figure 3 shows one of the simple cases of this. Note that there are 16 roughly similar composite structures. These 16 composites can also be seen as a single set, a higher-level structure.

Aquanet does not support “drawing on the space,” so there are no graphical hints about how the space is organized. Because there’s no alignment or gridding, the structures take on a very informal appearance (in contrast with our other examples of spatialized text). Our more complex Aquanet examples use recurrence to provide reading context for the objects.

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FP4CQIaLfYE.png?alt=media&token=eec0f5a5-6a46-4e67-81c0-25d5341f09ce)

                        - > Figure 7 shows a sample parse of an Aquanet discussion. Different structures found by the recognition algorithms are shown with different shading. The right-most column of objects is one of many ambiguous situations in this relatively simple spatial layout. In this case the layout could be interpreted as a list of items with a larger-than normal gap or, as the recognition algorithms decided here, there could be two separate shorter lists. Neither alternative is necessarily the correct one; the spatial freedom allows the author to leave such determinations implicit, and left up to the interpretation of the reader.

From this automatic heuristic parsing experiment we can conclude that (1) such parsing is feasible; (2) interaction will be important in guiding this kind of recognition (especially since the structures can be both idiosyncratic and ambiguous); and (3) that the hypertext system can provide facilities for spatialization that will render later systematic interpretation much easier.

        - The researchers encoded data spatially and assigned type-based characteristics from what they saw.

            - > We encoded the data in a uniform representation to capture spatial and visual aspects of the text objects; relative planar location and extent of each object was recorded. Each object was also assigned a type based on distinguishing graphical characteristics.

            - > For example, to encode the NoteCards sketches, we assigned one of three types to each textual object according to whether its font was regular, bold, or italic, and calculated its approximate extent according to number of lines and maximum line length. VNS objects were encoded according to representational type, font, and conversations with the author about their intent. Aquanet objects required no additional interpretation to fit into our data analysis framework

        - Then they built a prototype recognition algorithm to parse structure in spatialized text. The algorithm found aggregates, aligned taxonomic sets, and composites, which was often consistent with the authors' intent. (pgs. 225-227)

            - > Figure 6 simulates a parse that the recognition algorithms can perform; this example is a segment of a structure built in Aquanet, For the purposes of the figure, when a parsed structure inherits a type from its constituents, it is represented the same way; if a new type has been generated, an arbitrary new visual representation is shown. (pg. 225)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F3sTM1ZVzrG.png?alt=media&token=ad08e8aa-1ba1-490e-b036-aa654931bdf1) (pg. 226)

            - The higher the level of perceived structure, the more likely incomplete recognition occurred.

            - > Figure 7 shows a sample parse of an Aquanet discussion. Different structures found by the recognition algorithms are shown with different shading. The right-most column of objects is one of many ambiguous situations in this relatively simple spatial layout. In this case the layout could be interpreted as a list of items with a larger-than normal gap or, as the recognition algorithms decided here, there could be two separate shorter lists. Neither alternative is necessarily the correct one; the spatial freedom allows the author to leave such determinations implicit, and left up to the interpretation of the reader.  (pg. 226)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCdC9LOwGi4.png?alt=media&token=995f759d-7ccc-42c5-b41f-0fae7404172d)  (pg. 227)

###### Discourse Context

- **FromSource::** [[@marshallSearchingMissingLink1993]]
