#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:02:35 2019

@author: nicoboyajian
"""
import csv
import os

total_votes=0
khan_count=0
correy_count=0
li_count=0
otooley_count=0
winning=float(0)





election_data = os.path.join('..',"Resources","election_data.csv")

with open(election_data,newline="") as csvfile:
    election_data = csv.reader(csvfile,delimiter=",")
    election_header=next(election_data)
    for row in election_data:
        total_votes += 1
        if (row[2])==("Khan"):
            khan_count += 1
            percentage_khan=round(float(khan_count/total_votes)*100,2)
        elif (row[2])==("Correy"):
            correy_count += 1
            percentage_correy=round(float(correy_count/total_votes)*100,2)
        elif (row[2])==("Li"):
            li_count +=1
            percentage_li=round(float(li_count/total_votes)*100,2)
        elif (row[2])==("O'Tooley"):
            otooley_count+=1
            percentage_otooley=round(float(otooley_count/total_votes)*100,2)
            
    if percentage_khan>winning:
        winning= percentage_khan
        winner="Khan"
    elif percentage_correy>winning:
        winning = percentage_correy
        winner="Khan"
    elif percentage_li>winning:
        winning = percentage_li
        winner="Li"
    elif percentage_otooley>winning:
        winning = percentage_otooley
        winner="O'Tooley"

print(f"\nElection Results\n--------------------")
print(f"Total Votes: {total_votes}\n--------------------")
print(f"Khan: {percentage_khan}% ({khan_count})")
print(f"Correy: {percentage_correy}% ({correy_count})")
print(f"Li: {percentage_li}% ({li_count})")
print(f"O'Tooley: {percentage_otooley}% ({otooley_count})\n--------------------")
print(f"Winner: {winner}\n--------------------")


output_file=os.path.join('..',"Resources","election_output.csv")
with open(output_file,'w',newline="") as datafile:
    election_output=csv.writer(datafile)
    election_output.writerow(["Election Results"])
    election_output.writerow(["Total Votes",str(total_votes)])
    election_output.writerow([])
    election_output.writerow(["Khan",str(percentage_khan)+"%",str(khan_count)])
    election_output.writerow(["Correy",str(percentage_correy)+"%",str(correy_count)])
    election_output.writerow(["Li",str(percentage_li)+"%",str(li_count)])
    election_output.writerow(["O'Tooley",str(percentage_otooley)+"%",str(otooley_count)])
    election_output.writerow(["WINNER",str(winner)])
    
    
            
    