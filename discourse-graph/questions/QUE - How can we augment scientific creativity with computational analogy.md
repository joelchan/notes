---
title: [[QUE]] - How can we augment scientific creativity with computational analogy?
url: https://roamresearch.com/#/app/megacoglab/page/HESVKgDk5
author: Joel Chan
date: Fri Sep 18 2020 12:56:45 GMT-0400 (Eastern Daylight Time)
---

- #[[Question]]

    - Tags: key question for #[[D/Computational Analogy]]

    - Description {{word-count}}

        - Analogy is defined by relational similarity

            - [[@gentnerStructureMappingAnalogy1997]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FC0CKJWoVGw.png?alt=media&token=2cac9f86-f961-4fab-9bc0-51df1ca4265f)

        - [[[[CLM]] - Analogical retrieval in humans is dominated by surface similarity]] [[@gentnerAnalogicalRemindingGood1985]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FO5kmmXtt-d.png?alt=media&token=0ed35b29-10c3-4304-b35d-2687537c808f)

        - [[[[CLM]] - There is a 'Sweet Spot' in Analogical Distance. Somewhat far analogies lead to better creative outcomes than very near or very far analogies]]

        - Contribution: [[idea: purpose-mechanism schema]]

            - [[idea: purpose-mechanism schema]] is feasible target for scaling up

                - Purpose mechanism can be annotated feasibly, even for highly technical papers

                - We have working classifiers that do a fairly good job (F = ~.6ish?) of tagging purpose segments / spans in scientific texts

                    - Started with predicting overall soft vector

                    - Then did [[bi-LSTM]]

                    - Then did [[SpanRel]] + some other magic.

                        - This is currently our best-performing model (from our [unpublished manuscript](https://www.overleaf.com/project/5ee79084c20b3600018007b8))

                            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F36f_QbCHs6.png?alt=media&token=0b99d205-4254-4eda-9192-62af68ef552e))

                        - I'm a bit nervous about these numbers because we're still using the CSCW 50 papers from [[@chanSOLVENTMixedInitiative2018]] as our test set. This is a low-hanging fruit thing that is worth exploring further, and we'll need much more data for this

                            - can reach out ot [[Kenneth Huang]] who has ~11k COVID-19 papers annotated

                                - --> [[dataset/CODA-19]]

                                    - https://twitter.com/windx0303/status/1258427687191883778

                                - caveat is that purpose accuracy is... not great - F of about .6

                                - also shows later in [[@huangCODA19UsingNonExpert2020]] that [[sys/SciBERT]] actually does a really good job, about .7ish as well

                                - some nice comments in a submission here:

                                    - https://openreview.net/forum?id=XOkm8xdns5R&noteId=KMIbNQ-oqQK

                                - not sure how this intersects with genre stuff though... important open question and threat for our approach. we're making a major assumption that enough of what we need is in abstracts. is that true?

                                    - could be nuanced: abstract could be enough for purpose

                                    - but other stuff we need to get from

                                        - full-text

                                        - citation statements

                                        - etc

                    - [[Tom Hope]] has also explored using graph-based methods to augment the attention mechanisms

                    - And we've also explored the utility and feasibility of [[sys/Snorkel]]-like [[weak supervision]] to do a cue-based thing.

                        - IIRC, works better for purpose than mechanism

                - i think there is still some room here for improvement

                    - wondering about integration with [[sys/Semantic Scholar]]??

                        - coudl also get some real-time data on matches? not sure though - analytics on usage rate will be tough to get - real signal is whether it gets added to your library, which mendeley has

                            - so maybe integration with [[sys/Mendeley]] is the thing to explore.

            - [[idea: purpose-mechanism schema]] is useful for supporting analogical search

                - Can find matches

                    - For product texts [[@hopeAcceleratingInnovationAnalogy2017]]

                    - And also science papers [[@chanSOLVENTMixedInitiative2018]]

                        - New stuff from [[Hyeonsu]], with case study data

                - Interestingly, even when the purpose span predictions aren't super great, F-wise, we do ok

                    - Saw this with our explorations of [[sys/Snorkel]] too

        - [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

###### References

[[about these notes]]

- [[[[QUE]] - How can we augment scientific creativity with computational analogy?]]

    - [[[[QUE]] - How might domain distance modulate the effects of analogies on creative output?]]

        - [[[[CLM]] - There is a 'Sweet Spot' in Analogical Distance. Somewhat far analogies lead to better creative outcomes than very near or very far analogies]]

    - [[[[QUE]] - What are the mechanisms by which analogies help drive creative breakthroughs?]]

    - [[[[QUE]] - What factors control whether people appropriately benefit from analogies (especially far-field ones) during creative problem solving?]]

    - [[[[QUE]] - Can deep learning discover analogical representations?]]

    - [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]
