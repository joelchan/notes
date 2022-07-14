---
title: @cataliniMicrogeographyDirectionInventive2017
url: https://roamresearch.com/#/app/megacoglab/page/vdTT5gz3p
author: 
date: Sun Dec 06 2020 21:38:20 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Microgeography and the Direction of Inventive Activity

    - Meta: #lit-context

        - Authored by:: [[Christian Catalini]]

        - Year: [[2017]]

        - Publication: [[Management Science]]

        - Zotero link: [Zotero Link](zotero://select/items/7_7JU3TMFF)

        - URL: [Catalini (2017). Microgeography and the Direction of Inventive Activity. Management Science](https://doi.org/10.1287/mnsc.2017.2798)

    - Content

        - Abstract

            - I provide novel empirical evidence grounded in an original theoretical framework to explain why [[colocation (matters for the) innovation/collaboration]] rate, direction, and quality of scientific collaboration. To address endogeneity concerns due to selection into colocation and matching, I exploit the constraints imposed on the spatial allocation of labs on the Jussieu campus of Paris by the removal of asbestos from its buildings. Consistent with search costs (of innovation) [[search costs of innovation]] constituting a major friction to collaboration, ^^colocation increases the likelihood of joint research by 3.5 times^^, an effect that is mostly driven by lab pairs that face higher search costs ex ante. Furthermore, separation does not negatively affect collaboration between previously colocated labs. However, while colocated labs grow increasingly similar in topics and literature cited, separated ones embark on less correlated research trajectories. Research outcomes, instead, seem to be mostly influenced by how distance affects execution costs: after colocation, labs are more likely to pursue both lower-quality projects (a selection effect) and high-quality projects (an effort effect). Opposite effects on quality are observed after separation. Whereas search costs affect which scientists are likely to collaborate together, execution costs shape the quality of their output. The online appendix is available at https://doi.org/10.1287/mnsc.2017.2798. This paper was accepted by Ashish Arora, entrepreneurship and innovation.

        - PDF

            - {{pdf: https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FLh1onNhk9F.pdf?alt=media&token=7363b292-6b89-4362-9c98-5025ccc93d70}}

        - #context-snippets

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_2qBwM9Evs.png?alt=media&token=9d463e0e-65ac-47e0-a9c4-12b23d66090e)

    - #lit-context

        - setting: major research university in France

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDWJ7k-q7Wi.png?alt=media&token=b9772a51-d5d6-4ef5-af98-759b81f70dd0) (p. 4352)

        - "intervention": there is sort of [[m/natural experiment]] here since external circumstance prompted frequent relocations of labs

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fxb9jA35RIK.png?alt=media&token=673a61ca-c31a-4e10-96a4-9af227a03d85) (p. 4352)

            - Separation (change in distance) is considered as the exogenous variation that is injected into the process (p.4349)

                - has a nonsignificant effect

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKRKJV2ySz6.png?alt=media&token=d23d1c17-6888-42f2-9690-043039231d20)

        - analysis: used [[difference in difference analysis]] instead of regular OLS regression, to account for [[endogeneity bias]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMNUx1MSjZ9.png?alt=media&token=29f4e4c6-20b2-4a60-9797-47e91a9782e9) (p. 4354)

            - Outcome

                - reconstruction of fine-grained, longitudinal info on inventive outcomes (p.4349)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FxYRUDozG8K.png?alt=media&token=684fb996-3be9-477e-ac42-f74ada8ea339)

                - [[Research outcomes]] also = paper quality indicator (whether it stands in the highest quartile of the citation distribution) (p.4349)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKJ4nJswnht.png?alt=media&token=2628fa4b-38aa-4984-9f3f-e5d7260cf228)

        - **Experiment data**: publication records, citation information, geolocation data with re-identification API, affiliation string disambiguation (p.4352)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6-hcia7ue_.png?alt=media&token=5888c128-c385-40fc-b8d5-26b99cc331b7)

        - measures

            - differences in "ex-ante search costs" between labs: similarity/overlap in areas (as a proxy(?): cosine distance between keywords in pubs and refs)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fkcj-ZcPwO1.png?alt=media&token=269470e1-d30a-42ca-bd9d-b4888718adf9)

    - #[[📝 lit-notes]]

        - **How did they approach these questions/problems?** ((most of this is going to come from the methods sections, although some info about conceptualization of key concepts might be relevant to pull from intro/lit-review)) #lit-context

            - [[c/Dependent variables]]

            - [[c/Independent variables]]

                - 

        - **What did they find?** ((keep this as contextualized as possible; resist the urge to repeat claims or generalizations)) #[[observation-notes]] (March 8-19, week 6 & 7, Spring 2021

            - Primarily from Section 4.2

                - Claim new #1: The likelihood of collaboration where lab pairs conduct joint research [increases by (question comes here) 3.5 times](at the lab-pair-year level which exploits the variation in colocation and separation generated by the moves during asbestos-removal period (p.4354)

Control variable ([[explanatory variable]]) = colocation / separation, outcome variable = inventive outcome (dummy, 1/0?) 

The effect estimating equation in p.4354 as below, but also on nonlinear models and for different outcomes  

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Pc0-HEko.png?alt=media&token=3f8be83b-81e1-4a49-a2eb-b5a4b941e427)) (susceptibly = 0.05 / 0.0146), where the estimated coefficient $$\beta(collaborate | colocation) = .0146, p(collaborate | colocation) < .01$$) and [the number of times of collaboration increases 2.5--3.3 times more](((gZMue8EKh))), [due to colocation](((gjU-_3-g2))) [that caused a reduction in search cost and in joint execution cost](((58f8IXER9))).

                    - Hypotheses in p. 4357 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FoIbjHEDTed.png?alt=media&token=1141a0ee-961a-471a-86bf-4ca1a9b50268)

                    - Table 5, column (1), then for collaboration # see (3) and (2) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_2qBwM9Evs.png?alt=media&token=9d463e0e-65ac-47e0-a9c4-12b23d66090e)

                    - Empirical methodology (strategy)

                        - [The empirical strategy is justified](This methodological choice is considered as the [[exogenous variation/change]] and the level of analysis.) due to [the [[exogenous variation/change]]](((yQnq2xM93))) and the level of analysis **being lab-pairs**.

                        - estimating the effect of colocation on inventive outcomes using observational data (p.4353) = a [[difference in difference analysis]]

                            - at the lab-pair-year level which exploits the variation in colocation and separation generated by the moves during asbestos-removal period (p.4354)

Control variable ([[explanatory variable]]) = colocation / separation, outcome variable = inventive outcome (dummy, 1/0?) 

The effect estimating equation in p.4354 as below, but also on nonlinear models and for different outcomes  

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Pc0-HEko.png?alt=media&token=3f8be83b-81e1-4a49-a2eb-b5a4b941e427)

                        - This methodological choice is considered as the [[exogenous variation/change]] and the level of analysis.

                            - The methodology is **generally** likely to be biased: when labs value proximity to other labs they want to collaborate with, there is a [[selection effect of innovation]] that makes an [[endogeneity bias]]

For the case of this paper, there is an [[exogenous variation/change]] in terms of what neighbors a lab is offered 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F2OJbwdiKpv.png?alt=media&token=5f9d77e2-f449-4f77-a841-bb68dfae5241) (p.4353)

                            - The paper analyzes by lab-pair [[fixed effects]] to account for idiosyncratic reasons a lab pair may be more or less likely to collaborate in the first place. It also captures the degree of influence a pair of labs may have on campus resource allocation decisions (funding, personnel, space allocation). The analysis is different from [lab-year analysis](Results for lab-year re: equation (1) in p.4354 follows a similar [empirical strategy for lab pair](((JLp1k67tW))).). 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FcvL3IIHNzY.png?alt=media&token=2608c7f7-a094-44ea-9d61-a5dcb21e2def)

Based on ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fadav3cOO2h.png?alt=media&token=046db09b-4946-4358-803b-058adcc33ddf)  [[Xin Qian]]'s personal understanding is that they stratified by each lab's porforlio (same lab, different lab in institution, other French lab, international lab)

Definition of [[fixed effects]]: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fct0zMGQgM-.png?alt=media&token=fdc2c611-e0a5-4aa0-b7d8-277e9a75a25d)

                            - Results for lab-year re: equation (1) in p.4354 follows a similar [empirical strategy for lab pair](at the lab-pair-year level which exploits the variation in colocation and separation generated by the moves during asbestos-removal period (p.4354)

Control variable ([[explanatory variable]]) = colocation / separation, outcome variable = inventive outcome (dummy, 1/0?) 

The effect estimating equation in p.4354 as below, but also on nonlinear models and for different outcomes  

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Pc0-HEko.png?alt=media&token=3f8be83b-81e1-4a49-a2eb-b5a4b941e427)).

                                - Question: are the second row numbers (numbers? what goes inside the bracket?) reporting the coefficient β? ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fmi5KQidNYs.png?alt=media&token=bec12ec7-ac04-4653-8d93-caaf4f638653)

                                - outcome = shares of affiliations on the labs' papers changed during the moves ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FIm8URL-rmQ.png?alt=media&token=37865c6f-811d-4099-8a44-4116f377bf3c)

                                - Another result table at the lab-level highlights the breakdown between [[intensive margin lab pairs]] vs. [[extensive margin lab pairs]] group (whether labs had collaborated before relocation) (p.4356)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FBDkqP4r5Sv.png?alt=media&token=fff03829-b955-4852-9c98-4bd4153864bd)

                    - Disentangle the result of 3.5 ?

                        - [[Xin Qian]] didn't locate precisely where 3.5 comes from except this mention 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FLXzwQWkxRr.png?alt=media&token=0ff70ac8-1cbd-4888-8ec4-9144d74fde72)

                        - **Experiment data**: publication records, citation information, geolocation data with re-identification API, affiliation string disambiguation (p.4352)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6-hcia7ue_.png?alt=media&token=5888c128-c385-40fc-b8d5-26b99cc331b7)

                    - It supports a global claim (beyond the scope of this paper): [[colocation (matters for the) innovation/collaboration]]

                        - (Among which) the effect is (mostly driven by?) on lab pairs that face higher [[estimated [[search costs of innovation]]]]

                            - [[estimated [[search costs of innovation]]]] = knowledge distance between labs (p.4354) or Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).

                                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FeHz2raln6N.png?alt=media&token=ad09be8f-a679-45dc-8ad5-5b73f136631c)

                                - Cases where [[estimated [[search costs of innovation]]]] is already **low** means researchers attend the same conferences or read the same journals

                            - For lab-pairs with low [[estimated [[search costs of innovation]]]], column (1) and (3) shows that colocation has a positive but nonsignificant effect on the probability of collaboration

                                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FeSPUVLVr2Z.png?alt=media&token=0e2cb913-3466-4998-957a-aa8f6f42fd5a)

                - Claim new #2: [[separated labs / separation]] (characterized as [a longitutional lab relocation process](8YBG3lapX) that [created varying lab pairs](((CZYRQVrOj)))) [does not negatively affect](((dteyHW8K8))) whether-not collaboration: the estimated coefficient $$\beta(separation) = .0101, p(separate)>0.01$$, meaning as **positive and non-significant**, on whether-not collaboration between previously colocated lab. Explanation is that past exposure allows labs to contact a now-distant lab after the right opportunity has been identified.

                    - Column (1) and (2) show non-significant effect (p.4358). ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fr6s-Vp5FfL.png?alt=media&token=d82ce768-be2c-468a-ae20-0d77a2a21c95)

                    - [[search costs of innovation]] and [[Execution costs of innovation]] are largely implicit factors in this process (i.e., that does not show in the table as variables).

                - Claim new #3: [[separated labs / separation]] (characterized as [a longitutional lab relocation process](8YBG3lapX) that [created varying lab pairs](((CZYRQVrOj)))) [does not negatively affect](((DbHbtfPvk))) # of collaboration: the estimated coefficient $$\beta(\# of collaboration | separation) = - 0.4520, p(\# of collaboration | separation)>0.01$$, meaning as **negative and non-significant**, on the Poisson # of collaboration between previously colocated lab. Explanation is that past exposure allows labs to contact a now-distant lab after the right opportunity has been identified.

                    - Column (3) shows negative and non-significant effect (p.4358). ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fr6s-Vp5FfL.png?alt=media&token=d82ce768-be2c-468a-ae20-0d77a2a21c95)

                    - [[search costs of innovation]] and [[Execution costs of innovation]] are largely implicit factors in this process (i.e., that does not show in the table as variables).

                - Claim new #4: [the lab-year trends of separation on collaboration](![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKf8wfQ69tX.png?alt=media&token=33686225-82b4-472a-8338-cbae0c524920)) show a higher propensity to collaborate before the move, a slight decay in collaboration, and revert to mean collaboration propensity later. (These findings don't have numbers but a figure)

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKf8wfQ69tX.png?alt=media&token=33686225-82b4-472a-8338-cbae0c524920)

                - 

                - Review{{TODO}} Claim #4: Colocated lab pairs grow increasingly [similar (based on paper definition)](Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).) : find result table and numbers

                - New Claim #5: When previous search costs between lab pairs [(determined by proximity in knowledge space, abbr. as similarity, based on either keywords, or cited reference)](Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).) are low, colocation has **a positive but nonsignificant effect **on the probability of collaboration. $$\beta(collaborate|colocation, prev\;similar\;lab\;pairs) = .0056$$, according to [row 1 of column (1) data](((RnnfBKkGz)))

                - New Claim #6: When previous search costs between lab pairs [(determined by proximity in knowledge space, abbr. as similarity, based on either keywords, or cited reference)](Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).) are low, separation induces a decay in the likelihood of collaboration, $$\beta(collaborate|separation, prev\;similar\;lab\;pairs) = -.0197$$, according to [row 1 of column (1) data](((RnnfBKkGz))), where the author hypothesized as because some of marginal, within-field collaborations are only sustainable when joint execution costs are low.

                - New Claim #6: When previous search costs between lab pairs are high, colocation has **a positive and significant effect** $$p(collaborate|colocation, prev\;not-similar\;lab\;pairs) = .0179$$ in topics and literature cited.

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FeSPUVLVr2Z.png?alt=media&token=0e2cb913-3466-4998-957a-aa8f6f42fd5a)

                    - This claim supports a global claim: [[colocation (matters for the) innovation/collaboration]].

                    - Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).

                - Claim #5: The paper abstracts concludes that [[separated labs / separation]] [embark on less correlated](((9lQZMPd_a))) research trajectories.

            - Secondarily from Section 4.3

            - 

            - 

            - 

            - 

            - 

            - 

            - 

            - 

            - 

            - 

        - #[[observation-notes]] (starting from claims, and enrich the claim with details - created in week 4, and revised into flat claim with hyperlink in week 5, Spring 2021)

            - Additional observation notes (starting from claims, and enrich the claim with details) - created in week 4 and revised in week 5, Spring 2021

                Claim #1: [As an overarching claim, and a presupposition from prior literature](This can also be understood as an overarching claim, a presupposition summarized from prior work, or an ensemble of Claim #2 and Claim #4 (p.4349) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FT61THTC3UV.png?alt=media&token=aa13d12d-e778-4c48-9275-e5d374344359)), the paper states that [[search costs of innovation]] constitutes major friction to collaboration. This claim also [vaguely attributes / defines](((0RgWDii9F))) [[search costs of innovation]].

                    This can be understood simply as a definition of [[search costs of innovation]] (p.4350) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FiIORbQ0sXj.png?alt=media&token=6633034f-444f-470d-aebd-6c62ffe13eb3)

                    This can also be understood as an overarching claim, a presupposition summarized from prior work, or an ensemble of Claim #2 and Claim #4 (p.4349) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FT61THTC3UV.png?alt=media&token=aa13d12d-e778-4c48-9275-e5d374344359)

                Claim #2: The paper abstract summarizes [its major empirical result, i.e., the natural experiment](Empirical methodology (strategy) = estimating the effect of colocation on inventive outcomes using observational data (p.4353) = a [[difference in difference analysis]] at the lab-pair-year level which exploits the variation in colocation and separation generated by the moves during asbestos-removal period (p.4354)

Control variable ([[explanatory variable]]) = colocation / separation, outcome variable = inventive outcome (dummy, 1/0?) 

The effect estimating equation in p.4354 as below, but also on nonlinear models and for different outcomes  

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Pc0-HEko.png?alt=media&token=3f8be83b-81e1-4a49-a2eb-b5a4b941e427)) as colocation increases the likelihood of joint research by 3.5 times. [The empirical strategy is justified](((H0WvYsFEe))) due to [the [[exogenous variation/change]]](((hJ69uDZcJ))) and [the level of analysis being lab-pairs](). It supports a global claim (beyond the scope of this paper): [[colocation (matters for the) innovation/collaboration]]

                    Empirical methodology (strategy) = estimating the effect of colocation on inventive outcomes using observational data (p.4353) = a [[difference in difference analysis]] at the lab-pair-year level which exploits the variation in colocation and separation generated by the moves during asbestos-removal period (p.4354)

Control variable ([[explanatory variable]]) = colocation / separation, outcome variable = inventive outcome (dummy, 1/0?) 

The effect estimating equation in p.4354 as below, but also on nonlinear models and for different outcomes  

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Pc0-HEko.png?alt=media&token=3f8be83b-81e1-4a49-a2eb-b5a4b941e427)

                    The paper described the argument for this methodological choice as the [[exogenous variation/change]] and the level of analysis.

                        The methodology is **generally** likely to be biased: when labs value proximity to other labs they want to collaborate with, there is a [[selection effect of innovation]] that makes an [[endogeneity bias]]

For the case of this paper, there is an [[exogenous variation/change]] in terms of what neighbors a lab is offered 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F2OJbwdiKpv.png?alt=media&token=5f9d77e2-f449-4f77-a841-bb68dfae5241) (p.4353)

                        The paper analyzes by lab-pair [[fixed effects]] to account for idiosyncratic reasons a lab pair may be more or less likely to collaborate in the first place. It also captures the degree of influence a pair of labs may have on campus resource allocation decisions (funding, personnel, space allocation). The analysis is different from [lab-year analysis](Results for lab-year re: equation (1) in p.4354 follows a similar [empirical strategy for lab pair](((r6v87AIRP))).). 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FcvL3IIHNzY.png?alt=media&token=2608c7f7-a094-44ea-9d61-a5dcb21e2def)

Based on ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fadav3cOO2h.png?alt=media&token=046db09b-4946-4358-803b-058adcc33ddf)  [[Xin Qian]]'s personal understanding is that they stratified by each lab's porforlio (same lab, different lab in institution, other French lab, international lab)

Definition of [[fixed effects]]: ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fct0zMGQgM-.png?alt=media&token=fdc2c611-e0a5-4aa0-b7d8-277e9a75a25d)

                        Results for lab-year re: equation (1) in p.4354 follows a similar [empirical strategy for lab pair](Empirical methodology (strategy) = estimating the effect of colocation on inventive outcomes using observational data (p.4353) = a [[difference in difference analysis]] at the lab-pair-year level which exploits the variation in colocation and separation generated by the moves during asbestos-removal period (p.4354)

Control variable ([[explanatory variable]]) = colocation / separation, outcome variable = inventive outcome (dummy, 1/0?) 

The effect estimating equation in p.4354 as below, but also on nonlinear models and for different outcomes  

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0Pc0-HEko.png?alt=media&token=3f8be83b-81e1-4a49-a2eb-b5a4b941e427)).

                            Question: are the second row numbers (numbers? what goes inside the bracket?) reporting the coefficient β? ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fmi5KQidNYs.png?alt=media&token=bec12ec7-ac04-4653-8d93-caaf4f638653)

                            outcome = shares of affiliations on the labs' papers changed during the moves ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FIm8URL-rmQ.png?alt=media&token=37865c6f-811d-4099-8a44-4116f377bf3c)

                            Another result table at the lab-level highlights the breakdown between [[intensive margin lab pairs]] vs. [[extensive margin lab pairs]] group (whether labs had collaborated before relocation) (p.4356)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FBDkqP4r5Sv.png?alt=media&token=fff03829-b955-4852-9c98-4bd4153864bd)

                    (Among which) the effect is (mostly driven by?) on lab pairs that face higher [[estimated [[search costs of innovation]]]]

                        [[estimated [[search costs of innovation]]]] = knowledge distance between labs (p.4354) or Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).

                            ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FeHz2raln6N.png?alt=media&token=ad09be8f-a679-45dc-8ad5-5b73f136631c)

                            Cases where [[estimated [[search costs of innovation]]]] is already **low** means researchers attend the same conferences or read the same journals

                        For lab-pairs with low [[estimated [[search costs of innovation]]]], column (1) and (3) shows that colocation has a positive but nonsignificant effect on the probability of collaboration

                            ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FeSPUVLVr2Z.png?alt=media&token=0e2cb913-3466-4998-957a-aa8f6f42fd5a)

                    Disentangle the result of 3.5

                        [[Xin Qian]] didn't locate precisely where 3.5 comes from except this mention 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FLXzwQWkxRr.png?alt=media&token=0ff70ac8-1cbd-4888-8ec4-9144d74fde72)

                        **Experiment data**: publication records, citation information, geolocation data with re-identification API, affiliation string disambiguation (p.4352)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F6-hcia7ue_.png?alt=media&token=5888c128-c385-40fc-b8d5-26b99cc331b7)

                Claim #3: [[separated labs / separation]], characterized in this paper as [a longitutional lab relocation process](Starting 1997, five massive waves of lab relocation in the university campus of Paris Jussieu due to a ban of fire retardant (e.g., asbestos) in public buildings. Each time the lab faced short notice and with little influence on new location (p.4349) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F3o2PLpqkUw.png?alt=media&token=976fba0a-af61-48d4-8771-da01fbaaff2c) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FnHZ4zqm-WA.png?alt=media&token=3090f6d2-e95f-4b51-8304-3dc98d83cb15)) that [created varying lab pairs](((mTcI1tw1x))), [does not negatively affect](((7fih25Rah))) collaboration between previously colocated labs

                    Charactizing the separation

                        Starting 1997, five massive waves of lab relocation in the university campus of Paris Jussieu due to a ban of fire retardant (e.g., asbestos) in public buildings. Each time the lab faced short notice and with little influence on new location (p.4349) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F3o2PLpqkUw.png?alt=media&token=976fba0a-af61-48d4-8771-da01fbaaff2c) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FnHZ4zqm-WA.png?alt=media&token=3090f6d2-e95f-4b51-8304-3dc98d83cb15)

                        Separation creates new neighbors (lab pairs, with large variations) (p.4352) ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMAkM9Sam-J.png?alt=media&token=7a67b947-74ad-45e3-8d04-82e52e2c8adf)

                        Effect of [[separated labs / separation]] on collaboration propensity (p.4358)

                            Remains positive, despite a short drop around 0 - +1 year after separation.

                                Side note: the data for this figure likely drops all lab pairs where collaboration is never observed, hence the smaller number of observations.

                                    Also a limitation of entire study: [[sample size issue]]

                                        [[collaboration across labs are rare relative to collaborations within labs]], which limits the the set of tests that can be conducted on this sample (e.g., further splits of the sample across more fine-grained dimensions). (p.4361)

                                ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F4yeFWFlhwZ.png?alt=media&token=94d6310f-d03b-40f0-a510-a5feb1c99dd8)

                    Results show non-significant effect (p.4358), where [[search costs of innovation]] and [[Execution costs of innovation]] are largely implicit (i.e., that does not show in the table as variables) factors. ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fr6s-Vp5FfL.png?alt=media&token=d82ce768-be2c-468a-ae20-0d77a2a21c95)

                Claim #4: Paper results suggest that colocated lab pairs grow increasingly [similar (based on paper definition)](Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).) in topics and literature cited. This claim supports a global claim: [[colocation (matters for the) innovation/collaboration]].

                    Measurement / definition on [[lab-pair similarity]]  ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fb5S-ponFte.png?alt=media&token=052846a4-a7bf-4372-bb53-301bd80915e1) (p.4353) where **Cited references** are the articles, books or other materials listed in a bibliography or as works **cited** in a particular publication. Another rephrase of the definition in p.4358 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0mBwXGSbCH.png?alt=media&token=c8dd2cb7-f27a-44b3-b4c8-0d3fe73bcb90). The metric can be interpreted by the value as ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F7WYMv2-fuO.png?alt=media&token=51465fdc-1702-40fb-b161-1c123635c920) (p.4353).

                Claim #5: The paper abstracts concludes that [[separated labs / separation]] [embark on less correlated](Understanding from reader's perspective, by less correlated, the paper demonstrates with Figure 3(b) similarity in red, lower trend line for separation (p.4360)) research trajectories.

                    Understanding from reader's perspective, by less correlated, the paper demonstrates with Figure 3(b) similarity in red, lower trend line for separation (p.4360)

                        ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FMiLLHduKnW.png?alt=media&token=c0e16d0f-a69e-492b-a842-dc0b210a1f38)

                Claim #6: [Research outcomes]([[Research outcomes]] ~ = [[Research project quality]] only to the observable degree. (p.4359) the analysis is conditional on a project being developed, but empirically an additional issue arises from the fact that **not all projects are observed**: e.g., if scientists are overly optimistic about their chances of publishing their results, or if part of the projects that are initially developed are dropped before submission, then we will never see projects of the lowest quality (aka lowest [[Research outcomes]]). Also phrased as "that end up in a peer-reviewed publication are observed, meaning that the left tail of the outcome distribution (aka low-quality ones) is not observed. serendipitous). cited references and keywords may be able to capture the outcome of some of the interactions (planned or serendipitous) that do not translate into a paper, the analyses on the rate and quality of research misses them." (p.4361) To [[Xin Qian]]'s understanding, [[Research outcomes]] could be a concept to incorporate in [[D/Computational Analogy]] study design) ) are most influenced by how distance affects [[Execution costs of innovation]], i.e., [[Execution costs of innovation]] shape the quality of output. This claim is a union of [Claim #7](((rp0ul8wuM))) and [Claim #8](((5raNbWg4O))).

                    [[Research outcomes]] ~ = [[Research project quality]] only to the observable degree. (p.4359) the analysis is conditional on a project being developed, but empirically an additional issue arises from the fact that **not all projects are observed**: e.g., if scientists are overly optimistic about their chances of publishing their results, or if part of the projects that are initially developed are dropped before submission, then we will never see projects of the lowest quality (aka lowest [[Research outcomes]]). Also phrased as "that end up in a peer-reviewed publication are observed, meaning that the left tail of the outcome distribution (aka low-quality ones) is not observed. serendipitous). cited references and keywords may be able to capture the outcome of some of the interactions (planned or serendipitous) that do not translate into a paper, the analyses on the rate and quality of research misses them." (p.4361) To [[Xin Qian]]'s understanding, [[Research outcomes]] could be a concept to incorporate in [[D/Computational Analogy]] study design)

                Claim #7: After [[colocation (matters for the) innovation/collaboration]] happens (i.e., during the state of colocation), labs are [more likely to](Below result table explores how the [[Research project quality]] changes after the moves, conditional on the lab pairs (p.4361): 

Overall, colocation seems to increase the number of collaborations that will end **on both tails of** the distribution (first and fourth quartiles), and to decrease activity in the third quartile (negative and significant) and potentially in the second quartile (negative but not significant). 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FflQDKo_636.png?alt=media&token=50c55d5d-9772-4e3e-af0d-e0a1a7d84b01) 

One interpretation of this result is that these [[colocation (matters for the) innovation/collaboration]] constitute **arbitrage opportunities** across domains of science, and that if we were able to observe these pairs for substantially longer periods of time, the positive effect on the right tail may revert to the mean. (why? short-term benefit?) (p.4360) 

Another interpretation is that once faced with a more heterogeneous set of local peers, labs were encouraged to embark on higher-risk, higher-reward projects (which would be consistent with the increase in variance). (p.4360)) pursue both [lower-quality](((m1mVPB1Y4))) projects (a selection effect) and [higher-quality](((m1mVPB1Y4))) projects (an effort effect).

                    [[Research project quality]] = citation distribution, see also definition of [[Research outcomes]]

                    Below result table explores how the [[Research project quality]] changes after the moves, conditional on the lab pairs (p.4361): 

Overall, colocation seems to increase the number of collaborations that will end **on both tails of** the distribution (first and fourth quartiles), and to decrease activity in the third quartile (negative and significant) and potentially in the second quartile (negative but not significant). 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FflQDKo_636.png?alt=media&token=50c55d5d-9772-4e3e-af0d-e0a1a7d84b01) 

One interpretation of this result is that these [[colocation (matters for the) innovation/collaboration]] constitute **arbitrage opportunities** across domains of science, and that if we were able to observe these pairs for substantially longer periods of time, the positive effect on the right tail may revert to the mean. (why? short-term benefit?) (p.4360) 

Another interpretation is that once faced with a more heterogeneous set of local peers, labs were encouraged to embark on higher-risk, higher-reward projects (which would be consistent with the increase in variance). (p.4360)

                    Terms explained:

                        [[selection effect of innovation]]: From [[@cataliniMicrogeographyDirectionInventive2017]]: Selects which project to execute

                        [[effort effect of innovation]]: from [[@cataliniMicrogeographyDirectionInventive2017]]: Applying effort in execution to improve the quality of an idea (p.4349) [[TODO: add screenshot]]

                Claim #8: after [[separated labs / separation]] happens, lab pairs [does not lead to](Lab pairs that usually face high search costs (potentially also because space allocation is generally optimized by discipline) **are not only more responsive to** (sounds that responsive means negatively) changes in the distance (as we have seen in Table 7 ), but are also able to produce higher-impact research **when given the opportunity** (this clause sounds to be hypothetical) to take advantage of lower execution cost (why? meaning low-quality projects?) (p.4360-4361) 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUwoNTxaBIB.png?alt=media&token=594d4ffe-f2b7-4ace-8b63-e60e53481dce)) high-quality projects. It is opposite to [Claim #7](((rp0ul8wuM))).

                    Lab pairs that usually face high search costs (potentially also because space allocation is generally optimized by discipline) **are not only more responsive to** (sounds that responsive means negatively) changes in the distance (as we have seen in Table 7 ), but are also able to produce higher-impact research **when given the opportunity** (this clause sounds to be hypothetical) to take advantage of lower execution cost (why? meaning low-quality projects?) (p.4360-4361) 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUwoNTxaBIB.png?alt=media&token=594d4ffe-f2b7-4ace-8b63-e60e53481dce)

                Claim #9: recombination of ideas from more distant domains exhibit [[higher-variance projects]]

                    [[higher-variance projects]] = projects that offered higher **risk** but also higher **reward**

                        Note that risk and reward could be concepts to incorporate in [[D/Computational Analogy]] study design (e.g., questionnaire)

                    Relevant paper {{TODO}} check whether they are necessary to read.

                        Fleming L, Sorenson O (2004) Science as a map in technological search. Strategic Management J. 25(8–9):909–928.

                        Singh J, Fleming L (2010) Lone inventors as sources of breakthroughs: Myth or reality? Management Sci. 56(1):41–56.

                Claim #10: [Empirically, paper results show that the decay in across-lab collaborations is mostly driven by](Another result table at the lab-level highlights the breakdown between [[intensive margin lab pairs]] vs. [[extensive margin lab pairs]] group (whether labs had collaborated before relocation) (p.4356)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FBDkqP4r5Sv.png?alt=media&token=fff03829-b955-4852-9c98-4bd4153864bd))::::: [extensive margin lab pairs](((Lsc_NuToG)))—i.e., during the relocations, labs were substantially less likely to explore research with labs they had not collaborated with before.

                    Extensive margin lab pairs = collaborations (i.e., between labs that had NOT collaborated before the relocations versus not) (p.4356)

                Claim #11: [The effect of geography only **slightly facilitating (or obstructing)** collaborative work](Another result table at the lab-level highlights the breakdown between [[intensive margin lab pairs]] vs. [[extensive margin lab pairs]] group (whether labs had collaborated before relocation) (p.4356)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FBDkqP4r5Sv.png?alt=media&token=fff03829-b955-4852-9c98-4bd4153864bd)) on the [intensive margin lab pairs](((0NtQcdDJY))) (the coefficients are respectively positive in column (6) and negative in column (8), but in both cases not significant

                    Intensive margin lab pairs = collaborations (i.e., between labs that had collaborated before the relocations) (p.4356)

###### Discourse Context

- **Informs::** [[QUE - What are the most efficient routes to useful cross-boundary knowledge]]
- **Informs::** [[QUE - How and in what ways is collocation important for collaborative innovation]]
