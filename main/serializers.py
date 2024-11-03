# main/serializers.py
from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created']
        

class CommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'commenter', 'post', 'comment_content', 'created']  # päivitetty kentät 'user' -> 'commenter', 'content' -> 'comment_content', ja 'created_at' -> 'created'
        read_only_fields = ['commenter', 'created']  # commenter kenttä vain luettavaksi
        
class LikeSerializer(serializers.ModelSerializer):
    liker = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'liker', 'post']  # päivitetty kenttä 'user' -> 'liker'
