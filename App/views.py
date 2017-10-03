from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse


def home(resp):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
