from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'apis', views.VideoViewSet)

urlpatterns = [
    
    # path('upload/', views.VideoUploadView.as_view(), name="upload_video"),
] 

urlpatterns += router.urls
