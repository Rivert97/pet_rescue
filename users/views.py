from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer

class LoginView(KnoxLoginView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request, format=None):
		serializer = AuthTokenSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		login(request, user)
		return super(LoginView, self).post(request, format=None)

class UserList(generics.ListCreateAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

	def destroy(self, request, *args, **kwargs):
		user = self.get_object()
		user.is_active = False
		user.save()
		return Response(data={'detail': 'Success'})
	
