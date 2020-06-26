from django.shortcuts import render
import requests
import json

# Create your views here.

def login(request):
    return render(request, 'login.html')

def SubmitUser(request):
    Name=request.GET['username']
    Email=request.GET['emailid']
    Password=request.GET['pass']
    print(Email,Password,Name,"this is me")
    url = "http://127.0.0.1:8000/api/login/"

    payload = {"Email":Email,"Password":Password,"Name":Name}
    payload=json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    return render(request,'success.html',{'data':data})
    
