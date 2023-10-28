import re
from django.shortcuts import render, HttpResponse, redirect
from doubt.models import doubt, Answer
from django.contrib import messages
from django.contrib.auth.models import User


def doubthome(request):
    allPosts = doubt.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = doubt.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = Answer(comment=comment, user=user, post=post)
            comment.save()
            messages.success(
                request, "Your comment has been posted successfully")
        else:
            parent = Answer.objects.get(sno=parentSno)
            comment = Answer(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(
                request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")
