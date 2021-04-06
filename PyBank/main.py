
#PyBank
import os
import csv

#Input file path
csvpath_budget = os.path.join("..","PyBank","Resources","budget_data.csv")

#Variables
month_count = 0
net_total_profit = 0
monthly_change = 0
total_monthly_change = 0
prev_value = 0
max_profit = 0
max_loss = 0

#Open csv file
with open(csvpath_budget, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #Read header
    csv_header = next(csvreader)
    
    #Loop through rows
    for row in csvreader:
        #Month counter for each row
        month_count += 1
        month_value = int(row[1])
        #Net total profit counter for each row
        net_total_profit += month_value
        if month_count > 1:
            monthly_change = month_value - prev_value
        total_monthly_change += monthly_change
        if monthly_change > max_profit:
            max_profit = monthly_change
            max_profit_month = row[0]
        if monthly_change < max_loss:
            max_loss = monthly_change
            max_loss_month = row[0]
        prev_value = month_value
average_change = total_monthly_change / (month_count - 1) 

#Print to terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: $ {net_total_profit}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {max_profit_month}  ($ {max_profit})")
print(f"Greatest Decrease in Profits: {max_loss_month} ($ {max_loss})")

#Output file path
budget_data_output = os.path.join("..","PyBank","analysis", "PyBankOutput.txt") 

#Write to new txt file
with open(budget_data_output, 'w') as output:
    output.write(f"Financial Analysis\n")
    output.write(f"----------------------------\n")
    output.write(f"Total Months: {month_count}\n")
    output.write(f"Total: $ {net_total_profit}\n")
    output.write(f"Average Change: $ {average_change}\n")
    output.write(f"Greatest Increase in Profits: {max_profit_month}  ($ {max_profit})\n")
    output.write(f"Greatest Decrease in Profits: {max_loss_month} ($ {max_loss})\n")


