# from django.test import TestCase

# from moviepy.editor import *
# import os
# import numpy as np
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, ImageClip, ImageSequenceClip
# import emoji
# from PIL import Image, ImageDraw, ImageFont
# from pilmoji import Pilmoji
# # import emoji
# # from moviepy.video.VideoClip import TextClip
# # from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


# def process_clip(clip, text, x, y, fontsize):
        
#         processed_frames = []
#         font_color = (0, 0, 0) 

#         font = ImageFont.truetype('arial.ttf', fontsize)

#         i = 0
#         for frame in clip.iter_frames():
#             i += 1
#             print(i)
#             image = Image.fromarray(frame)

#             with Pilmoji(image) as pilmoji:
#                     pilmoji.text((x, y), text.strip(), (0, 0, 0), font)
        
#             processed_frame = np.array(image)

#             processed_frames.append(processed_frame)

#         # emoji_clip = ImageClip(processed_frames)
#         emoji_clip = ImageSequenceClip(processed_frames, fps=clip.fps)
#         processed_video = CompositeVideoClip([clip, emoji_clip])

#         # processed_video.write_videofile("E:\\repos\\video_text\\final_video.mp4")
#         return processed_video

# text = "Hello World!  😁"



# clip = VideoFileClip("E:\\repos\\video_text\\video_editors\\2023-10-08-1735394987510000\\video_1.mp4")


# clip1 = clip.subclip(0, 5)
# clip2 = clip.subclip(5, 5 + 3)  
# clip3 = clip.subclip(5 + 3)
# n_frames = sum(1 for x in clip2.iter_frames())
# print (n_frames)
# final_clip2 = process_clip(clip2, text, 50, 50, 50)
# final_clip = concatenate_videoclips([clip1, final_clip2, clip3])
# final_clip.write_videofile("E:\\repos\\video_text\\final_video.mp4")


