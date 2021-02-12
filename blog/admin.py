from django.contrib import admin
from .models import post,addcomment
# Register your models here.
@admin.register(post)

class userpost(admin.ModelAdmin):
	list_display=['Name','title','description']

@admin.register(addcomment)

class commentpost(admin.ModelAdmin):
	list_display=['comment','user','post','timestamp','comment_id']
'''
@admin.register(images)

class imagepost(admin.ModelAdmin):
	list_display=['image']
'''

