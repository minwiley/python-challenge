# Your script will need to do the following: Import a text file filled with a paragraph of your choosing.
# Assess the passage for each of the following:
	# Approximate word count; Approximate sentence count; 
	# Approximate letter count (per word); Average sentence length (in words)

# modules
import os
import csv
import re
import pandas as pd

paragraph1_csv = os.path.join("paragraph_1.txt")

with open(paragraph1_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	


# https://en.wikipedia.org/wiki/Regular_expression	
# .count()	
	
	
	
# Set variable for output file 	
output_file = os.path.join("PyParagraph_sum.txt")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    csvwriter = csv.writer(datafile, delimiter=',')
