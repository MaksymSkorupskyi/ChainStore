"""ChainStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from ChainStore import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('main/', views.main, name='main'),
    re_path('main/(?P<i>\d+)/(?P<j>\d+)/', views.main),
    re_path('main/(?P<i>\d+)/default/', views.main),
    re_path('main/(?P<i>\d+)/special/', views.main, kwargs={'j': -1}),

    re_path('post/(?P<slug>[\w\-]+)', views.post, name='news_post'),

    # Experiments with person
    path('', include('person.urls')),
    # path('person/', include('person.urls')),
    # re_path(r'^person/(?P<test>\w+)/', include('person.urls')),
    # re_path(r'^person /(?P<pk>\d+)/', include([
    #     path('add',add, name='person_add'),
    #     path('edit',edit),
    #     path('remove', remove )
    # ])),

    path('admin/', admin.site.urls),
]

# handler404 = 'ChainStore.views.http404'
handler404 = views.http404
