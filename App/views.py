# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
import json
from  App.utils import *
import codecs

def home(resp):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='sayid', passwd='111', db='test', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from book_list")
    data = dictfetchall(cursor)

    print(data)

    # return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
