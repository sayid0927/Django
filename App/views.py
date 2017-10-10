# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import json
from  App.utils import *
import codecs

def home(resp):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='sayid', passwd='111', db='test', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from book_name")
    data = dictfetchall(cursor)
    if len(data) == 0:
        jsons = json.dumps({"res": '00001', "msg": data})
    else:
        jsons = json.dumps({"res": '00000', "msg": data})
    return HttpResponse(jsons, content_type="application/json")

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
