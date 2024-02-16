from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('create/',views.create,name='create'),
    path('delete/<slug:post_slug>/',views.delete,name='delete'),
    path('update/<slug:edit_slug>',views.update_post,name='update')
]