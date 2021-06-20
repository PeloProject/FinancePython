#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery
import time
import sqlite3
import logging
import datetime


def new_brands_generator():

    url = 'http://www.jpx.co.jp/listing/stocks/new/index.html'
    q = PyQuery(url)
    #print(q)


    for d, i in zip(q.find('tbody > tr:even > td:eq(0)'), q.find('tbody > tr:even span')):
        date = datetime.datetime.strptime(d.text, '%Y/%m/%d').date()
        #print(i.get('id'))
        #print(date)
        yield (i.get('id'), date)

def insert_new_brands_to_db(db_file_name):
    conn = sqlite3.connect(db_file_name)
    with conn:
        sql = 'INSERT INTO new_brands(code,date) VALUES(?,?)'
        conn.executemany(sql, new_brands_generator())


insert_new_brands_to_db("/home/shinji/DB/kabutandb_test.sqlite3")