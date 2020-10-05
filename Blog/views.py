from django.shortcuts import render, HttpResponse

# Create your views here.
def BlogHome(request):
    return HttpResponse("this is Bloghome")

def BlogPost(request , slug):
    return HttpResponse(f'this is blogPost: {slug}')