from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.


def post(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        posts = Post.objects.all()
        context = {'posts': posts, 'form': form}
    return render(request, 'info/post.html', context=context)

