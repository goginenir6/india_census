from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from urllib import urlencode
import json, hashlib, os, requests, json
import unicodedata
import sys
# import urllib3
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from social_django.utils import load_strategy
import os, shutil
from urllib2 import Request, urlopen
import struct, argparse, io
from io import BytesIO, StringIO
import numpy as np
import pandas as pd



def index(request):
    if request.user.is_authenticated():
        context = RequestContext(request,{'request': request,'user': request.user})
        return render(request, 'home.html', {'context':context})
    else:
        return render(request, 'login.html', {})

@login_required
def home(request):
    print(request.user.is_authenticated())
    data = pd.read_csv("data/india-districts-census-2011.csv")
    # print data
    context = RequestContext(request,{'request': request,'user': request.user, 'data': data})
    return render(request, 'home.html', {'context':context})

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required
def india_census(request):
    if request.user.is_authenticated():
        context = RequestContext(request,{'request': request,'user': request.user})
        return render(request, 'india_census.html', {'context':context})

@login_required
def similar_districts(request):
    if request.user.is_authenticated():
        context = RequestContext(request,{'request': request,'user': request.user})
        return render(request, 'Comparision_states.html', {'context':context})

@login_required
def mobile_penetration(request):
    if request.user.is_authenticated():
        context = RequestContext(request,{'request': request,'user': request.user})
        return render(request, 'mobile_penetration.html', {'context':context})


"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End of views.py file  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5 """
