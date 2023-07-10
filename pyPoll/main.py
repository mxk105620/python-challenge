import os
import csv

csvpath = os.path.join("Resources/election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

Voter_ID= []
County =[]
Candidate_options=[]

candidate_votes={}
wining_count=0
total_votes=0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        total_votes=total_votes+1
        candidate_name=row[2]
        
        if candidate_name not in candidate_votes:
            Candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=1
        else:   
            candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

for candidate_name in candidate_votes:
    votes= candidate_votes[candidate_name]
    if votes>wining_count:
        wining_count=votes
        wining_candidate=candidate_name
print("winner:", wining_count, wining_candidate)

def percentage(candidate_votes, total_votes):
    percentage= round(100*(candidate_votes/total_votes), 3)
    return percentage
    
  
output_file=os.path.join("analysis/election_data_final.txt")

output =(
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)
for name in candidate_votes:   
    pct = percentage(candidate_votes[name], total_votes)
    candidate_line= f"{name}: {pct}% ({candidate_votes[name]})\n"
    output+=candidate_line

output+=(
    f"----------------------------\n"
    f"Winner: {wining_candidate}\n"
    f"----------------------------\n"
)
print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)




    

