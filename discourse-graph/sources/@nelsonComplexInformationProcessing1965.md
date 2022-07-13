---
title: @nelsonComplexInformationProcessing1965
url: https://roamresearch.com/#/app/megacoglab/page/Dwc8FE_Aa
author: Joel Chan
date: Sun Jun 28 2020 00:16:02 GMT-0400 (Eastern Daylight Time)
---

- #references

    - Title: Complex information processing: a file structure for the complex, the changing and the indeterminate

    - Meta:

        - Tags: #ref/Paper

        - Authored by::  [[Ted Nelson]]

        - Year: [[1965]]

        - Publication: Proceedings of the 1965 20th national conference

        - URL: https://doi.org/10.1145/800197.806036

        - Citekey: nelsonComplexInformationProcessing1965

    - Content

        - Placeholder

        - Abstract

            - THE KINDS OF FILE structures required if we are to use the computer for personal files and as an adjunct to creativity are wholly different in character from those customary in business and scientific data processing. They need to provide the capacity for intricate and idiosyncratic arrangements, total modifiability, undecided alternatives, and thorough internal documentation. I want to explain how some ideas developed and what they are. The original problem was to specify a computer system for personal information retrieval and documentation, able to do some rather complicated things in clear and simple ways. In this paper I will explain the original problem. Then I will explain why the problem is not simple, and why the solution (a file structure) must yet be very simple. The file structure suggested here is the Evolutionary List File, to be built of zippered lists. A number of uses will be suggested for such a file, to show the breadth of its potential usefulness. Finally, I want to explain the philosophical implications of this approach for information retrieval and data structure in a changing world.

###### Discourse Context



###### References

[[September 1st, 2021]]

- Picked up [[@nelsonComplexInformationProcessing1965]] again in the New Media Reader.

    - It obscures the prescient nature of this paper - look at the OG microfilm feel!!!

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FiD9CJuHQlf.png?alt=media&token=1b9b00c4-e89c-40f8-904d-cb5993b8d13c)

    - Core concept around [[blocks vs. pages]] - the [[zippered-list]]

        - which has three basic elements

            - entry

            - list

                - NOTE! entries can live in lists, but can show up in multiple lists!

            - link

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUUhCdVUzFV.png?alt=media&token=44b60c5d-e41b-4fc4-aa00-e70f02bdd127)

        - i think these map naturally to [[sys/RoamResearch]]

            - entry <--> block

            - list <--> page, parent block tree

                - these are stable contexts for entries/blocks to give meaning to each other

                - what's interesting here is that [[Ted Nelson]] didn't think past linear flat lists of entries; crossing this idea with an [[outliner]] expands the possibility space of relationships within a list!

                    - an entry *itself* becomes a list and context in terms of its children, greatly expanding the surface area of associative trails!

                    - so.. i initially thought that collapsing pages and blocks would have serious negative consequences, and go against the original design of a [[zippered-list]] that was designed to support complex, nonlinear, synthetic thinking.

                        - but now i'm not so sure. by instantiating this idea in an outliner.... it's possible to not need pages at all. and that's indeed exactly what we find with lots of user behaviors, with contentless pages

            - link <--> reference

                - allow for an additional way for blocks to escape their context and invade/fertilize new contexts

        - but also to [[sys/Obsidian]], but perhaps in a less obvious way

            - entry <--> atomic markdown file

            - list <--> non-atomic markdown file, folder

            - link <--> reference

            - there is a bit of friction in using this vanilla way though: so we get plugins like note refactor to make it easier to refactor into atomic notes (essentially creating entries), but also [[Desire Path]]s towards blocks as entries (which are just lines in a [[std/Markdown]] file)

        - and just for fun, back to the OG analog [[sys/Zettelkasten]]:

            - list <--> index, structure note, [[folgezettel]]

            - link <--> links

            - entry <--> zettel
