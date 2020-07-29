#import 
import os
import csv


# find open path

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    
    #---------------------------------------------------------------------
    
    
    
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    #---------------------------------------------------------------------

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #---------------------------------------------------------------------

    total_votes = (len(votes))
    print(total_votes)

    #---------------------------------------------------------------------

    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
    
    #---------------------------------------------------------------------
    #Calcs
    
    
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 4)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)
    
    #---------------------------------------------------------------------
    #Conditionals

    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

    #---------------------------------------------------------------------
    #print

print(f"Election Results" + "\n")
print(f"-----------------------------------" + "\n")
print(f"Total Votes: {total_votes}" + "\n")
print(f"-----------------------------------" + "\n")
print(f"Khan: {khan_percent}% ({khan_votes})" + "\n")
print(f"Correy: {correy_percent}% ({correy_votes})" + "\n")
print(f"Li: {li_percent}% ({li_votes})" + "\n")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})" + "\n")
print(f"-----------------------------------" + "\n")
print(f"Winner: {winner}" + "\n")
print(f"-----------------------------------")

    #---------------------------------------------------------------------
    #Outport

with open("Election_Results.txt", "w") as txtwriter:
    txtwriter.write("Election Results" + "\n")
    txtwriter.write("--------------------------" + "\n")
    txtwriter.write(f"Total Votes: {total_votes}" + "\n")
    txtwriter.write("--------------------------" + "\n")
    txtwriter.write(f"Khan: {khan_percent}00% ({khan_votes})" + "\n")
    txtwriter.write(f"Correy: {correy_percent}00% ({correy_votes})" + "\n")
    txtwriter.write(f"Li: {li_percent}00% ({li_votes})" + "\n")
    txtwriter.write(f"O'Tooley: {otooley_percent}00% ({otooley_votes})" + "\n")
    txtwriter.write(f"-----------------------------------" + "\n")
    txtwriter.write(f"Winner: {winner}" + "\n")
    txtwriter.write(f"-----------------------------------" + "\n")


