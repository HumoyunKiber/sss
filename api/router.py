from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    
    path('posts/',posts,name='posts'),
    path('post/<int:post_id>',post_detail,name='post_detail'),

    path('courses/',courses,name='courses'),
    path('course/<int:course_id>',course_details,name='course_detail'),

    path('members/',members,name='members'),
]
