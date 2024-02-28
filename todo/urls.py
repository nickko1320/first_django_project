from django.urls import path

from .views import (
    ListTaskAPIView,
    CreateTaskAPIView,
    RetrieveTaskApiView,
    UpdateTaskAPIView,
    DestroyTaskAPIView,
)

urlpatterns =  [
    path('todo_list/', ListTaskAPIView.as_view(), name='todo_list'),
    path('todo/todo_create/', CreateTaskAPIView.as_view(), name='todo_create'),
    path('todo/todo_retrieve/<pk>', RetrieveTaskApiView.as_view(), name='todo_retrieve'),
    path('todo/todo_update/<pk>', UpdateTaskAPIView.as_view(), name='todo_update'),
    path('todo/todo_destroy/<pk>', DestroyTaskAPIView.as_view(), name='todo_destroy'),
]