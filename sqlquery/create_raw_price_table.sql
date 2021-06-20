-- SQLite
CREATE TABLE raw_prices(
code TEXT,
date TEXT,
open REAL,
high REAL,
low REAL,
close REAL,
volume INTEGER,
PRIMARY KEY(code, date)
);