from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from user_administration.forms import UserForm, CustomUserForm

# Create your views here.


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
