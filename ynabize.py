#! /usr/bin/env python

# title          : ynabize.py
# description    : parse Danske Bank csv exports to a form
#                  that You Need A Budget understands
# author         : Niko Salakka
# date           : 20150304
# version        : 1.0
# lincense       : GPLv2
# usage          : ynabize.py filename/filepath
# python version : 3.4

from decimal import Decimal
import sys

# Get the filename from arguments
# and open the files for writing/reading.
filename = sys.argv[1]
infile = open(filename, encoding="latin-1")
outfile = open("ynab_%s" % filename, 'a+')

# Skip the header line.
next(infile)

# Write the YNAB header to output file.
outfile.write("Date,Payee,Category,Memo,Outflow,Inflow\n")

# Parse the input file line by line,
# properly form the fields, form the output line
# and and write it to file.
for line in infile:
    s = line.split(';')
    date = s[0].replace(".", "/").replace("-", "/")
    payee = s[1]
    outflow = ''
    inflow = ''

    flow = s[2].replace(",", ".").replace(" ", "")

    if Decimal(flow) < 0:
        inflow = flow
    else:
        outflow = flow

    output = "%s,%s,%s,%s,%s,%s\n" % (date, payee, 'IMPORT',
                                      '', outflow, inflow)
    outfile.write(output)
