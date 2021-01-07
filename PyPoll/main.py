#import the os module
import os

#import module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#initialize variables
votes = 0

#create dictionary to hold candidate names
candidates = {}

#open CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
    
        #count total number of votes by looping through and counting rows
        votes = votes + 1
        
        if row[2] in candidates:
            #incriminent candidate by 1
            candidates[row[2]] = candidates[row[2]] + 1
            #pass
        else:
            #add that candidate to dictionary with a count of 1
            candidates[row[2]] = 1
            #pass

#print summary to the screen
print(f"Total Votes: {votes}")

for key, value in candidates.items():

    #calculate the percent of vote each candidate received, formatted it to percent
    percent_vote = "{:.0%}".format(int(value)/votes)
    print(f"{key}: {percent_vote} ({value})")

    #determine the winner by using dict.get function
    winner = max(candidates, key=candidates.get)
    print(f"Winner: {winner}")

#write to txt file
with open("analysis.txt", "w") as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("---------------------------\n")
    txt_file.write(f"Total votes: {votes}\n")
    txt_file.write("---------------------------\n")
    for key,value in candidates.items():
        percent_vote = "{:.0%}".format(int(value)/votes)
        txt_file.write(f"{key}: {percent_vote} ({value})\n")
    txt_file.write("---------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("---------------------------")
