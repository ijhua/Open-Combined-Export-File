#set up imports
import pandas as pd
import numpy as np
import os
import datetime

#path to raw files
path=r'C:\Users\Isabelle\Python\Individual_Watch_Exports'

#name columns (headers)
my_columns=["Line","Date","Time","Off-Wrist Status","Activity","Marker","White Light","Red Light","Green Light","Blue Light","Sleep/Wake","Interval Status"]


#create empty dictionary of files
files = {}
for filename in os.listdir(path):
	subject_id = filename.split("_")[1]
	df=pd.read_csv(path + '\\' + filename, names = my_columns, encoding='utf-8', infer_datetime_format= True, low_memory=False) 
	df2=pd.DataFrame(df[(df["Interval Status"]=="ACTIVE")|(df["Interval Status"]=="REST")|(df["Interval Status"]=="REST-S")|(df["Interval Status"]=="EXCLUDED")])
# key by subject
	if subject_id in files.keys():
		files[subject_id] = files[subject_id].append(df2)
	else:
		files[subject_id] = df2


for subject in files:
	# dictionary file lookup
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
	#insert a new row for weekend. default value=A, so that it's different from everything else
	final.insert(loc=12, column='weekend', value='A')
	#define values for the weekend column. Everything has to be in the one line or else it doesn't work.
	# weekend=1, weekday=0. weekend starts at 5 pm on Friday and goes until 5 pm on Sunday (noninclusive)
	final['weekend'] = np.where((((final.index.weekday==4)&(final.index.time>datetime.time(17))))
		|((final.index.weekday==5))
		|(((final.index.weekday==6)&(final.index.time<datetime.time(17)))),1,0)
	files[subject] = final
	final.to_csv('C:\\Users\\Isabelle\\Python\\Merged_watch\\Merged_Subject_' + subject +"_Weekdayend"+".csv")
