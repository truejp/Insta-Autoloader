# Main Script to launch the app
# Includes: Scheduler, Primary Logics etc.

# import libraries
from instagrapi import Client
import os
import logging

# import functions
from functions import validate_folder

# config
ACCOUNT_USERNAME = "jpl_tester"
ACCOUNT_PASSWORD = "fJjC7cU65ftk372E"
MEDIA_FOLDER = "media"

# create log folder if not exists
if not os.path.exists("log"):
    os.makedirs("log")

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

# enter loop

# check local db if media has been uploaded

# randomly choose a folder that has not been uploaded