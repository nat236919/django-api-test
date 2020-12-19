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
    if request.method == 'POST':
        post_data = {
            'username': request.POST.get('usernameInput'),
            'email': request.POST.get('emailInput'),
            'catch_phrase': request.POST.get('catchPhraseInput')
        }
        new_user = User(**post_data)
        new_user.save()

    users = User.objects.all().order_by('id')
    context = {'data': users}
    return render(request, 'myapi/index.html', context)
