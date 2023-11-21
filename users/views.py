from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json


def login_page(request):
  return render(request, 'users/login.html')


def login_user(request):
  logout(request)
  resp = {"status":'failed','msg':''}
  username = ''
  password = ''
  if request.POST:
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        resp['status']='success'
      else:
        resp['msg'] = "Incorrect username or password"
    else:
      resp['msg'] = "Incorrect username or password"
  return HttpResponse(json.dumps(resp),content_type='application/json')



def logout_user(request):
  logout(request)
  return redirect('login')



