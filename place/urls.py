"""URL Configuration

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

from django.urls import path, re_path
from place.views import CountryList, CountryDetail, CountryEdit, CountryCreate, CountryDelete
from place.views import CityList, CityDetail, CityEdit, CityCreate, CityDelete

urlpatterns = [
    path('country/', CountryList.as_view(), name='country'),
    re_path(r'^country/(?P<pk>\d+)/$', CountryDetail.as_view(), name='country'),
    re_path(r'^country/(?P<pk>\d+)/edit$', CountryEdit.as_view(), name='country_edit'),
    re_path(r'^country/(new|add)/edit$', CountryCreate.as_view(), name='country_edit'),
    re_path(r'^country/(?P<pk>\d+)/delete$', CountryDelete.as_view(), name='country_delete'),

    path('city/', CityList.as_view(), name='city'),
    re_path(r'^city/(?P<pk>\d+)/$', CityDetail.as_view(), name='city'),
    re_path(r'^city/(?P<pk>\d+)/edit$', CityEdit.as_view(), name='city_edit'),
    re_path(r'^city/(new|add)/edit$', CityCreate.as_view(), name='city_edit'),
    re_path(r'^city/(?P<pk>\d+)/delete$', CityDelete.as_view(), name='city_delete'),
]

# urlpatterns = [
#     re_path('^person/(?P<person_id>\d+)/', views.person_detail, name='person_detail',)
#
# ]
