#modules
import os
import csv
import pandas as pd

print("Financial Analysis")
print("----------------------------")

csvpath = os.path.join("/Users/bjlim/Desktop/GW Homework/HW 3/python-challenge/PyBank/Resources/budget_data.csv")
df = pd.read_csv(csvpath)

#printing Total Months
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    monthcounter = 0
    for row in csvreader:
        monthcounter += 1 
    print("Total Months: " + str(monthcounter-1))

#printing net amount 
total = df["Profit/Losses"].sum()
print("Total: $" + str(total))

#Average Change
df_average = df.groupby('Date').mean().reset_index()
print("Average Change: $ " + df_average.head())
#Greatest Increase In Profits

#Greatest Decrease in Profits 