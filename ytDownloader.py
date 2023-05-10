from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

path_to_download = './downloaded_videos'

yd = yt.streams.get_highest_resolution()
yd.download(path_to_download)