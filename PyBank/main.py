# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

#Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    # Loop through looking for the months then add to counter
    month_counter = 0
    for row in csvreader:
       month_counter= (month_counter+ 1)

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months : {month_counter}")

    #Loop through looking for the net total amount of Profit/Losses over the entire period
    profit_sum = 0
    loss_sum = 0
    total_profit = 0
    profit = 0

    for row in csvreader:
        profit = int(row[1])
