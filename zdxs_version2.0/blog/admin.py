from django.contrib import admin
from blog.models import Blog,BlogComment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    fields = ('title','summury','body')
    list_display=['title','editor','summury']
    search_fields=('title','editor',)
    list_filter=('editor',)

class BlogCommentAdmin(admin.ModelAdmin):
    list_display=['commentator','link']
    list_filter=('link',)
    

admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
