from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('classrooms/create/', views.classroom_create, name='classroom_create'),
    path('classrooms/<int:pk>/edit/', views.classroom_edit, name='classroom_edit'),
    path('classrooms/<int:pk>/delete/', views.classroom_delete, name='classroom_delete'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/create/', views.grade_create, name='grade_create'),
    path('grades/<int:pk>/edit/', views.grade_edit, name='grade_edit'),
    path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
