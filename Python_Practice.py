print("Hello World")
print(5 + 2 * 3)
print(8//5-3)
print(8+ 22 *2 -4)
print(16-3/2 + 7 -1)
print(3**3%5)
print(5 + 9*3/2-4)

print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / 2 - 4) > 5 + (9 * 3 / (2 - 4)))

# lists
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[1])
print(counties[-1]) # prints the last item in the list
print(len(counties))

# Slicing list[start : end]
print(counties[0:2])
print(counties[0:1])
print(counties[:2])

# adding items to list list.append(), adds to end of list

counties.append("El Paso")
print(counties)

# list.insert(index, obj) to add to a specified location
counties.insert(2, "El Paso")
print(counties)

# list.remove(), removes the first instance of "El Paso"
counties.remove("El Paso")
print(counties)

# list.pop() to remove and return that item, at given index
counties.pop(-1) # or -3
print(counties)

# change or update in a list 
counties[2] = "El Paso"
print(counties)
print("*******************")
counties[2]= "Jefferson"
print(counties)
counties[1]= "El Paso"
print(counties)
counties.remove("Arapahoe")
print(counties)
counties.insert(3, "Denver")
print(counties)
counties.append("Arapahoe")
print(counties)
print("*******************")
print("***********Tuples*****************")
# my_tuple = tuple() or myTuple = ()
# tuples are immutable, cannot add or remove
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])

print("*******************")
print("***********Dictionaries*****************")
# A dictionary is an object that stores a collection of data.
# A Python dictionary has a key and a value, or key-value pairs.
# Values can be any data type or object
# Keys must be immutable objects, like integers, floating-point decimals, or strings.

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.values())  # get all values
print(counties_dict.keys()) # get all keys
print(counties_dict.get("Denver")) # get a specific value

# A list of dictionaries
print("************ A list of Dictionaries ************")

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.insert(1, {"county": "El Paso", "registered_voters": 461149})

print(voting_data)


# Making Decisions
print("************ Using Conditionals ************")

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("You received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
   print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


#counter loops (for) and condition-controlled loops (while)
print("************ Iteration ************")

for county in counties:
    print(county)


x = 0
while x <= 5:
    print(x)
    x = x + 1

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


for num in range(5): # range function
    print(num)  

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys(): # counties_dict.values()
    print(county)

for county in counties_dict: # to get the values of the keys
    print(counties_dict.get(county))

for key, value in dictionary_name.items():
    print(key, value)


# getting or printing each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data: # number of registered voters from each dictionary
     print(county_dict['registered_voters'])
print("\n")
#Membership and logical operators
print("************ Membership ************")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties: # in , not in
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties: # and, or, not(expression)
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#formatting strings f-strings
print("\n")
print("************ F-Strings************")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)