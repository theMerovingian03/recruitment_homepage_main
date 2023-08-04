from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submissions/', views.Submissions.as_view(), name='submissions'),  # Uncomment and add this line
    path('submit_form/', views.submit_form, name='submit_form'),
    path('upload_file/', views.upload_file, name='upload_file'),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
