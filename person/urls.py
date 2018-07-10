from django.urls import path, re_path
from person.views import PersonList, PersonDetail

urlpatterns = [
    path('person/', PersonList.as_view(), name='person'),
    re_path(r'^person/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person'),
]