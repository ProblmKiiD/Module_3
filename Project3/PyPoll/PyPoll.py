import os
import csv
import pandas as pd

pypoll_csv = os.path.join('/Users/deronpayton/Desktop/Project3/PyPoll/Resources/election_data.csv')

candidate_votes = {}
total_votes = 0

#I was having some trouble with organizing all the different value types with this assignment, but once I found the DictReader class on
#StackOverflow things fell into place. From there I knew what data I need to parse in, but I'll admit I still had trouble organzing the 
#information in the way the instuctions said to submit it. I had to get some help from ChatGPT for organzing the syntax, I'll comment below 
#exactly where
with open(pypoll_csv, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate_name = row["Candidate"]

        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1
#this was the area where I needed help from ChatGPT. But after having it break it down for me, I understand what it's doing. I'll admit, looking
#over the code I can understand what it's doing, but still having some issues writing it from scratch. Like I know what I need to do, but getting
#the order and syntax correct is still a small struggle.
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

election_winner = max(candidate_votes, key=candidate_votes.get)

print("")
print("Election Results")
print("")
print("----------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("----------------------------")
print("")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {vote_percentages[candidate]:.2f}% ({votes})")
print("")
print("----------------------------")
print("")
print(f"Winner: {election_winner}")
print("")
print("----------------------------")

with open("PyPoll_Results", 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("----------------------------\n")
    for candidate, votes in candidate_votes.items():
        textfile.write(f"{candidate}: {vote_percentages[candidate]:.2f}% ({votes})\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {election_winner}\n")
    textfile.write("----------------------------\n")