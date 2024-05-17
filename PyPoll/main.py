
import pandas as pd


df = pd.read_csv('Resources/election_data.csv')


TotalVotes = df['Ballot ID'].count()
CandidateCount1 = df['Candidate'].value_counts()['Charles Casper Stockham']
CandidateCount2 = df['Candidate'].value_counts()['Diana DeGette']
CandidateCount3 = df['Candidate'].value_counts()['Raymon Anthony Doane']
CandidateCount1P = df['Candidate'].value_counts(normalize=True)['Charles Casper Stockham']*100
CandidateCount2P = df['Candidate'].value_counts(normalize=True)['Diana DeGette']*100
CandidateCount3P = df['Candidate'].value_counts(normalize=True)['Raymon Anthony Doane']*100



f = open('Resources/ElectionAnalysis.txt', "w")


#print(df.head())
f.write(f'Election Results\n')
f.write(f'------------------------------\n')
f.write(f'Total Votes: {TotalVotes}\n')
f.write(f'------------------------------\n')
f.write(f'Charles Casper Stockham: {CandidateCount1P}% ({CandidateCount1})\n')
f.write(f'Diana DeGette: {CandidateCount2P}% ({CandidateCount2})\n')
f.write(f'Raymon Anthony Doane: {CandidateCount3P}% ({CandidateCount3})\n')
f.write(f'------------------------------\n')
f.write(f'Winner: Diana DeGette\n')
f.write(f'------------------------------\n')
#print(changes)








#from datetime import datetime
#filepath = os.path.join("Resources","budget_data.csv")

#with open(filepath, 'r') as csv_file:
  #  csv_reader = csv.reader(csv_file, delimeter=",")

  #  for line in csv_reader:
   #     date.append(datetime.strptime(row[0], "%b-%y"))
        # print(line)
