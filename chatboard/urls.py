from django.urls import path
from . import views


urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('post/<int:pk>/', views.post_list, name='post_list'),
    path('board/new/', views.board_new, name='board_new'),
    path('post/<int:pk>/new', views.post_new, name='post_new')
]