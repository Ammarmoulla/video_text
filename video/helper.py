import os
from moviepy.editor import VideoFileClip, TextClip

def new_path(video_path):

    first, second = os.path.dirname(video_path), os.path.basename(video_path)
    first += "-edit"
    res = os.path.join(first, second)
    return res

def edit_video(video_path, text_clip, x, y, timestep, duration, fontsize):


    video_text_path = new_path(video_path)
    video = VideoFileClip(video_path)
    
    text_clip = TextClip(text_clip, fontsize=int(fontsize, color='white')).set_position((x, y)).set_duration(duration)
            
    video_with_text = video.set_duration(duration).set_audio(None).add_textclip(text_clip)

    video_with_text.write_videofile(video_text_path, codec='libx264')