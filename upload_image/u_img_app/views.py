from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.renderers import TemplateHTMLRenderer

from .models import User, Image
from .serializers import UserSerializer, ImageSerializer

class UserList(generics.ListCreateAPIView):
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
    

class ImageList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name ='image_list.html'
    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request):
        images = Image.objects.all()
        return Response({'images': images})
    
    
class ImageDetail(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = ImageSerializer
    template_name ='image_detail.html'
    style = {'template_pack': 'rest_framework/vertical/'}
    
    def get_object(self, pk):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response({'serializer': serializer, 'image': image})

    def put(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'image': image})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    