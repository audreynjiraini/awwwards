from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url('^$', views.index, name = 'index'),
    url(r'^search/$', views.search_results, name = 'search_results'),
    url(r'^profile/', views.myprofile, name = 'profile'),
    url(r'^profile/update', views.update_profile, name = 'update_profile'),
    url(r'^project/new', views.new_project, name = 'new_project'),
    # url(r'^project/<int:id>', views.project_view, name = 'project_view'),
    url(r'^project/(?P<id>[0-9]+)/$', views.project_view, name = 'project_view'),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api/profiles/', views.ProfileList.as_view()),
    url(r'^api/projects/', views.ProjectList.as_view()),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)