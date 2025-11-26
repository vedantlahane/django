from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here
# 

def post_details(request,post_id):
    post = get_object_or_404(Post,id=post_id)

    return HttpResponse(f"<h1>{post.title}</h1><p>{post.content}</p>")

