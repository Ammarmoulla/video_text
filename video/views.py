import os
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.exceptions import APIException
import time
from .models import Video
from django.core.files.base import ContentFile
from .serializers import VideoSerializer
from .tasks import edit_video
from .helper import new_paths



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'], name="edit")
    def add_text(self, request, pk=None):

        video_orginal = self.get_object()
        video_path = video_orginal.video.path
        video_slug = video_orginal.slug
        video_obj = video_orginal.video

        try:
            with transaction.atomic():
                final_clip = edit_video(
                    video_path,
                    request.data['text'],
                    int(request.data['x']),
                    int(request.data['y']),
                    int(request.data['t']),
                    int(request.data['d']),
                    int(request.data['s'])
                )

                full_path, name_video = new_paths(video_path)

                final_clip.write_videofile(full_path, threads=4, audio = False, progress_bar = False) 
                content = open(full_path, 'rb').read()

                new_video = Video(slug = video_slug + "edit")
                new_video.video.save(name_video, ContentFile(content))
                new_video.save()

                os.remove(full_path)
            
        except Exception as e:
            transaction.rollback()
            raise APIException(str(e))      
        
        return Response({"edit":True}, status=status.HTTP_200_OK)