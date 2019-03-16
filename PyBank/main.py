#Homework 3 - PyBank
#David Kloepper
#Data Viz Bootcamp Cohort 3
#March 16th, 2019

#Import modules
import os
import csv

#Initalize variables
bankData = {}
totalMonths = 0
totalProfit = 0
totalChange = []
changeAmt = 0
lastMonthVal = 0
avgChange = 0.0
greatestIncr = 0
greatestIncrMonth = ""
greatestDecr = 0
greatestDecrMonth = ""

#Path to the input CSV
dataPath = os.path.join('budget_data.csv')

with open(dataPath, mode='r',newline='') as dataFile:

    # Initiate csv reader
    dataReader = csv.reader(dataFile, delimiter=',')

    # Read the header row first
    dataHeader = next(dataReader)

    #Load dictionary with CSV data
    bankData = {row[0]:row[1] for row in dataReader}

#Calc total months from length of dictionary
totalMonths = len(bankData)

#Loop through the dictionary
for key, value in bankData.items():

    #add to the total profit calculation
    totalProfit += int(value)

    #If there is no value for previous month, just get the value
    if lastMonthVal == 0:
        lastMonthVal = int(value)
    #If there is a value for last month, calculate the change from the 
    else:
        changeAmt = int(value) - lastMonthVal
        totalChange.append(changeAmt)
        lastMonthVal = int(value)

    #If the change is greater than the previously recorded increase, set that as the new largest increase and record that month
    if greatestIncr == 0 or changeAmt > greatestIncr:
        greatestIncr = changeAmt
        greatestIncrMonth = key

    #If the change is less than the previously recorded decrease, set that as the new largest decrease and record that month
    if greatestDecr == 0 or changeAmt < greatestDecr:
        greatestDecr = changeAmt
        greatestDecrMonth = key


#Calculate average
avgChange = round((sum(totalChange) / len(totalChange)),2)

#Print results to the console
print("")
print ("FINANCIAL ANALYSIS")
print ("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalProfit}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {greatestIncrMonth} (${greatestIncr})")
print(f"Greatest Decrease in Profits: {greatestDecrMonth} (${greatestDecr})")
print("")

# Specify the file output path
output_path = os.path.join("Financial_Summary.csv")

# Open the output file using "write" mode
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