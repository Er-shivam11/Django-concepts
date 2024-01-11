from rest_framework import generics
from rest_framework.views import APIView 
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Book
from django.shortcuts import render
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