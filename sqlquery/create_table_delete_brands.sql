-- SQLite
CREATE TABLE delete_brands( -- 廃止情報
code TEXT, -- 銘柄コード
date TEXT, -- 廃止日
PRIMARY KEY(code, date)
);