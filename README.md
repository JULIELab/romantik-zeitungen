# romantik-zeitungen
Code to create the data required by the Open ONI instance running on romantik-zeitungen.de.

The processing takes places in several stages:

1. amz_slurm.py generates Slurm scripts to extract the files from their archives and process them with Tesseract, to generate the required ALTO XML and PDFs.
2. Actual processing step on a cluster
3. Separation of all issues into their respective folders as required by Open OPI (via amzissue.py and xmltotext.py)

The ALTO portion of this data can also be found on Zenodo:

Bernd Kampe, Tinghui Duan, & Udo Hahn. 
(2020). OCRed text of the Allgemeine musikalische Zeitung (ALTO format) 
from 1798-1848 and 1863-1965 [Data set]. Zenodo. 
http://doi.org/10.5281/zenodo.3708427
