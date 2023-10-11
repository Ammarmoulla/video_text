import os
import base64

def new_paths(video_path):

    name_video = os.path.basename(video_path)[:-4] + "_edit.mp4"
    full_path = video_path[:-4] + "_edit.mp4"
    return full_path, name_video

def encode_image(frame):
    # buffer = frame.write_buffer(codec='jpeg')
    # retval, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(frame).decode("utf-8")

def decode_image(frame):
    return base64.decodebytes(frame.encode())


