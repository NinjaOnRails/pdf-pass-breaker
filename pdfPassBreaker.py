#! /usr/bin/env python3
# pdfPassBreaker.py - Goes through every word in a given txt dictionary
# and tries to break the password of the locked pdf file

import os, PyPDF2
import sys

pdf2D = sys.argv[1]

def passBreaker(dictio, pdf2D):
    dictContent = open(dictio).readlines()
    pdfReader = PyPDF2.PdfFileReader(open(pdf2D, 'rb'))
    for i in range(len(dictContent)):
        if pdfReader.isEncrypted == False:
            break
        print('Trying: ' + dictContent[i])
        if pdfReader.decrypt(dictContent[i][:-1].lower()) == 1:
                   print('The password is: ' + dictContent[i][:-1].lower())
                   break
        if pdfReader.decrypt(dictContent[i][:-1].upper()) == 1:
                   print('The password is: ' + dictContent[i][:-1].upper())
                   break
passBreaker('dictionary.txt', pdf2D)
