# Required functions for launcher.py
import os


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

def fcount(path, map = {}):
  count = 0
  for f in os.listdir(path):
    child = os.path.join(path, f)
    if os.path.isdir(child):
      child_count = fcount(child, map)
      count += child_count + 1 # unless include self
  map[path] = count
  return count

