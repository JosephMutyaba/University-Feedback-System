from django.urls import path
from . import views

urlpatterns = [
    path('', views.launch_view, name='launch'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register'),  
    path('feedback_form/', views.feedback_form_view, name='feedback_form'),
    path('display_content/', views.display_content_view, name='display_content'),
    path('display_content/', views.display_content_view, name='display_content'),
    path('edit_feedback/<int:feedback_id>/', views.edit_feedback_view, name='edit_feedback'),
    path('delete_feedback/<int:feedback_id>/', views.delete_feedback_view, name='delete_feedback'),
]
