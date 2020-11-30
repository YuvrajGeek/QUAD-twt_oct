from django.urls import path, include
from . import views
from .views import UserRegisterView
urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.LinksView, name='links'),
    path('conferences/', views.VideoConfView, name='videoconf'),
    path('todo/', views.TodoView, name='todo'),
    path('update_task/<int:pk>', views.updateTask, name='update_task'),
    path('delete_task/<int:pk>', views.deleteTask, name='delete_task'),
    path('delete_link/<int:pk>', views.deleteLink, name='delete_link'),
    path('delete_video_conf/<int:pk>',
         views.deleteVideoConfLink, name='delete_video_conf'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/register/', UserRegisterView.as_view(), name='register'),
    path('accounts/profile/', views.home, name='home'),
    path('questions/', views.MyQuestions, name='questions'),
    path('questions/<int:pk>', views.singlequestionview, name='singlequestion')
]
