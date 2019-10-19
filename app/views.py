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
    
    context = {
        'title': title,
    }
            
    return render(request, 'index.html', context)



