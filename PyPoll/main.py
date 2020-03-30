# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

#Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

  # Create a variable and set it as an List
  list_of_candidates = ["Khan", "Correy", "Li", "O'Tooley"]

    total_votes = 0
   

     #Loop through looking for the votes then add to counter
    vote_counter = 0
    for row in csvreader:

        #Count number of months 
        month_counter= (month_counter+ 1)

    print("Election ")
    print("------------------")
    print(f"Total Months : {month_counter}")
    print(f"Total : ${total_profit}")
    print(f"Average Change:{sum(List_of_changes)/ (month_counter-1)}")
    print(f"Greatest Increase in Profits : {Greatest_Increase_Date} (${Greatest_Increase})")
    print(f"Greatest Decrease in Profits : {Greatest_Decrease_Date} (${Greatest_Decrease})")print(list_of_candidates)
