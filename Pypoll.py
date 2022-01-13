#Assign  a variable for the file to load and the path
#file_to_load = 'Resources\election_results.csv'

#Open the electionresults and read the file-
#election_data = open(file_to_load, 'r')
#To do: perform  analysis.
#Close the file.
#election_data.close()

#open the election resultsand read the file
#with open(file_to_load) as election_data:

# To do: perform  analysis.
 #   print(election_data)

#Add our dependencies

#import csv
#import os

 #Assigna variable for the file  to load  and the path
#file_to_load = os.path.join("Resources","election_results.csv")

#open the election results and read the file
#with open(file_to_load) as election_data:

# To do: perform  analysis.
 #   print(election_data)

#create a filename variable to a direct  or indirect path to the file
#Asign a variable to save the file to a path
#file_to_save = os.path.join("analysis","election_analysis.txt")

#Using the open() function  with the "W" mode we  will write data to the file
#Open the election results and read the file.
#with open(file_to_save,"w") as txt_file:

# To do: read and analyze the data here
#Read the file object with the reader function
   # file_reader= csv.reader(election_data)

#Write some datato the file.
 #   txt_file.write("Counties in the Election\n--------------------\nAraphoe\nDenver\nJefferson")


#Add our dependencies

import csv
import os

 #Assigna variable for the file  to load  and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Asign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here
#Read the file object with the reader function
    file_reader = csv.reader(election_data)

#Print each row in the CSV file
    #for row in file_reader:
     #   print(row)

#Read and print the header row.
    headers= next(file_reader)
    print (headers)


    
#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidates won
#4. The total number of votes each candiates won
#5. The winner  of the election based on  popular vote.