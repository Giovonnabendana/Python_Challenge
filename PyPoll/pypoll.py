#!/usr/bin/env python
# coding: utf-8

# In[88]:


import csv
import os



#files to load and output
file_to_load = os.path.join(".", "Resources", "election_data.csv")

file_to_output = os.path.join(".", "election_analysis.txt")

#total vote counter
total_votes = 0


#candidate options and vote counters
candidate_votes = {}
candidate_options = []


#winnning candidate and winnning count tracker
winning_candidate = ""
winning_count = 0


with open(file_to_load) as election_data:
    
    
    #add to the  total vote
    reader = csv.reader(election_data)
    
    
    #read the header
    header = next(reader)
    #print(header)
    
    
    for row in reader:
        
        
        #add total vote count
        total_votes = total_votes + 1
        #print(row)
        
        
        #gets candidate name from each row
        candidate_name = row[2]
        
        
        #if candidate_name = row {}
        #if candidate does not match any existing candidate...
        #loop will discover new candidates
        
        if candidate_name not in candidate_options:
            
            #if not then Add the name to t he list of candidates in the running
            candidate_options.append(candidate_name)
            
            
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
            
            
            
#print(candidate_votes)
            
            
            
            
            
#print(candidate_options)
            
            
            
        
        
with open(file_to_output,"w") as txt_file:
    election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes {total_votes}\n"
    f"-------------------------\n"


    )
    print(election_results, end = "")
    
    txt_file.write(election_results)
        
    for candidate in candidate_votes:
    
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
    
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        
        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"  

    
        print(voter_output, end = "")
    
        txt_file.write(voter_output)
    
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)   

