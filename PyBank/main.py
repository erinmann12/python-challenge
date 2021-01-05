#import the os module
import os

#import module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#initialize variables
total = 0
months = 0
sum_change = 0
previous = 0
max_change = 0
min_change = 0

#open CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        #total profit/loss, needs to be float because rows are strings
        total = total + float(row[1])
        #count total number of months
        months = months + 1

        #Calculate the changes in profit/losses
        #Works for every month but the first one, so created code to modify that
        if months > 1:
            change = float(row[1]) - previous
            sum_change = sum_change + change

            #find max_change from month to month
            if change > max_change:
                max_change = change
                date_max_change = row[0]
            #find min_change from month to month
            if change < min_change:
                min_change = change
                date_min_change = row[0]
        #set previous to current row
        previous = float(row[1])

        change = float(row[1]) - previous
        sum_change = sum_change + change

#calculate average of changes in profit/losses
average = sum_change / (months-1)

#format numbers to dollars and cents for average
formatted_average = "${:.2f}".format(average)

#print summary to the screen
print(f"Total months: {months}")
print(f"Total: ${int(total)}")
print(f"Average Change: {formatted_average}")
print(f"Greatest Increase in Profits: {date_max_change} (${int(max_change)})")
print(f"Greatest Decrease in Profits: {date_min_change} (${int(min_change)})")

#write to txt file
with open("analysis.txt", "w") as txt_file:

    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------------\n")
    txt_file.write(f"Total months: {months}\n")
    txt_file.write(f"Total: {total}\n")
    txt_file.write(f"Average Change: {formatted_average}\n")
    txt_file.write(f"Greatest Increase in Profits: {date_max_change} (${int(max_change)})\n")
    txt_file.write(f"Greatest Decrease in Profits: {date_min_change} (${int(min_change)})")