---
title: [[CLM]] - Context and privacy are in tension when sharing knowledge with others
url: https://roamresearch.com/#/app/megacoglab/page/fqD4Jnmhr
author: Joel Chan
date: Fri Jan 07 2022 09:29:36 GMT-0500 (Eastern Standard Time)
---

- #[[🌲 zettels]] #[[Z]] {{word-count}}

    - Tags: #[[D/Synthesis Infrastructure]]

    - Description

        - There is an immense amount of value in personal knowledge graphs, whether they are represented in a latent way as a linear notebook, or (as is increasingly the case) as personal wikis or [[hypertext notebooks]]

        - Personal knowledge graphs used to be a niche domain of [[Hackers]], but, with the rise of tools like [[sys/RoamResearch]] and [[sys/TiddlyWiki]], is slowly but surely making its way through [[Explorers]] and even [[Virtuosos]] [[@chanWhereRubberMeets2020]].

        - As adoption of these resources grows, we are approaching critical mass of knowledge that could yield significant value if linked and/or made shareable in some way.

        - This means the vision of augmenting collective intelligence through [[sys/Federated Wikis]] is becoming less of a pipe dream, and more of a thing we might want to figure out how to actually do.

        - There is a critical problem here around the tension between [[privacy]] and [[context]] though, which we need to solve if we want to answer [[[[QUE]] - How can we best bridge private vs. public knowledge?]]

        - Personal knowledge graphs gain their power by being open and densely connected, without regard for ordinary boundaries between work and not-work and between projects. #[[Z]]

            - The power of networked thinking comes from breaking down artificial silos between knowledge, to power [[analogy]] and [[🧱 conceptual combination]], ultimately enabling a more sophisticated level of knowledge [[synthesis]].

            - For example, often, important [[context]] for ideas comes from the knowledge worker's personal assessment of the credibility of ideas.

            - These assessments can be quite personal and preliminary, such as downweighting a claim from a lab with a known (but not public) history of p-hacking or sensationalism until it is replicated by other labs.

            - Consider, for example, how [[Darwin's notebooks]] mixed in intensely personal musings and fears with incremental insights that were crucial for developing his theory of evolution [[@gruberDarwinManPsychological1974]].

                - In particular, his wrestling with the evidentiary gaps in his theory was intertwined with his musings about his reluctance to "go public" with his theory, given the hostile atmosphere for scientific explanations that left out a role of the Divine.

            - A related example: [[Isaac Newton]] took alchemy seriously [[@dryNewtonPapersStrange2014]]! He wrote extensively about it in his personal notes and private manuscripts, which you can view for yourself in the [online archive](https://www.newtonproject.ox.ac.uk/texts/newtons-works/alchemical) of his notes.

            - As another example, today, many users of [[hypertext notebooks]] like [[sys/RoamResearch]] freely mix the personal and the professional, and cross mention people, resources, and data across projects.

            - This blurring between the private and the public, between this-project and that-project, and between the personal and the professional, is incredibly generative for creative work.

            - But it also poses a serious challenge to any effort to make these graphs available in some way to others, whether directly, or through some kind of [[federation]] system.

            - How do we protect unauthorized or unwanted access to ideas and thoughts that might lead to harm for the knowledge sharer?

        - Well, you might say, let's just share the stuff that's ready to be shared, then, and only those things! Just the public-ready stuff. But there is a related challenge here that makes this problem harder: [[[[CLM]] - Knowledge must be recontextualized to be usefully reused]].

            - Without understanding why an idea was written, how it relates to other ideas, what its precise meaning is in the [[context]] of the knowledge sharer, and how that idea is warranted or grounded in observations, details, and evidence, the "mileage" of that piece of information is extremely limited.

            - The implication of this is that sharing __only__ entry points into a knowledge graph will likely severely blunt their usefulness for others.

        - So the challenge is really: How do we provide enough [[context]] in entry points from a knowledge graph to benefit the knowledge reuser, while protecting the [[privacy]] of the knowledge sharer?

###### Discourse Context

- **Informs::** [[QUE - How can we best bridge private vs. public knowledge]]
- **Informed By::** [[@gruberDarwinManPsychological1974]]
- **Informed By::** [[@chanWhereRubberMeets2020]]
- **Informed By::** [[@dryNewtonPapersStrange2014]]

###### References

[[September 24th, 2020]]

- #idea 1: exploring this problem: [[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]]

    - Here, we want to consider how we might design the conceptual model for elements of personal knowledge graphs that are shareable, to manage the tension between context and privacy.

    - One particularly interesting and difficult problem is how to decide whether "background" or [[context]] nodes (that link to a given target node in a graph) should be visible to a prospective reuser, and if so, to what extent.

        - We suspect it will need to be [[context]]ual in some way: what's inappropriate for a labmate to see from a PhD student's notes is different from what a PI should see, and is different entirely from what another researcher who doesn't know the student should see.

        - For example, would a "privacy" flag for these nodes be workable? How would that flag even be conceptualized? Or computed?

        - But of course privacy is not the only consideration here: we need to balance this against the likelihood that the node is "needed" to usefully re[[context]]ualize the target node. What might a model for that look like?

        - A vexing issue here is that, as the usefulness of a personal knowledge graph grows (in proportion to its density, interconnectedness, and boundary-blurring), the feasibility of manually flagging things as useful and/or private approaches zero.

        - Could formal approaches like [[compression]] theory help with this predictive task?

    - We would like to study this problem, and hopefully come up with some possible solutions to this. Or, we would like to know if this problem is fundamentally insurmountable, in which case the project of [[sys/Federated Wikis]] may be out of reach.
[[@acmsigchiUISTCSCWCelebration2020]]

- powerful concept of [[interpersonal distance]] - makes me think of [[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]] and [[[[QUE]] - How can we best bridge private vs. public knowledge?]]

    - --> [[D/Democratizing Design]]
[[October 17th, 2020]]

- cc [[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]]

    - but could imagine this idea of [[information friction]] being related to [[compression]]

        - rather than classifying items for sensitivity directly, we almost simulate kinds of inferences we might make that we'd consider sensitive, and then backpropagate what would be necessary to make those inferences
[[November 14th, 2020]]

- This remains an important problem for [[D/Synthesis Infrastructure]] and [[[[QUE]] - How can we best bridge private vs. public knowledge?]], separate from [[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]]

    - What can we actually share usefully with others, regardless of whether we're comfortable with it?

        - Contra [[[[CLM]] - Most private annotations aren't useful to other people]]
[[December 9th, 2021]]

- Side note: with the [[[[EXP]] - [[D/Synthesis Infrastructure]] - Field study for discourse graph extension]] being of uncertain privacy here, I'm feeling the need much more strongly for a [private space]([[[[CLM]] - Context and privacy are in tension when sharing knowledge with others]]) where all of my notes can intermingle and I can write just for my own eyes

    - Choosing where things will go gives me the distinct sensation of... being ungrounded and uncertain and... almost paralyzed?

    - I'm pretty bullish now on the idea that things should be private by default (where private may also include extremely trusted others) for creative knowledge work

        - In the back of my head I'm thinking of the contrast with [[open-source]]
