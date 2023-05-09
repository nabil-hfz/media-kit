from pytube import Playlist


class PlayListDownloader:
    def __init__(self, playlistLink: str, videosPath: str = './Videos'):
        self.playlistLink = playlistLink
        self.videosPath = videosPath
        self.playlist = Playlist(playlistLink)

    def run(self):
        index = 1
        currentPlaylist = self.playlist
        print("Start downloading videos of ", len(currentPlaylist.videos))
        for video in currentPlaylist.videos:
            print(f"Downloading {video.title}...")
            stream = video.streams.get_highest_resolution()
            stream.download(self.videosPath, filename=f'Video{index}.mp4')
            index += 1
        print("All videos downloaded successfully!")

# git rm -r --cached --ignore-unmatch my_project_env
# git rm -r --cached --ignore-unmatch venv
