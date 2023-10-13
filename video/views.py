import os
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.db import transaction
from rest_framework.exceptions import APIException

from .models import Video
from django.core.files.base import ContentFile
from .serializers import VideoSerializer
from .tasks import edit_video
from .helper import new_paths



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'slug'

    @action(detail=True, methods=['post'], name="add_text")
    def add_text(self, request, pk=None):

        video_orginal = self.get_object()
        video_path = video_orginal.video.path
        video_slug = video_orginal.slug

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

                final_clip.write_videofile(full_path, threads=4, ) 
                content = open(full_path, 'rb').read()

                new_video = Video(slug = video_slug + "edit")
                new_video.video.save(name_video, ContentFile(content))
                new_video.save()

                os.remove(full_path)
            
        except Exception as e:
            transaction.rollback()
            raise APIException(str(e))      
        
        return Response({"edit":True}, status=status.HTTP_200_OK)
    
    def download_video(self, request):
        video_orginal = self.get_object()
        print(video_orginal.video.name)
