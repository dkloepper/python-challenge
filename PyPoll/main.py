
import os
import csv

#Set the file path
dataPath = os.path.join('election_data.csv')

#Function to output the results string so it can be printed to different locations
def printResults(totVotes, results):
    resultsString = "Election Results\n"
    resultsString = resultsString + "-------------------------\n"
    resultsString = resultsString + "Total Votes: " + str(totVotes) + "\n"
    resultsString = resultsString + "-------------------------\n"
    #print(f"Number of Votes: {totVotes}")            
    winnerVotes = 0
    votePct = 0.000
    for key, value in results.items():
        votePct = value/totVotes*100
        #print(f"{key}: {votePct}% ({value})")
        resultsString = resultsString + key + ": " + str(round(votePct,3)) + "% (" + str(value) + ")\n"
        if winnerVotes == 0 or int(value) > winnerVotes:
            winner = key
            winnerVotes = int(value)
    #print(f"WINNER: {winner}")
    resultsString = resultsString + "-------------------------\n"
    resultsString = resultsString + "Winner: " + winner + "\n"
    resultsString = resultsString + "-------------------------\n"

    return resultsString

#initialize the variables
candidates = {}
totalVotes = 0

#open the electtion data file
with open(dataPath,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
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

#Print results to the terminal
print(printResults(totalVotes,candidates))

#Print results to a text file
output_path = os.path.join("Election_Results.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(printResults(totalVotes,candidates))








