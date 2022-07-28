---
title: @ribaupierreExtractingDiscourseElements2017
url: https://roamresearch.com/#/app/megacoglab/page/cY1yepcjX
author: Joel Chan
date: Sun Feb 16 2020 12:44:15 GMT+0800 (Malaysia Time)
---

- #references

    - Title: Extracting discourse elements and annotating scientific documents using the SciAnnotDoc model: a use case in gender documents

    - Meta

        - Tags: #ref/Paper [[DSynthesis Infrastructure]]

        - Authored by:: [[Hélène de Ribaupierre]]

        - Year: [[2017]]

    - #lit-context

    - [[📝 lit-notes]]

        - [[Joel Chan]]

        - [[Jay Patel]]

            - __Feel free to have free-floating notes that don't neatly fit into the boxes below!__

            - ## #inspectionalread

                - __What questions are the authors tackling and how do they intersect with what we care about? What key concepts or ideas or people do you notice that might be useful for us? What are some of the possible major contributions/results we will care about from this source?__

                    - **Meta**

                        - How to Read Creatively

                            - Ideate <- Read

                            - Read -> Ideate

                        - Structured Abstracts (metadata conventions)

                        - Multiverse analyses

                    - **Goals/Problems**

                        - Use complex queries to search information scapes for semantic meaning in a variety of unstructured papers or inconsistently structured papers (e.g. find all definitions of gender and how its meaning changed over time)

                            - Can't Elicit or GPT-3 directly do this? Semantic Scholar? Lens.org?

                    - **Key Background/Approach**

                        - It's only getting harder to search across millions of papers.

                        - Three antecedents

                            - Machine-readable docs: not empirically studied yet

                            - NLP: " lack effective methods to extract and describe semantically a number of more structured and fine-grained entities (pg. 2)"

                            - InfoSci: empirically-derived models of scholars' search process are too task-specific

                        - Current Study

                            - Unites Machine-readable docs, NLP, and InfoSci

                                - Users annotates texts

                                - NLP tools aid annotation

                                - InfoSci: ???

                        - Proposed Benefits

                            - Key Effect 1: Enable semantic search (across fields?)

                            - Side Effect 1: visualize scholarly knowledge

                                - Jay: this is tricky with a great deal of data and a multiverse of visuals would need to be toggled through to find meaning

                            - Side Effect 1: cross-reference documents

                                - Jay: Does this mean cross-disciplinary and interdisciplinary research or just using similar concepts and procedures across papers?

                    - **Audience**

                        - Scholars seeking to conduct thorough lit reviews.

            - ## methods notes

                - **study 1**

                    - User studies aka human studies

                        - survey (closed form responses)

                        - semi-structured interviews (open form responses)

                        - too little info on procedure

                        - Scholars do not focus on the whole document.

                        - **SciAnnotDoc Model**

                            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fq-HVkHa_Ol.png?alt=media&token=14b6284f-d9d5-41f9-8944-fd3f82003dd0)

                            - **Dimensions**

                                - 1. **Metadata**: e.g. author names, journal name, publisher, date of publication (Note: see MDOC standards in progress)

                                - 2. **Textual content**: representation of  terms

                                    - domain ontology (SIPS 2019)

                                - 3. **Discourse elements**: Core to SciAnnotDoc model; e.g. findings, definitions, methodology, hypothesis, related work (see Jay's outline of 3 Act Research). Text can be a finding and a definition

                                - **4. Relational Elements:** relational structure of discourse elements in the paper to other discourse elements within and between papers (CiTO type ontology for agree/disagree/confirm)

                - **study 2**

            - ## results of interest and discussion

                - __One block for each result of interest. we'll refactor this together into EVD notes__

                    - ### summary

                        - __nest details and screenshots (e.g., key figures, quotes) under here__

                    - ### grounding context

                        - __block ref in major methods details from the source methods / context block we might need later to make sense of this result, particularly as they might conflict with others. __

                    - __also discuss possible critiques/claims. create source CLM notes for author conclusions (if you like), or reference other CLMs that we have that engage with this__

                - __Also can discuss meta-results (combinations of results) in a similar template.____

###### Discourse Context

- **Informs::** [[CLM - Compression is necessary for synthesis]]
- **Informs::** [[CLM - Scientists read strategically, not linearly]]
- **Informs::** [[QUE - How can we best bridge private vs. public knowledge]]
- **Informs::** [[QUE - What (existing) systems facilitate individual synthesis]]
- **SourceFor::** [[EVD - Scientists more often nonlinearly read subsections of papers for findings, hypotheses or othe...ion, rather than linearly reading whole documents - @ribaupierreExtractingDiscourseElements2017]]
- **SourceFor::** [[EVD - 10 scholars self-reported that they read specific fragments and sections, such as findings an...g new ideas, and writing articles or new projects - @ribaupierreExtractingDiscourseElements2017]]
