from rest_framework import status
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import User, Image, Tier
from .serializers import UserSerializer, ImageSerializer

import logging
import sys
logging.basicConfig(
    level=logging.INFO,
    handlers=[ 
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)])


class UserList(generics.ListCreateAPIView, LoginRequiredMixin):
    serializer_class = UserSerializer
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    

class ImageList(generics.ListCreateAPIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='image_list.html'
    style = {'template_pack': 'rest_framework/vertical/'}
    
    def get(self, request):
        images = Image.objects.all()
        return Response({'images': images})
    
    
class ImageDetail(generics.RetrieveAPIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = ImageSerializer
    template_name ='image_detail.html'
    style = {'template_pack': 'rest_framework/vertical/'}
    
    def get_object(self, request):
        try:
            pk = int(request.data['id_image'])
            image = Image.objects.get(pk=pk)
            return image
        except Image.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        image = self.get_object(request)
        serializer = ImageSerializer(image)
        return Response({'serializer': serializer, 'image': image})

    def post(self, request):
        image = self.get_object(request)
        serializer = ImageSerializer(image, data=request.data)
        
        # create tier for a user who is an owner of an image
        user = User.objects.get(pk=int(request.data['user']))
        tier_list = []
        
         # a link to a thumbnail that is 200 px in height
        thumbnail = Tier.objects.create(height=200, image2=image.id_image) 
        thumbnail.resized = Image.open(image).thumbnail(height=200)   
        # a link to a thumbnail that is 400 px in height
        thumbnail2 = Tier.objects.create(height=400, image2=image.id_image)
        thumbnail2.resized = Image.open(image).thumbnail(height=400)
            
        if user.account_tiers == 'B': # basic account
            tier_list.append(thumbnail)
            
        elif user.account_tiers == 'PR': # premium account
            tier_list.append(thumbnail)
            tier_list.append(thumbnail2)
            
        else: # enterprise account
            tier_list.append(thumbnail)
            tier_list.append(thumbnail2)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'image': image, 'tier_list': tier_list})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        image = self.get_object(request)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    