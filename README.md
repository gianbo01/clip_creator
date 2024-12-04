# YouTube Video Scene Splitter

## Overview

This Python script provides a comprehensive tool for downloading YouTube videos, converting them to a 9:16 aspect ratio (vertical format), and splitting them into individual scene clips.

## Features

- Download videos directly from YouTube
- Crop videos to 9:16 aspect ratio
- Automatically detect and split videos into scenes
- Configurable scene detection parameters

## Prerequisites

- Python 3.8+
- FFmpeg installed on your system
- The following Python libraries:
  - moviepy
  - yt-dlp
  - python-dotenv
  - scenedetect

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gianbo01/youtube-video-scene-splitter.git
   cd youtube-video-scene-splitter
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Install FFmpeg:
   - Download from [FFmpeg official site](https://ffmpeg.org/download.html)
   - Set the path in `config.env`

2. Configure `config.env`:
   ```
   # Path to FFmpeg binary
   FFMPEG_PATH="C:\\path\\to\\ffmpeg\\bin"

   # Scene detection threshold (default: 27.0)
   TRESHOLD=27.0

   # Use only luma channel for scene detection
   LUMA_ONLY=False
   ```

## Usage

Run the script with a YouTube video URL:
```bash
python main.py
# Or pass the URL directly
python main.py "https://youtube.com/video_url"
```

The script will:
1. Download the video
2. Crop it to 9:16 aspect ratio
3. Split into scene clips
4. Save clips in the `./clip` directory

## Customization

You can adjust scene detection parameters in `config.env`:
- `TRESHOLD`: Lower values make scene detection more sensitive
- `LUMA_ONLY`: Use only luminance for scene detection

## Output

- Downloaded and processed videos are temporarily stored in `./tmp`
- Scene clips are saved in `./clip`

## Requirements File

Create a `requirements.txt` with:
```
moviepy
yt-dlp
python-dotenv
scenedetect
```

## Troubleshooting

- Ensure FFmpeg path is correctly set
- Check internet connection for YouTube downloads
- Verify Python and library versions

## License

Read [MIT License](https://github.com/gianbo01/youtube-video-scene-splitter/blob/main/LICENSE)

## Contributing

Contributions are welcome! Please submit pull requests or open issues.

## Disclaimer

Respect YouTube's terms of service and copyright regulations when downloading videos.
