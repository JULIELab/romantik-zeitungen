w#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:24:02 2019

@author: kampe

This script will unpack all files from their archives, which where downloaded
from the respective digital libraries. It will then create a Slurm script
(https://slurm.schedmd.com/) which contains the commands to generate PDF and
ALTO XML output for all files of that archive.

Requires: Slurm, Tesseract >= 4.1
"""

import glob
import os
from os.path import basename, join
import stat # to set executable bit

# Please change the path to point the directory that contains the downloaded
# archives
path = '/var/local/kampe'
basedir = f'{path}/AmZ'

archives = glob.glob(path + '/*.zip')
zipnames = [basename(archive) for archive in archives]

volumes = {z.split('_')[0] for z in zipnames}
for key in volumes:
    exdir = join(basedir, key)
    script = '%s/%s.sh' % (basedir, key)
    with open(script, 'x') as bash:
        _ = bash.write('#!/bin/bash\n')
        _ = bash.write('mkdir -p %s\n' % (exdir))
        _ = bash.write("unzip '%s/%s_*.zip' -d %s\n" % (path, key, exdir))
        _ = bash.write('for f in %s/%s*.jpg;do tesseract "$f" %s/"$(basename $f .jpg)" -l deu alto ;done\n' % (exdir, key, exdir))
        _ = bash.write('for f in %s/%s*.jpg;do tesseract "$f" %s/"$(basename $f .jpg)" -l deu pdf ;done\n' % (exdir, key, exdir))
    st = os.stat(script)
    os.chmod(script, st.st_mode | stat.S_IEXEC)
    slurm = '%s/%s-slurm.sh' % (basedir, key)
    with open(slurm, 'x') as bash:
        _ = bash.write('#!/bin/bash\n')
        _ = bash.write('#SBATCH --mem=1G --cpus-per-task=3\n')
        _ = bash.write('srun -o ocr_%j /usr/bin/time -v {0}.sh'.format(exdir))
    st = os.stat(slurm)
    os.chmod(slurm, st.st_mode | stat.S_IEXEC)
