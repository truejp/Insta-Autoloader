# Main Script to launch the app
# Includes: Scheduler, Primary Logics etc.

# import libraries
import os
import time
import random
import logging
import datetime
from instagrapi import Client
from tinydb import TinyDB, Query

# import functions
from functions import validate_folder
from functions import list_files
from functions import list_folders

# config
ACCOUNT_USERNAME = "jpl_tester"
ACCOUNT_PASSWORD = "fJjC7cU65ftk372E"
MEDIA_FOLDER = "media"
DB_FILE = "db/db.json"
CRED_DB_NAME = "insta_db"
UPLOAD_DB_NAME = "upload_db"

# create log folder if not exists
if not os.path.exists("log"):
    os.makedirs("log")

if not os.path.exists("db"):
    os.makedirs("db")

# create log file if not exists
logging.basicConfig(filename='log/app_primary.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

logging.info("")
logging.info("")
logging.info("Launching app...")
print("Launching app...")

# login to instagram
logging.info("Attempt login to instagram")
print("Attempt login to instagram")
cl = Client()
# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# login validation
# user_id = cl.user_id_from_username("jpl_tester")
# medias = cl.user_medias(user_id, 20)
# logging.info("Fetched Account Info for user: " + str(cl.user_info(user_id)))


# validate media folder, check if it's empty
subf = validate_folder(MEDIA_FOLDER)
logging.info("Folder /" + MEDIA_FOLDER + " is not empty. Starting upload process with " + str(subf) + " subfolder(s).")
print("Folder /" + MEDIA_FOLDER + " is not empty. Starting upload process with " + str(subf) + " subfolder(s).")

# load folder structure
root_list = list_folders(MEDIA_FOLDER)

# load db
db = TinyDB(DB_FILE)
cred_db = db.table(CRED_DB_NAME)
upload_db = db.table(UPLOAD_DB_NAME)

# enter loop
while True:
    # check if there are more folders than already uploaded
    if (len(root_list) <= len(upload_db.all())):
        logging.info("All folders have been uploaded. Exiting app.")
        print("All folders have been uploaded. Exiting app.")
        break
    while True:
        # randomly choose a folder that has not been uploaded
        curr_root = random.choice(root_list)[0]
        # check if folder was previously uploaded
        if (len(upload_db.search(Query().folder == curr_root)) > 0):
            logging.info("Folder " + curr_root + " has been uploaded. Skip this folder.")
            print("Folder " + curr_root + " has been uploaded. Skip this folder.")
            continue
        else:
            break

    logging.info("Randomly choose folder: " + curr_root)
    print("Randomly choose folder: " + curr_root)

    # check files in subfolder
    subf_list = list_files(MEDIA_FOLDER + "/" + curr_root)
    logging.info("Found " + str(len(subf_list)) + " files in folder: " + curr_root)
    print("Found " + str(len(subf_list)) + " files in folder: " + curr_root)

    valid_files = []
    # check if filetypes are .mp4 or .jpg
    for subf in subf_list:
        if ((os.path.splitext(subf)[1] == ".mp4") | (os.path.splitext(subf)[1] == ".jpg")):
            logging.info("Found file: " + subf)
            print("Found file: " + subf)
            valid_files.append(subf)

    # if there are valid files, start uploading process
    if (len(valid_files) > 0):
        i = 0
        for file in valid_files:
            i+=1
            print("Uploading " + str(len(valid_files)) + " files in folder: " + curr_root + " (" + str(i) + "/" + str(len(valid_files)) + ")")
            logging.info("Uploading " + str(len(valid_files)) + " files in folder: " + curr_root)

            # upload file(s) to instagram
            if (os.path.splitext(file)[1] == ".mp4"):
                # upload video
                logging.info("Uploading video: " + file)
                print("Uploading video: " + file)
                # cl.video_upload(file, "Video from Python")
            elif (os.path.splitext(file)[1] == ".jpg"):
                # upload photo
                logging.info("Uploading photo: " + file)
                print("Uploading photo: " + file)
                # cl.photo_upload(file, "Photo from Python")
            else:
                logging.info("File type not supported: " + file)
                print("File type not supported: " + file)
                continue

            # put uploaded file into db
            upload_db.insert({'folder': curr_root, 'file': file, 'uploaded_at': str(datetime.datetime.now()), 'account': ACCOUNT_USERNAME})
        
    # go to sleep for 20 to 45 seconds before next loop
    sleep_time = random.randint(20, 45)
    logging.info("Sleeping for " + str(sleep_time) + " seconds before next loop.")
    print("Sleeping for " + str(sleep_time) + " seconds before next loop.")
    time.sleep(sleep_time)

    # end of script