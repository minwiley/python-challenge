# Your task is to create a Python script that analyzes the records to calculate each of the following:
# modules
import os
import csv

	# The total number of months included in the dataset
months_entire = []
	# The total net amount of "Profit/Losses" over the entire period
profit_loss = []
	# The average change in "Profit/Losses" between months over the entire period
between_months = []
	# The greatest increase in profits (date and amount) over the entire period
GreatIncrease = []
	# The greatest decrease in losses (date and amount) over the entire period
GreatDecrease = []

# cereal
budget_data_csv = os.path.join("budget_data.csv")

# countmonths = 0

with open(budget_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)
	print(f"Header: {csv_header}")

	row_count = len(open(budget_data_csv).readlines())
	print("row_count: ", row_count)


# Set variable for output file
output_file = os.path.join("PyBank_sum.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    csvwriter = csv.writer(datafile, delimiter=',')
    csvwriter.writerow(['Total Months: ', row_count])


    



#     # Specify the file to write to
# output_path = os.path.join("..", "output", "new.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])



	# row_count = sum(1 for in open(budget_data_csv))
	# print("row_count:",row_count)

	# for row in csvreader:
	# 	# countmonths = countmonths + 1 
	# 	countmonths += 1
	# 	print ("countmonths:", countmonths)

		# len(open(filename).readlines())
	 # 	print(len(row(0)))

	# 	# if row 0 
	# 	count 


# with open (cereal_csv,newline="") as csvfile:
# 	csvreader = csv.reader(csvfile,delimiter=",")
# 	# different object
# 	csv_header = next(csvreader, None)
# 	print(f"Header: {csv_header}")

# 	for row in csvreader:
# 		if float(row[7]) >= 5:
# 			print(row)
# 		# print(row[7])