from django.urls import path, re_path

from person.views import PersonList, PersonDetail, PersonDelete, person_edit

urlpatterns = [
    path('person/', PersonList.as_view(), name='person'),
    re_path(r'^person/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person'),
    re_path(r'^person/(?P<pk>\d+|new)/edit$', person_edit, name='person_edit'),
    re_path(r'^person/(?P<pk>\d+)/delete$', PersonDelete.as_view(), name='person_delete'),
]

# from django.urls import path, re_path
# from person.views import PersonList, PersonDetail
#
# urlpatterns = [
#     path('person/', PersonList.as_view(), name='person'),
#     re_path(r'^person/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person'),
# ]
