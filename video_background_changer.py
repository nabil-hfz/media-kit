from moviepy.editor import *

input_video_path = './Videos/'
input_video_path_slides = './Slides/'
output_video_path = './Videos Result/'
output_audio_path = './Audios Result/'

st = 1
N = 30
for i in range(st, N + 1):
    print('String with video ', i)
    vi = input_video_path + 'Video{}.mp4'.format(i)

    video = VideoFileClip(vi)
    ip = input_video_path_slides + 'Slide{}.jpg'.format(i)
    # print('video path: ', vi)
    # print('image path: ', ip)

    title = ImageClip(ip).set_start(0).set_duration(video.duration).set_pos(("center", "center"))

    vo = output_video_path + 'Video{}.mp4'.format(i)
    final = CompositeVideoClip([video, title], size=title.size)
    final.write_videofile(vo)

    # Extract audio
    audio = video.audio

    # Save audio as an mp3 file
    amp3 = output_audio_path + 'Audio{}.mp3'.format(i)
    audio.write_audiofile(amp3)

    # Close the clips
    video.close()
    audio.close()
    final.close()
