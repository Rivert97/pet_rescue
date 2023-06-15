from django.urls import path
from knox import views as knox_views

from . import views

urlpatterns = [
	path('', views.UserList.as_view(), name='user-list'),
	path('<int:pk>', views.UserDetail.as_view(), name='user-detail'),
	path('login/', views.LoginView.as_view(), name='knox-login'),
	path('logout/', knox_views.LogoutView.as_view(), name='knox-logout'),
	path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox-logoutall'),
]
