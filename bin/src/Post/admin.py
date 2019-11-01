from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ["created","active"];
    list_display = ["title","user","img","created","active"];
    search_fields = ["title","content"];
    


admin.site.register(Post, PostAdmin)
