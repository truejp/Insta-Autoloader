# Required functions for launcher.py
import os
import logging

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

def list_folders(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        r.append(dirs)
    # remove all empty entries from list
    r = [x for x in r if x != []]
    return r

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

def fcount(root_dir):
  map = {}
  count = 0
  for f in os.listdir(root_dir):
    child = os.path.join(root_dir, f)
    if os.path.isdir(child):
      child_count = fcount(child)
      count += child_count + 1 # unless include self
  map[root_dir] = count
  return count

def validate_folder(PATH):
    # validate media folder, check if it's empty
    if not os.path.exists(PATH):
        print("Folder /" + PATH + " not found")
        logging.error("Folder /" + PATH + " not found. Exiting...")
        print("Exiting...")
        exit(1)
    logging.info("Folder /" + PATH + " found.")
    print("Folder /" + PATH + " found.")
    subf = fcount(PATH)

    if subf == 0:
        print("Folder /" + PATH + " is empty")
        logging.error("Folder /" + PATH + " is empty. Exiting...")
        print("Exiting...")
        exit(1)
    return subf


