#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:24:45 2019

@author: kampe

Script to manually inspect all of the issue boundaries.
This works for the issues compiles by the BSB (Bayerische Staatsbibliothek),
as their archives also contains OCR output that can be used for this case.

In other cases, it's necessary to extract the text out of the ALTO files first.
"""

from datetime import date, timedelta
import glob
import os
import re
import shutil
import textdistance
from typing import List

title = "MUSIKALISCHEZEITUNG."
title_part1 = "MUSIKALISCHE"
title_part2 = "ZEITUNG."

header = re.compile("----- ([0-9]{1,3}) / ([0-9]{1,3}) -----\n")
levenshtein = textdistance.Levenshtein()


def match_title(lines: List[str]) -> bool:
    """
    Performs fuzzy matching on the upper part of a page to find a title.

    Parameters
    ----------
    lines : List[str]
        The text of a page, line by line.

    Returns
    -------
    bool
        True, if a title has been found, False otherwise.

    """
    if len(lines) < 7:
        return False
    # Find a hit on one line
    for line in lines[:7]:
        text = line.rstrip().upper().replace(" ", "")
        if levenshtein.distance("BEYLAGE", text) <= 1 or levenshtein.distance(
            "BEYLAGE", text
        ):
            return True
        if levenshtein.distance(title, text) <= 3:
            return True
    for i in range(6):
        if (
            levenshtein.distance(
                title, (lines[i] + lines[i + 1]).rstrip().upper().replace(" ", "")
            )
            <= 3
        ):
            return True
    return False


def issue_begin(path: str) -> List[int]:
    """
    Find all front pages of issues by scanning the OCR output of the BSB
    for issue headers.

    Parameters
    ----------
    path : str
        Path to a text file that contains OCR output prepared by the BSB.

    Returns
    -------
    start_page : List[int]
        Indexes of all the first pages.

    """
    lines = []
    page = 0
    start_page = []
    with open(path, "rt") as bsb:
        for line in bsb:
            match = header.match(line)
            if match is not None:
                found_title = match_title(lines)
                if found_title:
                    start_page.append(page)
                lines.clear()
                page = int(match.group(1))
            else:
                lines.append(line)
    return start_page


# Please change the path to point the directory that contains the text files
main = "/var/local/kampe/AmZ/"
txts = glob.glob(main + "**/*.txt", recursive=True)
txts = sorted(txts)

# There's no loop around the counter (index), because batches need to be
# checked manually, in case the heuristic couldn't detect a boundary and there
# are larger gaps in the list of indices returned by issue_begib().
index = 0
print(txts[index])
issue_frontpage = issue_begin(txts[index])
# There should be 52 issues in a batch, except for volume 9 (65 issues)
print(len(issue_frontpage))
# Shows all indices
print(issue_frontpage)

# These directories have been created earlier by amz_slurm.py
volume = os.path.dirname(txts[index])
files = glob.glob(os.path.join(volume, "bsb*_*.*"))
bsb_matcher = re.compile(r"bsb[0-9]{7,8}_([0-9]{1,5})(\.[a-z2]{3})")
max_page = max(int(bsb_matcher.match(os.path.basename(x)).group(1)) for x in files)
issue = list(
    zip(issue_frontpage[1:], [x - 1 for x in issue_frontpage[2:]] + [max_page])
)

# The starting date has to be adjusted per volume, usually a Wednesday
start = date(1799, 10, 2)
if start.isoweekday() < 3:
    start = start + timedelta(days=3 - start.isoweekday())
elif start.isoweekday() > 3:
    start = start + timedelta(days=(3 + 7) - start.isoweekday())

# Move all the files in an issues into the directory structure required by
# Open ONI, using the list of indices created earlier
current = start
for t in range(len(issue_frontpage) - 1):
    issue_dir = os.path.join(volume, current.strftime("%Y%m%d01"))
    os.mkdir(issue_dir)
    for f in files:
        issue_file = os.path.basename(f)
        match = bsb_matcher.match(issue_file)
        page_number = int(match.group(1))
        if issue[t][0] <= int(page_number) <= issue[t][1]:
            running_nr = "%04d" % (page_number - issue[t][0] + 1,)
            shutil.move(f, os.path.join(issue_dir, running_nr + match.group(2)))
    current += timedelta(days=7)

## Dry run, just create directories
start = date(1799, 10, 2)
if start.isoweekday() < 3:
    start = start + timedelta(days=3 - start.isoweekday())
elif start.isoweekday() > 3:
    start = start + timedelta(days=(3 + 7) - start.isoweekday())


dirs = sorted(x for x in glob.glob(volume + "/*") if os.path.isdir(x))
current = start
for t in range(len(issue_frontpage) - 1):
    issue_dir = os.path.join(volume, current.strftime("%Y%m%d01"))
    shutil.move(dirs[t], issue_dir)
    current += timedelta(days=7)

## IA

volume = os.path.dirname(txts[index])
files = glob.glob(os.path.join(volume, "bub_gb_*_*.*"))
bub_matcher = re.compile(r"bub_gb_[A-Za-z]+_([0-9]{1,5})(\.[a-z2]{3})")
max_page = max(int(bub_matcher.match(os.path.basename(x)).group(1)) for x in files)
issue = list(
    zip(issue_frontpage[1:], [x - 1 for x in issue_frontpage[2:]] + [max_page])
)

start = date(1837, 1, 1)
if start.isoweekday() < 3:
    start = start + timedelta(days=3 - start.isoweekday())
elif start.isoweekday() > 3:
    start = start + timedelta(days=(3 + 7) - start.isoweekday())

# Move all the files in an issues into the directory structure required by
# Open ONI
current = start
for t in range(len(issue_frontpage) - 1):
    issue_dir = os.path.join(volume, current.strftime("%Y%m%d01"))
    os.mkdir(issue_dir)
    for f in files:
        issue_file = os.path.basename(f)
        match = bub_matcher.match(issue_file)
        page_number = int(match.group(1))
        if issue[t][0] <= int(page_number) <= issue[t][1]:
            running_nr = "%04d" % (page_number - issue[t][0] + 1,)
            shutil.move(f, os.path.join(issue_dir, running_nr + match.group(2)))
    current += timedelta(days=7)
