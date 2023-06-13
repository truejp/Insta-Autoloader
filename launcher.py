# import libraries
from instagrapi import Client
import os
import logging

# import functions
from functions import fcount

# global vars
ACCOUNT_USERNAME = "jpl_tester"
ACCOUNT_PASSWORD = "fJjC7cU65ftk372E"

# create log folder if not exists
if not os.path.exists("log"):
    os.makedirs("log")

# create log file if not exists
logging.basicConfig(filename='log/app_primary.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

logging.info("Launching app...")

# login to instagram
logging.info("Attempt login to instagram")
cl = Client()
# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# login validation
# user_id = cl.user_id_from_username("jpl_tester")
# medias = cl.user_medias(user_id, 20)
# logging.info("Fetched Account Info for user: " + str(cl.user_info(user_id)))


# check folder structure
if not os.path.exists("img"):
    print("Folder /img not found")
    logging.error("Folder /img not found. Exiting...")
    exit(1)

path = "img"
map = {}
subf = fcount(path, map)
print(subf)

if subf == 0:
    print("Folder /img is empty")
    logging.error("Folder /img is empty. Exiting...")
    exit(1)

logging.info("Folder /img is not empty. Starting upload process with " + str(subf) + " subfolders.")


