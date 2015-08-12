#set up imports
import pandas as pd
import numpy as np

#name columns
my_columns=["Line","Date","Time","Off-Wrist Status","Activity","Marker","White Light","Red Light","Green Light","Blue Light","Sleep/Wake","Interval Status"]

#print the csv
print (pd.read_csv("Subject_01_04_03_2015_9_00_00_AM_New_Analysis.csv", skiprows=153,names=my_columns, engine='python'))

'''
This code can open an export file. I set it to skip the first 153 lines, which is hopefully the same number in each subject export file. When it prints the csv, the columns are sometimes put underneath, probably because there is a limit on the screen size. I don't know what impact this will have in the future when we try to join csv files together. 
'''
