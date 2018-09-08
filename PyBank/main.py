
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


    

