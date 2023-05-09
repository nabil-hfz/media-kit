from moviepy.editor import *

input_audio_path = './Audios Result/'
input_image_path = './Slides/'
output_video_path = './Videos Result/'


st = 1
N = 30
for i in range(st, N + 1):
    print(f'Processing audio file {i}')

    # Load the MP3 file Part_01
    audio_file = f'{input_audio_path}Part_{i:02d}.mp3'
    audio = AudioFileClip(audio_file)

    # Load the image file Slide1.jpg
    image_file = f'{input_image_path}Slide{i}.jpg'
    image = ImageClip(image_file, duration=audio.duration)

    # Combine image and audio
    video = image.set_audio(audio)

    # Save the result as an MP4 video
    output_file = f'{output_video_path}Video{i}.mp4'

    # video.write_videofile(output_file, codec='libx264', audio_codec='aac')
    video.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24)
