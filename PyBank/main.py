
# PyBank

# # modules
import os
import csv

months_entire = 0
ttl_profit_loss = 0
prof_loss = []
between_months = []

# cereal & udemy examples reference
budget_data_csv = os.path.join("budget_data.csv")

with open(budget_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)
	print(f"Header: {csv_header}")

	for row in csvreader:
		ttl_profit_loss = ttl_profit_loss + int(row[1])
		prof_loss.append(int(row[1]))
		between_months.append(row[0])
		all_months = len(between_months)
		# row_count = len(open(budget_data_csv).readlines())
		avg_sum = round(ttl_profit_loss / all_months,4)

	print("Total Months: ", all_months)
	print(f"Total: ${ttl_profit_loss}")
	print(avg_sum)

GreatIncrease = prof_loss[0]
GreatDecrease = prof_loss[0]
ttl_profit_loss = 0

for srev in range(len(prof_loss)):
	if (prof_loss[srev] >= GreatIncrease):
		GreatIncrease = (prof_loss[srev])
		GreatIncrease_month = (between_months[srev])
	elif prof_loss[srev] <= GreatDecrease:
		GreatDecrease = prof_loss[srev]
		GreatDecrease_month = between_months[srev]
	ttl_profit_loss += prof_loss[srev]

print(GreatIncrease_month, GreatIncrease)
print(GreatDecrease_month, GreatDecrease)
print(ttl_profit_loss)

# Set variable for output file 	
output_file = os.path.join("PyBank_sum.txt")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    csvwriter = csv.writer(datafile, delimiter=',')
    csvwriter = csv.writer(datafile)    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow(['Total Months: \t'+ str(all_months)])
    csvwriter.writerow(['Total: \t$' + str( ttl_profit_loss)])
    csvwriter.writerow(['Greatest Increase in Profits: \t' + str(GreatIncrease_month) + '\t$' + str(GreatIncrease)])
    csvwriter.writerow(['Greatest Decrease in Profits: \t' + str(GreatDecrease_month) + '\t$' + str(GreatDecrease)])


    



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




budget_data_csv = os.path.join("budget_data.csv")

months = []
revenue = []

with open(budget_data_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)
	print(f"Header: {csv_header}")

	for row in csvreader:
		months.append(row[0])
		revenue.append(int(row[1]))

#find total months
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set total revenue = 0 
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
for r in range(len(revenue)):
	if revenue[r] >= greatest_inc:
		greatest_inc = revenue[r]
		great_inc_month = months[r]
	elif revenue[r] <= greatest_dec:
		greatest_dec = revenue[r]
		great_dec_month = months[r]
	total_revenue += revenue[r]

#calculate average_change
average_change = round(total_revenue/total_months, 2)


1170593

-1196225



