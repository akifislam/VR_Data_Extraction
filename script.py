import csv
import statistics
import glob

path = "/Users/akifislam/Desktop/VR_Data_Extraction/10"


file = open('WPMandTotalER.csv')
csvreader = csv.reader(file)

ERRORS = []  # A list of total errors
WPMS = []  # A list of total WPMs

for wpm in csvreader:
    WPMS.append(float(wpm[0]))

file = open('WPMandTotalER.csv')
csvreader2 = csv.reader(file)

for error in csvreader2:
    ERRORS.append(float(error[6]))



# Calculating Mean, Median, Mode for WPM
mean_WPM = statistics.mean(WPMS)
median_WPM = statistics.median(WPMS)
# mode_WPM = statistics.mode(WPMS)

# Calculating Mean, Median, Mode for ERRORS
mean_ERROR = statistics.mean(ERRORS)
median_ERROR = statistics.median(ERRORS)
# mode_ERROR = statistics.mode(ERRORS)

print("For Words Per Minutes (WPM) :")
print(f"Mean : {mean_WPM}, Median : {median_WPM}\n")
print("For Errors :")
print(f"Mean : {mean_ERROR}, Median : {median_ERROR}\n\n")






csv_files = glob.glob(path + "/**/WPMandTotalER.csv", recursive = True)

print(csv_files)




