### PC File sorter using python modules
## Overview
This script is designed to automatically organize files in a specified directory (Downloads folder by default) into categorized subfolders. The files are sorted based on their extensions, with separate folders for CSV files, image files, PDF files, video files, and audio files. The script also schedules the sorting operation to run automatically every Saturday at 18:00.

# Prerequisites
Python 3.x installed on your system.
Basic understanding of Python programming.
How It Works
Directory Setup:

The script checks if the specified subfolders (csv files, image files, pdf files, video files, audio files) exist within the target directory.
If the folders do not exist, the script automatically creates them.
File Sorting:

The script lists all files in the target directory (Downloads folder).
It then checks each file's extension and moves it to the appropriate subfolder.
The supported file types and their respective folders are:
CSV Files: .csv, .xls
Image Files: .png, .jpeg, .jpg, .webp
PDF Files: .pdf
Video Files: .mkv, .mp4
Audio Files: You can add more extensions as needed.
Scheduling:

The script uses the schedule library to run the sorting operation every Saturday at 18:00.
Continuous Operation:

The script enters an infinite loop to keep checking and executing the scheduled task at the defined time.
Installation
Clone or Download the Repository:

Clone this repository to your local machine or download the file_sorter.py script.
Install Required Libraries:

Ensure you have the schedule library installed. You can install it using pip:
bash
Copy code
pip install schedule
Set the Target Path:

Update the path variable in the script to point to your desired directory. By default, it is set to the Downloads folder:
python
Copy code
path = r"C:/Users/taiwo/Downloads/"
Usage
Run the Script:

Execute the script in your terminal or command prompt:
bash
Copy code
python file_sorter.py
Automated Sorting:

The script will automatically create necessary folders and move files based on their extensions.
Every Saturday at 18:00, the script will automatically run the sorting process.
Stopping the Script:

To stop the script, you can interrupt it by pressing Ctrl + C in your terminal or command prompt.
Customization
Adding More File Types:

You can add more file types to the script by extending the if-elif conditions in the filesorter() function. For example:
python
Copy code
elif '.mp3' in file and not os.path.exists(path + 'audio files/' + file):
    shutil.move(path + file, path + 'audio files/' + file)
Changing the Schedule:

To change the day and time the script runs, modify the schedule.every().saturday().at("18:00").do(filesorter) line. For example, to run every Monday at 9 AM:
python
Copy code
schedule.every().monday().at("09:00").do(filesorter)
