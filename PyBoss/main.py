import pandas as pd
import csv
import os

# data_file = "employee_data.csv"
# data_file_pd = pd.read_csv(data_file)
# data_file_pd.head()
# print(data_file_pd.head())
employee_data_csv = os.path.join("employee_data.csv")

emp_id = []
Name = []
DOB = []
SSN = []
State = []
first_name = []
last_name = []
state_abbrev = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(employee_data_csv, newline="") as csvfile:
	csvreader = csv.DictReader(csvfile, delimiter=",")
	csv_header = next(csvreader, None)

# The State data should be re-written as simple two-letter abbreviations.
	for row in csvreader:
		emp_id.append(row["Emp ID"])
		DOB.append(row["DOB"])
		SSN.append(row["SSN"])
		State.append(us_state_abbrev[row["State"]])
# The Name column should be split into separate First Name and Last Name columns.
		name = row["Name"].split(" ")
		first_name.append(name[0])
		last_name.append(name[1])
# The DOB data should be re-written into MM/DD/YYYY format.
# The SSN data should be re-written such that the first five numbers are hidden from view.

updated = zip(emp_id, first_name, last_name, DOB, SSN, State)

	# print(first_name)
	# print(last_name)
	# print(State)

# Set variable for output file 	
output_file = os.path.join("PyBoss_sum.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    csvwriter = csv.writer(datafile, delimiter=',')
    csvwriter.writerow(["Emp ID", "First Name", "Lame Name", "DOB", "SSN", "State"])
    csvwriter.writerow(updated)

