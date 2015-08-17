#set up imports
import pandas as pd
import numpy as np

#define dataframe
#df=DataFrame("Subject_01_04_03_2015_9_00_00_AM_New_Analysis.csv")

#name columns
my_columns=["Line","Date","Time","Off-Wrist Status","Activity","Marker","White Light","Red Light","Green Light","Blue Light","Sleep/Wake","Interval Status"]

#define parts of the csv
file= pd.read_csv("Subject_01_04_03_2015_9_00_00_AM_New_Analysis.csv", names=my_columns)

#print the csv
print (file[(file["Interval Status"]=="ACTIVE")|(file["Interval Status"]=="REST")|(file["Interval Status"]=="REST-S")|(file["Interval Status"]=="EXCLUDED")])

df = pd.DataFrame(file[(file["Interval Status"]=="ACTIVE")|(file["Interval Status"]=="REST")|(file["Interval Status"]=="REST-S")|(file["Interval Status"]=="EXCLUDED")])
df.to_csv("New_Watch_File.csv")
