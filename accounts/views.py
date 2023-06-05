from rest_framework.authtoken.models import Token
from .models import User, Customer, Astrologer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer, CustomerSerializer, AstrologerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AstrologerViewSet(viewsets.ModelViewSet):
    queryset = Astrologer.objects.all()
    serializer_class = AstrologerSerializer
