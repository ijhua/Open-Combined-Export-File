Files that deal with the _summary_ data:
# OpenCombinedExportFile
This code opens the combined export file and prints only the sleep data without the headers. Then, it saves the new data table as a csv. 
#CombinedExportFilePandas
Basically the same as the OpenCombinedExportFile, but this one uses pandas and prints only the sleep data with headers. 

Files that deal with the _raw_ data:
# OpenWatchFilePandas
The code opens the raw data from the watch export files and concatenates them together in one big file. Subject numbers are preserved.
#NewWatchFile
Opens the csv files by subject and concatenates all the files of one subject together. Currently does not succeed in opening the csv file. 
#CombineAllWatchFiles
Opens the individual files by subject and concatenates the two together. Then adds in the missing times. Does _not_ mark whether the day is weekend or weekday.
#WeekendWatchLabel:
Opens the individual files by subject and concatenates the two together. Then adds in the missing times.  The code then labels whether or not the time stamp is between 5pm on Friday to 5pm on Sunday (noninclusive) . 1=yes, 0= no. It is built on the concatenating code (CombineAllWatchFiles).
