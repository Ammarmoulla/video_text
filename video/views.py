from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import Video
from .serializers import VideoSerializer

from .helper import edit_video


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'], name="edit")
    def add_text(self, request, pk=None):

        video_orginal = self.get_object()
        # print(video_orginal.slug + "-edit")
        
        text_clip =  request.data['text']
        x = int(request.data['x'])
        y = int(request.data['y'])
        timestep = int(request.data['t'])
        duration = int(request.data['d'])
        fontsize = int(request.data['s'])

        new_file = edit_video(video_orginal.video.path, text_clip, x, y, timestep, duration, fontsize)
        # new_video = Video()
        # new_video.video = new_file
        # new_video.slug = video_orginal.slug + "-edit"
        # # new_video.save()
        return Response({"edit":True}, status=status.HTTP_200_OK)


# Create your views here.

# class VideoUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         video_serializer = VideoSerializer(data=request.data)
#         if video_serializer.is_valid():
#             video_serializer.save()
#             return Response(video_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class VideoViewSet(viewsets.ViewSet, viewsets.ModelViewSet):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     parser_classes = (MultiPartParser, FormParser)

    # def get_queryset(self):
    #     slug = self.request.data['slug']
    #     return Video.objects.filter(slug=slug)
        
    # def create(self, request):
    #     video_serializer = VideoSerializer(data=request.data)
    #     if video_serializer.is_valid():
    #         video_serializer.save()
    #         return Response(video_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        