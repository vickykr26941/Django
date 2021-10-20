from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import permissions

# third party import 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .serializers import PostSerializer
from .models import Post 


class TestView(APIView):
    # def get(self,request,*args,**kwargs):
    #     data = {
    #         'name' : 'vicky kumar',
    #         'roll' : '18CS98',
    #         'age' : 25
    #     }
    #     return Response(data)

    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs,many=True)
        return Response(serializer.data)
    

    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# def test_view(request):
#     data = {
#         'name' : 'vicky kumar',
#         'roll' : '18CS98',
#         'age' : 25
#     }
#     return JsonResponse(data)

