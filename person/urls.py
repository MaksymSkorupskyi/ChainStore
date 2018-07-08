from django.urls import re_path
from person import views

urlpatterns = [
    re_path('^person/(?P<person_id>\d+)/', views.person_detail, name='person_detail',)

]