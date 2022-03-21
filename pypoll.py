
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
#The data we need to retrieve

#Add you dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
data_to_retrieve = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initializing an accumulator
Total_votes = 0
candidate_options = []
# Open the election results and read the file.
with open(data_to_retrieve) as election_data:

#To do: perform analysis.
    
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
       # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
             # Add it to the list of candidates
            candidate_options.append(candidate_name)

 #Print the candidate list.
print(candidate_options)









#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentageof votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote 