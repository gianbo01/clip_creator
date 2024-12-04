from src.download_video import dl_video
from src.crop_video_to_9_16 import crop_video_to_9_16
from src.split_video import split_video
import sys
import os
import shutil
from dotenv import load_dotenv

# Construct the path to the .env file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, 'config', 'config.env')

# Load the environment variables
load_dotenv(dotenv_path=ENV_PATH)


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        url_video = sys.argv[1]
    else:
        url_video = input("Insert YouTube video's URL: ")
    
    # Create clip folder if not exists
    if not os.path.exists("clip"):
        os.makedirs("clip")

    # Create tmp folder if not exists
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    pathVideo = "./tmp"
    
    dl_video(url_video, pathVideo)

    input_video = "./tmp/videodl.mp4"
    output_video = "./tmp/video_9_16.mp4"
    crop_video_to_9_16(input_video, output_video)

    input_file = output_video
    output_folder = "./clip"

    split_video(input_file, output_folder)

    # Delete tmp folder
    shutil.rmtree("tmp")

    if os.path.exists("./src/__pycache__"):
        shutil.rmtree("src/__pycache__")