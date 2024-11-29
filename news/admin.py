from django.contrib import admin

from news import models


# Register your models here.

@admin.register(models.NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'pub_date', 'content')
    list_filter = ('author', 'pub_date')
    search_fields = ('author', 'content')
