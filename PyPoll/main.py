import os
import csv
csvpath_poll = os.path.join("..","PyPoll","Resources","election_data.csv")
votes = 0
candidates = []
candidate_votes = {}

#Open csv file
with open(csvpath_poll, "r") as data_file:
    file_reader = csv.reader(data_file)
    header = next(file_reader)
    for row in file_reader:
        votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    max_votes = 0
    for candidate in candidates:
        vote_percent = (candidate_votes[candidate] / votes) * 100
        vote_format = "{:,.3f}".format(vote_percent)
    

#Print to terminal
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {votes}")
print(f"----------------------------")
max_votes = 0
for candidate in candidates:
        vote_percent = (candidate_votes[candidate] / votes) * 100
        vote_format = "{:,.3f}".format(vote_percent)
        print(f"{candidate}: {vote_format}% ({candidate_votes[candidate]})")
        if vote_percent > max_votes: 
            winner = candidate
            max_votes = vote_percent
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")
#Output file path
election_data_output = os.path.join("..","PyPoll","analysis", "PyPollOutput.txt") 

#Write to new txt file
with open(election_data_output, 'w') as output:
    output.write(f"Election Results\n")
    output.write(f"----------------------------\n")
    output.write(f"Total Votes: {votes}\n")
    output.write(f"----------------------------\n")
    for candidate in candidates:
        vote_percent = (candidate_votes[candidate] / votes) * 100
        vote_format = "{:,.3f}".format(vote_percent)
        output.write(f"{candidate}: {vote_format}% ({candidate_votes[candidate]})\n")
        if vote_percent > max_votes: 
            winner = candidate
            max_votes = vote_percent
    output.write(f"----------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write(f"----------------------------\n")