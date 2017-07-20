from django.contrib import admin
from .models import Post, Comment, Contact, Parallel
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Parallel)