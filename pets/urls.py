from django.urls import path

from . import views

urlpatterns = [
	path('', views.PetList.as_view(), name='pet-list'),
	path('<int:pk>', views.PetDetail.as_view(), name='pet-detail'),
	path('records/', views.RecordList.as_view(), name='record-list'),
	path('records/<int:pk>', views.RecordDetail.as_view(), name='record-detail'),
	path('records/<int:record_pk>/logs/', views.RecordLogList.as_view(), name='record-list'),
]
