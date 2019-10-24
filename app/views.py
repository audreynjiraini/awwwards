from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from .forms import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# Create your views here.

def index(request):
    
    title = 'AudRate'
    projects = Project.objects.all()
    
            
    return render(request, 'index.html', {"projects": projects, "title": title})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any project"
        
        return render(request, 'search.html', {"message": message})
    
    
@login_required(login_url = '/accounts/login/')
def myprofile(request):
    
    user = request.user
    # author = user.profile
    
    projects = Project.objects.filter(author = user.profile)
    title = f'{user.first_name} {user.last_name}'
    
    return render(request, 'myprofile.html', {'projects': projects, 'title': title})


@login_required(login_url = '/accounts/login/')
def update_profile(request):
    
    user = request.user
    title = f'Edit {user.first_name} {user.last_name}\'s Profile'
    
    if request.method == 'POST':
      profile_form = ProfileUpdateForm(request.POST, request.FILES,instance = user.profile)
      contact_form = ContactUpdateForm(request.POST)
      
      if profile_form.is_valid() and contact_form.is_valid():
         profile_form.save()
         
         contact = contact_form.save(commit = False)
         contact.profile = user.profile
         contact.save()
         
         return redirect('myprofile')
     
    else:
        profile_form = ProfileUpdateForm(instance = user.profile)
        contact_form = ContactUpdateForm()

    return render(request, 'update_profile.html', {'title': title, 'profile_form': profile_form, 'contact_form': contact_form})


@login_required(login_url = '/accounts/login/')
def new_project(request):
    
    user = request.user
    title = 'New Project'

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        
        if project_form.is_valid():
            project = project_form.save(commit = False)
            project.author = user.profile
            project.save()
            
            return redirect('index')
    else:
        project_form = ProjectForm()

    return render(request, 'new_project.html', {'title': title, 'project_form': project_form})



def project_view(request,project_id):
    
    project = Project.objects.filter(pk = project_id)
    
    try:
        project = Project.objects.get(pk = project_id)
        
    except Project.DoesNotExist:
        raise Http404("Sorry. The project does not exist.")

    return render(request, 'project_view.html', { 'project': project})


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        
        return Response(serializers.data)
    
    
    def post(self, request, format = None):
        serializers = ProfileSerializer(data = request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)
        
        return Response(serializers.data)
    
    
    def post(self, request, format = None):
        serializers = ProjectSerializer(data = request.data)
        
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)