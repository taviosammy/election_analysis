
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
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(data_to_retrieve) as election_data:

#To do: perform analysis.
    
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        Total_votes += 1
       # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
             # Add it to the list of candidates
            candidate_options.append(candidate_name)
            #track candidate's vote
            candidate_votes[candidate_name] = 0
        # Determine winning vote count and candidate

        
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {Total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
        
            # 2. Retrieve vote count of a candidate.
            Votes = candidate_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = (float(Votes) / float(Total_votes) * 100)

            # 1. Determine if the votes are greater than the winning count.
            if (Votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = Votes
                winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            #Taking the candidates' vote

            #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
            candidate_result = f"{candidate_name}: {vote_percentage:.1f}% ({Votes:,})\n"
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_result)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_result)
            #5. The winner of the election based on popular vote 
            winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)




    #1. The total number of votes cast
    #2. A complete list of candidates who received votes
    #3. The percentageof votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular vote 