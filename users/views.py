from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from .serializers import UserRegistrationSerializer

@csrf_exempt
@require_POST
def user_registration(request):
    serializer = UserRegistrationSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_POST
def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Both username and password are required'}, status=400)
