from django.contrib import admin
from .models import *

admin.site.register(Home)
admin.site.register(Course)
admin.site.register(Member)

class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 1  # Number of extra forms to display

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'info')
    list_filter = ('date',)
    inlines = [PostImagesInline]

admin.site.register(Post, PostAdmin)
admin.site.register(PostImages)
