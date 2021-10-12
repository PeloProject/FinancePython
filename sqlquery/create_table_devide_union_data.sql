-- SQLite
CREATE TABLE devide_union_data( -- 廃止情報
code TEXT, -- 銘柄コード
date_of_right_allotment TEXT, -- 権利確定日
before REAL, -- 分割・併合前株数
after REAL, -- 分割・併合後株数
PRIMARY KEY(code, date_of_right_allotment)
);