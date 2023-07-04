import os

# Module for reading CSV files
import csv
cwd=os.getcwd()
csvpath = os.path.join(cwd,"Resources/budget_data.csv")

Date =[]
Profit_losses= []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    
for row in csvreader:
        Date.append(row[0])
        Profit_losses.append(row[1])
        
        total_month= len(Date)
        print(total_month)
       
        Total = sum(Profit_losses)
        Print(Total)

        Greatest_decrease = min(Profit_losses)
        for row in csvreader:
            if Profit_losses==row[1]:
                print(row,Greatest_decrease)

        Greatest_increase = max(Profit_losses)  
        for row in csvreader:
            if Profit_losses== row[1]:
                print(row, Greatest_increase)
    