# Insta-Autoloader
 Autoloader for Insta API

## Requirements
- Instagrapi 2023
- Python >=3.8

## Install

### 1. Install neccessary libraries
First, install Python with the option "Add to PATH". Afterwards, reboot your system.
```
pip install instagrapi
```

### 2. Prepare image folders
Copy your desired images to the repository. The tool only accepts .mp4 videos as well as .jpg images. Max resolution on upload will be 1080x1080. Images will be resized automatically.

### 3. Launch script and let it run
Launch the application using the command ```python launcher.py```.

## Additional notes
- Logs can be found in /log/ folder
- Files have to be put into /img/xxxxx/my_image.jpg
- If you want to upload multiple images into a single post, paste multiple images in the same folder

## Todo
- [ ] Random Delay between API calls
- [ ] Max. Number of uploads per Day
- [ ] Add paid proxy service to application
- [ ] Add external notification interface to check app status