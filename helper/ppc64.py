#!/usr/bin/python3

##########################################################################
#
# This file will be used to store helper functions for PPC64 ISA
#
#
##########################################################################

import PyPDF2

import utils


class PPC64:
    def __init__(self, i_pdf):
        self.pdf = i_pdf
        self.instructions = []
        self.opcodes = []
        self.page = []
        self.isa_version = []
        self.description = []

        # creating a pdf file object
        self.pdfFileObj = open(i_pdf, 'rb')
        # creating a pdf reader object
        self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
        # Total number of pages
        self.pages = self.pdfReader.numPages

        self.extract_information_from_pdf()

    def extract_information_from_pdf(self):

        # Set this bool to False until we get to the correct appendix that
        # has all the instructions list
        begin_instruction_processing = False

        # Loop through all pages until you get to
        # Appendix F. Power ISA Instruction Set Sorted by Version
        # The first line must contain a reference to the correct page
        for page_num in range(self.pages):
            # creating a page object
            i_pageObj = self.pdfReader.getPage(1440)  # <----- replace this with page_num
            i_text = i_pageObj.extractText()
            i_header = ((i_text.split('\n')[0]).strip()).replace(' ', '')
            if "PowerISAInstructionSetSortedbyVersion" in i_header:
                begin_instruction_processing = True

            if begin_instruction_processing:
                # Break the page into elements based on newline and then strip to remove any leading
                # or trailing spaces, and also remove all spaces in between chars
                i_text = i_text.replace(' ', '').split('\n')
                i_text = [s.strip() for s in i_text]
                i_text = [s.strip() for s in i_text]


                x = 1
