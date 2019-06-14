import os
import csv

input_filepath = os.path.join("..","..","Resources","election_data.csv")
output_filepath = os.path.join("Election_Results.txt")

with open(input_filepath,"r",encoding="UTF-8",newline="") as poll_data_file:
   
    poll_data = csv.reader(poll_data_file,delimiter=",")

    # create a list of candidates
    candidates = [row[2] for row in poll_data]
    # sort the list of candidates by name
    candidates.sort()
 
    total_votes = len(candidates) - 1

    # create a list of lists with the totals vote count, the percent of votes and 
    # the total number of votes for each candidate. 
    candidate_votes = [[candidate,round((candidates.count(candidate)/total_votes)*100,3),candidates.count(candidate)] for candidate in set(candidates) if candidate != "Candidate"] 
    
    # sort the list in descending order based on the 2 element of the list (percentage of votes)
    from operator import itemgetter
    candidate_votes = sorted(candidate_votes, key=itemgetter(1),reverse=True)
    
    # use string formating to create list of strings with the required output format
    candidates_data = [f"{candidate_votes[i][0]}:  {candidate_votes[i][1]}%  ({candidate_votes[i][2]})" for i in range(0,len(candidate_votes))]
    
    # create output_message with the summary info
    output_message = (f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
    
    # add to the output_message the results for each candidate
    for candidate_data in candidates_data:
        output_message = output_message + "\n" + str(candidate_data)
    
    # print to console
    print(output_message)

    # write to txt file
    with open(output_filepath,"w",newline="") as poll_results_file:
        
        poll_results_file.writelines(output_message)
