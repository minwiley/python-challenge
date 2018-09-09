# PyPoll




# # modules
import os
import csv
import pandas as pd

votes = []

Voter_ID = []
County = []
Candidate = []

election_data_csv = os.path.join("election_data.csv")
with open(election_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)
	print(f"Header: {csv_header}")

# The total number of votes cast
	for row in csvreader:
		votes.append(row[0])
		ttl_votes =len(votes)
	print("Total num votes: ", ttl_votes)

election_data = "election_data.csv"

election_data_pd = pd.read_csv(election_data)
election_data_pd.head()
print(election_data_pd.head())

unique = election_data_pd["Candidate"].unique()
print(unique)
# A complete list of candidates who received votes
# ['Khan' 'Correy' 'Li' "O'Tooley"]

count_candidates = election_data_pd["Candidate"].value_counts()
print(count_candidates)


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
	csvwriter.writerow(['Total Votes: \t' + str(ttl_votes)])
	csvwriter.writerow(['-------------------'])


