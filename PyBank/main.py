


import pandas as pd


df = pd.read_csv('Resources/budget_data.csv')


TotalMonths = df['Date'].count()
Total = df['Profit/Losses'].sum()
changes = df['Profit/Losses'].diff()
Average = changes.mean()
Greatest = changes.max()
Decrease = changes.min()

f = open('Resources/FinancialAnalysis.txt', "w")


#print(df.head())
f.write(f'Total Months: {TotalMonths}\n')
f.write(f'Total: {Total}\n')
f.write(f'Average Change: {Average}\n')
f.write(f'Greatest Increase in Profits: {Greatest}\n')
f.write(f'Greatest Decrease in Profits: {Decrease}\n')
#print(changes)








#from datetime import datetime
#filepath = os.path.join("Resources","budget_data.csv")

#with open(filepath, 'r') as csv_file:
  #  csv_reader = csv.reader(csv_file, delimeter=",")

  #  for line in csv_reader:
   #     date.append(datetime.strptime(row[0], "%b-%y"))
        # print(line)
