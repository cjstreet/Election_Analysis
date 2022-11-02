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
print("The time right now is ", now)



# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a varible to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data: 

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
   # for row in file_reader:
      #  print(row)





# Assign a variable for the file to load and the path.
#--------file_to_load = 'Resources/election_results.csv'

#with open(filename) as file_variable:

# Open the election results and read the file.
#---------election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#-----------election_data.close()

