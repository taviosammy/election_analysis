# Election_Analysis

##Project Overview

We were given the task of auditing a local congressional election. Using Python the objective was to read a csv file with election data, process the data to find specific election details then output these finding to a text file.

##Resources

Data source: election_results.csv
Software   : Visual Studio code version 1.65.2
             Python 3.10
             
             
##Objectives to find:
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won plus The total number of votes each candidate won
5. The winner of the election based on popular vote
6. A list of the counties that participated in the vote
7. The number of votes and the percentage of total votes from each county 
8. The county with the largest turnout
             
##Summary

###There were 3 candidates in the election:
Charles Casper Stockham
Diana DeGette
Raymon Anthony Doane

###The Results:

https://user-images.githubusercontent.com/99847046/159719676-3edbe0a9-6c10-4953-9d99-daed6b5a7ed7.png

###Audit Summary

The code used to execute this audit is very flexible and can be used (with the right modifications) to assess any election data.
Modifying the open path and read function to determine the source of the data is the first necessary step.
We would need to adjust the path to retrieve new data.
https://user-images.githubusercontent.com/99847046/159729533-e31d1bdb-fc68-417e-8af2-e84f431659f6.png

The name of the variables can changed to the user's liking to make it easier to read and understand, that however doesn't influence the functionality of the code.

It would also be important to assess any new data to know what column the desired variable is found in and change the index to save the variable as the key.  Example, If the candidate name was found in the 4th column instead of the 3rd like the image below, the row index would have to change accordingly.
Another area the image below shows is if there is the need to track another dimension to election additional to the candidates or the county, like say aligned political party for example.  Another IF statement that has a new dictionary, list to store the new variable and the variable itself would be place in the for loop below to track the votes associated to political parties just as we tracked votes to the candidate names and county names.

https://user-images.githubusercontent.com/99847046/159733476-62b88bf4-a22a-4732-8319-4b795cb84acd.png
