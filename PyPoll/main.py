# PyPoll
# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# # modules
import os
import csv

votes = []

election_data_csv = os.path.join("election_data.csv")
with open(election_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)
	print(f"Header: {csv_header}")

	for row in csvreader:
		votes.append(row[0])
		ttl_votes =len(votes)
	print("Total num votes: ", ttl_votes)


# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Set variable for output file 	
output_file = os.path.join("PyPoll_sum.txt")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
	csvwriter = csv.writer(datafile, delimiter=',')
	csvwriter = csv.writer(datafile)    
	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['-------------------'])
	csvwriter.writerow(['Total number of votes: \t' + str(ttl_votes)])
	csvwriter.writerow(['-------------------'])