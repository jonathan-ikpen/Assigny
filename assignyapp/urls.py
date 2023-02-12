from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('<int:pk>', views.submit, name='submit'),
    path('assignment', views.assignment, name='assignment'),
    path('view_answers', views.view_answers, name='view_answers'),
    path('profile', views.profile, name='profile'),
    path('student_score_table', views.student_scores, name='student_score_table'),
    path('open_answer/<int:pk>/', views.mark_answers, name='mark_answers'),
    path('logout', views.signout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view_assignments', views.view_assignments, name='view_assignments'),
    path('scores', views.student_scores, name='student_scores'),
    path('d/<int:pk>', views.delete, name='delete'),
    path('<int:pk>', views.refresh, name='refresh'),

 ]