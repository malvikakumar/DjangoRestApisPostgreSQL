from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return JsonResponse({'message': 'Success'}, status=status.HTTP_200_OK)
        else:
            messages.info(request, 'invalid username or password')
            return JsonResponse({'messages': 'invalid username or password'}, status=status.HTTP_403_FORBIDDEN)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            print('user created')
            return JsonResponse({'message': 'Success'}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'message': 'Unable to Register'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
