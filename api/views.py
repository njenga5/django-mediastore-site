from django.utils import timezone
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from commonops.models import CustomUser as User
from dashboard import models
from . import serializers


class UserView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(email=request.GET.get('email'))
            if not check_password(request.GET.get('password', ''), user.password):
                raise User.DoesNotExist
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        token = request.data.pop('token', None)
        if not token or request.GET.get('token', '') != token or len(request.GET.get("token", '')) != 20:
            return Response({'error':'forbidden'}, status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            user = User.objects.get(email=request.GET.get('email'))
            if not check_password(request.GET.get('password', ''), user.password):
                raise User.DoesNotExist
            serializer = serializers.UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {**serializer.data}
                data['password'] = binascii.unhexlify(data['password'].encode()).decode()
                return Response(data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        

class PhotosView(ListCreateAPIView):
    serializer_class = serializers.PhotoSerializer
    def get_queryset(self):
        queryset = models.Photo.objects.filter(user__email=self.kwargs.get('email')).order_by("-upload_date")
        return queryset



class VideosView(ListCreateAPIView):
    serializer_class = serializers.VideoSerializer
    def get_queryset(self):
        queryset = models.Video.objects.filter(user__email=self.kwargs.get('email')).order_by("-upload_date")
        return queryset
    


class MusicsView(ListCreateAPIView):
    serializer_class = serializers.MusicSerializer
    def get_queryset(self):
        queryset = models.Music.objects.filter(user__email=self.kwargs.get('email')).order_by("-upload_date")
        return queryset

        
class SinglePhotoView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PhotoSerializer
    def get_queryset(self):
        queryset = models.Photo.objects.filter(user__email=self.request.GET.get('email'))
        return queryset
