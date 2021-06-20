#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery
import time
import sqlite3
import logging

# *********************************************************************
# 銘柄を取得
# *********************************************************************
def get_raw_price(code, pageNo):
    logging.basicConfig(filename='./price.log', level=logging.DEBUG)
    logging.info('code :' + (str)(code) + '| page :' + (str)(pageNo))
    
    url = 'https://kabutan.jp/stock/kabuka/?code={}&ashi=day&page={}'.format(code, pageNo)

    q = PyQuery(url)

    print('code :' + (str)(code) + '| page :' + (str)(pageNo))

    #if len(q.find('.stock_kabuka_dwm td')) == 0:
    #    return None

    
    length = len(q.find('.stock_kabuka_dwm td,.stock_kabuka_dwm time'))
    nodes = q.find('.stock_kabuka_dwm td,.stock_kabuka_dwm time')
    for n in range(length):
        checkNum = n % 8
        #print(checkNum)
        
        if checkNum == 0:
            # 日付取得
            date = nodes[n].text
            print(date)
        elif checkNum == 1:
            # 始値取得
            open = nodes[n].text
            print(open)
        elif checkNum == 2:
            # 高値取得
            high = nodes[n].text
            print(high)
        elif checkNum == 3:
            # 安値取得
            low = nodes[n].text
            print(low)
        elif checkNum == 4:
            # 終値取得
            close = nodes[n].text
            print(close)
        #elif checkNum == 5:
            # 前日比取得
        #elif checkNum == 6:
            # 前日比％取得
        elif checkNum == 7:
            # 出来高取得
            volume = nodes[n].text
            print(volume)
            yield code, date, open, high, low, close, volume



# *********************************************************************
# 複数情報取得処理
# *********************************************************************
def raw_prices_generator(code_range):
    for code in code_range:
        for pageNo in range(1,10):
            addParams = get_raw_price(code, pageNo)
            for param in addParams:
                if param:
                    yield param
        time.sleep(2)

# *********************************************************************
# 銘柄をDBに登録
# *********************************************************************
def insert_raw_prices_to_db(db_file_name, code_range):
    conn = sqlite3.connect(db_file_name)
    with conn:
        sql = 'INSERT INTO raw_prices(code, date, open, high, low, close, volume) ' \
              'VALUES(?,?,?,?,?,?,?)'
        conn.executemany(sql, raw_prices_generator(code_range))

# 実行
#params = get_raw_price(1301,1)
#for param in params:
#    print(param)
#raw_prices_generator(range(1301,1301))
insert_raw_prices_to_db("/home/shinji/DB/kabutandb_test.sqlite3", range(1301,1302))