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
from .serializers import VideoSerializer
from .tasks import edit_video



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'], name="edit")
    def add_text(self, request, pk=None):

        video_orginal = self.get_object()

        # try:
        #     with transaction.atomic():

        start_time = time.time()
        edit_video(
            video_orginal.slug,
            video_orginal.video.path,
            request.data['text'],
            int(request.data['x']),
            int(request.data['y']),
            int(request.data['t']),
            int(request.data['d']),
            int(request.data['s'])
        )
        print(time.time() - start_time)
        # edit_video.delay(
        #     video_orginal.slug,
        #     video_orginal.video.path,
        #     request.data['text'],
        #     int(request.data['x']),
        #     int(request.data['y']),
        #     int(request.data['t']),
        #     int(request.data['d']),
        #     int(request.data['s'])
        # )
                
        # transaction.on_commit(lambda: task_execute.delay(job_params))

        # except Exception as e:
        #     raise APIException(str(e))      
        
        return Response({"edit":True}, status=status.HTTP_200_OK)
