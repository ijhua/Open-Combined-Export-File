#set up imports
import pandas as pd
import numpy as np
import os
import datetime


path=r'C:\Users\Isabelle\Python\Summary_Data'
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

#read the file into csv
file=(pd.read_csv(path+"\\"+file_name, usecols=my_columns, engine='python'))
#print(file[file["Interval Type"]=="SLEEP"]) #print the csv into the console

#put into DataFrame
df = pd.DataFrame(file[file["Interval Type"]=="SLEEP"])

#insert a new row for weekend. default value=A, so that it's different from everything else
df.insert(loc=4, column='weekend', value='A')

# create datetime object
enddate = pd.to_datetime(df.iloc[:,8])
enddate = enddate.astype(datetime.date)

# index on datetime
df.index = pd.DatetimeIndex(enddate)
weekday=df.index.weekday

#define values for the weekend column. Everything has to be in one line or else it doesn't work.
# weekend=1, weekday=0. Base on wake date. Not necessarily accurate all of the time 
df['weekend'] = np.where((weekday==5)|(weekday==6),1,0)

#reset index
df=df.reset_index(drop=True)

#to csv
df.to_csv(path+"\\New_Export_File.csv", encoding='utf-8')
