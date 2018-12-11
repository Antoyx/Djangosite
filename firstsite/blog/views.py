from django.shortcuts import render
#from django.http import HttpResponse
#httpresponse was used for printing text, now we switched to http templates


posts = [
    {
        'author': 'coreyMS',
        'title': 'blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'second poser',
        'title': 'blog Post 2',
        'content': 'FSecond post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})


