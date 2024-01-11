from rest_framework import generics
from rest_framework.views import APIView 
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Book
from django.shortcuts import render
from django.shortcuts import render
import moviepy.editor
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# end points as api/books http://127.0.0.1:8000/api/books/
    

# Update your views.py

from rest_framework_simplejwt.views import TokenObtainPairView

class JWTView(TokenObtainPairView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # Custom logic before or after obtaining the token
        response = super().post(request, *args, **kwargs)
        # Additional data to include in the response
        custom_data = {'message': 'Assume here is a token which you forward as a variable {{token}}'}
        response.data.update(custom_data)
        return response
    
def booklist(request):
    books = Book.objects.all()
    return render(request, 'booKlist.html', {'books': books})



import os
from django.conf import settings
from moviepy.editor import VideoFileClip, concatenate_videoclips
from django.shortcuts import render

def merge_videos(request):
    # Construct the full path to the videos using MEDIA_ROOT
    video_1_path = os.path.join(settings.MEDIA_ROOT, "1.mp4")
    video_2_path = os.path.join(settings.MEDIA_ROOT, "2.mp4")

    # Grabbing the videos from storage
    clip_1 = VideoFileClip(video_1_path)
    clip_2 = VideoFileClip(video_2_path)

    # Concatenate the videos
    merged_video = concatenate_videoclips([clip_1, clip_2])

    # Saving the merged video as output.mp4 in the media folder
    output_path = os.path.join(settings.MEDIA_ROOT, "output.mp4")
    merged_video.write_videofile(output_path, codec='libx264')

    return render(request, 'video_merged.html', {'output_path': output_path})

