from moviepy.editor import *

input_video_path = './Videos/'
output_audio_path = './Audios Result/'

st = 1
N = 30
for i in range(st, N + 1):
    print('String with audio ', i)

    vi = input_video_path + 'Video{}.mp4'.format(i)

    # Load the video
    video = VideoFileClip(vi)

    # Extract audio
    audio = video.audio

    # Save audio as an mp3 file
    amp3 = output_audio_path + 'Audio{}.mp3'.format(i)
    audio.write_audiofile(amp3)

    # Close the clips
    video.close()
    audio.close()
