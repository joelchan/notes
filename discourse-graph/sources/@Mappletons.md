---
title: @Mappletons
url: https://roamresearch.com/#/app/megacoglab/page/IDmSh3oX4
author: Joel Chan
date: Wed May 20 2020 19:54:37 GMT-0400 (Eastern Daylight Time)
---

- [[Maggie Appleton]]

###### Discourse Context



###### References

[[May 25th, 2020]]

- #roamhack via [[@Mappletons]] - using custom css to "color" the building blocks of what I'm writing. Could be an interesting new way to "[converse with the problem](Past thought thread on this [here](((53LAHoah7))), framing it in terms of conversing with the problem/argument in the [[Donald Schön]] sense of [[Reflection-in-Action]] and [[Reflective Conversation with the Design Material]])"

    - Could even be a way to visually color whether I'm building on "stubs" or not. :)

    - Example:

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FFDrNeqPgdD.png?alt=media&token=5a5c7e32-d2ed-45b8-a59e-b96c25ef60f2)

    - [[sys/Codex]] has really interesting concept of [[Standoff Properties]] as a way to bridge the world of text with the world of entities.  [[@neillCodexAtlasRelations2019]] - have known about this for awhile, not sure why I'm only now putting this into here.
[[roamcssarchive]]

- [[@Mappletons]]

    - [[Site-wide]]

        - ```css
h1,
h2,
h3,
h4,
h5,
h6 {
    font-family: "Lato", sans-serif;
    font-size: 3em;
}
div,
textarea {
    font-family: "Open Sans", sans-serif;
    font-weight: 400;
    color: #3F4758;
    font-size: 1.002em;
}
.roam-block-container {
    max-width: 1000px;
}

.rm-pomodoro {
    background: #fff !important;
    color: #ff4747 !important;
    padding: 4px 14px;
    line-height: 2em;
    font-weight: 600;
    border-radius: 2em;
    border: 1px solid #ff474770;
}

.rm-pomodoro {
    background: #ff6956 !important;
    color: #fff !important;
    padding: 4px 14px;
    line-height: 2em;
    font-weight: 600;
    border-radius: 2em;
    border: 1px solid #ed5845;
}

.rm-pomodoro::first-letter {
  margin-right: 8px;
}

.rm-query {
    border: 0.5px solid #e4e9ec;
    border-radius: 5px;
    
}

.rm-query .rm-query-title {
    background-color: #f7f8f8;
    padding: 0.8em;
    color: #d1dbe2;
    font-size: 80%;
}

.rm-reference-main.rm-query-content {
    padding: 0.8em;
}

.rm-reference-main .rm-reference-item .rm-block-text {
    font-size: 90%;
}

.rm-ref-page-view-title span {
    
}

.rm-reference-main .rm-reference-item .controls {
    margin-left: -1em;
}

.rm-ref-page-view {
    padding: 0.4em 0.2em;
}

.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper .starred-pages .page {
    padding: 6px;
}

div.flex-v-box.starred-pages-wrapper > div.flex-h-box > span {
    font-size: 14px !important;
    opacity: 80%;
    letter-spacing: 0.04em;
}

div.roam-sidebar-container.noselect > div > div {
    font-size: 14px !important;
    letter-spacing: 0.03em;
    
}

#block-input {
    background: white;
}

.roam-body #block-input > span > div {
    padding: 6px 24px;
    background: white;
}

span.bp3-icon-small.bp3-icon-star {
    display: none;
    visibility: hidden;
}

.roam-block {
    max-width: 850px;
}

#right-sidebar > div {
    background-color: #f7f8fa;
    border-left: 1px solid #e9ebef;
}
.controls .simple-bullet-outer .simple-bullet-inner {
    background-color: #e5e9f2;
}
.block-border-left {
    border-left: 1px solid #f3f6f7;
}
.kanban-board {
    background-color: #fff;
}
.kanban-card {
    background-color: white;
    margin: 8px;
    box-shadow: 0px 1px 2px #9eb3c0a8;
    padding: 10px;
    border-radius: 2px;
    line-height: 1.3em;
}
.kanban-title {
    text-align: center;
    font-weight: 600;
    font-size: 1.1em;
    opacity: 80%;
    color: #485f6f;
    padding-top: 8px;
    border-bottom: 1px solid #c5d1d8;
}
.kanban-column {
    background-color: #e7eff3;
    margin: 0px 4px 0px 4px;
    padding: 4px;
    min-width: 200px;
    border-radius: 3px;
}


.rm-block-ref::before {
    content: '';
    display: inline-block;
    width: 2px;
    border-radius: 40px;
    height: 12px;
    background: #ff913c;
    margin-right: 8px;
}
.rm-block-ref {
    /*border-bottom: none;*/
    font-size: 1em;
    color: #515e70;
}
.rm-block-ref:hover {
    background: none;
    cursor: pointer;
}
.checkmark {
    background: #fff;
}
.check-container input:checked ~ .checkmark {
    background: #33bdea;
}
.check-container input:checked ~ .checkmark:after {
    border-color: #fff;
}
.rm-reference-item {
    margin-top: 8px;
    border-radius: 6px;
    border: 1px solid #e4e9ee;
    margin-right: 8px;
    flex: 1 1 100%;
    word-break: break-word;
    background-color: #f7f9fb;
    padding: 8px;
}

.rm-level2 {
    font-size: 1.5em;
}
.rm-level3 {
    color: #939aae;
    font-weight: 400;
    font-size: 1.3em;
}
.rm-page-ref {
    color: #9aabd0;
}
.rm-page-ref-link-color {
    color: #ec6f35;
    font-weight: 600;
}
a {
    color: #8A3CC8;
}
.intercom-app,
.intercom-launcher-frame,
#intercom-container {
    display: none !important;
}
.roam-body .roam-app .roam-sidebar-container {
    background-color: white;
    border-right: 1px #eee solid;
}
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper .starred-pages .page,
.roam-body .roam-app .roam-sidebar-container > * {
    opacity: 80%;
    box-shadow: none;
}
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .starred-pages-wrapper .starred-pages .page:hover,
.roam-body .roam-app .roam-sidebar-container .roam-sidebar-content .log-button:hover {
    background: white;
    color: black;
    opacity: 100%;
}
#buffer.tall {
    height: calc(100vh - 50px) !important;
}
.check-container {
    padding-right: 4px;
}
span.rm-page-ref {
    border-radius: 2px;
    padding-left: 1px;
    padding-right: 1px;
}
.content span.rm-page-ref {
    padding: 4px 1px 1px;
    /* required for fixing azo */
}
.center-proj {
    text-align: center;
}

```
[[WP JCDL Where the semantic publishing rubber meets the scholarly practice road]]

- Examples of [[Digital Garden]]s from [[@Mappletons]]

    - https://twitter.com/Mappletons/status/1250532315459194880
[[July 12th, 2020]]

- cool lightning talk by [[@Mappletons]] on [[embodied cognition]] and implications for how we think about [[second brain]] stuff and [[Tools for Thought]]: https://maggieappleton.com/neocyborgs

    - cc [[[[CLM]] - Where possible, design systems, not tools]]

    - reminded me of this excellent paper on implications of [[embodied cognition]] for [[HCI]]: [[@klemmerHowBodiesMatter2006]]

    - leads to rabbit hole back to [[standpoint theory]] and the idea of [[[[CLM]] - Knowledge is fundamentally contextual]]

        - really great summary of what [[@harawaySituatedKnowledgesScience1988]] says about how [[context]] really really matters (and what that means) when evaluating and interpreting knowledge claims [[@harrisonMakingEpistemologicalTrouble2011]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FUMEyGlsYop.png?alt=media&token=6d4ce0df-ed3f-4b47-9243-454d2831bb91)

        - is it a fool's errand to try to combine these repeated insights (see [[communities of practice]], [[Cynefin model]], [[@ackermanSharingKnowledgeExpertise2013]], etc.) about the [[context]]ual and situated nature of knowledge with the project of a [[Semantic Web]]? situated semantic webs?

            - quick search for intersection of situated cognition and semantic web, and i'm not really seeing any coherent body of work. not sure if i'm looking in the right place, though.

                - https://scholar.google.com/scholar?hl=en&as_sdt=0%2C21&q=situated+cognition+semantic+web&btnG=

                - on [[sys/ConnectedPapers]]: https://www.connectedpapers.com/main/4a49c51b6a17a41e7634c0d169915e0e18bbbb78/Situated-Cognition-in-the-Semantic-Web-Era/graph

                    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FI5I_fyoBpM.png?alt=media&token=69f993f3-1eae-4e96-aeaf-c67594f20256)
[[May 23rd, 2020]]

- Loving the metaphor of [[Knowledge Gardening]]. Seeing folks on the [[Digital Garden]] [[Digital Gardeners Telegram group]]  talk about planting [[Seedlings]] and using [[SRS]] to bring them back to attention, to systematically grow them ([[@Mappletons]])

    - The framing is meditative, and slow, evokes ideas of pruning as well as watering and growing. Love it! Really resonates.
[[sysEvergreen Notes]]

- Nice visual explainers by [[@Mappletons]] here:

    - [Growing the Evergreens](https://maggieappleton.com/evergreens)

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F40U38iKI59.png?alt=media&token=48942e36-4f14-434a-8c4b-7ce085c2ffd6)
[[June 14th, 2020]]

- Very stimulating email conversation with [[Andy Matuschak]] about [creativity-applications](A deliberate practice of memory like [[SRS]] that is focused in this way on the particulars might seem like a bad idea because of [[🧱 fixation]]: but would it increase [[🧱 fixation]]? I think there is reason to think it might have the opposite effect. Might it not "atomize" the particulars, and distribute them across space and time, enervating their connections to various other particulars, and in that way support the delicate balance of specificity and [[abstraction]]?) of [[SRS]]. Want record in particular his notes on this, around [[rprogrammable attention]] as a key mechanism, and similar applications as [[@Mappletons]] and others for [[SRS]] as a way to [develop a writing inbox practice](((lPBSy-X09)))

    - https://notes.andymatuschak.org/Spaced_repetition_may_be_a_helpful_tool_to_incrementally_develop_inklings?stackedNotes=z2gqazXUkf9qyFjMQg4W3dw6yegnAJszvDywN&stackedNotes=z7yRMBXGc81KkUwLxefodzfnnfKXx63vXzP88
