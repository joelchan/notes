---
title: [[QUE]] - How might AI systems assist with problem (re)formulation?
url: https://roamresearch.com/#/app/megacoglab/page/pzqEX4UJL
author: Joel Chan
date: Tue Nov 09 2021 09:52:17 GMT-0500 (Eastern Standard Time)
---

- [[Playground: Problem formulation vs. NLP subtasks]]
- # Synthesis

    - Model #[[dependsOn]] answers to [[[[QUE]] - How do people effectively (re)formulate creative problems?]]
- ---
- # Sources

    - Here
- ---
- # Meta

    - Tags:

###### References

[[November 10th, 2021]]

- The core spark for this project is a curiosity about how [[transformer language model]]s might help with (analogical) [[problem (re)formulation]], as a subset of question: [[[[QUE]] - How might AI systems assist with problem (re)formulation?]]

    - Why do we care about problem reformulation?

        - A better problem formulation is the foundation of creative work.

        - And it's also really hard for people. I think? Need to figure this out. This is our intuition, but what is our evidence? How much do we believe this? #[[➰ breadcrumbs]] ^^Jason: Yes, I have worked on problem framing a lot and it's definitely hard.^^

            - Especially novices.

                - Entry points:

                    - [[@macneilFramingCreativeWork2021]] - error analysis of novice problem frames

                    - [[🧱 fixation]], see, e.g., [[@dowParallelPrototypingLeads2010]] - "can't see it any other way"

            - But even experts.

                - I'm thinking of the star trek and "style" stuff. Easy to get stuck in your "one good trick", streetlight effect or hammer looking for nail. In other words, [[🧱 fixation]].

            - They could use help with this!

            - The more thoughtful design of systems that integrate here I think is the longer term project ^^Jason: Yes, [[Stephen MacNeil]] and I have worked on building design systems with a focus on problem framing.^^

    - Why are we interested in language models?

        - One inspiration is the general idea that these new class of models has demonstrated uncommon ability to surprise (in a good way).

            - I'm thinking of how [[sys/AlphaGo]] helped even world-class experts see the game of Go differently (see [[@metzSadnessBeautyWatching2016]]).

                - This seems related to [[Margaret Boden]]'s notion of [[transformational creativity]] (see [[@bodenChapterCreativity1996]])

            - But I think these are not the same as what we're thinking.

                - Our aims here are a bit more modest. We're not as interested in an autonomous agent, so much as we are interested in exploring the capabilities of AI systems like [[transformer language model]]s, which have high levels of adaptability and generativity [[@bommasaniOpportunitiesRisksFoundation2021]] via the paradigm of [[prompt programming]] (so they don't need to be expensively developed through [[supervised learning]] or even [[fine-tuning]])

                    - MANY other examples from just a quick search

                        - Deep Learning Trends: top 20 best uses of GPT-3 by OpenAI: https://www.educative.io/blog/top-uses-gpt-3-deep-learning

                        - Calvin French-Owen on Twitter: "I've been experimenting with GPT-3 and wow! I haven't seen a technology this magical in a long time Yes, the model is shockingly good. More interestingly, it opens up programming to anyone who can write. Writing tools will become the new thinking tools. https://t.co/cCsCvRW3Hs" / Twitter: https://twitter.com/calvinfo/status/1286332337563684865

                        - Siddharth Karamcheti on Twitter: "Since getting academic access, I’ve been thinking about GPT-3’s applications to grounded language understanding — e.g. for robotics and other embodied agents. In doing so, I came up with a new demo: Objects to Affordances: “what can I do with an object?” cc @gdb https://t.co/ptRXmy197P" / Twitter: https://twitter.com/siddkaramcheti/status/1286168606896603136

                        - shreyashankar/gpt3-sandbox: The goal of this project is to enable users to create cool web demos using the newly released OpenAI GPT-3 API with just a few lines of Python.: https://github.com/shreyashankar/gpt3-sandbox

                        - Learn Awesome on Twitter: "Using GPT-3 for automatic quiz generation on any topic and then evaluating the students' answers. This thing is fantastic! @sama https://t.co/qutUffWh7J" / Twitter: https://twitter.com/learn_awesome/status/1286189729826738176

                        - Compose.ai | GPT-3 Demo: https://gpt3demo.com/apps/compose-ai

                        - Adflow | GPT-3 Demo: https://gpt3demo.com/apps/adflow-ai

                        - Anyword | GPT-3 Demo: https://gpt3demo.com/apps/anyword

                        - Pencil | GPT-3 Demo: https://gpt3demo.com/apps/trypencil

                        - Sudowrite | GPT-3 Demo: https://gpt3demo.com/apps/sudowrite

                        - GPT-3 Recipe Builder | GPT-3 Demo: https://gpt3demo.com/apps/gpt-3-recipe-builder

                        - Red Diaries Fellini Forward by Campari | GPT-3 Demo: https://gpt3demo.com/apps/red-diaries-fellini-forward-by-campari

                        - GPT-Startup | GPT-3 Demo: https://gpt3demo.com/apps/gpt-startup

                        - IdeasAI | GPT-3 Demo: https://gpt3demo.com/apps/ideasai

                        - ideasby.ai | GPT-3 Demo: https://gpt3demo.com/apps/ideasby-ai

                        - 500+ Openers for Tinder written by GPT-3 | GPT-3 Demo: https://gpt3demo.com/apps/500-openers-for-tinder-written-by-gpt-3

                        - AI Weirdness | GPT-3 Demo: https://gpt3demo.com/apps/ai-weirdness

                        - GPT-3 pickup lines | GPT-3 Demo: https://gpt3demo.com/apps/gpt-3-tries-pickup-lines

                        - things are a little crazy rn | GPT-3 Demo: https://gpt3demo.com/apps/things-are-a-little-crazy-rn

                        - Wisdom_by_GPT3 | GPT-3 Demo: https://gpt3demo.com/apps/wisdom-by-gpt3

                        - FABLE - The Future of Storytelling: https://fable-studio.com/

                    - One concrete example of this is [[sys/GPT-2]], which was used to generate the popular [[sys/AI Dungeon]]

                    - There's also some emerging evidence that [[[[CLM]] - [[transformer language model]]s have some analogical reasoning ability]], contra [[[[QUE]] - Can deep learning discover analogical representations?]]

                        - another line of evidence for this might be the insane performance of giant language models like [[sys/GPT-3]]

                - These AIs surprise and transform the problem space by *doing creative things*.

        - We do need to ground this in a clear-eyed understanding of [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] and also [[[[QUE]] - Can deep learning discover analogical representations?]]
[[April 18th, 2022]]

- [[[[QUE]] - How might AI systems assist with problem (re)formulation?]]

    - [[idea: sociotechnical analogical connector]]

        - GPT-3 stuff
[[November 18th, 2021]]

- Quick notes for inspiration on [[[[QUE]] - How do people effectively (re)formulate creative problems?]] to feed into [[[[QUE]] - How might AI systems assist with problem (re)formulation?]]

    - [[@cassTransformYourIndustry2019]]

        - it's a case description (not formal academic) from [[IDEO]], illustrating how "analogous research" works, to help with problem reformulation

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FzVSHGBo3lX.png?alt=media&token=7429a5dd-5c4a-4463-9423-bd16376dbf65)

        - the case starting point is a hospital that wans to redesign the entire patient experience (super broad)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F1S2czKyJ5I.png?alt=media&token=10aa6270-2c28-486e-a05d-47d8939cef8a)

        - they went to an airport for inspiration, to see what solutions and problems were there, based on a shared mapping of complexity of the experience, and a sense that this industry had invested in solutions to make it better (I am... personally doubtful? :P)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FpRCmLLzPus.png?alt=media&token=5ef35b18-8897-4b3c-a588-af8c9ff9ff43)

        - what they noticed:

            - many different pathways for customers; in contrast to "one option" for their patients

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Fc9qZnFjVSJ.png?alt=media&token=f6ce843e-fcbe-4556-8ded-c378053900d9)

            - customer service desk; a place to also go beyond the standard job description

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FZLcue5z0Ak.png?alt=media&token=a23503f5-a54f-4359-bb1a-4adf599d7412)

        - which led to ideas for prototypes to test

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FDxJdiST6ys.png?alt=media&token=136262ad-aaa4-49cb-bdb2-7308bde5f40e)

        - this case is evocative on the surface as an example (hospitals and airports!), but maybe isn't super insightful in the details. i particularly wish i had a better sense of where the problem formulations *started*; i can see from the examples where the problem formulations were *missing*, i guess, but i'm not sure if the problem to start with was too... high level?

        - what i'm noticing about this case:

            - how interleaved problems and solutions are... this feels important.

            - the immersive nature of the experience; it was embodied, not abstract; this kind of gets back to what [[AJ Rudd Jr]] is exploring

        - still, useful to reify this as a case/example: [[[[EVD]] - hospital workers reformulated the problem of designing a better patient experience based on insights from exploring an analogous setting of customer experience in airports - [[@cassTransformYourIndustry2019]]]]

    - and back to [[@schonReflectivePractitionerHow1983]]

        - > ...although problem setting is a necessary condition for technical problem solving, it is not itself a technical problem. When set the problem, we select what we will treat at the "things" of the situation, we set the boundaries of our attention to it, and we impose upon it a coherence which allows us to say what is wrong and in what directions the situation needs to be changed. Problem setting is a process in which, interactively we __name__ the things to which we will attend and __frame__ the context in which we will attend to them (p. 41)

            - great #quotes for [[problem (re)formulation]]

            - this noticing here reminds me very much of [[[[EVD]] - Representing a mutilated checkerboard in a way that made perceptual features of squares more salient facilitated problem reformulation and insight - [[@kaplanSearchInsight1990]]]]
[[November 16th, 2021]]

- On my mind: [[[[QUE]] - What do we know about [[transformer language model]]s' natural language generation capabilities?]] and [[[[QUE]] - How might AI systems assist with problem (re)formulation?]]

    - Want to think through two things: 1) what's a basic intuition for how they work, and 2) let's start compiling some evidence we have on its capabilities

    - We'll start with [[@brownLanguageModelsAre2020]]

        - Hmm interesting - here they seem to anticipate later results on potential advantages of *fewer* (and maybe no???) examples for [[few-shot learning]]? Here they discuss the hypothesis that brittleness and vulnerability to adversarial attacks might grow larger as the training data grows: [[[[CL]] - Potential to exploit spurious correlations in training data fundamentally grows with expressiveness model and narrowness of training distribution]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F-PPevoPi2O.png?alt=media&token=d480395a-2198-4eb0-bc0a-ccf9029e54a2) (p. 3)

        - The basic intuition for how the language models work:

            - I don't full understand the details yet of how the training and the model for [[sys/GPT-3]] work. But I do know that:

                - The architecture is a [[transformer architecture]]

                    - One of the secret sauces is [[self-attention]], which helps with the problem of updating weights appropriately for connections to context beyond the immediate surroundings of a word/token

                        - Original source for this is [[@vaswaniAttentionAllYou]]

                - The encoding of words/tokens is [[Byte-Pair Encoding (BPE)]]

                    - in this way it reminds me of [[charNN]] architectures

                - It's the same basic architecture as [[sys/GPT-2]], which is described in [Radford et al. (2019)]([[@radfordLanguageModelsAre2019]])

                - [[dataset/Common Crawl]] is the base, but with some mods:

                    - filtering for "quality" (see Appendix A)

                    - fuzzy deduplication (see Appendix A)

                    - enriching with some other curated datasets, e.g., WEbText, Wikipedia

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ff-olxLm3nt.png?alt=media&token=61808470-eeac-4eaf-809e-7da99bba0901) (p. 8)

            - They are trained in an unsupervised fashion to basically do one task: predict some word(s)/token(s) of set size M based on some context of word(s)/token(s) of set size N.

        - Technically what distinguishes the [[few-shot learning]] paradigm from [[fine-tuning]] is that you basically condition the output with some demonstrations and instructions, but don't allow any weight updates (so the underlying model is fundamentally the same)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2Ft426DcxvAq.png?alt=media&token=4a311fb0-6fdd-4e2a-88ea-8c01b276e2ad) (p. 6)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FQRpWGIQXPo.png?alt=media&token=38b562e0-f2e0-4168-b93b-9644ba23823f) (p. 7)
