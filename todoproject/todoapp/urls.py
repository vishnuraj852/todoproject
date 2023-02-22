from . import views

from django.urls import path, include

urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvbhome/', views.TaskListView.as_view(), name='cvbhome'),
    path('cvbdetail/<int:pk>/', views.TaskDetialview.as_view(), name='cvbdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cvbdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cvbdelete'),
]
