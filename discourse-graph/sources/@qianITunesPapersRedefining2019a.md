---
title: @qianITunesPapersRedefining2019a
url: https://roamresearch.com/#/app/megacoglab/page/dHZZbVBov
author: Joel Chan
date: Wed Mar 18 2020 11:42:16 GMT-0400 (Eastern Daylight Time)
---

- #references

    - Title: Beyond iTunes for Papers: Redefining the Unit of Interaction in Literature Review Tools

    - Meta

        - Tags: #[[D/Synthesis Infrastructure]] #ref/Paper

        - [[Authored by]]::  [[Xin Qian]] ,  Matt J. Erhart ,  [[Aniket Kittur]] ,  [[Wayne Lutters]] ,  [[Joel Chan]]

        - Year: 2019

        - Publication: [[CSCW]] '19

        - URL: https://doi.org/10.1145/3311957.3359455

    - #lit-context

        - Poster, not full paper

        - No eval

        - Our first published salvo for #[[D/Synthesis Infrastructure]], describing the [[[[ART]] - Knowledge Compressor]] work

###### Discourse Context

- **Informs::** [[CLM - Most scholarly communication infrastructure operates on the document as the base unit]]
- **Informs::** [[QUE - How can we best bridge private vs. public knowledge]]
- **Informs::** [[QUE - How might we characterize scientists' synthesis practices from a processtool perspective]]

###### References

[[June 8th, 2020]]

- Really cool to see how our [[D/Synthesis Infrastructure]] is starting to gain some traction. Honest signal from [[Andy Matuschak]] about hte value of our ideas: he [[SRS]]-ed our [[@qianITunesPapersRedefining2019a]] paper!

    - https://twitter.com/andy_matuschak/status/1270138015495581696

    - https://notes.andymatuschak.org/Grounded_claims%2C_after_Qian_et_al?stackedNotes=z6X8U64HPkrUaTw8uuDDQSBkVUhRMpUdupdzd

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FRu_WgT7iST.png?alt=media&token=18a33ab8-1645-4ae5-a6ba-2979c2743b80)
[[WP TOCHI Requirements framework for synthesis systems]]

- if you have a system that primarily works with too coarse of a unit and struggles to represent anything lower than that as a first-class object that you can see and manipulate (see #[[@qianITunesPapersRedefining2019a]])

    - notebooks escape this because YOU decide what counts, whereas the data structure of the "itunes for papers" **foregrounds** the document and **backgrounds** what you actually care about
[[QUE - How might we characterize scientists' synthesis practices from a processtool perspective]]

- Tools generally are "iTunes for papers" [[@qianITunesPapersRedefining2019a]] - I think this is very fair

    - [[@bosmanInnovationsScholarlyCommunication2016]] - can see by far most popular tools are "iTunes for papers": Reference management tools like [[sys/EndNote]], [[sys/Mendeley]], and [[sys/Zotero]] were the most frequently mentioned "cite" tools by [researchers](((TqJhckxKb))) worldwide responding to an online survey in [[2015]]. These top 3 tools collectively accounted for ~60% of responses.

        - European-leaning, but we get some confirmation/corroboration in smaller, more focused samples

            - [[@willisDocumentsDistributedScientific2014]] Sample of 12 social scientists used mix of Endnote and Mendeley for reference management

            - [[@qianOpeningBlackBox2020]] [ecology of tools](![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FpfGp_fY99U.png?alt=media&token=db2472d9-6884-467c-8ae0-5db27fcb6643)) includes Zotero and Mendeley

            - [[@hoangOpportunitiesComputerSupport2018]][researchers](((R4yIJzOBs))) basically never used specialized software for their [[systematic review]]s: instead, the most common tools were [[sys/Microsoft Excel]] and [[sys/EndNote]]
[[sysOpen Research Knowledge Graph]]

- basically the same motivaiton as us, even making the same general argument about the "[wrong unit of analysis]([[[[CLM]] - Most scholarly communication infrastructure operates on the document as the base unit]])" as we do in [[@qianITunesPapersRedefining2019a]]

    - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FS_LKSl-WHu.png?alt=media&token=beaffdd4-8fb7-46d7-93b3-320a35754014)
[[December 1st, 2020]]

- Novel augmentations of familiar tools that lower the costs of creating shareable representations (key cost is identifying and attaching context). We build on our preliminary work in [[@qianITunesPapersRedefining2019a]]

    - it turns out that a suped up PDF reader (with connections to open annotations like [[sys/Hypothes.is]]), so that the annotations are hyperlinkable, and a notetaking system with [[std/Hypertext]] affordances (like [[hypertext notebooks]]) are probably sufficient to produce the kinds of things we want

        - it's also technically feasible to move some of the hypertext affordances like [[bi-directional links]] and [[transclusion]] into something like Google Docs

        - and people are familiar with these affordances already, thanks to the ubiquity of [[sys/Wiki]]s
