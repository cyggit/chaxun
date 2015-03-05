from django.shortcuts import render,render_to_response
import datetime
from chaxun.settings import  BASE_DIR

# Create your views here.

def index(request):
    return  render_to_response('login.html')

def current_time(request):
    now=datetime.datetime.now()
    return render_to_response('login.html',{'current_date':now})

def test(request):
    return  render_to_response('login.html')