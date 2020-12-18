from django.shortcuts import render
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


# Index render
def index(request):
    context = {
        'data': 'testttttttttt',
    }
    return render(request, 'myapi/index.html', context)
