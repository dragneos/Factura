#-*- encoding: utf -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from itertools import chain

from django.template import RequestContext
from datetime import datetime ,timedelta
from django.db import connection
from django.contrib.auth.models import User

from django.contrib.auth import login , logout , authenticate
from django.http import HttpResponseRedirect

# Create your views here.

