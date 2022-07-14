---
title: [[EVD]] - estimated semantic networks of animal concepts from montessori-educated children were more interconnected, with shorter paths between concepts and fewer subcommunities, compared to networks from traditional-schooled but comparable children - [[@denervaudEducationShapesStructure2021]]
url: https://roamresearch.com/#/app/megacoglab/page/jScHaY6Fl
author: Joel Chan
date: Tue Mar 15 2022 10:55:28 GMT-0400 (Eastern Daylight Time)
---

- # Summary

    - estimated semantic networks of animal concepts from montessori-educated children were more interconnected, with shorter paths between concepts and fewer subcommunities, compared to networks from traditional-schooled but comparable children

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7aHUer0evF.png?alt=media&token=cf1ba046-bf98-4277-ab1f-99363dd9f278) (p. 3)

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FAZen14iS-z.png?alt=media&token=dabe714b-1fb9-464e-b312-986ecacecb7b)
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F4ogsqIPX-L.png?alt=media&token=9fa732ba-1fb2-4a01-8687-f5fbfee4ee07) (pp. 2-3)
- # Grounding Context

    - compare montessori kids to comparable kids (wrt SES, nonverbal intelligence) from other schooling systems, 67 kids in total

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FrycDCyaRtc.png?alt=media&token=445952fa-ab39-4e1d-a73d-c69bcead5233) 
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKwSV1sEwC_.png?alt=media&token=ab464c01-2a06-4666-8096-791b9b21324c)
(p. 4)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzboND2S8yj.png?alt=media&token=39ce2fe6-cb89-457f-9497-2231e700e1c9) (p. 2)

    - procedures: do verbal fluency task (name as many animals in 60s), and creativity assessment (standard tasks from Evaluation of Potential Creativity)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FN0IkB6RHUK.png?alt=media&token=923be4ff-bb03-42b4-b72e-ab0dc7c93e39) (p. 5)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDnE4cskRkd.png?alt=media&token=22263a5d-7b20-4e30-9c1f-91477edb7892) (p. 5)

        - WSN8hkRcq

    - measures: clustering coefficient, average shortest path length (ASPL) and modularity (Q) of estimated filtered semantic networks of the animal names from the kids

        - network construction/estimation

            - dump all responses into a participant-word matrix, so each word is a column, and each participant is a row, and each cell is 0/1 depending on whether participant mentioned the word. this is kind of like a word-document matrix. equate number of nodes across groups

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0oToYzqv9m.png?alt=media&token=13a38aa2-7bcf-4437-80ee-6d17b7847fe4)
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FVVRiPfyuXv.png?alt=media&token=b5e316f7-ed9d-4b56-8325-916407d9a691) (p. 5)

            - then for each pair, look at the two "participant vectors" (i.e., the column of 1s and 0s of occurrences across participants)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FsZwDPGqwwj.png?alt=media&token=b1945d69-2503-44a6-8312-50be0384ebf7) (p. 5)

            - then draw a filtered network from the similarity matrix using [[m/Triangulated Maximally Filtered Graph (TMFG)]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FAjRpsnRRvW.png?alt=media&token=c04e35a2-f0aa-4356-99a6-39d29c03a0a1) (p. 5)

                - method is from [[@massaraNetworkFilteringBig2017]], and can be replicated using R package described in [[@christensenSemanticNetworkAnalysis2021]]

        - network metrics: clustering coefficient, average shortest path length (ASPL) and modularity (Q)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fk3I3R5wz7m.png?alt=media&token=23dc3f85-456e-46f0-b403-c57ccc02b58f)

        - network estimation sampling for each group: estimate 1000 case-wise bootstrapped simulated networks from each group (basically, for each group, for 1000 times, grab N-M participants from the group, [construct the network](((E5BAJ-R3Q))), and then compute the [network metrics](((Z37PYNsQe))))

###### Discourse Context

- **Informs::** [THE - interaction-oriented theory of creative inspiration from examples.md](THE - interaction-oriented theory of creative inspiration from examples.md)
- **Consistent With::** [EVD - higher conceptual flexibility to classify organisms based on taxonomic and ecological relatio...ed in more unstructured interactions with organisms - @betzDevelopmentConceptualFlexibility2020.md](EVD - higher conceptual flexibility to classify organisms based on taxonomic and ecological relatio...ed in more unstructured interactions with organisms - @betzDevelopmentConceptualFlexibility2020.md)
- **FromSource::** [@denervaudEducationShapesStructure2021.md](@denervaudEducationShapesStructure2021.md)

