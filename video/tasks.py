from django.core.files.base import ContentFile
from celery import shared_task
from .models import Video
from .helper import edit_video, new_paths

@shared_task
def task_execute(job_params):

    final_clip = edit_video(
        job_params["video_path"], 
        job_params["text_clip"],
        job_params["x"],
        job_params["y"], 
        job_params["timestep"],
        job_params["duration"],
        job_params["fontsize"]
    )
    full_path, name_video = new_paths(job_params["video_path"])

    new_video = Video()
    final_clip.write_videofile(full_path)
    content = open(full_path, 'rb').read()
    new_video.video.save(name_video, ContentFile(content))
    new_video.slug = job_params["video_slug"]
    final_clip.delete()
    new_video.save()

