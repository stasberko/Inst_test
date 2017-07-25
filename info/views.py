from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.


def post(request):
    form = PostForm(request.POST or None)
    posts = Post.objects.select_related('author').values('text', 'likes', 'author__username').all().order_by('-date')
    if form.is_valid():
        form.save()
    context = {'posts': posts, 'form': form}
    return render(request, 'info/post.html', context=context)
