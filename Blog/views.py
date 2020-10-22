from django.shortcuts import render, HttpResponse ,redirect
from Blog.models import Post,BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras

# Create your views here.
def BlogHome(request):
    allPosts = Post.objects.all()
    #print(allPosts)
    context = {'allPosts':allPosts}
    return render(request,'Blog/bloghome.html',context)
    #return HttpResponse("this is Bloghome")

def BlogPost(request, slug):
    post =  Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    
    #print(comments,replies)
    context = {"post":post, "comments": comments,"user": request.user, 'replyDict':replyDict}

    return render(request,'Blog/blogpost.html', context)
    #return HttpResponse(f'this is blogPost: {slug}')

def postComment(request):
    if request.method =='POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentSno")
        if parentSno =="":

            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent =  BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")