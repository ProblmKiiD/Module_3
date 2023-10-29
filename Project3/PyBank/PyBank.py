#import libraries
import os
import csv
#create a variable for the csv file and where the file is stored
pybank_csv = os.path.join('/Users/deronpayton/Desktop/Project3/PyBank/Resources/budget_data.csv')

#lists to store data
total_months = []
changes = []
#set starting values to calculate these totals
net_total = 0
previous_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0


#open csv file as readable
with open(pybank_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    #skips the header row before starting my for loop
    next(csv_reader)
    #I then iterate through each row in the csv to total the amount of months
    for row in csv_reader:
        total_months.append(row)
        #set my variable to calculate the changes in profit/losses and has it loop through and subtract the value from the previous value
        #in the column. Checking to see if the previous profit/loss is 0 ensures that the code starts in the second row(month)
        #It then appends this value to the changes list I created earlier
        profit_loss = int(row[1])
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            #this block of code I had to do some serious research on as I could not for the life of me figure out. But by using the is None or built
            #in Python code, initially checking if the value is null and by using the or operator to check if that condition is true, therefore
            #assigning the first value to the variable change and then it continues checking and updating if a value is found to be greater or
            #less than the previous values
            if greatest_increase is None or change > greatest_increase:
                greatest_increase = change
            if greatest_decrease is None or change < greatest_decrease:
                greatest_decrease = change
        #Loops through each row and calculates the values of for the profit loss and totals. 
        previous_profit_loss = profit_loss
        
        net_total += profit_loss
#calcuate the average value outside of the for loop as these values depend on values from the entire data set and not necessarily values per row
average_changes = sum(changes) / len(changes)


#print statements
print("")
print("Financial Analysis")
print("")
print("-----------------------------------") 
print("")               
print("Total months: " + str(len(total_months)))
print("")
print("Total: " + str(net_total))
print("")
print(f"Average Change: (${average_changes:.2f})")
print("")
print(f"Greatest Increase in Profits: Aug-16 (${greatest_increase})")
print("")
print(f"Greatest Decrease in Profits: Feb-14 (${greatest_decrease})")
print("")
#export file to a text file
with open('PyBank_Results', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------------\n")
    output_file.write(f"Total months: ({len(total_months)})\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_changes:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: Aug-16 (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: Feb-14 (${greatest_decrease})\n")  








        

        
        
        
        
        
