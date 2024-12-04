from scenedetect import detect, ContentDetector
from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os

def split_video(input_file, output_folder):
    TRESHOLD = float(os.getenv("TRESHOLD"))
    LUMA_ONLY = bool(os.getenv("LUMA_ONLY"))

    detector = ContentDetector(
        threshold = TRESHOLD,
        luma_only = LUMA_ONLY,
    )
    
    
    print("Detecting scenes...")
    scenes = detect(input_file, detector)

    
    print("Loading video...")
    video = VideoFileClip(input_file)

    for i, scene in enumerate(scenes):
        print(f"Processing scene {i+1}...")
        start_time = scene[0].get_seconds()
        end_time = scene[1].get_seconds()
        
        clip = video.subclip(start_time, end_time)
        
        output_file = f"{output_folder}/clip_{i+1}.mp4"
        clip.write_videofile(output_file, codec="libx264")

    video.close()