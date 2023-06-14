"""
URL configuration for pet_rescue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from pets import views

urlpatterns = [
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls, name="admin"),
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
	path('pets/', views.PetList.as_view(), name='pet-list'),
	path('pets/<int:pk>', views.PetDetail.as_view(), name='pet-detail'),
	path('records/', views.RecordList.as_view(), name='record-list'),
	path('records/<int:pk>', views.RecordDetail.as_view(), name='record-detail'),
	path('records/<int:record_pk>/logs/', views.RecordLogList.as_view(), name='record-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
