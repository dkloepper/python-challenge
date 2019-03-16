#Homework 3 - PyBank
#David Kloepper
#Data Viz Bootcamp Cohort 3
#March 16th, 2019

#Import modules
import os
import csv

#Function to output the results string so it can be printed to different locations
def printResults(totVotes, results):
    resultsString = "Election Results\n"
    resultsString = resultsString + "-------------------------\n"
    resultsString = resultsString + "Total Votes: " + str(totVotes) + "\n"
    resultsString = resultsString + "-------------------------\n"          
    
    winnerVotes = 0
    votePct = 0.000
    #Loop through the candidate results and calculate the percent of vote while building results string
    for key, value in results.items():
        votePct = value/totVotes*100
        resultsString = resultsString + key + ": " + str(round(votePct,3)) + "% (" + str(value) + ")\n"
        if winnerVotes == 0 or int(value) > winnerVotes:
            winner = key
            winnerVotes = int(value)
    resultsString = resultsString + "-------------------------\n"
    resultsString = resultsString + "Winner: " + winner + "\n"
    resultsString = resultsString + "-------------------------\n"
    
    #Function returns the string of the final results
    return resultsString

#initialize the variables
candidates = {}
totalVotes = 0

#Set the file path for the input data
dataPath = os.path.join('election_data.csv')

#open the election data file
with open(dataPath,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header row
    line = next(csvreader,None)

    #Read through the CSV
    for row in csvreader:

        #Add to total number of votes for each row read
        totalVotes += 1

        #Track candidate voted for
        candidate = row[2]

        #Check if candidate exists in dictionary of candidates
        #if in dictionary already, add one vote
        if candidate in candidates:
            candidates[candidate] += 1
        #else add candidate to dictionary and set votes to one
        else:
            candidates[candidate] = 1

#Print results to the terminal, calling the print results function
print(printResults(totalVotes,candidates))

#Set file path for output file
output_path = os.path.join("Election_Results.txt")

#Print results to a text file, calling print results function
with open(output_path, 'w') as txtfile:
    txtfile.write(printResults(totalVotes,candidates))








