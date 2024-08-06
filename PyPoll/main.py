#Modules 
import os 
import csv

#Set path for input file

csvpath = os.path.join("Resources","election_data.csv")

#Lists to store data


total_votes = 0
candidate_name = []
voter_count = {}
percentage = []
winner_name = ""
winner_count = 0



#Open the CSV file
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	#Skip the header
	next(csvreader)

	#Loop through the votes
	print("Election Results")
	print("-------------------------")
	for row in csvreader:

		# Add number of votes
		total_votes = total_votes + 1
		#Add candidate name
		candidate_name = row[2]
		
		# Make a dictionary with candidate names and vote counts 
		if candidate_name not in voter_count:
		#Reset the counter for vote counts
			voter_count[candidate_name] = 0
		# Add votes to each candidate's vote count 
		voter_count[candidate_name] = voter_count[candidate_name] + 1 

        #Determine total votes for each candidate

print(f'Total votes: {total_votes}')
print("-------------------------")	 	
for candidate,votes in voter_count.items():
	#Print name and votes received for each candidate
	percentage = (votes/total_votes) * 100
	print(f'{candidate}: {percentage:.3f}% ({votes})')
		#Determine the winner
	if votes > winner_count:
		winner_count = votes
		winner_name = candidate 

	
print("-------------------------")	
print(f'Winner: {winner_name}') 
print("-------------------------")

#Set path for output file 

output_file = os.path.join("analysis","election_analysis.txt")
	
#Open the output file 

with open(output_file, "w") as file:

#Print statements to output file 
	print("Election Results", file=file)
	print("---------------------", file=file)
	print(f'Total votes: {total_votes}', file=file)
	print("-------------------------", file=file)
	for candidate,votes in voter_count.items():
		percentage = (votes/total_votes) * 100
		print(f'{candidate}: {percentage:.3f}% ({votes})', file=file)
	print("-------------------------", file=file)
	print(f'Winner: {winner_name}', file=file)
	print("-------------------------", file=file) 


 
			
	
	
	
	
	
	
	





