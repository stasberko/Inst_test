from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post, name='post')
    #url(r'^(?P<post>/d*)/', views.post, name='post')
]