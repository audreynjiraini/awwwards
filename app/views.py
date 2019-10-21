from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView


# Create your views here.

def index(request):
    
    title = 'AudRate'
    projects = Project.objects.all()
            
    return render(request, 'index.html', {'title': title, 'projects': projects})



def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        
        return render(request, 'search.html', {"message": message})