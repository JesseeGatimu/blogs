from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post
from django.shortcuts import get_object_or_404
from .permissions import IsAuthor

class PostListCreateAPI(APIView):
    def get_permissions(self):
        if self.request.method=="GET":
            return []
        return [IsAuthor()]
        
    def get(self,request):
        posts=Post.objects.all().order_by('-created_at')
        serializer=PostSerializer(posts,many=True)
        return Response({
            "message":"Posts fetched successfully",
            "data":serializer.data
        },status=status.HTTP_200_OK)

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({
                "message":"Post created successfully",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPI(APIView):
    def get_permissions(self):
        if self.request.method=="GET":
            return []
        return [IsAuthor()]
    
    def get(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        serializer=PostSerializer(post)
        return Response({
            "message":"Post fetched successful",
            "data":serializer.data
        },status=status.HTTP_200_OK)

    def put(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        self.check_object_permissions(request,post)
        serializer=PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Post updated successfully",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        self.check_object_permissions(request,post)
        serializer=PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Post updated successfully",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        self.check_object_permissions(request,post)
        post.delete()
        return Response({
            "message":"Post deleted successfully"
        },status=status.HTTP_204_NO_CONTENT)


