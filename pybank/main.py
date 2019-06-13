import os
import csv

input_filepath = os.path.join("..","..","Resources","budget_data.csv")
output_filepath = os.path.join("..","..","Resources","Financial_Analysis.txt")

with open(input_filepath,"r",encoding="UTF-8",newline="") as budget_data_file:
   
    budget_data = csv.reader(budget_data_file,delimiter=",")
    
    # create a list of dates for first column in CSV
    dates = [row[0] for row in budget_data]
    # return pointer to begining of file
    budget_data_file.seek(0)
    
    # create a list of profit/losses values for second column in CSV
    profit_losses = [row[1] for row in budget_data]

    # calculate total months as the length of the either list -1 to exclude header
    total_month = len(list(dates))-1
    
    # use comprehenasion to calculate the total ammount of profit_losses. Negative values
    # are not considered digits by the isdigit() method, therefore the negative sign needs to
    # be strip in order to include them up in the total
    total_amount = sum(int(amount) for amount in profit_losses if amount.lstrip("-").isdigit())

    # create a list of profit_changes. I am initializing the list with 0 profit/loss change 
    # for the first month. The result ($-2288.2) is different than the one shown 
    # because it is considering the first month to not have any profit/loss changes, terefore
    # it is dividing by the total_months not the total_months with profit change (which would
    # exclude the first month)

    profit_changes = ['Changes',0]

    for i in range(2,len(profit_losses)):
        profit_changes.append(int(profit_losses[i]) - int(profit_losses[i-1]))
    
    # find the greatest increase and decrease in the list skiping the header row
    greatest_profit_increase = max(amount for amount in profit_changes if amount != 'Changes')
    greatest_profit_decrease = min(amount for amount in profit_changes if amount != 'Changes') 
    average_profit_change = round(sum(amount for amount in profit_changes if amount != 'Changes')/total_month,2) 

    # find the dates for the greatest increase and decrease in the dates list
    date_greatest_increase = str(dates[profit_changes.index(greatest_profit_increase)])
    date_greatest_decrease = str(dates[profit_changes.index(greatest_profit_decrease)])

    message = (f"\nFinancial Analysis\n----------------------------\nTotal month: {total_month} \nTotal: ${total_amount}\nAverage  Change: ${average_profit_change}\nGreatest Increase in Profits: {date_greatest_increase} (${greatest_profit_increase})\nGreatest Decrease in Profits: {date_greatest_decrease} (${greatest_profit_decrease})")
    print(message)

with open(output_filepath,"w",newline="") as budget_analysis_file:
    
    budget_analysis_file.writelines(message)


