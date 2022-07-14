---
title: [[QUE]] - How can we support explicit contention with evidence when synthesizing knowledge claims?
url: https://roamresearch.com/#/app/megacoglab/page/g15ZZU-pK
author: Joel Chan
date: Wed Oct 21 2020 16:58:53 GMT-0400 (Eastern Daylight Time)
---

- #[[🌲 zettels]] #[[Question]]

    - Tags: #[[D/Synthesis Infrastructure]]

    - Description

        - Reasoning and [[synthesis]] at any reasonable scale benefits from some kind of computational and/or quantitative aggregation.

        - Examples

            - Consider the case of [[COVID-19]], where we now want to make fine-point tradeoff decisions that hinge on strength of evidence in addition to strenght of claims, weighing these against the cost of interventions and so on.

            - Another example is [[IVEO Matrix]], where the "Empirical support score" parameter is helpful for driving further progress, and a key reason that real users find it helpful compared to just narrative reports: ((NrpnffL-6)). But the score itself was the outcome of negotation and knowledge work.

            - In the limit, [[systematic review]]s do sophisticated computations over these quantitative "fixed" values of evidence level to reach an overall conclusion about the weight of evidence behind a single claim. These are extremely valuable! But they do presuppose a level of "fixedness" and consensus over what constitutes certainty or strength of evidence, which may or may not exist!

        - Leaving this out entirely can devolve into mere "counting" and consensus (e.g., based on reputation of authors), which leaves much to be desired! Although this might be all that is really possible epistemically for certain fields of inquiry, and any more quantitative sophistication might be performative rather than actually useful.

        - The core issue here is that evidence is not binary (yes or no). There is nuance behind it.

            - And this nuance matters.

                - It tells us where the argument is "soft", or where we might want to push.

                - And the *reasons* behind the softness and uncertainty may give us clues as to what to do next to resolve tensions and construct novel explanations.

                - In the simplest case, we can use nuanced evidence to decide that one of two competing explanations or claims has more weight.

        - But the notion of "levels of evidence" is contentious, especially in settings with high [[interdisciplinarity]] - the explicit articulation and negotiation of degrees of belief and [[uncertainty]], about [[epistemology]] even, might be where true interdisciplinary progress happens. Prematurely "compressing" these nuances into a single [[context]]-less number threatens the real usefulness of that number for synthesis.

            - reminds me of [[@suriAdvancementsResearchSynthesis2009]]'s point about the need to deal with heterogeneity in the evidence types and assumptions, not just integrate over RCTs or something. [*](reminds me of [[@suriAdvancementsResearchSynthesis2009]]'s point about the need to deal with heterogeneity in the evidence types and assumptions, not just integrate over RCTs or something.)

            - later [[Sally Thorne]] follows up on this to say "let's rediscover the narrative review! [[@thorneRediscoveringNarrativeReview2018]] [*](later [[Sally Thorne]] follows up on this to say "let's rediscover the narrative review! [[@thorneRediscoveringNarrativeReview2018]])

                - [[@greenhalghTimeChallengeSpurious2018]] then cites [[@thorneRediscoveringNarrativeReview2018]] to critique the fetishizing of systematic reviews, noting that (similar ot my point), #CLlaim [[[[CLM]] - [[systematic review]]s are typically narrowly focused, and provide less insight]]. [*](((TR1PCdTi8)))

            - Also great discussion with [[Jodi Schneider]] on debates in "[[evidence-based medicine]]" over what constitutes different levels of evidence

            - Compressing these debates into a single number is technically and mechanically valuable, needed even, for [[synthesis]] at realistic scale. But you run a high risk of short-circuiting the needed reasoning to make it happen in a trustworthy manner.

        - What does this mean for conceptual models of [[provenance]] / [[uncertainty]] / [[evidence]] in knowledge graphs for [[synthesis]]?

            - At the least, it seems likely that we would like to have some way to represent or link to the negotiated *rationale* for anything that is like an empirical support score.

            - The thorniness of this problem, though, might be why models like [[std/SEPIO]] and [[std/Micropublication]]s leave out quantitative scores entirely.

        - Much prior work has grappled with these conceptual difficulties.

            - [[@niccolucciExpressingReliabilityCIDOC2017]] build on the original [[std/CIDOC-CRM]] model -- developed to formally represent evidence in archeology --- and proposes using [[fuzzy logic]], formally distinct from [[[probability]]], to express [[uncertainty]] in classification of items

                - There is significant controversy still over this proposal, however; as of [[October 21st, 2020]], it's still an [open issue](http://www.cidoc-crm.org/Issue/ID-349-belief-values) in the [[std/CIDOC-CRM]] issue list

                - One [issue](https://hyp.is/ewJrXBPnEeu5POdJtyFI7w/www.cidoc-crm.org/Issue/ID-349-belief-values) is a desire to *separate* issues of being ([ontology]([[ontologies]])) from issues of knowing ([[epistemology]]):

                    - There is a related rationale behind the postulation that [[std/Nanopublications]] should be absolute [[@kuhnBroadeningScopeNanopublications2013](#Claim Natural-language nanopublications should be atomic, independent, declarative, and absolute #Atomicity)]: the idea is that the claim is a statement of ontology, and we then offload expressions of [[uncertainty]] to a property

            - People have worked on the goal of representing evidence [[@brushSEPIOSemanticModel2016]], [[uncertainty]] [[@dewaardFormalisingUncertaintyOntology2012]], and [[provenance]] of publications [[@grothAnatomyNanopublication2010]].

            - In [[@clarkMicropublicationsSemanticModel2014]], there is a general sense of support, with the lowest being some kind of authorship attribution. But I'm pretty sure the support/challenge relationship is binary, in the formal sense. I'm not quite sure then how this is translated into computational reasoning. Maybe it's implicit here, so we explicitly have to reason about the support *types* (has attribution only, has data and methods). THis might lead to quite different dynamics, although maybe slower to start with, might lead to deeper [[synthesis]] than including a belief number??

            - [[@brushSEPIOSemanticModel2016]]'s [[std/SEPIO]] feels similar to [[@clarkMicropublicationsSemanticModel2014]], in that it doesn't really care about assigning numbers, and is more about making sure that there is direct documentation of "lines of evidence" - what *kind* of support is there for each claim?

                - They support connecting to the [[std/Evidence and Conclusion (ECO)]] ontology, which describes types of scientific evidence (but NOT strength!) in bio

            - Different from [[std/Micropublication]] and [[std/SEPIO]], [[@dewaardFormalisingUncertaintyOntology2012]] propose [[std/ORCA]], which includes not just the type of basis of certainty (although it's quite a bit less granular than [[std/SEPIO]]'s "[[evidence lines]]": it's either "reasoning", "data", or "unidentified"), but also explicit ordinal values of certainty

            - In some areas, such as [[systematic review]]s, we have an established hierarchy of evidence that is used

            - [[@grothAnatomyNanopublication2010]] almost punts on this issue completely, specifying evidence in terms of other [[std/Nanopublications]] that refer to a given nanopub. This is considerably less expressive than having access to details of the data, or some taxonomy of types or lines of evidence

        - In general, a more quantitative approach is more amenable to computational, *quantitative* integration; if, however, it doesn't include rich, explicit mappings between the number and the [[context]] behind the number, we're nervous about its utility in practice

        - ON the flip side, a more qualitative approach (e.g., [[evidence lines]]), as exemplified by [[@clarkMicropublicationsSemanticModel2014]] and [[@brushSEPIOSemanticModel2016]], is less readily quantifiable in a sophisticated sense, but possibly more useful for the early stages of [[synthesis]], particularly where there is [[interdisciplinarity]]

            - One challenge maybe is that not all subdomains have a nice ontology of evidence types, although it's

###### Discourse Context

- **Informed By::** [[@brushSEPIOSemanticModel2016]]
- **Informed By::** [[@niccolucciExpressingReliabilityCIDOC2017]]
- **Informed By::** [[@suriAdvancementsResearchSynthesis2009]]
- **Informed By::** [[@greenhalghTimeChallengeSpurious2018]]
- **Informed By::** [[@thorneRediscoveringNarrativeReview2018]]
- **Informed By::** [[@clarkMicropublicationsSemanticModel2014]]
- **Informed By::** [[@dewaardFormalisingUncertaintyOntology2012]]
- **Informed By::** [[@grothAnatomyNanopublication2010]]
