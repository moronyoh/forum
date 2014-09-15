from django.http.response import HttpResponseNotFound
from django.shortcuts import render_to_response

from forum import models


# Create your views here.
def index(request):
    topics = models.Topic.get_last_topic()
    return render_to_response(
        'topic_list.html',
        {
            'topics': topics,
        })
    
def topic_detail(request, slug):
    topic = models.Topic.get_topic(slug)
    if len(topic) != 1:
        return HttpResponseNotFound()
    topic = topic[0]
    comments = topic.get_comments()
    return render_to_response(
        'topic_detail.html',
        {
            'topic': topic,
            'comments': comments,
        })