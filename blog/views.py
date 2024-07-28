from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Post
from django.urls import reverse


# Create your views here.


def blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, body=content)
            return redirect('blog')

    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog.html', context)


def post(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_detail.title = request.POST['title']
        post_detail.body = request.POST['content']
        post_detail.save()
        return redirect('post', post_id=post_detail.id)

    if request.method == 'DELETE':
        post_detail.delete()
        return JsonResponse({'redirect': reverse('blog')})

    return render(request, 'post.html', {'post': post_detail})
