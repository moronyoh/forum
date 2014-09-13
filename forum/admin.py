from django.contrib import admin
from forum import models


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Category, CategoryAdmin)


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'category', 'title', 'creation_date',
        'last_modification_date')
admin.site.register(models.Topic, TopicAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'creation_date',
        'last_modification_date')
admin.site.register(models.Comment, CommentAdmin)