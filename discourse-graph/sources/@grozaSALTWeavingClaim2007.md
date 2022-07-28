---
title: @grozaSALTWeavingClaim2007
url: https://roamresearch.com/#/app/megacoglab/page/g4qlnB2fq
author: Joel Chan
date: Tue Jun 16 2020 03:13:20 GMT+0800 (Malaysia Time)
---

- #references

    - Title: SALT: Weaving the Claim Web

    - Meta:

        - Tags: #ref/Paper

        - Authored by::  [[Tudor Groza]]

        - Year: [[2007]]

        - Publication: The Semantic Web

        - URL:

        - Citekey: grozaSALTWeavingClaim2007

    - Content

        - Placeholder

        - **Extracted Annotations (6/15/2020, 5:01:00 PM)**

            - "One of our main goals was to support the creation of knowledge networks via claims stated in scientific publications by leveraging the document semantics. Each of the claims is addressable by a unique identifier, and a set of such structured documents can be integrated to form a network of interlinked resources. In this way a semantic web of scientific literature is growing, document by document. Metaphorically speaking, the information in the documents is liberated from their surrounding document and can be integrated and re-used in new and unexpected ways." ([Groza et al 2007:1](zotero://open-pdf/library/items/4FDS8SB3?page=1))

            - __goal sounds like synthesis! ([note on p.1](zotero://open-pdf/library/items/4FDS8SB3?page=1))__

            - "give authors the possibility of working at a finer-grained level, by being able to cite claims within a publication" ([Groza et al 2007:2](zotero://open-pdf/library/items/4FDS8SB3?page=2))

            - "To achieve this goal, a mechanism for global and local claim identification is needed." ([Groza et al 2007:2](zotero://open-pdf/library/items/4FDS8SB3?page=2))

            - "SALT allows the author of a scientific publication to enrich the document with formal descriptions of claims, supports and rhetorical relation as part of their writing process" ([Groza et al 2007:2](zotero://open-pdf/library/items/4FDS8SB3?page=2))

            - __compression ([note on p.2](zotero://open-pdf/library/items/4FDS8SB3?page=2))__

            - __author is contributor ([note on p.2](zotero://open-pdf/library/items/4FDS8SB3?page=2))__

            - "In our model, objects correspond to claims, concepts to representations of a claim in a publication as such (e.g. "Joe's paper at ISWC2007") and symbols are the actual strings of text in a particular, physical PDF file" ([Groza et al 2007:3](zotero://open-pdf/library/items/4FDS8SB3?page=3))

            - "r" ([Groza et al 2007:4](zotero://open-pdf/library/items/4FDS8SB3?page=4))

            - "Pr" ([Groza et al 2007:4](zotero://open-pdf/library/items/4FDS8SB3?page=4))

            - "eviously, SALT had support for claim identification, but did not take into account the issue of multiple representations" ([Groza et al 2007:4](zotero://open-pdf/library/items/4FDS8SB3?page=4))

            - __multiplicity ([note on p.4](zotero://open-pdf/library/items/4FDS8SB3?page=4))__

            - "In our vision of a Web of documents, an author will want to refer to and cite claims, not whole publications" ([Groza et al 2007:7](zotero://open-pdf/library/items/4FDS8SB3?page=7))

            - __hah, just like our KC prototype! ([note on p.7](zotero://open-pdf/library/items/4FDS8SB3?page=7))__

            - "group of eight researchers, who all had knowledge of Semantic Web and Semantic Annotations technologies" ([Groza et al 2007:9](zotero://open-pdf/library/items/4FDS8SB3?page=9))

            - "ach participant annotated one of their own papers and was given a set of explanations of the model and instructions on how to perform the annotations beforehand. The evaluation consisted of seven annotations tasks as follows: (i) Rhetorical block annotation, (ii) Claims markup, (iii) Support markup, (iv) Annotation of rhetorical relations between claims and supports, (v) Nuclei and sattelites markup, (vi) Annotation of rhetorical relations between nuclei and sattelites, and (vii) Annotation of domain knowledge." ([Groza et al 2007:9](zotero://open-pdf/library/items/4FDS8SB3?page=9))

            - "ith increasing complexity of the annotation task at hand, the participants' overall impression decreased. The annotation of rhetorical blocks, which is also the simplest of the tasks, was deemed most intuitive, while the annotation of rhetorical relations at the other end of the scale was deemed not intuitive, but instead" ([Groza et al 2007:10](zotero://open-pdf/library/items/4FDS8SB3?page=10))

            - "ather complex by most participants (see Fig. 7). Similarly, Fig. 8 A shows that the plausibility of terminology and soundness of the model were considered high by 7 out of 8 participants, whereas fewer and f" ([Groza et al 2007:11](zotero://open-pdf/library/items/4FDS8SB3?page=11))

            - "fewer participants said this about the more complex annotation tasks (6 found annotation of claims and support plausible, 4 found nucleus/satellite annotation plausible, while no one found the handling of rhetorical relations plausible). Figure 8 B supports the same tendency from yet another angle: none of the participants found the benefit of simple annotations (rhetorical blocks and claim/support) unclear, while 3 were unsure about the benefit of nucleus/satellite annotation and 7 about rhetorical relations" ([Groza et al 2007:11](zotero://open-pdf/library/items/4FDS8SB3?page=11))

            - "tion plausible, while no one found the handling of rhetorical relations plausible). Figure 8 B supports the same tendency from yet another angle: none of the participants found the benefit of simple annotations (rhetorical blocks and claim/support) unclear, while 3 were unsure about the benefit of nucleus/satellite annotation and 7 about rhetorical relations" ([Groza et al 2007:11](zotero://open-pdf/library/items/4FDS8SB3?page=11))

            - "we see the development of tools which aid the user in the authoring process as crucial" ([Groza et al 2007:11](zotero://open-pdf/library/items/4FDS8SB3?page=11))

            - "most of the participants needed to revisit the documentation numerous times during the annotation process, and some had in fact admitted that they had not read the documentation at all before the evaluation" ([Groza et al 2007:11](zotero://open-pdf/library/items/4FDS8SB3?page=11))

    - [[📝 lit-notes]]

        - methods notes

            - system

                - The system consists of a markup scheme for denoting, with varying levels of complexity and specificity, what claims are in a given document.

                    - Basically you want to mark claims (and supports) and relations between them, as well as "rhetorical annotation" (where in the document it is, e.g., abstract, methods, etc.)

                        - claims and supports are similar to [[Stephen E. Toulmin]]

                        - "nuclei" and "satellites" are generalizations of claims and supports

                    - As far as I can tell, this markup doesn't really include any level of [[formality]]

                    - Unfortunately, I have no idea, from the description, what the authoring experience is like at all!

                        - Best I can tell is that inserting claims from __other__ papers uses markup similar to \cite in [[LaTeX]]

                        - But I have no idea how you "mark" [[rhetorical blocks]]

            - They did a little user study with a group of 8 authors, had them try out the markup scheme on their own papers

                - "group of eight researchers, who all had knowledge of Semantic Web and Semantic Annotations technologies" ([Groza et al 2007:9](zotero://open-pdf/library/items/4FDS8SB3?page=9))

        - What's notable for us in the context of [[QUE - What is the user experience of semantic authoring within regular scholarly workflows]]

            - similar to [[@monsWhichGeneDid2005]]

            - BUT, they find that, beyond the simple task of annotating [[rhetorical blocks]]

        - Found:

            - [[EVD - Participants who marked up their own papers with a formal semantic scheme perceived the task ...n contrast to formally marking rhetorical relations between claims - @grozaSALTWeavingClaim2007]]

            - [[EVD - Participants who marked up their own papers with a formal semantic scheme self-reported that ...d less clear in terms of payoff compared to formally making claims - @grozaSALTWeavingClaim2007]]

###### Discourse Context

- **Informs::** [[QUE - What is the user experience of semantic authoring within regular scholarly workflows]]
- **SourceFor::** [[EVD - Participants who marked up their own papers with a formal semantic scheme perceived the task ...n contrast to formally marking rhetorical relations between claims - @grozaSALTWeavingClaim2007]]
- **SourceFor::** [[EVD - Participants who marked up their own papers with a formal semantic scheme self-reported that ...d less clear in terms of payoff compared to formally making claims - @grozaSALTWeavingClaim2007]]
