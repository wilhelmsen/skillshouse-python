#!/usr/bin/python
# coding : utf-8

import os
import sys
import argparse


parser = argparse.ArgumentParser(description='list n files in directory')
parser.add_argument('files',
                    metavar='N',
                    type=int,
                    nargs='+',
                    help='How many files should be listed')

parser.add_argument('--directory',
                    dest='directory',
                    action='store_const',
                    type=str,
                    default='.',
                    help='directory to list')




