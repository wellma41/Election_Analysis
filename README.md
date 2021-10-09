# Election_Analysis
Colorado Board of Elections Python Analysis 
#Election Analysis

## Overview of Project
	The purpose of this code is to itemize an election board's csv file into easily digestable information.
	The results of this analysis produced a break down of the ballots per county, and the results pertaining to each candidate.   


## Results

### Total Votes: 369,711

### County Results
	
	-Denver county had 306,055 votes or 82.8% of the total, making it the largest county by far. 
	-Jefferson county had 38,855 votes or 10.5% of the total.
	-Arapahoe county had 24,801 votes or 6.7% of the total.
	
### Candidate Results
	
	-Winner: Dianna Degette with 272,892 votes or 73.8% of the total.
	-2nd: Charles Casper Stockham with 85,213 votes or 23.0% of the total.
	-3rd: Raymon Anthony Doane wit h11,606 votes or 3.1% of the total.

## Election Audit Summary

	This audit was performed using a python script. 
	This script works by identifying unique candidate and county names and counting how many times that name appeared in the election_results.csv file.
	It should work for any election as long as the election_results.csv file is kept within the same directory path and updated in the same format as this election.
	In short, it should work as long as the same election_results file is updated with the new data and kept in the format (ballot ids, county name, candidate name).
 
### Suggested Modifications

	-You could make an i = input() function where you could input the file name or the path of the file in the 'file_to_load = os.path.join(input)' so you can make a new csv file for each election.
	-We could break down the results by county if we populated a new list with dictionaries using nested for loops.

	####Suggestion
	'''
	cancounty = 0
	county_dictlist =()
	'
	'
	for row in reader
		For x in range(len(counties)):
			if counties(x) not in county_dictlist:
				county_dictlist.append({"county":counties(x)})
		
			For y in range(len(candidate_options)):
			
				if candidate_name == candidate_options(y) and county == counties(x)
					county_dictlist[x][candidate_options(y)] += 1
						
	'''	
