-- SQLite
CREATE TABLE applied_devide_union_data( -- 廃止情報
code TEXT, -- 銘柄コード
date_of_right_allotment TEXT, -- 権利確定日
PRIMARY KEY(code, date_of_right_allotment)
);