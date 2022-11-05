# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
import csv
import os

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.

print("******************************************************\n")
print("The time right now is ", now)
print("******************************************************\n")
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a varible to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data: 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    # print(headers)

# Print each row in the CSV file.
    for row in file_reader:
          # Add to the total vote count.
        total_votes += 1
         #get the candidate name from each row
        candidate_name = row[2]
         # if we haven't already added this candidate then add him/her to candidate options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
         # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
     # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
         # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
print("******************************************************\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
print("******************************************************\n")
# print the total votes
print("The total votes are: " + str(total_votes))
#message = (
   # f"Here are the candidates options: {candidate_options:,} .")
print(candidate_votes)
# Assign a variable for the file to load and the path.
#--------file_to_load = 'Resources/election_results.csv'

#with open(filename) as file_variable:

# Open the election results and read the file.
#---------election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#-----------election_data.close()

