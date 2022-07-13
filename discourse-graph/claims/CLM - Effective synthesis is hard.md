---
title: [[CLM]] - Effective synthesis is hard
url: https://roamresearch.com/#/app/megacoglab/page/wCVWAVCp6
author: Joel Chan
date: Thu Apr 30 2020 15:40:50 GMT-0400 (Eastern Daylight Time)
---

- #[[🌲 zettels]]

    - Tags: #synthesis #[[Z]]

    - Description

        - For example, [[[[CL]] - Systematic reviews are rarely updated even when they need to be]]

        - Synthesis also takes a really long time! For example, we know that [[[[CL]] - Systematic reviews take a very long time to complete and update]]

        - [[systematic review]]s are so painful that some describe it as being "[enslaved to the trapped data](#> The Data Extraction Process seemed particularly demanding to those involved in the corresponding tasks. The Coordinating Editor (P1) described [[systematic review]]ers as being "enslaved to the trapped data", with reviewers "chiseling the mine" to get at the data they needed. (p.208) #synthesis)" #[[@knightEnslavedTrappedData2019]].

        - See also: [[[[CLM]] - Doctoral students struggle to effectively synthesize literature]]

    - R-Sources

        - #[[@jonesBurdenKnowledgeDeath2009]]

            - #> "...if one is to stand on the shoulders of giants, one must first climb up their backs, and the greater the body of knowledge, the harder this climb becomes."  (p.284) #synthesis

        - [[@greenhalghTimeChallengeSpurious2018]]

            - #CLlaim [[[[CLM]] - [[systematic review]]s are typically narrowly focused, and provide less insight]]

        - [[Notes from discussion with UMD START folks]] about [[IVEO Matrix]] and how it was so hard that they instituted rules for managing expectations as a result of that

###### Discourse Context

- **Informed By::** [[@knightEnslavedTrappedData2019]]
- **Informed By::** [[@greenhalghTimeChallengeSpurious2018]]
- **Informed By::** [[@jonesBurdenKnowledgeDeath2009]]

###### References

[[December 6th, 2020]]

- Quick idea: to make motivation for [[D/Synthesis Infrastructure]], and work out consequences of [[[[CLM]] - Effective synthesis is hard]] and [[[[CLM]] - Effective synthesis is rare]]...

    - It's hard to measure these, they're like hidden costs

    - But we can make some analogies here, maybe, to software reuse: imagine that everytime you started a new project, you either had to a) start from scratch, or b) run through a terrible gauntlet to get to reusable code (e.g., everyone else's code is poorly documented)

        - What is the estimated force multiplier of having access to clean reusable code in software engineering?

        - Could extrapolate a bit then to our setting
[[May 8th, 2020]]

- More on [[[[CLM]] - Effective synthesis is rare]] and/or [[[[CLM]] - Effective synthesis is hard]]

    - Important new paper to read, updates on [[@petrosino1999lead]] to give insight into the process and challenges of producing [[systematic review]]s (particularly [[Cochrane systematic reviews]]): [[@turnerProducingCochraneSystematic2017]]

    - lots more insight into the challenges of [[systematic review]] process in [[@ervinMotivatingAuthorsUpdate2008]]

    - Spending more time on the upfront stuff because I want to crystallize what the requirements are **for** (for [[P: Synthesis requirements theory paper]])

        - To reiterate, it's about requirements for data structures, and then ideas about authoring tools that can get us there (diagnosing as UX problem). Mostly individual, not focused on tools to support __collaborative__ sensemaking and synthesis.

            - The collaborative piece comes into play as we think about the possible mechanisms for constructing and managing the [[infrastructure]], not the target activity per se

    - [[I wonder]] if [[systematic review]]s [tend to be way more narrow]( [[@greenhalghTimeChallengeSpurious2018]] then cites [[@thorneRediscoveringNarrativeReview2018]] to critique the fetishizing of systematic reviews, noting that (similar ot my point), ((3tX8yzDeS)).) precisely because [[[[CLM]] - Effective synthesis is hard]]?

    - Struck by how many of these threads are in specialized journals. Not in infosci. WHY?? Too niche?

    - This paper [[@reyndersContactingAuthorsModified2019]] is super interesting: it's kind of about [[context]]

        - [[systematic review]] teams very frequently (on the order of 70% of the time) need to contact authors for additional details (context) for reported findings #synthesis

        - When extra information is obtained from authors, this frequently changes the review in substantial ways

    - #[[@flemingCochraneNonCochraneSystematic2013]]
[[May 1st, 2020]]

- Chewing again on this thread: There is definitely a sense in the scholarly air that review papers (though immensely valuable to a field) are very hard to write, and somewhat of a "fool's errand" for [[ECRs]]. But I'm wondering now about the numbers and precision behind this sense. __Are__ review papers really all that rare?  on [[[[CLM]] - Effective synthesis is rare]] / [[[[CLM]] - Effective synthesis is hard]]

    - Resurfacing [[@booteScholarsResearchersCentrality2005]], which actually includes an intriguing data point - the level of synthesis in regular manuscripts frequently subpar (p.4) not sure how this answers my original question though: this gives p $$p(synthesisissue | issue)$$, not $$p (synthesisissue | paper)$$. Also, need to look into it: usually people give suggestions anyway, even if hte paper is overall ok. We want to know about the proportion of times a lack of synthesis happens that is serious enough that it undermines. Maybe $$p(reject|synthesisissue)$$ will give us that?

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FkvKYAl6XHt?alt=media&token=7ba5b416-a000-4bf1-9064-9d7f0316549e)

        - The citation tree for this turns out to be a goldmine. Some samplings:

            - [[R: alaviReviewKnowledgeManagement2001]] (cited by [[@roweWhatLiteratureReview2014]])

            - Distinguishing literature reviews from [[Synthesis Systems]]s, with a somewhat derogatory summary of "non-systematic reviews" [[R: robinsonLiteratureReviewsVs2015]] - could be an interesting explanation for why [[Z: Publishing review papers is hard]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FGKCQOPm_dK.png?alt=media&token=8e076a88-c840-42a8-8a68-8e1cc3384038)

        - In general, we really need to ground the whole [[D/Synthesis Infrastructure]] work in the [[MIS]] [[Knowledge Management]] world: it is a close cousin of what we're doing, and lots of the insights we are building on were in the context of these organizational [[Knowledge Management]] systems (cf. [[@ackermanSharingKnowledgeExpertise2013]])

        - Important paper here: [[@levySystemsApproachConduct2006]] (I think same person [[Timothy J. Ellis]] who did [[@ellisFrameworkProblemBasedResearch2008]])

            - #appraisal Has some really nice #example-of the __outputs__ of [[synthesis]], but I wish there was more about the __process__! HOW do you get to those outputs? Think harder? Work longer?
[[Week of January 10th, 2022]]

- see new study, using [[sys/RobotReviewer]] (among other tools) to do a full [[systematic review]]s in just 2 weeks! looking really good as a solution to [[[[CLM]] - Effective synthesis is hard]] (specifically [[[[CL]] - Systematic reviews take a very long time to complete and update]]) h/t [[Ought Machine Learning Reading List]] - Google Docs: https://docs.google.com/document/d/1Z1mQ47FqzNBzNvalWgSnyGph7A4Q7MndOEqsqv_mto0/edit#

    - A full systematic review was completed in 2 weeks using automation tools: a case study - PubMed: https://pubmed.ncbi.nlm.nih.gov/32004673/ [[@clarkFullSystematicReview2020]]

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FneJ_BqEYDA.png?alt=media&token=c7b29109-ec0d-4e29-b0bc-8f105a78f512)

    - commentary

        - Is it always possible to complete a systematic review in 2 weeks? Further thoughts and considerations - Journal of Clinical Epidemiology: https://www.jclinepi.com/article/S0895-4356(20)30135-9/fulltext [[@yanItAlwaysPossible2020]]

        - Not all systematic reviews can be completed in 2 weeks—But many can be (and should be) - Journal of Clinical Epidemiology: https://www.jclinepi.com/article/S0895-4356(20)30822-2/fulltext [[@clarkNotAllSystematic2020]]

    - related

        - The Impact of Systematic Review Automation Tools on Methodological Quality and Time Taken to Complete Systematic Review Tasks: Case Study - PubMed: https://pubmed.ncbi.nlm.nih.gov/34057072/ [[@clarkImpactSystematicReview2021]]

            - faster and equal to or better in terms of quality for novices compared to manual

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F1NX40hN-XP.png?alt=media&token=c00a8467-f663-41d2-94e2-58ad2816961d)
[[CL - Science is getting less bang for its buck]]

- Possibly because #[[[[CLM]] - Effective synthesis is hard]] and also [rare]([[[[CLM]] - Effective synthesis is rare]]), since #[[[[CLM]] - Scientific fields stall without adequate theoretical synthesis]]

    - Our [[synthesis]] apparatus was probably ok for a world in which there was less to synthesize, and possibly less [[Scatter]]. But the world has changed (e.g., [[interdisciplinarity]] is way more of a thing, there is way more to synthesize now, way more [[Scatter]]), and our synthesis apparatus has hardly changed at all. So it's quite plausible that our effective synthesis rate would fall quite a bit behind where we need it to be.

    - It's hard to study the level of [[synthesis]] directly (and in particular draw a causal link between that and "progress", which is in itself really tricky to measure, since we rely a lot on scientometrics and bibliometrics, and [[[[CLM]] - Citation practices in science are far from optimal]]), but we have lots of anecdotal evidence at least.
[[March 25th, 2021]]

- Need to brain dump a TON of stuff about a case study #example-of [[[[CLM]] - Effective synthesis is hard]]: the case of 5G and EMR safety. It's related also to [[tools for conviviality]] in complicated ways.

    - It's a random connection: [[Ronald N. Kostoff]] (of [[literature-based discovery]] fame (e.g., [[@kostoffLiteraturerelatedDiscovery2009]]): really excellent, thoughtful examination of [[text mining]] techniques, including [roadmapping](https://ieeexplore.ieee.org/abstract/document/922473)!!) is now.... a major voice sounding an alarm against 5G (see this [monograph](https://smartech.gatech.edu/bitstream/handle/1853/62452/LARGEST_UNETHICAL_MEDICAL_EXPERIMENT_FINAL.pdf?sequence=4&isAllowed=y) and [this paper](https://www.sciencedirect.com/science/article/abs/pii/S037842742030028X)!?

    - But his past deep experience examining the quality of scientific literature and how to use it for innovation gives me pause.

    - I... hate how hard it is to know what's the case.

        - This is where the rubber really meets the road for [[[[CLM]] - Prevailing incentives in academia are bad for science]]: lives can hang in the balance, especially when it comes to how hard it is for science to really inform policymaking - without a clear sense of what we know and don't know, it's tough to make good policy to regulate the rollout of 5G: the gap between what industry is trying to do and regulation is literally on the order of decades.

        - [This Vox article](https://www.vox.com/2018/7/16/17067214/cellphone-cancer-5g-evidence-studies) did a serious effort to examine the case, and found a) some potential concerns, but also b) just a general lack of quality.

    - Side note: I can't unsee the 5G rollout as an example of not-[conviviality]([[tools for conviviality]]) (FASTER! BETTER! BIGGER! = Good)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCydaaE4nZM.png?alt=media&token=416a0f60-1683-4328-8ecb-95e8b66f7faf)

    - This is... easy to paint as conspiratorial. And in fact, it's deeply intertwined with conspiracy theories, including that [5G is the cause of the coronavirus pandemic](https://www.spiritofchange.org/info-to-consider-on-5g-and-the-coronavirus/), with really really basic scientific errors like - a virus is emitted by a sick cell, and not a pathogen

    - And I hate that I feel like our only options are:

        - snide dismissal of things that are not "peer-reviewed literature" (without really reckoning with the quality issues in the literature)

            - see [here](https://www.quora.com/Serious-What-evidence-is-there-to-support-claims-that-5G-is-something-we-should-be-concerned-about) and [here](https://www.quora.com/Why-do-anti-vaxxers-think-5G-is-causing-Covid-19) for examples of how Q&A can basically be useless without a sophisticated way to bring evidence into the conversation (the Vox article is a nice counterexample I think)

        - wholehearted embrace, veering into conspiratorial thinking

        - related: pick people to trust, since it's too hard to really know what's the case

    - This feels like a serious gap in our sensemaking [[infrastructure]] - it is glacially hard/slow to know what is the case even from public knowledge!

        - What if we could deploy crack teams to figure out what is the case from literature (beyond a scoped laborious RCT-only [[systematic review]]) in a way taht is constantly updatable and eminently inspectable, to hold alongside expert witness and opinion, and more easily infused into deliberations

            - This is, I think, the shared vision of Roam

        - Don't want to overstate the case. We have some really heroic efforts by, for example, [[Joel Moskowitz]] from Berkeley, who heads up the [[org/EMFscientist]] group (that led an [appeal](https://emfscientist.org/index.php/emf-scientist-appeal) to WHO in 2015 signed by ~255 scientists as of [[January 14th, 2021]]), and had a [piece published in Scientific American](https://blogs.scientificamerican.com/observations/we-have-no-reason-to-believe-5g-is-safe/) that states the case more forcefully than the Vox article, and maintains a [blog](https://www.saferemr.com/) on this issue

            - Side note: reallllllllly frustrated by the strong emphasis on LOOK HOW MANY EXPERTS ARE SIGNING THIS - feels like we're fighting with the wrong rules!! The deck is stacked against informed dissent, if affiliations and prestige markers are the first/major/only line of evidence/warrant for claims!

                - Related: The sites and outlets where this stuff gets discussed has a strong LACK of prestige-signals

                    - some recent papers on [[literature-based discovery]], including [[@smalheiserRediscoveringDonSwanson2017]], are published in the Journal of Data and Information Science, which used to be an international journal, traditionally "less prestigious"... - wondering how this is juxtaposed with frustrations in the metascience/reform community about the tabloid nature of prestigious outlets like Cell, Nature, Science, PNAS, Psych Science, etc.

                        - but there are serious conerns here!! see, e.g., this paper [[@kostoffUnderreportingAdverseEvents2016]] had a 5-day lag between submission and acceptance????

                            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCrjGTgsjM5.png?alt=media&token=50bb38a3-ef20-42a3-b4d9-63e555051d09)

                    - blogs

    - With the [[context]] of recent events, including the ongoing challenge to overturn dogma about 6 ft and fomite tranmission emphasis in favor of aerosol transmission, and the contentious debates about the efficacy of masks and lockdowns, and the fact that my research on synthesis seems to be more well-received amongst "para" academics and [[independent researchers]] who are further from the prestige core... makes me stop and take this a bit more seriously and be wary of knee-jerk dismissal.

        - Dissent is precious. It must be protected and cultivated.
[[January 17th, 2021]]

- what if it weren't so [hard to know what we know]([[[[CLM]] - Effective synthesis is hard]])? what if effective synthesis were straightforward?

    - how many of these biotech companies are we leaving on the table? what would happen to incentives? to theoretical progress?
[[January 8th, 2021]]

- Finally, some "hard" data for estimating [[[[CLM]] - Effective synthesis is hard]]:

    - h/t [[Cornell Library's Guide to Evidence Synthesis]]'s [breakdown](https://guides.library.cornell.edu/evidence-synthesis/types) of different types of [[synthesis]]

        - cf. [[Jodi Schneider]]'s favorite [[@grantTypologyReviewsAnalysis2009]], which includes [[systematic mapping]]

    - there is a tool called [[sys/PredicTER]] that estimates how long it will take to complete a [[systematic review]] or [[systematic mapping]] study

        - http://predicter.org/

        - estimates based on 5 years of experience with [[systematic review]]s/maps at Collaboration for Environmental Evidence (but details of the estimation approach aren't known here)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ff-bw3QvN2m.png?alt=media&token=d41ffd36-b9af-4cca-9bf6-04ba15fecbab)

                - https://hyp.is/UDCCLFIAEeu_QN8tSyxahw/predicter.org/

            - [default estimate](https://estech.shinyapps.io/predicter/) is about 164 days of full-time work for a typical systematic review (even longer for systematic mapping, which typically doesn't synthesize!)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FdOsX4AiI-8.png?alt=media&token=0045805c-f6cb-4a51-943d-d6cc64e560c5)

                - note here that, if a [[D/Synthesis Infrastructure]] exists, the costs would go down not only for the "synthesis" steps (from meta-data extraction down to "synthesis", which is approximately 40% of the total time, but also the screening, and to a lesser extent, the searching steps, which take about 17% and 5% of the total costs, respectively)
[[November 6th, 2020]]

- [[[[CLM]] - Effective synthesis is hard]]

    - There just isn't a way right now for most scholars to actually do the kind of synthesis we need, on a regular, ongoing basis.

    - Consider a simple thought experiment: we really should be processing our literature to the same level of rigor as a systematic review. But even under very favorable incentive regimes, people struggle to complete systematic reviews on time, and rarely update them.
[[April 14th, 2021]]

- contra [[[[CLM]] - Effective synthesis is hard]] - progress!!

    - [[Paul Glasziou]]: we're making lots of progress!! from 1-2 years per review in [[2015]] to ~1-2 weeks now

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FKpp7Us4Z28.png?alt=media&token=9d94a011-f730-4dc2-97f1-c9b2073f76f4)
[[April 13th, 2021]]

- great way to think through to what extent [[[[CLM]] - Effective synthesis is hard]]

    - scoping review from 34 studies

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fk1DG4goHpg.png?alt=media&token=80152e47-a716-4d51-9046-5337abaaffcd)

    - results:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FJkzjzgHGeQ.png?alt=media&token=f07baf6b-5975-4630-8abe-89f227e5216f)

        - of particular interest:

            - data extraction per study is about 41-65 mins

            - critical appraisal is about 20-30 mins per study

            - project management and coordination also major cost. is this a hidden cost of lack of [[context]]? what if there was a way to enable [[Stigmergic Coordination]]?

    - hold off on conclusions for now, sicne manuscript is still in prep, and no critical appraisal was done

    - commentary

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRpFSuc3qbp.png?alt=media&token=0191b731-e74d-49a1-979e-ab5aefb2ac5f)
