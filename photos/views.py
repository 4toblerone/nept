from django.shortcuts import render
from django.http import HttpResponse
from models import Post
# Create your views here.

def index(request):
    #add to session starting_from=0
    #return first 5 photos via return_next_posts
    if request.is_ajax():
        #call return_next_posts
        #get from request  start_from
        #increment from request start_from
        pass
    else:
        if request.method == 'POST':
            #if user is trying to submit new photo
            pass
        else:
            #if user is first time on the page
            request.session['start_from']=0
            #increment start_from at the end

    return HttpResponse("yo")


def return_next_posts(starting_from=0, number_of=5):
    """should return certain batch of photos/posts
        starting_from getting from session?
    """

    posts_list = Post.objects.all().order_by('-pub_date')[starting_from:starting_from+number_of+1]
    return posts_list