from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from 

# Create your views here.
@csrf_exempt
def user_creation_view(request):
    if request.method == 'POST':
        print(dir(request), request.body)
        info = json.loads(request.body)
        username = info["username"]
        password = info["password"]
        if User.objects.filter(username=username, password = password).exists():
            pass
        else:
            p = User(username=username)
            p.set_password(password)
            p.save(force_insert=True)
        return HttpResponse("Data Saved")
