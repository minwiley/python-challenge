# # modules
import os
import csv
import re

paragraph1_csv = os.path.join("paragraph_1.txt")

with open(paragraph1_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
