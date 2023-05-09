from pytube import Playlist

# create a playlist object
playlist = Playlist("https://www.youtube.com/playlist?list=PLFF2BCBF1CEF2D436")
vid = './Videos/'
index = 1
# loop through each video in the playlist
for video in playlist.videos:
    # download the highest resolution version of the video
    stream = video.streams.get_highest_resolution()

    print(f"Downloading {video.title}...")
    stream.download(vid, filename=f'Video{index}.mp4')
    index += 1

print("All videos downloaded successfully!")
