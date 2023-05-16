
from rest_framework import generics, status
from .models import User, Customer, Astrologer
from .serializers import UserSerializer, CustomerSerializer, AstrologerSerializer

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = self.authenticate_user(username, password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'user_id': user.id,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def authenticate_user(self, username, password):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None

class UserViewSet(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AstrologerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Astrologer.objects.all()
    serializer_class = AstrologerSerializer

class AstrologerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Astrologer.objects.all()
    serializer_class = AstrologerSerializer




from django.shortcuts import render
# from .forms import UserForm
# from .models import User
#
# # Create your views here.
# def registerUser(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data['password']
#             user = form.save(commit=False)
#             user.set_password(password)
#             user.role = User.CUSTOMER
#             user.save()
#     else:
#         form = UserForm()
#     context = {
#         'form': form,
#     }
#     return render(request,'accounts/register.html', context)