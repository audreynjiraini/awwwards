from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from .forms import *


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
    
    
@login_required(login_url = '/accounts/login/')
def myprofile(request):
    
    current_user = request.user
    author = current_user
    
    projects = Project.objects.filter(author)
    title = f'{current_user.first_name} {current_user.last_name}'
    
    return render(request, 'myprofile.html',{'projects': projects, 'title': title})


@login_required(login_url = '/accounts/login/')
def update_profile(request):
    
    current_user = request.user
    title = f'Edit {current_user.first_name} {current_user.last_name}\'s Profile'
    
    if request.method == 'POST':
      profile_form = ProfileUpdateForm(request.POST, request.FILES,instance = current_user.profile)
      contact_form = ContactUpdateForm(request.POST)
      
      if profile_form.is_valid() and contact_form.is_valid():
         profile_form.save()
         
         contact = contact_form.save(commit = False)
         contact.profile = current_user.profile
         contact.save()
         
         return redirect('myprofile')
     
    else:
        profile_form = ProfileUpdateForm(instance = current_user.profile)
        contact_form = ContactUpdateForm()

    return render(request, 'update_profile.html', {'title': title, 'profile_form': profile_form, 'contact_form': contact_form})


@login_required(login_url = '/accounts/login/')
def new_project(request):
    
    current_user = request.user
    title = 'New Project'

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        
        if project_form.is_valid():
            project = project_form.save(commit = False)
            project.author = current_user.profile
            project.save()
            
            return redirect('index')
    else:
        project_form = ProjectForm()

    return render(request, 'new_project.html', {'title': title, 'project_form': project_form})


@login_required(login_url = '/accounts/login/')
def project_view(request, id):
    
    current_user = request.user
    project = Project.objects.get(pk = id)
    title = f'{project.title} by {project.author.user.first_name}'

    return render(request, 'project_view.html', {'title': title, 'project': project})
