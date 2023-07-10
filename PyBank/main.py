import os
import csv
import textwrap
cwd=os.getcwd()
csvpath = os.path.join(cwd,"Resources/budget_data.csv")

Date =[]
Profit_losses= []
netchange= []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    for row in csvreader:
        Date.append(row[0])
        Profit_losses.append(int(row[1]))


total_month= len(Date)
c= ("Total Months: " + str(total_month))

Sum= sum(Profit_losses)
d= ("Total: "+str(Sum))


for y in range(len(Profit_losses)):
    if y<(total_month-1):
       netchange.append(Profit_losses[y+1]-Profit_losses[y])

netchangetotal=sum(netchange)
Average_change=(float(netchangetotal)/(total_month-1))
#e1=(Average_change, "type: ", type(Average_change))
e=("Average Change: "+ "$"+str(Average_change))

Greatest_increase = max(netchange)  

for x in netchange:
    if x == Greatest_increase:
        index= netchange.index(x)
        b= Date[index]

f=("Greatest Increase in Profits: "+str(b)+ " "+ str(Greatest_increase))


Greatest_decrease = min(netchange)
for y in netchange:
    if y == Greatest_decrease:
        index= netchange.index(y)
        d= Date[index]

g=("Greatest Decrease in Profits: "+ str(d)+ " "+ str(Greatest_decrease))

#summary=zip(c,d,e,f,g)
#summary=zip(total_month,str(Sum), str(Average_change), str(Greatest_increase),b,str(Greatest_decrease),d)

output_file=os.path.join(cwd,"analysis/budget_data_final.txt")
#with open(output_file, 'w') as output_file:
    # output_file.write("Financial analysis")
    # output_file.write(c)
    # output_file.write(d)
    # output_file.write(e)
    # output_file.write(f)
    # output_file.write(g)
    
output =(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${Sum}\n"
    f"Average Change: ${Average_change:.2f}\n"
    f"Greatest Increase in Profits: {b} (${Greatest_increase})\n"
    f"Greatest Decrease in Profits: {d} (${Greatest_decrease})\n")

print(output)
# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)

 
    
   
        
        

