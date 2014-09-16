from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete='SET_NULL', null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50)
#     owner = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title[:50])
        super(Post, self).save(*args, **kwargs)

    def get_comments(self, page=1, number_of_comment_per_page=10):
        #         comments = self.comment_set.all()
        #         return comments
        comments = Comment.objects.filter(parent=self)
        return comments[number_of_comment_per_page * (page - 1):number_of_comment_per_page * page]

    def __unicode__(self):
        return self.title


class Topic(Post):
    resolved = models.BooleanField(default=False)

    @classmethod
    def get_topic(cls, slug):
        topic = Topic.objects.filter(slug=slug)
        if len(topic) != 1:
            return None
        else:
            return topic[0]

    @classmethod
    def get_last_topic(cls, number=10):
        if not isinstance(number, int):
            number = 10
        topics = Topic.objects.order_by('creation_date')
        return topics[:number]


class Comment(models.Model):
    parent = models.ForeignKey(Post)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True)
