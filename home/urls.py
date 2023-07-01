from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("register", views.register, name='register'),
    path("insertuser", views.insertuser, name='insertuser'),
    path("show", views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('edit/<int:id>', views.edit)
]
