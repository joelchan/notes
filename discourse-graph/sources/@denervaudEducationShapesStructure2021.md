---
title: @denervaudEducationShapesStructure2021
url: https://roamresearch.com/#/app/megacoglab/page/wYn3ln_N-
author: Joel Chan
date: Tue Mar 15 2022 10:19:43 GMT-0400 (Eastern Daylight Time)
---

- Title:: Education shapes the structure of semantic memory and impacts creative thinking
- Author(s):: [[Solange Denervaud]], [[Alexander P. Christensen]], [[Yoed N. Kenett]], [[Roger E. Beaty]]
- Abstract:: Education is central to the acquisition of knowledge, such as when children learn new concepts. It is unknown, however, whether educational differences impact not only what concepts children learn, but how those concepts come to be represented in semantic memory—a system that supports higher cognitive functions, such as creative thinking. Here we leverage computational network science tools to study hidden knowledge structures of 67 Swiss schoolchildren from two distinct educational backgrounds—Montessori and traditional, matched on socioeconomic factors and nonverbal intelligence—to examine how educational experience shape semantic memory and creative thinking. We find that children experiencing Montessori education show a more flexible semantic network structure (high connectivity/short paths between concepts, less modularity) alongside higher scores on creative thinking tests. The findings indicate that education impacts how children represent concepts in semantic memory and suggest that different educational experiences can affect higher cognitive functions, including creative thinking.
- Type:: [[Article]]
- Publication:: npj Science of Learning
- URL : https://www.nature.com/articles/s41539-021-00113-8
- Date Added:: [[March 15th, 2022]]
- Zotero links:: [Local library](zotero://select/groups/2451508/items/J7KCTA92), [Local library](https://www.zotero.org/groups/2451508/items/J7KCTA92)
- Tags:: #[[Human behaviour]], #[[Long-term memory]]
- PDF links : [Denervaud et al. - 2021 - Education shapes the structure of semantic memory .pdf](zotero://open-pdf/groups/2451508/items/CUW5KUBJ)
- #lit-context

    - methods

        - compare montessori kids to comparable kids (wrt SES, nonverbal intelligence) from other schooling systems, 67 kids in total

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FrycDCyaRtc.png?alt=media&token=445952fa-ab39-4e1d-a73d-c69bcead5233) 
![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKwSV1sEwC_.png?alt=media&token=ab464c01-2a06-4666-8096-791b9b21324c)
(p. 4)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzboND2S8yj.png?alt=media&token=39ce2fe6-cb89-457f-9497-2231e700e1c9) (p. 2)

        - procedures: do verbal fluency task (name as many animals in 60s), and creativity assessment (standard tasks from Evaluation of Potential Creativity)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FN0IkB6RHUK.png?alt=media&token=923be4ff-bb03-42b4-b72e-ab0dc7c93e39) (p. 5)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDnE4cskRkd.png?alt=media&token=22263a5d-7b20-4e30-9c1f-91477edb7892) (p. 5)

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

            - network estimation sampling for each group: estimate 1000 case-wise bootstrapped simulated networks from each group (basically, for each group, for 1000 times, grab N-M participants from the group, [construct the network](network construction/estimation), and then compute the [network metrics](((Z37PYNsQe))))
- #[[📝 lit-notes]]

    - [[Joel Chan]] for [[[[THE]] - interaction-oriented theory of creative inspiration from examples]]

        - results

            - [[[[EVD]] - estimated semantic networks of animal concepts from montessori-educated children were more interconnected, with shorter paths between concepts and fewer subcommunities, compared to networks from traditional-schooled but comparable children - [[@denervaudEducationShapesStructure2021]]]]

###### Discourse Context

- **Informs::** [[THE - interaction-oriented theory of creative inspiration from examples]]
- **SourceFor::** [[EVD - estimated semantic networks of animal concepts from montessori-educated children were more in...orks from traditional-schooled but comparable children - @denervaudEducationShapesStructure2021]]

###### References

[[March 15th, 2022]]

- this connects back to finding of network differences between montessori and "regular" kids from that paper from [[Roger E. Beaty]]: [[[[EVD]] - estimated semantic networks of animal concepts from montessori-educated children were more interconnected, with shorter paths between concepts and fewer subcommunities, compared to networks from traditional-schooled but comparable children - [[@denervaudEducationShapesStructure2021]]]]

    - uses this [[m/Triangulated Maximally Filtered Graph (TMFG)]] method for estimating a network. it's a bit strange, but seems.... useful? roots in big data. lots of usage by [[Yoed N. Kenett]] and friends

        - motivation: something about efficiency and having some kind of computable structure

            - from [here](https://link.springer.com/article/10.3758/s13428-018-1032-9)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FS9htkrUjpQ.png?alt=media&token=3c08566a-f7f4-483a-96c1-0e9d1284a761)

            - from [here](https://journals.sagepub.com/doi/10.1002/per.2157)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FTktx1l4kEY.png?alt=media&token=c64bfbfc-11c0-44a1-9823-5419401c83dc)
[[March 18th, 2022]]

- potential inspiration: semantic network filtering, like [[m/Triangulated Maximally Filtered Graph (TMFG)]], as in this paper: [[[[EVD]] - estimated semantic networks of animal concepts from montessori-educated children were more interconnected, with shorter paths between concepts and fewer subcommunities, compared to networks from traditional-schooled but comparable children - [[@denervaudEducationShapesStructure2021]]]]

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fqte9wyd3eM.png?alt=media&token=1896fba5-8ae9-4299-a35f-48f1b9bb3d5b)
