#!/usr/bin/python3

##########################################################################
#
# This file will be used to extract information from the
# Instruction Set Architecture (ISA)
#
# Current supported ISAs include:
# PPC64
# RISCV
# x86
##########################################################################

import sys
import logging
import time
import string
import datetime
import getopt
import random
import subprocess
import os
import csv
import PyPDF2

# ---------Set sys.path for MAIN execution---------------------------------------
full_path = os.path.abspath(os.path.dirname(sys.argv[0])).split('ISA_Reference')[0]
full_path += "ISA_Reference"
sys.path.append(full_path)
# Walk path and append to sys.path
for root, dirs, files in os.walk(full_path):
    for dir in dirs:
        sys.path.append(os.path.join(root, dir))


import riscv
import ppc64
import x86
import utils

def usage():
    print("Usage: Please provide a pdf file for ISA")
    print("Example: python Main.py POWER_ISA_tags_v3.1")

def main(argv):

    if len(argv) < 1:
        print("Please provide a <ISA>.pfd file")
        raise Exception
    elif len(argv) > 1:
        print("Please provide only one pfd file at a time")
        raise Exception
    else:
        i_pdf = argv[0]

    if "PowerISA" in i_pdf.rsplit('/')[-1]:
        i_isa_object = POWERISA.newobject(i_pdf)
    else:
        print("Unrecognized ISA")

    # creating a pdf file object
    pdfFileObj = open(i_pdf, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(1440)

    # extracting text from page
    #print(pageObj.extractText())
    x = pageObj.extractText()
    #x = x.replace(' ', '')
    x = x.strip()
    x = x.split('\n')



    # closing the pdf file object
    pdfFileObj.close()

if __name__ == "__main__":
    main(sys.argv[1:])
