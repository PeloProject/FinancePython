#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyquery import PyQuery
import time
import sqlite3
import logging

# *********************************************************************
# 銘柄を取得
# *********************************************************************
def get_brand(code):
    url = 'https://kabutan.jp/stock/?code={}'.format(code)

    logging.basicConfig(filename='./brand.log', level=logging.DEBUG)
    logging.info('code :' + (str)(code))

    q = PyQuery(url)
    
    print('code :' + (str)(code))

    if len(q.find('.company_block')) == 0:
        return None

    try:
        name = q.find('.company_block h3')[0].text
        q2 = q.find('.si_i1_1 h2').eq(0).clone()
        short_name = q2.remove('span').text()
        market = q.find('.si_i1_1 span')[1].text
        unit = q.find('#kobetsu_left td')[17].text.split()[0]
        sector = q.find('#stockinfo_i2 a')[0].text
        #name = q.find('#kobetsu_right > h4')[0].text
        #short_name = q.find('td.kobetsu_data_table1_meigara').text
        #market = q.fine('td.kobetsu_data_table1meigara + td').text
        #unit_str = q.fine('.stock_st_table:eq(1) > tr:eq(5) >' \
        #                  ' td.tar:eq(0)')[0].text
        #unit = int(unit_str.split()[0].replace(',',''))
        #sector = q.find('.kobetsu_data_table2 a')[0].text

    except ValueError:
            return None

    #return code, name
    return code, name, short_name, market, unit, sector

# *********************************************************************
# 複数銘柄取得処理
# *********************************************************************
def brands_generator(code_range):
    for code in code_range:
        brand = get_brand(code)
        if brand:
            yield brand
        time.sleep(2)

# *********************************************************************
# 銘柄をDBに登録
# *********************************************************************
def insert_brands_to_db(db_file_name, code_range):
    conn = sqlite3.connect(db_file_name)
    with conn:
        sql = 'INSERT INTO brands(code, name, short_name, market, unit, sector) ' \
              'VALUES(?,?,?,?,?,?)'
        conn.executemany(sql, brands_generator(code_range))

# 実行
insert_brands_to_db("/home/shinji/DB/kabutandb_test.sqlite3", range(1301,1310))
#get_brand(1301)


