#import 
import os
import csv


# find open path

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)


# * Your task is to create a Python script that analyzes the records to calculate each of the following:

# Read the header row first (skip this step if there is no header)
    
    csv_header = next(csvreader)
    month = []
    net_profit = []    
    p_l_change = []  
    avg_p_l = []
    
    print(f"Header: {csv_header}")               

    #-------------------------------------------------------------
      
    for row in csvreader:
        month.append(row[0])
        net_profit.append(row[1])
    print(len(month))

    #-------------------------------------------------------------

    profit_int = map(int,net_profit)
    net_p_l = (sum(profit_int))
    print(net_p_l)
    #-------------------------------------------------------------
    i = 0
    for i in range(len(net_profit) - 1):
        profit_loss = int(net_profit[i+1]) - int(net_profit[i])
 
    #-------------------------------------------------------------
        p_l_change.append(profit_loss)
    Total = sum(p_l_change)

    #-------------------------------------------------------------

    avg_p_l = round(Total / len(p_l_change), 2)
    print(avg_p_l)  
    #-------------------------------------------------------------
    greatest_increase = max(p_l_change)
    print(greatest_increase)
    g = p_l_change.index(greatest_increase)
    month_increase = month[g+1]
    #-------------------------------------------------------------
    greatest_decrease = min(p_l_change)
    print(greatest_decrease)
    d = p_l_change.index(greatest_decrease)
    month_decrease = month[d+1]

#-----------------------------------------------------------------

print(f"Financial Analysis"+"\n")
print(f"----------------------------"+"\n")
print("Total months: " + str(len(month)))
print("Total: $ " + str(net_p_l))  
print("Average Change: $" + str(avg_p_l))
print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")


with open("Financial Analysis.txt", "w") as txtwriter:
    txtwriter.write("Election Results" + "\n")
    txtwriter.write(f"----------------------------"+"\n")
    txtwriter.write(("Total months: " + str(len(month))) +"\n")
    txtwriter.write(("Total: $ " + str(net_p_l)) +"\n")
    txtwriter.write(("Average Change: $" + str(avg_p_l)) +"\n")
    txtwriter.write((f"Greatest Increase in Profits: {month_increase} (${greatest_increase})") +"\n")
    txtwriter.write((f"Greatest Decrease in Losses: {month_decrease} (${greatest_decrease})") +"\n")
  

