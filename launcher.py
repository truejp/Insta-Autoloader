# import libraries
from instagrapi import Client
import os
import logging

# global vars
ACCOUNT_USERNAME = "adw0rd"
ACCOUNT_PASSWORD = "adw0rd"

# create log folder if not exists
if not os.path.exists("log"):
    os.makedirs("log")

# create log file if not exists
logging.basicConfig(filename='log/app_primary.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

logging.info("Launching app...")

# login to instagram
logging.info("Attempt login to instagram")
cl = Client()
# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# login validation
user_id = cl.user_id_from_username("adw0rd")
medias = cl.user_medias(user_id, 20)
logging.info("Fetched Account Info for user: " + str(cl.user_info(user_id)))


# check folder structure
if not os.path.exists("img"):
    print("Folder /img not found")
    logging.error("Folder /img not found. Exiting...")
    exit(1)

subf = len(os.walk('img').next()[1])
if len(os.walk('img').next()[1]) == 0:
    print("Folder /img is empty")
    logging.error("Folder /img is empty. Exiting...")
    exit(1)

logging.info("Folder /img is not empty. Starting upload process with " + str(subf) + " subfolders.")



# global functions for worker

def upload_photo():
    # upload single photo
    media = cl.photo_upload(
        "/app/image.jpg",
        "Test caption for photo with #hashtags and mention users such @adw0rd",
        extra_data={
            "custom_accessibility_caption": "alt text example",
            "like_and_view_counts_disabled": 1,
            "disable_comments": 1,
        }
    )

def upload_video():
    # upload single video
    media = cl.video_upload(
        "/app/video.mp4",
        "Test caption for photo with #hashtags and mention users such @adw0rd",
        extra_data={
            "custom_accessibility_caption": "alt text example",
            "like_and_view_counts_disabled": 1,
            "disable_comments": 1,
        }
    )

def upload_album():
    # upload album
    medias = cl.album_upload(
        [
            {
                "type": "photo",
                "file": "/app/image1.jpg",
                "usertags": [
                    {"user_id": 123456789, "position": [0.625347, 0.562977]},
                    {"user_id": 123456789, "position": [0.562977, 0.495935]},
                ], # optional field for tagging users in photo (usertags) 
            },
            {
                "type": "photo",
                "file": "/app/image2.jpg",
                "usertags": [
                    {"user_id": 123456789, "position": [0.625347, 0.562977]},
                    {"user_id": 123456789, "position": [0.562977, 0.495935]},
                ], # optional field for tagging users in photo (usertags)
            },
            {
                "type": "photo",
                "file": "/app/image3.jpg",
                "usertags": [

                ], # optional field for tagging users in photo (usertags)
            },
            {
                "type": "video",
                "file": "/app/video.mp4",
                "usertags": [
                    {"user_id": 123456789, "position": [0.625347, 0.562977]},
                    {"user_id": 123456789, "position": [0.562977, 0.495935]},
                ], # optional field for tagging users in photo (usertags)
            },
        ],
        "Test caption for album with #hashtags and mention users such @adw0rd",
        extra_data={
            "custom_accessibility_caption": "alt text example",
            "like_and_view_counts_disabled": 1,
            "disable_comments": 1,
        }
    )

