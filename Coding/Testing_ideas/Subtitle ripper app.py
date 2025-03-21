from youtube_transcript_api import YouTubeTranscriptApi as yttrans
import urllib.request
import simplejson
import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import time
import os

file_path=input("please give path to save results in\n>")

def convert_to_srt(entry, index):
    start_time = entry['start']
    end_time = start_time + entry['duration']

    srt_start_time = format_time(start_time)
    srt_end_time = format_time(end_time)

    text = entry['text']

    

    return f"{index}\n{srt_start_time} --> {srt_end_time}\n{text}\n"


def format_time(seconds):
    milliseconds = int((seconds - int(seconds)) * 1000)
    time_obj = time.gmtime(seconds)
    formatted_time = time.strftime("%H:%M:%S,", time_obj)
    return f"{formatted_time}{milliseconds:03}"

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=path)
    except:
        print("An error has occurred")
    else:
        print("Download is completed successfully")


episodes=[]
while True:
    video_request=input("Please enter the final part of the youtube URL\n When done enter 'done'\n>")
    if video_request.lower()=="done" or video_request=="" or not video_request:
        break
    else:
        episodes.append(video_request)


directory=file_path

for episode in episodes:
    try:
        srt=yttrans.get_transcript(f"{episode}",languages=['ar'])
        r = requests.get(f"https://www.youtube.com/watch?v={episode}")
        soup = BeautifulSoup(r.text,features="html.parser")
        link = soup.find_all(name="title")[0]
        title = str(link)
        title = title.replace("<title>","")
        title = title.replace("</title>","")
        title = title.split("-")[0].strip()
        title=title.split(":")[1]
        new_filename=f"{title}.srt"
        path = os.path.join(directory, title)
        os.mkdir(path)
        download(f"https://www.youtube.com/watch?v={episode}")
        with open(f"{path}/{title}.srt", "a+", encoding="utf-8") as file:
            i=1
            for line in srt:
                file.write(f"{str(convert_to_srt(line,i))}\n")
                i+=1
        print(f"Episode: {title} completed")
    except(FileExistsError):
        print(f"Failed on episode {episode} (title: {title})")
        continue
    
    





