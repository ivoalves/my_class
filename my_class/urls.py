"""my_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from professor.urls import router


urlpatterns = [
    url(r'^api/token/', obtain_auth_token,name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'layout/$',TemplateView.as_view(template_name='layout.html')),
    url(r'$',TemplateView.as_view(template_name='professor/index.html')),
    url(r'$',TemplateView.as_view(template_name='turma/index.html')),
]
