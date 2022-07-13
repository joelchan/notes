---
title: [[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving
url: https://roamresearch.com/#/app/megacoglab/page/0LH8jvA31
author: Joel Chan
date: Tue Sep 22 2020 20:59:31 GMT-0400 (Eastern Daylight Time)
---

- #[[🌲 zettels]] #[[Z]]

    - Tags: #[[D/Computational Analogy]]

    - Description

        - Analogies are rarely a perfect match. There are always some mismatches.

        - Sometimes these mismatches are on "core" attributes, that seem "critical" to the problem. For example, someone working on nanoscale heat transfer may find it very important that any analogical match respect the core attribute of scale (nano).

            - The idea of "core" attributes is closely related to the core [[analogy]] concept of  [[Z: Alignable differences]]: some attributes are considered "structural" (or at least not "surface") because they are critically connected to the core (systems) of relations involved in the analogical match

        - We frequently see in our attempts to provide analogical inspirations to real-world creatives (e.g., scientists, engineers, designers), that [[[[CLM]] - People rapidly reject analogical matches when there is a clear attribute mismatch]].

        - However, the effect of core attribute mismatches on creativity is controversial. There are competing effects / explanations

            - [[[[CLM]] - "Core" attribute mismatches in analogical inspiration harm creativity]]

            - [[[[CLM]] - "Core" mismatches in analogical inspiration improve creativity]]

        - What might explain the mixed effects of attribute mismatches on creative output?

            - One important distinction might be the **timescale / immediacy** of the effect of the analogy, with positive and negative impacts showing up at different timescales.

                - For example, there is some evidence that [[[[CLM]] - Paths to creative breakthroughs are frequently oblique]], and [analogies might be similar]([[[[CLM]] - A significant proportion of the benefits of analogical stimuli is oblique or indirect]]).

                    - We sort of inch towards something like this in our experiments with [[Hyeonsu]] ([[WP: Augmenting scientific creativity with analogical inspirations]]), with our ideas about [[generative misalignment]], and focusing more on "creative adaptation" vs. direct application

                        - To be more precise, though, we're still evaluating the "worth" of individual ideas, instead of considering its downstream effects, which would be closer to the idea in [[[[THE]] - Accretion theory of ideation]]

                - So maybe the way to think about this is in terms of different mechanisms or pathways of inspiration?

                    - More direct path --> try to match on key domain constraints and attributes

                    - More indirect path (not sure if higher ceiling, might just be needed for different problems) --> ignore matching, use [[generative misalignment]]??

            - Separately, maybe there needs  [[[[CLM]] - There is a 'Sweet Spot' in Analogical Distance. Somewhat far analogies lead to better creative outcomes than very near or very far analogies]]

                - could put an upper bound on what domains are actually useful: need to have some critical threshold of [[Z: Alignable differences]]

            - Could be mediated by whether those mismatches are on [[Z: Alignable differences]]

###### Discourse Context

- **Informs::** [[QUE - What factors control whether people appropriately benefit from analogies (especially far-field ones) during creative problem solving]]
- **Informs::** [[QUE - How can we augment scientific creativity with computational analogy]]

###### References

[[November 2nd, 2020]]

- Probably most concrete place to start: qualitative analysis of the data we got from [[Hyeonsu]]'s paper, digging more into the [attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]) (need to get data from Hyeonsu)

    - --> creativity and cognition paper?
[[September 22nd, 2020]]

- Thinking again about [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

    - Alright, so what does this all mean for system-building anyway?

        - What happens if we ignore attributes altogether?

            - We might see a worst of all worlds:

                - If you're fairly sure that your constraints are immovable (e.g., laws of physics!), then failing to model attributes and screen out analogies that mismatch on key attributes will lead to frustration and not yield any real benefits beyond maybe tickling the noggin

                - OTOH, if you really *want* to be challenged in your assumptions and revisit the problem, you *still* want some relational match, but you *do* benefit from [[generative misalignment]] (N.B., looking more closely at [the examples we cite](![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F-1EUVOBBTX.png?alt=media&token=093ae177-772d-4994-aa25-4227d4a93b83)), I'm not sure that we actually see this kind of thing happening - the examples that did lead to useful thinking were still matching on key attributes like material and scale). Ignoring this then leads to weak sauce matches that won't give you what you need

        - So then the problem is how to get these attributes. And I think we have some evidence that [[Z: Problem-critical attributes are often implicit]]

            - Seems related to [[common sense]] - although [[[[CL]] - Common sense concepts are fundamentally fuzzy]], we might be ok if we could get some signal somehow...?

                - Some nascent ideas here: #idea pushing on the [attribute problem](((U1Bb05b-y))) feels like one of the most impactful things to push on, specifically how to efficiently __discover__ these attributes

        - So I'm fairly sure we need to somehow model or account for these attributes in our systems. Otherwise, we'll likely be nothing more than a parlor trick.

    - I think a reasonable next #[[➰ breadcrumbs]] step is to pick apart more examples of what these "attributes" look like, and where they might be missing or how to get them, see if there is some underlying structure or pattern that we can exploit

        - I suspect we can formulate the problem in a simpler way than "solve [[common sense]] reasoning" or "build a more complete [[sys/CYC]]"!!

            - And if we do it right, we might not need to do much innovation in the way of modeling. Which is ok, if our goal is a better system, not necessarily fundamental advances in commonsense reasoning. Although it would be nice bonus if we also learned some tricks that might help with that cause.

    - [[@yuDistributedAnalogicalIdea2016]] finds that
[[October 30th, 2020]]

- Do the near vs. [[far analogies]] thing from the diss - relevant and useful for [[D/Computational Analogy]] and the [attribute stuff]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]).

    - --> [[[[QUE]] - How might domain distance modulate the effects of analogies on creative output?]]

        - Digging back into this was also substantively useful, for resurfacing the idea of "expertise mediation" as another spin on the [attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]): if I show you something from a far domain, and your understanding of that domain is shallow, it's not going to be very useful to you, probably even if it's quite thoroughly explained - what needs to happen is a fruitful iteration or co-evolution (a la [[@dorstCreativityDesignProcess2001]] and [[@helmsCompoundAnalogicalDesign2008]]) between your problem space and the other problem space

            - See these excerpts from the dissertation discussion on this point

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FopBJK2rVAv.png?alt=media&token=80011078-0c6b-475d-8160-4c3254e94409)

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FT-C1RHKiE5.png?alt=media&token=fbbec25e-f1d6-4aca-823b-408595611b2b)

                    - [[@hargadonTechnologyBrokeringInnovation1997]]

            - A subtle variation of a "find collaborators" model might be a variation on Julie Hui's [[sys/IntroAssist]] [[@huiIntroAssistToolSupport2018]]

                - Where might we test something like this? In ConservationX????

                - What would we need to get started?

                    - Would be easiest with academic work, can leverage citation network.

                    - Just specify papers you've written, or ones you know really well, and those define your "network position"

                    - Then whenever we find analogical matches that overlap with your network position, we suggest an intro between you and the seeker
[[October 9th, 2020]]

- Made me think more about the [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]] stuff:

    - Again, the whole framing of a search engine seems to cut off a HUGE chunk of

    - The framing of improv might be much more useful and generative

        - This got sparked by the AI-scaffolded exploration discussion
[[October 7th, 2020]]

- Pulling more on [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

    - Feeling like I want to develop the positive effects more, because they are more interesting, potentially; attribute mismatches leading to "bad matches" is an obvious point. How to harness it for [[generative misalignment]] is more subtle and potentially transformative if we find that these misalignments are important engines of progress

        - This is an interesting path because the normal way we think about analogical innovation is direct transfer

        - This harks back to my notes back in my PhD about pathways of analogical innovation. [[analogy]]

    - Thinking now of the surfboard paper [[@helmsCompoundAnalogicalDesign2008]]

    - Some old notes also on the "indirect route" of analogical innovation

        - {{embed: Indirect transfer}}

    - Also inhale my old proposal for my master's thesis, which had a TON of writing and thinking in it about [[analogy]] and [[conceptual change]] --> [[Joel Master's thesis proposal]]

        - Godl mine of thoughts and references

            - [[@bhattaInnovationAnalogicalDesign1994]] has idea of "non-local adaptation of design [analogies]([[analogy]])

    - Seems critical to work with attribute mismatches? Or at least work through them, use them as a signal light for things to change

    - Does this imply that we need to model attributes directly?

        - I'm not so sure, bc in the cases we have so far (e.g., in [these references](but the process laid out here dovetails nicely with what is observed in [[@helmsCompoundAnalogicalDesign2008]] and [[@gentnerAnalogyCreativityWorks1997]], as well as in [[@gruberDarwinManPsychological1974]], and what we see in person)), the attributes and their inferences might emerge through the working out of the mapping, over an extended period, rather than it being given directly.

        - Or push past their tendency to [rapidly reject attribute mismatching analogs](This by itself is not strong evidence that attribute mismatches harm creativity, though.)? Although this might be more of a mindset thing than a system thing...

        - This implies that we might not need to model the attributes directly, but instead try to optimize retrieval of analogs with a high potential for this sort of mismatch?

            - We'd like to be able to predict which analogical matches have high potential for [[generative misalignment]]. Is this possible? Can we do an initial pilot study to get a feel for this?

            - Too far would not yield generative misalignment, I think, because... attribute mismatches might be too many??

        - Or empower the searcher to discover these mismatches?

    - Just dropping thi shere from [[Hyeonsu]]'s CHI submission [[WP: Augmenting scientific creativity with analogical inspirations]]:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F0RQuOLajNQ.png?alt=media&token=ce6a52fc-4584-4c04-999f-38ec888e7609)

        - Partial purpose matches (high level purpose match, but not low level purpose match) mediating the positive benefits of analogy --> maybe modeling and matching on low-level purposes is both infeasible/hard AND undesirable?

    - Something from [[@holyoakMentalLeapsAnalogy1996]] about partial matches being important, bc this leaves (more) space for [[analogical inference]]s - completely isomorphic matches don't have as much room for this
[[🌱🌾 Research Garden]]

- [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

    - [[[[CLM]] - "Core" mismatches in analogical inspiration improve creativity]]
[[October 8th, 2020]]

- Thinking again about the [attribute stuff]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]])

    - There is a question here: why would you be open to looking at [[far analogies]]?

        - And that's kind of really the main thrust of the whole [[D/Computational Analogy]] project

        - [[near analogies]] and direct transfer are powerful, but... a little boring, I think?

        - Thinking back to how [[IDEO]] thinks about [[analogy]], they slot it into the early stages of the design process, as a way to open up a design space, and frame a problem

            - I'm now thinking back also to an anecdote from [[Kees Dorst]]'s book on [[🧱 framing]] [[@dorstFrameInnovationCreate2015]]

                - Designers used an [[analogy]] to a music festival to (re)frame the problem of night violence in King's Cross from a crime prevention/reduction problem to an entertainment frame

        - Reminds me of work on the relationship between analogical distance and function, by [[@dunbarHowScientistsThink1997]] and others (including me!)
[[October 21st, 2020]]

- seems relevant for [[WP: Reimagining the (analogical) search engine]] and [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

    - [[@choiEffectsTaskComplexity2019]]

    - see also: [[@zhangEffectiveUserInteraction2018]]

        - people might be very used to judging relevance very quickly from very small snippets of information - not a great match for interacting with [[analogy]]
[[October 15th, 2020]]

- Ok getting back on track a bit.... A super high value next step is to flesh out the zettels for [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

    - This gets at the #idea 2: [[outline/2020-10 - supporting explicit reasoning over evidence context for claims (ASIST workshop)]]

    - And also helps me think through more of the details of what system  we might want to make, what the technical mechanics are, etc.

    - And substantively advances [[D/Computational Analogy]], of course!

    - Some initial thoughts about the model for [[uncertainty]]: "no numbers without a shared context and agreed-upon "algorithm" / justification for assessment (rubric??)"

    - Other than the attributes stuff, thinking more about examples of [[synthesis]] to prototype

        - beyond a [[systematic review]], what we can study is when there's multiple competing explanations, or multiple competing phenomena and they're trying to **generate **possible resolutions.

            - within this, we can think about how we need to represent [[context]] so that it's possible to dig into the context and try to find what can possibly explain or resolve the contradiction.

            - examples:

                - competing explanations about the benefits of [[far analogies]] (still close to attributes stuff), these are examples that we can begin to walk up the regrets about this case is a very important case. This is how size can progress me somebody.

                - competing explanations for the effect of of ideological extremism [[@wasowAgendaSeedingHow2020]]

                - competing explanations and theories about the role of children in transmission for [[COVID-19]]
[[November 24th, 2020]]

- the [attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]) still seems important, but i don't quite feel like we have an angle of attack, at least on the access side

    - but i suspect that, again going back to [[analogy workshop with Bex's lab in 2017]] as an example of this, "processing analogies with people"
[[October 16th, 2020]]

- Working on speccing out more of the [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]] stuff

    - Focus on speccing out the "micropubs".

    - The papers are:

        - "sweet spot" stuff (partial evidence)

            - [[@chanBestDesignIdeas2015]]

            - [[@fuMeaningFarImpact2013]]

            - There's more... check citation trees from [[[[CLM]] - There is a 'Sweet Spot' in Analogical Distance. Somewhat far analogies lead to better creative outcomes than very near or very far analogies]] - basically sets up a controversy, mixed effects thing... far, but not too far. Well, what do we mean by far? If relational similarity is fixed, then distance is a function of the "attributes" (entities and their properties, aka one-place relations in [[Structure-Mapping Theory]]). But we don't necessarily distinguish between the attributes.

        - our "preprints"

            - [[WP: Augmenting scientific creativity with analogical inspirations]]

        - Core/direct

            - [[@yuDistributedAnalogicalIdea2016]]

            - [[@gilonAnalogyMiningSpecific2018]]

        - case studies

            - [[@gentnerAnalogyCreativityWorks1997]] -- theoretical, example, partial evidence

            - [[@dorstFrameInnovationCreate2015]] -- example, partial evidence (doesn't really get into the attributes thing, but helps us see the possibility of alternative mechanism pathways)

        - theoretical

            - [[@holyoakMentalLeapsAnalogy1996]]

    - And then there are also "observations"

        - Re: your question about eliciting hidden assumptions/constraints, one strategy we've found that is quite effective is to have an interactive conversation with (analogical) inspirations about a problem: we've had situations where one of us played a "useful fool" role of suggesting things that might be useful, but in a nonthreatening enough way that the scientist could reject it or think through it, and often this led them to drop previously hidden assumptions, or discover implicit assumptions that are important. You can take a look at this notes doc we kept while doing something like this with a mechE research lab (J = me, N = Niki Kittur, my postdoc advisor), jamming over inspirations for stretchable actuators at small (nano?) scales: https://docs.google.com/document/d/1-shjMif_2UBBmxq2sD6CaBoGsvux449_X1ewz3NZnQ0/edit?usp=sharing - we've also seen this anecdotally in most of hte real-world instances where we've deployed some versions of our systems, where the value of the analogies is often in the provocation of a restructuring of the problem, not (just) the provision of an actual workable solution.

    - Fleshed out what we have so far for the idea that [[[[CLM]] - "Core" attribute mismatches in analogical inspiration harm creativity]], and my sense is that we don't really have great *direct* evidence (i.e., directly considering "core" mismatches in attributes) for either this or its opposing claim.
[[October 16th, 2020]]

- substantive comments on the [analogy stuff]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]])

    - it matters from whom the analogy comes

    - it matters whether there is a cultural fit

    - it matters whether you have knowledge of the source

    - analogy to [[excitation]] - which is value neutral

        - everyone had biomarkers for elevated excitation

            - but they can interpret it very differently depending on... who is interviewing them

        - interviewed ppl standing over a canyon

        - --> [[desirable difficulty]]

        - there's also individual differences in baseline [[excitation]], claims [[Hans Eysenck]]

            - but be careful! https://journals.sagepub.com/doi/10.1177/1359105318820931

            - [[![]]]
[[October 30th, 2020]]

- Digging back into this was also substantively useful, for resurfacing the idea of "expertise mediation" as another spin on the [attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]): if I show you something from a far domain, and your understanding of that domain is shallow, it's not going to be very useful to you, probably even if it's quite thoroughly explained - what needs to happen is a fruitful iteration or co-evolution (a la [[@dorstCreativityDesignProcess2001]] and [[@helmsCompoundAnalogicalDesign2008]]) between your problem space and the other problem space

    - See these excerpts from the dissertation discussion on this point

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FopBJK2rVAv.png?alt=media&token=80011078-0c6b-475d-8160-4c3254e94409)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FT-C1RHKiE5.png?alt=media&token=fbbec25e-f1d6-4aca-823b-408595611b2b)

            - [[@hargadonTechnologyBrokeringInnovation1997]]

    - A subtle variation of a "find collaborators" model might be a variation on Julie Hui's [[sys/IntroAssist]] [[@huiIntroAssistToolSupport2018]]

        - Where might we test something like this? In ConservationX????

        - What would we need to get started?

            - Would be easiest with academic work, can leverage citation network.

            - Just specify papers you've written, or ones you know really well, and those define your "network position"

            - Then whenever we find analogical matches that overlap with your network position, we suggest an intro between you and the seeker
[[October 2nd, 2020]]

- Revisiting [the attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]) for [[D/Computational Analogy]]

    - #researcharguments ideas

        - #idea Descriptive study of the nature and distribution of critical attributes in real-world analogical problem solving

            - [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]

            - But [[Z: Problem-critical attributes are often implicit]], and common-sense reasoning is still a hard open problem in [[NLP]]

            - Thus, systems that leverage these attributes could facilitate the discovery of [[far analogies]] that are either 1) more immediately useful (because they do not mismatch on critical attributes), or 2) more generative through triggering creative [[problem (re)formulation]] (e.g., through [[generative misalignment]]) because they *do* target some mismatches on critical attributes, especially those that might be latent or implicit for the searcher.

            - How can we discover problem-critical attributes in analogical queries for scientific problems at scale?

            - We want to get at this question by conducting a systematic study of the nature and distribution of critical attributes in real-world analogical problem solving.

            - Our goal is to use this taxonomy to identify heuristics that could help systems identify these attributes at scale. A secondary goal is to test the assumption that these attributes can be **mined** (which may be false! It could be that we need to **generate** them on the fly for each query).

            - We aim to contribute a taxonomy of these attributes that maps **where** critical attributes might be found in the context of scientific analogical queries (e.g., in the abstract, query, related work, etc.)
[[November 3rd, 2020]]

- Quick prototype of #researcharguments around the [attribute problem]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]]) for [[D/Computational Analogy]]

    - we have created a system that can automatically retrieve analogical inspirations for researchers from large corpora of research papers

        - the system can identify matching research papers for a target abstract or query based on shared purpose (i.e., retrieve other papers that solve similar problems), even if they are outside the target problem domain

            - from [[WP: Augmenting scientific creativity with analogical inspirations]]

                - we can label abstract spans as purpose/mechanism with ~60% accuracy

                    - The [prediction model](((i52eDy7Sp))) achieved F1 scores of about .64 when predicting purpose/mechanism spans for the 50 papers in [[@chanSOLVENTMixedInitiative2018]], annotated by experts

                - using our span predictions as input for embeddings, we can identify (partial) purpose matches between papers at ~60% accuracy

                    - ~60% of the top 50 matches [retrieved](((ft6qE7B28))) using [embeddings](((OVq7p4ySL))) of the model's [span predictions](((i52eDy7Sp))) as the representation were judged to be at least [high-level purpose matches](((i3alg9uw5)))

        - there still seem to be a number of questions here

            - our primary validation set is 50 papers from a very focused corpus - would love to at least see some kind of k-fold validation or cross-validation from the 10k papers

                - we are uncertain about the "goldness" of the 10k papers, which is problematic for training - see here [[November 23rd, 2018]] annotation audit:

    - however, our tests of our system with real users reveal substantial gaps between the expected value of our analogies and the realized value (at least in the session)

        - for example, [[[[CLM]] - People rapidly reject analogical matches when there is a clear attribute mismatch]], even when there is a purpose match

    - #Question : **how can we design our systems to maximize the beneficial impact of analogical inspirations** (assuming they do have value)?

        - if we believe the main bottleneck is *not* matching

            - change the system

                - augment the search interface to promote discovery and subsetting/control of attributes

                    - targets problem that [[Z: Problem-critical attributes are often implicit]], and also highly [[context]]ual

                    - [[Hyeonsu]]'s [[UIST]] stuff:

                - help the user be more "accurate" in judgments of analogical value

                    - this is the path being explored by [[Chen Shani]]

            - involve more human processing --> [[idea: sociotechnical analogical connector]]

        - if we think the main bottleneck is matching (or there are still significant gains on the matching end)

            - explicitly account for attributes in our computational approach

                - incorporate attributes into our representation and matching

                    - but need to find/represent them

                        - hard because [[Z: Problem-critical attributes are often implicit]]

                            - ^^... or are they?^^

                        - some hints in [[@gilonAnalogyMiningSpecific2018]], relying on open [[common sense]] knowledge bases like [[sys/CYC]]

            - maximize purpose/mechanism prediction and matching accuracy

                - could test this with a perfect oracle

                    - in a way, our [[analogy workshop with Bex's lab in 2017]] was a bit of a test of this, in that the "analogical inspirations" came from Niki and I

    - we should make analogical inspiration systems

        - [[analogy]] is a powerful strategy for improving creative work

            - Maybe mention ~3 examples from previous paper, biomimicry and else?

        - people's ability to leverage the power of analogy is limited by their memory, which tends to favor easily accessible knowledge, including predominantly [[near analogies]]

            - "limited by their memory" is a piece of interesting new claim [?]

        - therefore, systems that augment people's access to analogical inspirations, particularly outside their direct domain, could significantly augment people's capacity for creative work

            - At some point, I wonder if the project idea can be simplified to reach a greater set audiences. Would the meaning change if say, we use "support" / "improve" for "augment"?

    - alternatively, what is the best way to measure the impact of analogical inspirations?
[[November 23rd, 2020]]

- thinking about the [[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]] stuff again

    - how can we get it?

    - wondering if we can get some signals from the mechanism labels?

        - while we probably want to show different mechanisms, the nature of the mechanism might give us clues about core attributes?

        - should do a quick look through some examples

            - maybe starting with Hyeonsu’s data?
[[Writing inbox for week of June 29th, 2020]]

- Want to think more carefully about the "center of gravity" problem of "[attributes/properties]([[[[CLM]] - Core attribute (mis)matches mediate the benefits of analogies in real-world, complex problem solving]])" for [[D/Computational Analogy]]

    - This is relevant to [[WP: Augmenting scientific creativity with analogical inspirations]], as well as what [[Chen Shani]] is doing. Feel like we have an edge here? Definitely a lot more complex than the basic word vector analogy stuff.

    - Possible papers:

        - #[[@goelInformationprocessingAccountCreative2011]] - idea of [[co-evolution of problem and solution space]]

        - #[[@smallMapsScienceInterdisciplinary2010]] - analyzing muhc more recent {{alias: [[example-of]] examples of}} [[analogy]] transfer in science

            - older but gold #[[@oppenheimerAnalogyScience1956]]

        - ideas about alignable / non-alignable differences in analogical mappings from [[Structure-Mapping Theory]] #[[@gentnerStructureMappingTheoretical1983]]

            - k let's start with #[[@gentnerAnalogicalProcessesHuman2010]]

    - The central issue we're seeing is that many of the attributes that are central to a "good/useful" mapping (either correctly projecting inferences, or correctly rejecting a false positive match) are "[latent]([[Z: Problem-critical attributes are often implicit]])", both in the text and in the mind of the analogy seeker. This is a very hard problem! Could interactions based around [[progressive alignment]] help? Overview in #[[@gentnerAnalogicalProcessesHuman2010]], should use that to identify the seminal experiment/paper
