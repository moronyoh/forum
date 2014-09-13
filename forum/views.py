from django.http.response import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response

from forum import models


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the forum index.")
    
def topic_detail(request, slug):
    topic = models.Topic.get_topic(slug)
    if not topic:
        return HttpResponseNotFound()
    comments = topic.get_comments()
    return render_to_response(
        'topic_detail.html',
        {
            'topic': topic,
            'comments': comments,
        })