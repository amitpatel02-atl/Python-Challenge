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

    total_profit = 0
    List_of_changes =[]
    Greatest_Increase = 0
    Greatest_Decrease = 0

    # Loop through looking for the months then add to counter
    month_counter = 0
    for row in csvreader:

       # Count number of months 
       month_counter= (month_counter+ 1)

       # Calculate Total Profit
       total_profit = total_profit + int(row[1])

       # Calculate month-to-month change
       if month_counter ==1:
           previous = int(row[1])
       else:
            month_to_month_change = int(row[1]) - previous
            previous = int(row[1])
            List_of_changes.append(month_to_month_change)

            # Calculate greatest increase in profits:
            if Greatest_Increase < month_to_month_change:
                Greatest_Increase = month_to_month_change
                Greatest_Increase_Date = str(row[0])

            elif Greatest_Decrease > month_to_month_change:
                Greatest_Decrease = month_to_month_change
                Greatest_Decrease_Date = str(row[0])

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months : {month_counter}")
    print(f"Total : ${total_profit}")
    print(f"Average Change: float("{0:.2f}".format{sum(List_of_changes)/{month_counter} - 1)")
    print(f"Greatest Increase in Profits : {Greatest_Increase_Date} {Greatest_Increase}")
    print(f"Greatest Decrease in Profits : {Greatest_Decrease_Date} {Greatest_Decrease}")
   