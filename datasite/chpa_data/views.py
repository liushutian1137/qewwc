from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import pandas as pd
# Create your views here.

def connect_sql(sql):
    conn = pymysql.connect(host='localhost', user='root', passwd='********', db='douban', charset="utf8",
                           use_unicode="True", port=3306)
    # conn = pymysql.connect(host='49.232.138.111', user='root', passwd='******', db='douban', charset="utf8",
    #                        use_unicode="True", port=3306)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return data


def index(request):
    sql = 'select count(1) from novel_info'
    df = pd.DataFrame(connect_sql(sql))
    return HttpResponse(df.to_html())
