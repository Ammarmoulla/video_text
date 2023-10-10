import os
import numpy as np
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, ImageSequenceClip
from PIL import Image, ImageFont
from pilmoji import Pilmoji

def new_paths(video_path):

    name_video = os.path.basename(video_path)[:-4] + "_edit.mp4"
    full_path = video_path[:-4] + "_edit.mp4"
    return full_path, name_video


def process_clip(clip, text, x, y, fontsize):
        
        processed_frames = []

        font = ImageFont.truetype('arial.ttf', fontsize)

        for frame in clip.iter_frames():

            image = Image.fromarray(frame)

            with Pilmoji(image) as pilmoji:
                 pilmoji.text((x, y), text.strip(), (0, 0, 0), font)
        
            processed_frame = np.array(image)

            processed_frames.append(processed_frame)

        emoji_clip = ImageSequenceClip(processed_frames, fps=clip.fps)
        processed_video = CompositeVideoClip([clip, emoji_clip])

        return processed_video


def edit_video(video_path, text_clip, x, y, timestep, duration, fontsize):

    clip = VideoFileClip(video_path) 
   
    clip1 = clip.subclip(0, timestep)
    clip2 = clip.subclip(timestep, timestep + duration)  
    clip3 = clip.subclip(timestep + duration)  


    final_clip2 = process_clip(clip2, text_clip, x, y, fontsize)

    final_clip = concatenate_videoclips([clip1, final_clip2, clip3])

    return final_clip




