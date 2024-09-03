import os, shutil
import schedule
import time

path = r"C:/Users/taiwo/Downloads/"

file_name = os.listdir(path)

folder_names = ['csv files', 'image files', 'pdf files', 'video files', 'audio files']

def filesorter():
    #check if there is not file then create it
    for loop in range(0,4):
        if not os.path.exists(path + folder_names[loop]):
            os.makedirs(path + folder_names[loop])

    #put files in filders
    for file in file_name:
        if '.csv' in file and not os.path.exists(path + 'csv files/' + file):
            shutil.move(path + file, path + 'csv files/' + file)
        elif '.xls' in file and not os.path.exists(path + 'csv files/' + file):
            shutil.move(path + file, path + 'csv files/' + file)
        elif '.png' in file and not os.path.exists(path + 'image files/' + file):
            shutil.move(path + file, path + 'image files/' + file)
        elif '.jpeg' in file and not os.path.exists(path + 'image files/' + file):
            shutil.move(path + file, path + 'image files/' + file)
        elif '.jpg' in file and not os.path.exists(path + 'image files/' + file):
            shutil.move(path + file, path + 'image files/' + file)
        elif '.webp' in file and not os.path.exists(path + 'image files/' + file):
            shutil.move(path + file, path + 'image files/' + file)
        elif '.pdf' in file and not os.path.exists(path + 'pdf files/' + file):
            shutil.move(path + file, path + 'pdf files/' + file)
        elif '.mkv' in file and not os.path.exists(path + 'video files/' + file):
            shutil.move(path + file, path + 'video files/' + file)
        elif '.mp4' in file and not os.path.exists(path + 'video files/' + file):
            shutil.move(path + file, path + 'video files/' + file)
    

filesorter()

#schdule
schedule.every().saturday().at("18:00").do(filesorter)

#run
while True:
    schedule.run_pending()
    time.sleep(1)
