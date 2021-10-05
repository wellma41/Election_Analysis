#retrieve data
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

# ref 3.4.2
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

#election_data = open(file_to_load, 'r')
# Open the election results and read the file

with open(file_to_load) as election_data:
     print(election_data)

#perform analysis


#close the file
#election_data.close()