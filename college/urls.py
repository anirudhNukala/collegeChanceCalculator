from django.urls import path

from . import views

urlpatterns = [ 
    path('list', views.list, name='list'),
    path('',views.chance, name='chance'),
    path('details',views.stats, name='stats'),
    path('create', views.create, name='create'),
    path('submit_create_college', views.submit, name='sumbit'),
    path('delete', views.delete, name='delete'),
    path('submitdelete', views.submitdelete, name='submitdelete'),
    path('student', views.student, name='student'),
    path('submit_student', views.submitstudent, name='submitstudent'),
    path('studentlist', views.studentlist, name="studentlist"),
    path('studentdetails', views.studentstats, name="studentstats"),
    path('studentdelete', views.studentdelete, name='studentdelete'),
    path('studentsubmitdelete', views.studentsubmitdelete, name='student.submitdelete'),
    path('checkstatus', views.checkstatus, name='checkstatus'),
    path('collegecolor', views.collegecolor, name='collegecolor'),
    path('studentchance', views.studentchance, name='studenchance'),
    path('colleges/<int:pk>/', views.college_element, name='college-detail'),
    path('colleges', views.college_collection, name='colleges'),
    path('map', views.map, name='map')
    ]
