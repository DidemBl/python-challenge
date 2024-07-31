#Modules 
import os 
import csv

#Set path for input file

csvpath = os.path.join("Resources","budget_data.csv")

#Lists to store data

months = []
profit_loss = []
changes_over_time =[]



#Open the CSV file
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader)

	#Loop through the budget records

	for row in csvreader:

		# Add month, total profits/losses for the entire period
		months.append(row[0])
		profit_loss.append(row[1])
	
	#Convert list elements into integers using list comprehension
	total = sum(int(num)for num in profit_loss)

	
	
	#Calculate changes in profits and losses over time 

	for i in range(len(profit_loss) - 1):
		month_1 = profit_loss[i]
		month_2 = profit_loss[i+1]
		change = int(month_2) - int(month_1)
		changes_over_time.append(change)

	print("Financial Analysis")
	print("---------------------")
	
	print(f"Total months: {len(months)}")
	print(f"Total: ${total}")
	#print(changes_over_time)

	average = round(sum(int(num) for num in changes_over_time) / len(changes_over_time),2)
	print(f"Average change: ${average}" )
	max_increase = max(int(num) for num in changes_over_time)
	print(f"Greatest Increase in Profits: ${max_increase}" )
	max_decrease = min(int(num) for num in changes_over_time)
	print(f"Greatest Decrease in Profits: ${max_decrease}")

	#Set path for output file 

	output_file = os.path.join("analysis","financial_analysis.txt")
	
	#Open the output file 

	with open(output_file, "w") as file:
	#Print statements to output file 
		print("Financial Analysis", file=file)
		print("---------------------", file=file)
		print(f"Total months: {len(months)}", file=file)
		print(f"Total: ${total}", file=file)
		print(f"Average change: ${average}", file=file)
		print(f"Greatest Increase in Profits: ${max_increase}", file=file)
		print(f"Greatest Decrease in Profits: ${max_decrease}", file=file) 
 