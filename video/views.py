from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.exceptions import APIException

from .models import Video
from .serializers import VideoSerializer

from .tasks import task_execute



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'], name="edit")
    def add_text(self, request, pk=None):

        video_orginal = self.get_object()

        try:
            with transaction.atomic():

                job_params = {
                    "video_slug": video_orginal.slug,
                    "video_path": video_orginal.video.path,
                    "text_clip": request.data['text'],
                    "x": int(request.data['x']),
                    "y":  int(request.data['y']),
                    "timestep": int(request.data['t']),
                    "duration": int(request.data['d']),
                    "fontsize": int(request.data['s'])
                }
        
        # task_execute(job_params)
        # task_execute.delay(job_params)
                
                transaction.on_commit(lambda: task_execute.delay(job_params))

        except Exception as e:
            raise APIException(str(e))      
        
        return Response({"edit":True}, status=status.HTTP_200_OK)
