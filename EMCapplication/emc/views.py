from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, QueryDict, HttpResponseForbidden
from django.core.context_processors import csrf
 
from forms import ImageUploadForm
from models import ExampleModel
from django.conf import settings


# Dictionary to add objects passed to the through to the HTML
script_args = {}
script_args['theme'] = "a"
    

def home(request):
  return render_to_response("emc/home.html", script_args)

def upload_pic(request):
  
  c = {}
  c.update(csrf(request))  
  script_args['c'] = c
  
  if request.method == 'POST':
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
      m = ExampleModel()
      m.model_pic = form.cleaned_data['image']
      m.save()
      return HttpResponse('image upload success')
    
  return render_to_response("emc/upload_pic.html", c)    
  #return HttpResponseForbidden('allowed only via POST')
  
def photos(request):
  
  photos = ExampleModel.objects.all()
  
  script_args['photos'] = photos
  
  script_args['PATH_TO_FILE'] = settings.PATH_TO_FILE
  
  return render_to_response("emc/photos.html", script_args)    
  
  