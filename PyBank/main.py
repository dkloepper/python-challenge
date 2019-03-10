#Goals:
#Total number of months in the data
#Net total amount of profits and losses over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#EXAMPLE OUTPUT:
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#Import modules
import os
import csv

#Initalize variables
bankData = {}
totalMonths = 0
totalProfit = 0
avgChange = 0.0
greatestIncr = 0
greatestIncrMonth = ""
greatestDecr = 0
greatestDecrMonth = ""

#Read in the CSV
dataPath = os.path.join('budget_data.csv')

#Experimenting with DictReader
#dataFile = csv.DictReader(open(dataPath))
#for row in dataFile:
#    print (row)

with open(dataPath, mode='r',newline='') as dataFile:

    # CSV reader specifies delimiter and variable that holds contents
    dataReader = csv.reader(dataFile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    dataHeader = next(dataReader)

    # Read each row of data after the header
    #for row in dataReader:
    #    bankData.update(f"row[0]:row[1]")

    bankData = {row[0]:row[1] for row in dataReader}

totalMonths = len(bankData)

for key, value in bankData.items():
    totalProfit += int(value)
    if greatestIncr == 0 or int(value) > greatestIncr:
        greatestIncr = int(value)
        greatestIncrMonth = key
    if greatestDecr == 0 or int(value) < greatestDecr:
        greatestDecr = int(value)
        greatestDecrMonth = key

avgChange = totalProfit / totalMonths

print("")
print ("FINANCIAL ANALYSIS")
print ("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalProfit}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {greatestIncrMonth} (${greatestIncr})")
print(f"Greatest Decrease in Profits: {greatestDecrMonth} (${greatestDecr})")
print("")

# Specify the file to write to
output_path = os.path.join("Financial_Summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["FINANCIAL ANALYSIS"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {totalMonths}"])
    csvwriter.writerow([f"Total: ${totalProfit}"])
    csvwriter.writerow([f"Average Change: ${avgChange}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatestIncrMonth} (${greatestIncr})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatestDecrMonth} (${greatestDecr})"])