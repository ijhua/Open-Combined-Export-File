#Files that deal with the summary data:
## OpenCombinedExportFile
This code opens the combined export file and prints only the sleep data without the headers. Then, it saves the new data table as a csv. 
##CombinedExportFilePandas
Basically the same as the OpenCombinedExportFile, but this one uses pandas and prints only the sleep data with headers into a new csv ("New_Export_File"). 
##SummaryCalculations
Calculates average and standard deviation of onset, offset, duration, and efficiency for weekends and weekdays from the raw data in the CombinedExportFilePandas. Also calculates social jetlag from calculated midsleep on freedays and workdays. Prints calculated data to a new csv. Format of time is in hours, not H:MM:SS. 
The code uses dictionaries, which are inherently unordered in python, but the supposed disorder is not unorderly. The order that the subjects (keys) are printed may change, but the data associated with them does not. I.e. data from subject 1 is always with subject 1, even if subject 1 is not at the top of the list. 

#Files that deal with the raw data:
## OpenWatchFilePandas
The code opens the raw data from the watch export files and concatenates them together in one big file. Subject numbers are preserved.
##NewWatchFile
Opens the csv files by subject and concatenates all the files of one subject together. Currently does not succeed in opening the csv file. 
##CombineAllWatchFiles
Opens the individual files by subject and concatenates the two together. Then adds in the missing times. Does _not_ mark whether the day is weekend or weekday.
##WeekendWatchLabel:
Opens the individual files by subject and concatenates the two together. Then adds in the missing times.  The code then labels whether or not the time stamp is between 5pm on Friday to 5pm on Sunday (noninclusive) . 1=yes, 0= no. It is built on the concatenating code (CombineAllWatchFiles).
