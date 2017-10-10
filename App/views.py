# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from  App.utils import *
import codecs

def home(resp):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='sayid', passwd='111', db='test', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from book_list")
    # re = cursor.fetchall()
    # fields = cursor.description
    data = dictfetchall(cursor)
    # column_list = []
    # for i in fields:
    #     column_list.append(i[0])

    # with codecs.open('json.txt', 'w+',encoding='utf-8') as f:
    #     for row in re: # 一次循环，row代表一行，row以元组的形式显示。
    #         result = {} # 定义Python 字典
    #         result[column_list[0]] = row[0] # 将row中的每个元素，追加到字典中。　
    #         result[column_list[1]] = str(row[1])# Python字段格式 和json字段格式转换
    #         result[column_list[2]] = str(row[2])
    #         # result[column_list[3]] = row[3]
    #         # result[column_list[4]] = str(row[4])
    #         jsondata = json.dumps(result, ensure_ascii=False)  # Python的dict --转换成----> json的object
    #         f.write(jsondata + '\n')# 写入文件
    # f.close()
    resp = {'errorcode': 100, 'detail': 'Get success'}
    # return HttpResponse(json.dumps(resp), content_type="application/json")
    # return HttpResponse(json.dumps(resp,ensure_ascii=False), content_type="application/json")
    print(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
