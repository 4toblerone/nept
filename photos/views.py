from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Post
from django.shortcuts import  render
from django.template import RequestContext
from forms import UploadForm

# Create your views here.

def index(request):
    #add to session starting_from=0
    #return first 5 photos via return_next_posts
    #context = RequestContext(request, )
    if request.is_ajax():
        #call return_next_posts
        #get from request  start_from
        #increment from request start_from
        pass
    else:
        if request.method == 'POST':
            #if user is trying to submit new photo
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                description = form.cleaned_data['description']
                #think about resizing to a certain size!
                #it has to be a photo (jpg, npg...) not some other
                #file type
                photo = form.cleaned_data['photo']

                #create and save post, but save with status pending !DONE!///
                Post(description=description, photo=photo).save()
                #also return notification regarding the success or failure
                #of post submission
                return HttpResponseRedirect('')#to return clean form
            else:
                #handle badly submitted forms aka
                #someone putted something that isn't a photo
                return HttpResponseRedirect('')
        else:
            #if user is first time on the page
            form = UploadForm()
            posts = Post.objects.filter(status=Post.ACCEPTED)
            request.session['start_from']=0
            #increment start_from at the end

    return render(request, 'photos/index.html', {'form':form, 'posts':posts})

def d(request):
    return HttpResponse("D")

def return_next_posts(starting_from=0, number_of=5):
    """should return certain batch of photos/posts
        starting_from getting from session?
    """

    posts_list = Post.objects.all().order_by('-pub_date')[starting_from:starting_from+number_of+1]
    return posts_list