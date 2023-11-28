from pytube import YouTube
from pydub import AudioSegment
import sys
import os

if len(sys.argv) != 2:
    exit(1)
print(sys.argv[1])

# video_url = sys.argv[1]
# YouTube(video_url).streams.first().download("D:\\IA\\song\\original_video")

video_url = sys.argv[1]

output_directory = r'D:\\IA\\song\\original_video'
os.makedirs(output_directory, exist_ok=True)

video = YouTube(video_url)

audio = video.streams.filter(only_audio=True).first()
audio.download(output_path=output_directory)

# Get the default output file path (example: 'video_title.webm')
original_file_path = os.path.join(output_directory, audio.default_filename)

# Convert the downloaded audio file to MP3 using pydub
audio = AudioSegment.from_file(original_file_path, format="webm")
mp3_file_path = os.path.join(output_directory, os.path.splitext(audio.default_filename)[0] + ".mp3")
audio.export(mp3_file_path, format="mp3")

# Delete the original webm file
os.remove(original_file_path)

print(f"Video downloaded as MP3: {mp3_file_path}")