import os
import csv

input_filepath = os.path.join("..","..","Resources","election_data.csv")
output_filepath = os.path.join("..","..","Resources","Election_Results.txt")

with open(input_filepath,"r",encoding="UTF-8",newline="") as poll_data_file:
   
    poll_data = csv.reader(poll_data_file,delimiter=",")

    candidates = [row[2] for row in poll_data]

    total_votes = len(candidates) - 1

    output_message = (f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
    
    print(output_message)




    with open(output_filepath,"w",newline="") as poll_results_file:
        
        poll_results_file.writelines(output_message)
