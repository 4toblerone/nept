from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Post
from django.shortcuts import  render
from django.template import RequestContext
from forms import UploadForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.


def index(request):
    #add to session starting_from=0
    #return first 5 photos via return_next_posts
    #context = RequestContext(request, )


    if request.method  == 'POST':
        #if user is trying to submit new photo
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid() and request.is_ajax() :
            description = form.cleaned_data['description']
            print description
            #think about resizing to a certain size!
            #it has to be a photo (jpg, npg...) not some other
            #file type
            photo = form.cleaned_data['photo']
            #create and save post, but save with status pending !DONE!///
            #Post(description=description, original_photo=photo, ).save()
            #also return notification regarding the success or failure
            #of post submission
            return HttpResponse(json.dumps({'message':"success"}))#to return clean form
        else:
            #handle badly submitted forms aka
            #someone putted something that isn't a photo
            #when called using ajax it's being recognized as invalid
            #it is required to use FormData as wrapper around form data in html
            #form_object.serialize() works only for form without file fields
            errors =  form.errors
            print errors
            #print "request: ", request
            return HttpResponse(json.dumps({'message':errors}))
    else:
        #if user is first time on the page
        form = UploadForm()
        #get latest Posts (doing that by putting minus sign)
        #negativ index slicing is not allowed while querying in Django
        #take care of case when the number of posts is less then list_end
        #it take cares by it self
        list_end = 3
        posts = Post.objects.filter(status=Post.ACCEPTED).order_by('-pub_date')[:list_end]
        request.session['start_from']=list_end
        #increment start_from at the end

    return render(request, 'photos/index.html', {'form':form, 'posts':posts})


def return_next_posts(request, number_of=5):
    """should return certain batch of photos/posts
        starting_from getting from session
    """
    if request.is_ajax():
        frm = request.session['start_from']
        posts = Post.objects.filter(status=Post.ACCEPTED).order_by('-pub_date')[frm:frm+number_of]
        #'start_from' cannot be larger than number of posts
        #this if/else ensures that
        end = len(posts)<=number_of
        if end :
            request.session['start_from']+=number_of-len(posts)
        else:
            request.session['start_from']+=number_of

        data = {'img_urls': [x.medium_photo.url for x in posts], "end":end}
        result = json.dumps(data)
        print result, "rezultat"
        return HttpResponse(result)

def get_posts(request, num_of_posts=3, order = "-pub_date"):
    frm =  request.session['start_from']
    posts =  posts = Post.objects.filter(status=Post.ACCEPTED).order_by(order)[frm:frm+num_of_posts]
    #this can not be larger then the number of posts
    request.session['start_from']+=num_of_posts
    return posts

def d(request):
    return HttpResponse("D")

def city_parts(request):
    pass