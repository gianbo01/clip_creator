from moviepy.editor import VideoFileClip

def crop_video_to_9_16(input_file, output_file, codec='libx264', audio_codec='aac'):
    
    clip = VideoFileClip(input_file)
    
    width, height = clip.w, clip.h
    
    target_ratio = 9 / 16
    current_ratio = width / height

    if current_ratio > target_ratio:
        # too wide video, crop sides
        new_width = int(height * target_ratio)
        x_center = width / 2
        crop_width = new_width
        crop_height = height
        x1 = int(x_center - crop_width / 2)
        y1 = 0
    else:
        # too tall video, crop top and bottom
        new_height = int(width / target_ratio)
        y_center = height / 2
        crop_width = width
        crop_height = new_height
        x1 = 0
        y1 = int(y_center - crop_height / 2)

    
    cropped_clip = clip.crop(x1=x1, y1=y1, width=crop_width, height=crop_height)

    # save cropped video
    cropped_clip.write_videofile(
        output_file,
        codec=codec,
        audio_codec=audio_codec,
        ffmpeg_params=["-crf", "23"], # lower is better quality
        remove_temp=True,
        preset="medium",  
        threads=4  # use more threads for faster processing
    )

    # Close the clips to free up resources
    clip.close()
    cropped_clip.close()

    print(f"Cropped video saved as -> {output_file}")