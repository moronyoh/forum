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


def topic_detail(request, slug, page=1):
    page = int(page)
    topic = models.Topic.get_topic(slug)
    if not topic:
        return HttpResponseNotFound()
    else:
        comments = topic.get_comments(page=page)
        if page > 1 and len(comments) == 0:
            comments = topic.get_comments(page=1)
        return render_to_response(
            'topic_detail.html',
            {
                'topic': topic,
                'comments': comments,
            })
