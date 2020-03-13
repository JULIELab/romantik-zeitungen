#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:59:22 2019

@author: kampe

Just a helper script that extracts text from a batch of XML files and writes
it all to one larger file.
To be used together with amzissue.py
"""
import glob
from typing import List
from xml.etree.ElementTree import iterparse

def write_text(xmlfiles: List[str], output: str):
    """
    Extracts text from a batch of XML files and writes it all to one larger
    file.

    Parameters
    ----------
    xmlfiles : List[str]
        A list of XML files.
        
    output : str
        Destination of the text output.

    Returns
    -------
    None.

    """
    with open(output, "wt") as out:
        for i, source in enumerate(xmlfiles):
            # Imitates formatting of BSB files
            _ = out.write("----- %s / %s -----\n" % (i, len(xmlfiles)))
            context = iterparse(source, events=("start", "end"))
            context = iter(context)
            for event, elem in context:
                if event == "start" and "CONTENT" in elem.attrib:
                    _ = out.write(elem.attrib["CONTENT"] + "\n")


# Please change the path to point the directory that contains the text files
xmlfiles = sorted(glob.glob("/var/local/kampe/IA/bub_gb_ahZDAAAAcAAJ_jp2/*.xml"))
output = "/var/local/kampe/IA/bub_gb_ahZDAAAAcAAJ_jp2/ocr.txt"
write_text(xmlfiles, output)
