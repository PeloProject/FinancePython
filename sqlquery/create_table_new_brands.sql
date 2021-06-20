-- SQLite
CREATE TABLE new_brands( -- 上場情報
code TEXT, -- 銘柄コード
date TEXT, -- 上場日
PRIMARY KEY(code, date)
);