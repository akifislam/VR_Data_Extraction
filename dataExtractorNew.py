import csv
import statistics
import glob
import time
import math

# /Users/akifislam/Desktop/VR_Data_Extraction/1/Ishmam Zahin/Gesture Contorller/WPMandTotalER.csv

# 7 Refers to New Controller File
# 8 Referes to New Hand File

path = "/Users/akifislam/Desktop/VR_Data_Extraction/1"
newCSVfile = open('/Users/akifislam/Desktop/VR_Data_Extraction/Output/1st_10_Summary.csv', 'w')
writer = csv.writer(newCSVfile)
serial_counter = 0
writer.writerow(['Serial','Username', 'Experiment Name', 'Mean WPM', 'Median WPM', 'Mean Error', 'Median Error'])

for cur_path in glob.glob(path + "/**/WPMandTotalER.csv", recursive = True):

    print("----------")
    print(cur_path[46:])

    userdetails = ""
    username = ""
    experiment_name = ""
    slashCounter = 0

    for letter in cur_path[46:]:
        userdetails+= letter

        if (letter == '/'):
            slashCounter += 1

        if (slashCounter == 2):
            break

    isName = True
    for letter in userdetails:
        if(letter=='/'):
            isName=False
            continue
        if(isName):
            username+=letter
        else:
            experiment_name+=letter


    print("Username : " +username)
    print("Experiment : " +experiment_name)

    file = open(cur_path)
    csvreader = csv.reader(file)

    ERRORS = []  # A list of total errors
    WPMS = []  # A list of total WPMs

    for wpm in csvreader:
        if(math.isnan(float(wpm[0]))==False):
            WPMS.append(float(wpm[0]))


    file = open(cur_path)
    csvreader2 = csv.reader(file)

    for error in csvreader2:
        if (math.isnan(float(error[6]))==False):
            ERRORS.append(float(error[6]))

    # Calculating Mean, Median, Mode for WPM
    mean_WPM = statistics.mean(WPMS)
    median_WPM = statistics.median(WPMS)
    # mode_WPM = statistics.mode(WPMS)

    # Calculating Mean, Median, Mode for ERRORS
    mean_ERROR = statistics.mean(ERRORS)
    median_ERROR = statistics.median(ERRORS)
    # mode_ERROR = statistics.mode(ERRORS)
    serial_counter+=1

    writer.writerow([serial_counter,username,experiment_name,mean_WPM,median_WPM,mean_ERROR,median_ERROR])
    print(f"WPM Mean : {mean_WPM}, WPM Median : {median_WPM}")
    print(f"Error Mean : {mean_ERROR}, Error Median : {median_ERROR}")
    print()

newCSVfile.close()




# print(csv_files)





