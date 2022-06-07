import json
from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Product

def index(request):
  return JsonResponse({"status": "online"})


def products(request):
  return JsonResponse({"all": list(Product.objects.all().values())}, safe=False)


# USER MANAGEMENT
class Users:
  def create(request):
    if request.method == 'POST':
      username = request.POST.get('username', None)
      email = request.POST.get('email', None)
      password = request.POST.get('password', None)
      try:
        user = User.objects.get(username=username)
        return JsonResponse({"status": "failure", "message": "User with this Username already exists."}, safe=False)
      except User.DoesNotExist:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return JsonResponse({"status": "success"}, safe=False)
        else:
          return JsonResponse({"status": "failure"}, safe=False)
    else:
      return JsonResponse({"status": "failure", "message": "Invalid request."}, safe=False)

  def login(request):
    if request.method == 'POST':
      username = request.POST.get('username', None)
      password = request.POST.get('password', None)
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return JsonResponse({"status": "success"}, safe=False)
      else:
        return JsonResponse({"status": "failure", "message": "Invalid username or password."}, safe=False)
    else:
      return JsonResponse({"status": "failure", "message": "Invalid request."}, safe=False)

  def logout(request):
    if request.method == 'POST':
      logout(request)
      return JsonResponse({"status": "success"}, safe=False)
    else:
      return JsonResponse({"status": "failure", "message": "Invalid request."}, safe=False)
  
  def get_user(request):
    if request.method == 'GET':
      user = request.user
      if user.is_authenticated:
        return JsonResponse({"status": "success", "user": user.username}, safe=False)
      else:
        return JsonResponse({"status": "failure", "message": "User is not authenticated."}, safe=False)
    else:
      return JsonResponse({"status": "failure", "message": "Invalid request."}, safe=False)

  def delete(request):
    if request.method == 'POST':
      password = request.POST.get('password', None)
      user = authenticate(request, username=request.user.username, password=password)
      if user is not None:
        user.delete()
        return JsonResponse({"status": "success"}, safe=False)
      else:
        return JsonResponse({"status": "failure", "message": "Invalid password."}, safe=False)
    else:
      return JsonResponse({"status": "failure", "message": "Invalid request."}, safe=False)