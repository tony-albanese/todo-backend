from django.urls import path
from todo import views
urlpatterns = [
    path('todo/', views.TodoList.as_view()),
    path('<int:pk>/', views.TodoDetailView.as_view())
]