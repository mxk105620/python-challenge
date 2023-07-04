import os
import csv
cwd=os.getcwd()
csvpath = os.path.join(cwd,"Resources/election_data.csv")

def student (voter_data):
    Voter_ID= int(voter_data[0])
    County= str(voter_data[1])
    Candidate= str(voter_data[2])

    total_voters=len(Voter_ID)
    print(total_voters)




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
set_res=set(Candidate)
list_res= (list(set_res))
   
 for item in list_res:
        print(item)
   # for row in csvreader:
    #    print(row)
   

#names of all candidates + percentage + total votes
#winner name
