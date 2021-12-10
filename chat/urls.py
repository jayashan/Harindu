from django.contrib import admin
from django.urls import path, include
from.import views
from django.conf.urls import url
from django.contrib import admin
from chat.views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    path("",views.home,name='home'),
    url(r'^chat', ChatterBotAppView.as_view(), name='main'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),

]