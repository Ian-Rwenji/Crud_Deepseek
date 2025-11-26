from django.urls import path
from .import views


urlpatterns = [
    path('',views.item_list,name='Item_list'),
    path('create/',views.item_create,name='item_create'),
    path('update/<int:pk>/',views.item_update,name='item_update'),
    path('delete/<int:pk>/',views.item_detail,name='item_delete'),


]