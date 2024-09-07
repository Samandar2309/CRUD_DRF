from django.urls import path

from .views import *

urlpatterns = [
    path('/post/', PostView.as_view()),
    path('/post/<int:pk>/', PostDetailView.as_view()),
    path('/category/', CategoryView.as_view()),
    path('/category/<int:pk>/', CategoryDetailView.as_view()),
    path('/post/create/', PostCreateView.as_view()),
    path('/post/<int:pk>/update/', PostUpdateView.as_view()),
    path('/post/<int:pk>/delete/', PostDeleteView.as_view()),
    path('/category/create/', CategoryCreateView.as_view()),
    path('/category/<int:pk>/update/', CategoryUpdateView.as_view()),

]
