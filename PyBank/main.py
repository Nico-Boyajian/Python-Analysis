#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:44:06 2019

@author: nicoboyajian
"""

import csv
import os


budget_data = os.path.join('..',"Resources","budget_data.csv")

total_months=0
total_profit =0
average_change=0
greatest_increase=0
greatest_decrease=0
total_difference =0
average_change = 0




with open(budget_data,newline="") as csvfile:
    budget=csv.reader(csvfile, delimiter=",")
    budget_header = next(budget)
    list =[]
    for row in budget:
       total_months +=1
       total_profit += int(row[1])
       list.append(row[1])
       
       if int(row[1])>greatest_increase:
           greatest_increase=int(row[1])
           greatest_increase_month = row[0]
       if int(row[1])<greatest_decrease:
           greatest_decrease=int(row[1])
           greatest_decrease_month = row[0]
    for i in range(int(total_months-1)):
        difference = int(list[i+1])-int(list[i])
        total_difference += difference
        
    average_change = round(total_difference/int(total_months-1),2)
    
               
           
       
print("Financial Analysis\n------------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")


output_file = os.path.join('..',"Resources","budget_output.csv")
with open(output_file,"w",newline="") as datafile:
    budget_output=csv.writer(datafile)
    budget_output.writerow(["Financial Analysis"])
    budget_output.writerow(["Total Months:",str(total_months)])
    budget_output.writerow(["Net Profit","$"+str(total_profit)])
    budget_output.writerow(["Average Change","$" +str(average_change)])
    budget_output.writerow(["Greatest Increase in Profits","$"+str(greatest_increase)])
    budget_output.writerow(["Greatest Decrease in Profits","$"+str(greatest_decrease)])

       


        