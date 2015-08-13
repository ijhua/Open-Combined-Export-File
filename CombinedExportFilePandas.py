#set up imports
import pandas as pd
import numpy as np

file_name="Combined_Export_File.csv"
my_columns=["Subject ID","Data Start Date","Data Start Time",
	"Interval Type","Interval#","Start Date","Start Time",
	"End Date","End Time","Duration","Off-Wrist","%Off-Wrist",
	"%Invalid SW","Efficiency","Wake Time","%Wake","Sleep Time",
	"%Sleep","Exposure White","Avg White","Max White","TALT White",
	"%Invalid White","Exposure Red","Avg Red","Max Red","TALT Red",
	"%Invalid Red","Exposure Green","Avg Green","Max Green",
	"TALT Green","%Invalid Green","Exposure Blue","Avg Blue",
	"Max Blue","TALT Blue","%Invalid Blue","#Scores","#Manual",
	"#Scheduled","#No Responses","Avg Score","Avg Manual","Avg Scheduled",
	"#Scores (A)","#Manual (A)","#Scheduled (A)","#Late Scores (A)",
	"#No Responses (A)","Avg Score (A)","Avg Manual (A)",
	"Avg Scheduled (A)","Avg Late Score (A)","#Scores (B)",
	"#Manual (B)","#Scheduled (B)","#Late Scores (B)",
	"#No Responses (B)","Avg Score (B)","Avg Manual (B)",
	"Avg Scheduled (B)","Avg Late Score (B)"]

#print the csv
file=(pd.read_csv(file_name, usecols=my_columns, engine='python'))
print(file[file["Interval Type"]=="SLEEP"])

df = pd.DataFrame(file[file["Interval Type"]=="SLEEP"])
df.to_csv("New_Export_File.csv", encoding='utf-8')
