# !/usr/bin/python
# -*- coding: utf-8 -*-


from pyquery import PyQuery
import config
# kabutanのセクターを取得
q = PyQuery('https://kabutan.jp/stock/?code=7203')
#print(q)
sector = q.find('#stockinfo_i2 a')[0].text
print(sector)
print(config.DB_SAVE_DIR)
