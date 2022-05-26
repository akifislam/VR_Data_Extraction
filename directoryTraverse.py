import glob

path = "/Users/akifislam/Desktop/VR_Data_Extraction/10"

text_files = glob.glob(path + "/**/WPMandTotalER.csv", recursive = True)

print(len(text_files))
