#!/usr/bin/python3

"""
removes lines from a csv file based on user input criteria
"""

import csv
import sys

input("The file we're working with needs to be in the same directory " +
        "as this .exe file.\nHit Enter.")

filename = input("Enter the file name\nRemove any special characters " + 
        "the filename first\nThe file should be exported from excel " +
        "into \"csv\" format. For help on this see\n" + 
        "https://www.ablebits.com/office-addins-blog/2014/04/24/convert-" +
        "excel-csv/\nYour Entry: ")
fields = input("What should I look for to identify the line to be " + 
        "removed?\ne.g. if each line to be removed begins with x in the " +
        "first column you would enter \"x\" here (minus the quotes).\n" +
        "If we're looking for something thats blank just hit enter\n" +
        "Your Entry: ")

column = int(input("enter the column number that we should be looking for " +
        "that field. e.g. If it's the first column enter \"1\" (minus " +
        "the quotes\nYour Entry: "))

column -= 1


with open(filename,'r') as input, open(filename + "-output.csv","w") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[column] != fields:
            writer.writerow(row)

print("output written to " + filename + "-output.csv")
