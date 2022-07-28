---
title: [[QUE]] - How can we augment scientific creativity with computational analogy?
url: https://roamresearch.com/#/app/megacoglab/page/HESVKgDk5
author: Joel Chan
date: Sat Sep 19 2020 00:56:45 GMT+0800 (Malaysia Time)
---

- [[question]]

    - Tags: key question for [[DComputational Analogy]]

    - Description {{word-count}}

        - Analogy is defined by relational similarity

            - [[@gentnerStructureMappingAnalogy1997]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0CKJWoVGw.png?alt=media&token=2cac9f86-f961-4fab-9bc0-51df1ca4265f)

        - [[CLM - Analogical retrieval in humans is dominated by surface similarity]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FO5kmmXtt-d.png?alt=media&token=0ed35b29-10c3-4304-b35d-2687537c808f)

        - [[CLM - There is a 'Sweet Spot' in Analogical Distance. Somewhat far analogies lead to better creative outcomes than very near or very far analogies]]

        - Contribution: [[idea purpose-mechanism schema]]

            - [[idea purpose-mechanism schema]]

                - Purpose mechanism can be annotated feasibly, even for highly technical papers

                - We have working classifiers that do a fairly good job (F = ~.6ish?) of tagging purpose segments / spans in scientific texts

                    - Started with predicting overall soft vector

                    - Then did [[bi-LSTM]]

                    - Then did [[SpanRel]]

                        - This is currently our best-performing model (from our [unpublished manuscript](https://www.overleaf.com/project/5ee79084c20b3600018007b8))

                            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F36f_QbCHs6.png?alt=media&token=0b99d205-4254-4eda-9192-62af68ef552e))

                        - I'm a bit nervous about these numbers because we're still using the CSCW 50 papers from [[@chanSOLVENTMixedInitiative2018]]

                            - can reach out ot [[Kenneth Huang]]

                                - --> [[datasetCODA-19]]

                                    - https://twitter.com/windx0303/status/1258427687191883778

                                - caveat is that purpose accuracy is... not great - F of about .6

                                - also shows later in [[@huangCODA19UsingNonExpert2020]]

                                - some nice comments in a submission here:

                                    - https://openreview.net/forum?id=XOkm8xdns5R&noteId=KMIbNQ-oqQK

                                - not sure how this intersects with genre stuff though... important open question and threat for our approach. we're making a major assumption that enough of what we need is in abstracts. is that true?

                                    - could be nuanced: abstract could be enough for purpose

                                    - but other stuff we need to get from

                                        - full-text

                                        - citation statements

                                        - etc

                    - [[Tom Hope]]

                    - And we've also explored the utility and feasibility of [[sysSnorkel]]

                        - IIRC, works better for purpose than mechanism

                - i think there is still some room here for improvement

                    - wondering about integration with [[sysSemantic Scholar]]

                        - coudl also get some real-time data on matches? not sure though - analytics on usage rate will be tough to get - real signal is whether it gets added to your library, which mendeley has

                            - so maybe integration with [[sysMendeley]]

            - [[idea purpose-mechanism schema]]

                - Can find matches

                    - For product texts [[@hopeAcceleratingInnovationAnalogy2017]]

                    - And also science papers [[@chanSOLVENTMixedInitiative2018]]

                        - New stuff from [[Hyeonsu]]

                - Interestingly, even when the purpose span predictions aren't super great, F-wise, we do ok

                    - Saw this with our explorations of [[sysSnorkel]]

        - [[CLM - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

###### Discourse Context

- **Informed By::** [[CLM - There is a 'Sweet Spot' in Analogical Distance. Somewhat far analogies lead to better creative outcomes than very near or very far analogies]]
- **Informed By::** [[CLM - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]
- **Informed By::** [[CLM - Analogical retrieval in humans is dominated by surface similarity]]
- **Informed By::** [[@hopeAcceleratingInnovationAnalogy2017]]
- **Informed By::** [[@chanSOLVENTMixedInitiative2018]]
- **Informed By::** [[@gentnerAnalogicalRemindingGood1985]]
- **Informed By::** [[@gentnerStructureMappingAnalogy1997]]
- **Informed By::** [[@huangCODA19UsingNonExpert2020]]
