#!/usr/bin/python
# coding : utf-8
#
#
# small argparse example 
# run with 
# python 005_small_script.py 4 --directory=/tmp/
#
# or 
#
# python 005_small_script.py
#
# to see argparse options

import os
import sys
import argparse


parser = argparse.ArgumentParser(description='list N files in directory')
parser.add_argument('N',
                    type=int,
                    help='How many files should be listed')

parser.add_argument('--directory',
                    default='.',
                    help='directory to list')


args = parser.parse_args()

files = os.listdir(args.directory)
for fn in files[:min(args.N, len(files))]:
    print(fn)


