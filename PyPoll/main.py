import pandas as pd 
import csv
import os


#making lines function so i don't have to repeat
def lines_across():
    print("----------------------------")
#printing header
print("Election Results")
lines_across()

#reading csv file and storing it as a df named df
csvfile = os.path.join("/Users/bjlim/Desktop/GW Homework/HW 3/python-challenge/PyPoll/Resources/election_data.csv")
df = pd.read_csv(csvfile)

#printing total votes
total = df["Voter ID"].count()
print("Total Votes: " + str(total))
lines_across()

#printing names


Khan = df.loc[df['Candidate']=="Khan"]
Khan_count = Khan["Voter ID"].count()
Khan_percentage = round(Khan_count/total * 100, 5)
print("Khan: " + str(Khan_percentage) + "% (" + str(Khan_count) + ")")

Correy = df.loc[df['Candidate']=="Correy"]
Correy_count = Correy["Voter ID"].count()
Correy_percentage = round(Correy_count/total*100, 5)
print("Correy: " + str(Correy_percentage) + "% (" + str(Correy_count) + ")")


Li = df.loc[df['Candidate']=="Li"]
Li_count = Li["Voter ID"].count()
Li_percentage = round(Li_count/total * 100, 5)
print("Li: " + str(Li_percentage) + "% (" + str(Li_count) + ")")

OTooley = df.loc[df['Candidate']=="O'Tooley"]
OTooley_count = OTooley["Voter ID"].count()
OTooley_percentage = round(OTooley_count/total * 100, 5)
print("O'Tooley: " + str(OTooley_percentage) + "% (" + str(OTooley_count) + ")")
lines_across()
print("Winner: Khan")
lines_across()

# Results
# Election Results
# ----------------------------
# Total Votes: 3521001
# ----------------------------
# Khan: 63.00001% (2218231)
# Correy: 19.99999% (704200)
# Li: 14.0% (492940)
# O'Tooley: 3.0% (105630)
# ----------------------------
# Winner: Khan
# ----------------------------