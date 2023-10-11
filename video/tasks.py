import os
import numpy as np
from celery import shared_task, group
from django.core.files.base import ContentFile
from .helper import encode_image, decode_image, new_paths
from PIL import Image, ImageFont
from pilmoji import Pilmoji
from moviepy.editor import ImageSequenceClip, CompositeVideoClip, VideoFileClip, concatenate_videoclips
from .models import Video


@shared_task
def process_frame(frame, text, x, y, fontsize):

    image = Image.fromarray(frame)

    font = ImageFont.truetype('arial.ttf', fontsize)

    with Pilmoji(image) as pilmoji:
        pilmoji.text((x, y), text.strip(), (0, 0, 0), font)

    # image.show()
    processed_frame = np.array(image)

    print(1)
    return processed_frame


def process_clip(clip, text, x, y, fontsize):
    
    processed_frames = []

    # job = group([
    #     process_frame.s(frame, text, x, y, fontsize)
    # ])

    # result = job.apply_async()

    # result.ready()  # have all subtasks completed?
    
    # result.successful()
    for frame in clip.iter_frames():
        processed_frame = process_frame.delay(frame, text, x, y, fontsize).get()
        processed_frames.append(processed_frame)


    emoji_clip = ImageSequenceClip(processed_frames, fps=clip.fps)
    processed_video = CompositeVideoClip([clip, emoji_clip])

    return processed_video

#@shared_task
def edit_video(video_slug, video_path, text_clip, x, y, timestep, duration, fontsize):

    clip = VideoFileClip(video_path) 

    clip1 = clip.subclip(0, timestep)
    clip2 = clip.subclip(timestep, timestep + duration)  
    clip3 = clip.subclip(timestep + duration)  


    final_clip2 = process_clip(clip2, text_clip, x, y, fontsize)

    final_clip = concatenate_videoclips([clip1, final_clip2, clip3])

    full_path, name_video = new_paths(video_path)

    new_video = Video()
    final_clip.write_videofile(full_path)
    content = open(full_path, 'rb').read()
    new_video.video.save(name_video, ContentFile(content))
    new_video.slug = video_slug
    # final_clip.delete()
    new_video.save()

    # return final_clip

