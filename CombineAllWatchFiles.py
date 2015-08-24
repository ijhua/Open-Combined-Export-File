#set up imports
import pandas as pd
import numpy as np
import os
import csv
import datetime



#path to raw files
path=r'C:\Users\Isabelle\Python\Individual_Watch_Exports'


#name columns (headers)
my_columns=["Line","Date","Time","Off-Wrist Status","Activity","Marker","White Light","Red Light","Green Light","Blue Light","Sleep/Wake","Interval Status"]



#os.listdir takes a list of the files in the directory (which in this case is the path to the files)
files = {}
for filename in os.listdir(path):
	subject_id = filename.split("_")[1]
	df=pd.read_csv(path + '\\' + filename, names = my_columns, encoding='utf-8', infer_datetime_format= True) 
	df2=pd.DataFrame(df[(df["Interval Status"]=="ACTIVE")|(df["Interval Status"]=="REST")|(df["Interval Status"]=="REST-S")|(df["Interval Status"]=="EXCLUDED")])
# key by subject
	if subject_id in files.keys():
		files[subject_id] = files[subject_id].append(df2)
	else:
		files[subject_id] = df2
for subject in files:
	# get dictionary lookup
	data = files[subject]
	# create datetime object
	mergetime = pd.to_datetime(data.iloc[:,1] + " " + data.iloc[:,2])
	mergetime = mergetime.astype(datetime.datetime)
	# index on datetime
	data.index = pd.DatetimeIndex(mergetime)
	# reindex with missing values
	drange = pd.date_range(start=min(mergetime), end=max(mergetime), freq='15s')
	final = data.reindex(drange)
	final['Time'] = drange.time
	final['Date'] = drange.date
	files[subject] = final
	final.to_csv('C:\\Users\\Isabelle\\Python\\Merged_watch\\Merged_Subject_' + subject +".csv")
