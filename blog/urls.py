from django.conf.urls import url
from django.urls import path, include
from blog import views

urlpatterns = [
    path('index/', views.index),
    url(r'^article/(?P<id>[0-9]+)$', views.article),
    path('commit-comment/', views.commitComment),
]
