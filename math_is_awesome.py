#this it to help you learn python
''' to calculate the various things I've given you to do'''


import math
import csv


with open ('/Users/maxmende/Downloads/USM Service Data - Corporate Network (1).csv') as csvfile:
    scanner = csv.DictReader(csvfile)
    for row in scanner: 
        if row['osr_rating'] == 'R1'or row['osr_rating'] == 'R2':
            print(row['hostname'], row['vuln_title'], row['osr_rating'])

    print(row)
    for row in scanner:
        if row['osr_rating'] == 'R1':
            R1s = count(row['osr_rating'])
            print(R1s)
        
