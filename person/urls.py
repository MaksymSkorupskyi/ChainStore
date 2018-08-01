from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from person.views import PersonList, PersonDetail, PersonDelete, person_edit

urlpatterns = [
    path('person/', login_required(PersonList.as_view()), name='person'),
    re_path(r'^person/(?P<pk>\d+)/$', login_required(PersonDetail.as_view()), name='person'),
    re_path(r'^person/(?P<pk>\d+|new)/edit$', login_required(person_edit), name='person_edit'),
    re_path(r'^person/(?P<pk>\d+)/delete$', login_required(PersonDelete.as_view()), name='person_delete'),
]

# from django.urls import path, re_path
# from person.views import PersonList, PersonDetail
#
# urlpatterns = [
#     path('person/', PersonList.as_view(), name='person'),
#     re_path(r'^person/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person'),
# ]
