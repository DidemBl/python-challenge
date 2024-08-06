# Modules
import os
import csv
# Set path for input file
csvpath = os.path.join("Resources/election_data.csv")
# Dictionary to store candidate vote counts
voter_count = {}
# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row
    # Loop through the rows in the CSV file
    for row in csvreader:
        candidate_name = row[2]
        # Update the vote count for the candidate
        if candidate_name not in voter_count:
            voter_count[candidate_name] = 0
        voter_count[candidate_name] += 1
# Calculate the total number of votes
total_votes = sum(voter_count.values())
# Print the results
print(f"Total Votes: {total_votes}")
for candidate, votes in voter_count.items():
    print(f"{candidate}: {votes} votes")
# Optional: If you want to calculate and print percentages, you can do so here
print("\nElection Results:")
for candidate, votes in voter_count.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")