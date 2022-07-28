#!/usr/bin/env python
# coding: utf-8

import os
import re
import math

def get_full_page_refs(text):
    
    # first grab wikilinks
    wikilinks = []
    # left square brackets and their indices
    for m in re.finditer(r'\[{2}', text):
        start, stop = m.span()
        wikilinks.append((start, stop, "start"))
    # right square brackets and their indices
    for m in re.finditer(r'\]{2}', text):
        start, stop = m.span()
        wikilinks.append((start, stop, "stop"))
    # sort into a sequence
    wikilinks.sort(key=lambda x: x[0])
    # for w in wikilinks:
    #     print(w)
    
    # now use these to grab the full page refs!! super hacky
    fullrefs = []

    idx = 0
    # go through the wikilinks
    while idx < len(wikilinks):
        now = wikilinks[idx]
        print("iterating onto ", now, " at index ", idx)
        print(text[now[0]:now[1]+5])
        if now[2] == "start" and not re.match(r"\[\[.+\]\(", text[now[0]:now[1]+200]): # latter pattern catches the dumb markdown ref edge case
            begin = now
            nowidx = idx
            print("Found new starting point: ", begin)
            # look ahead in pairs
            lefti = idx + 1
            righti = lefti + 1
            innerpair = False
            foundend = False
            while lefti < len(wikilinks) and foundend == False:
                # if we're not at the end already
                if righti < len(wikilinks):
                    # get the stuff
                    left = wikilinks[lefti]
                    right = wikilinks[righti]
                    print("checking", left, right)
                    # CASE: immediate end found!
                    if left[2] == "stop" and (innerpair != True or foundend == False):
                        end = left
                        print("found end immediately!")
                        print("large: ", begin, end, "\n")
                        fullrefs.append((begin[0], end[1]))
                        foundend = True
                        # resume after the lefti
                        idx = righti
                        print("next index is ", idx)
                        break
                    # CASE: found a pair
                    elif left[2] == "start" and right[2] == "stop":
                        # continue
                        print("found a pair!")
                        print("pair: ", left, right)
                        innerpair = True
                        # hop to the next pair
                        lefti = righti + 1
                        righti = lefti + 1
                    # CASE: found end eventually
                    elif left[2] != "start" and right[2] == "stop":
                        end = right
                        print("found end eventually!")
                        print("large: ", begin, end, "\n")
                        fullrefs.append((begin[0], end[1]))
                        foundend = True
                        # resume after the righti
                        idx = righti + 1
                        print("next index is ", idx)
                        break
                    else:
                        print("didn't find anything...")
                        # hop to the next pair
                        lefti = righti + 1
                        righti = lefti + 1
                        idx = nowidx + 1
                else: # we got to the end
                    left = wikilinks[lefti]
                    print("checking last one", left)
                    if foundend != True and left[2] == "stop":
                        end = left
                        print("found end eventually!")
                        print("large: ", begin, end, "\n")
                        fullrefs.append((begin[0], end[1]))
                        foundend = True
                        # resume after the lefti
                        idx = lefti + 1
                        print("next index is ", idx)
                        break
                    else:
                        # hop to the next pair
                        lefti = righti + 1
                        righti = lefti + 1
                        # resume at next index from where we were (this might be the [[markdown ref]()] edge case)
                        idx = nowidx + 1
        else:
            idx += 1

    print("\nNow grabbing each full ref text...")
    return [text[ref[0]:ref[1]] for ref in fullrefs]

def clean_page_refs(text, pagerefs):
    textclean = text
    for ref in pagerefs:
        # remove all complex page names
        refclean = ref.replace("[[","").replace("]]","")
        # remove special characters
        refclean = re.sub(r'[<>:"/\\|\?*[\]]', "", refclean)
        # truncate
        if len(refclean) > 200:
            leftend = math.ceil((200-3)/2)
            rightstart = math.floor((200-3)/2)-3
            refclean = f"{refclean[:leftend]}...{refclean[-rightstart:]}"

        textclean = textclean.replace(ref, f"[[{refclean}]]")
    return textclean

DIRNAME = "/Users/joelchan/Projects/discourse-graph-exports/megacoglab_query-results_202207280845"

os.mkdir(f"{DIRNAME}/discourse-graph/")

counter = 0

mapping = {
    "QUE": "questions",
    "CLM": "claims",
    "EVD": "evidence",
    "THE": "theories",
    "PTN": "patterns",
    "ART": "artifacts"
}

for fname in os.listdir(DIRNAME):
    #if counter > 100:
    #    break
    if fname.endswith(".md"):
        try:
            content = open(f"{DIRNAME}/{fname}", encoding="utf-8").read()
            print("processing ", fname)
            # check if discourse context is empty
            split = content.split("######")
            # find the one that has discourse context in it
            dcmatches = list(filter(lambda x: 'Discourse Context\n\n' in x, split))
            if len(dcmatches) > 0:
                dc = dcmatches[0]
                if len(dc) > 25:
                    print("has discourse context! adding...")

                    # remove reference context, which is everything after discourse context
                    dci = split.index(dc)
                    cleaned = "######".join(split[:dci+1])

                    # output
                    dpath = mapping.get(fname[:3], "skip")
                    if dpath != "skip":
                        fdir = f"{DIRNAME}/discourse-graph/{dpath}/"
                        # fullpagerefs = get_full_page_refs(cleaned)
                        # cleaned = clean_page_refs(cleaned, fullpagerefs)
                        if not os.path.exists(fdir):
                            os.mkdir(fdir)
                        open(f"{fdir}/{fname}", 'w').write(cleaned)
                    elif fname.startswith("@"):
                        fdir = f"{DIRNAME}/discourse-graph/sources/"
                        if not os.path.exists(fdir):
                            os.mkdir(fdir)
                        # fullpagerefs = get_full_page_refs(cleaned)
                        # cleaned = clean_page_refs(cleaned, fullpagerefs)
                        open(f"{fdir}/{fname}", 'w').write(cleaned)
                    else:
                        print("not something we want to save rn, skipping...")

                else:
                    print("no discourse context, skipping...")
        except UnicodeDecodeError:
            print("Unicode decode error for ", fname)

