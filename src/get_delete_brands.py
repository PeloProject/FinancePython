#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery
import time
import sqlite3
import logging
import datetime


def delete_brands_generator():
    url = 'https://www.jpx.co.jp/listing/stocks/delisted/index.html'
    q = PyQuery(url)
    #print(q)

    for d, i in zip(q.find('tbody > tr:even > td:eq(0)'), q.find('tbody > tr:even > td:eq(2)')):
        date = datetime.datetime.strptime(d.text, '%Y/%m/%d').date()
        #print(i.get('id'))
        #print(date)
        yield (i.text, date)

def insert_delete_brands_to_db(db_file_name):
    conn = sqlite3.connect(db_file_name)
    with conn:
        sql = 'INSERT INTO delete_brands(code,date) VALUES(?,?)'
        conn.executemany(sql, delete_brands_generator())

insert_delete_brands_to_db("/home/shinji/DB/kabutandb_test.sqlite3")