# PyPoll

# modules
import os
import csv
import pandas as pd

votes = []
Voter_ID = []
County = []
Candidate = []

k_votes = 0
c_votes = 0
l_votes = 0
o_votes = 0

election_data_csv = os.path.join("election_data.csv")
with open(election_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)
	# print(f"Header: {csv_header}")

# The total number of votes cast
# The total number of votes each candidate won
	for row in csvreader:
		votes.append(row[0])
		ttl_votes =len(votes)

		if row[2] == "Khan":
			k_votes += 1
		elif row[2] == "Correy":
			c_votes += 1
		elif row[2] == "Li":
			l_votes += 1
		elif row[2] == "O'Tooley":
			o_votes += 1
	print('Election Results')
	print('-------------------')			
	print("Total votes: ", ttl_votes)
	print('-------------------')			

	# print('Khan: ', k_votes)
	# print('Correy: ', c_votes)
	# print('Li: ', l_votes)
	# print("O'Tooley: ", o_votes)

votes_list = [k_votes,c_votes,l_votes,o_votes]

vote_dict = {"Khan":k_votes, 
				"Correy": c_votes, 
				"Li": l_votes,
				"O'Tooley":o_votes
				}
# print(vote_dict)

# The percentage of votes each candidate won
k_percent = ('{0:.3f}%'.format((k_votes/ttl_votes)*100))
c_percent = ('{0:.3f}%'.format((c_votes/ttl_votes)*100))
l_percent = ('{0:.3f}%'.format((l_votes/ttl_votes)*100))
o_percent = ('{0:.3f}%'.format((o_votes/ttl_votes)*100))
print('Khan: ', k_percent, '(',k_votes,')\n'
	"Correy: ", c_percent, '(',c_votes,')\n'
	"Li: ", l_percent,  '(',l_votes , ')\n'
	"O'Tooley: " ,o_percent, '(',o_votes,')\n'
	)
	
print('-------------------')	

# The winner of the election based on popular vote.
winner = max(vote_dict, key = lambda x: vote_dict.get(x))
print('Winner:', winner)
print('-------------------')	
election_data = "election_data.csv"

election_data_df = pd.read_csv(election_data)
election_data_df.head()
# print(election_data_df.head())

# A complete list of candidates who received votes
# ['Khan' 'Correy' 'Li' "O'Tooley"]

# Set variable for output file 	
output_file = os.path.join("PyPoll_sum.txt")
 # Open the output file
with open(output_file, "w", newline='') as datafile:
	csvwriter = csv.writer(datafile, delimiter=',')
	csvwriter = csv.writer(datafile)    
	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['-------------------'])
	csvwriter.writerow(['Total Votes: \t' + str(ttl_votes)])
	csvwriter.writerow(['-------------------'])
	csvwriter.writerow(['Khan: ' + k_percent + '%\t' + '(' + str(k_votes) +')'])
	csvwriter.writerow(['Correy: ' + str(c_percent) + '%\t' + '(' + str(c_votes) +')'])
	csvwriter.writerow(['Li: ' + str(l_percent) + '%\t' + '(' + str(l_votes) +')'])
	csvwriter.writerow(["O'Tooley: " + str(o_percent) + '%\t' + '(' + str(o_votes) +')'])
	csvwriter.writerow(['-------------------'])
	csvwriter.writerow(['Winner: \t' + str(winner)])
