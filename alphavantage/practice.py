import sqlite3

conn = sqlite3.connect('msftData.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS data;
CREATE TABLE "data" ( "date" TEXT, "time" TEXT, "open" INTEGER, "high" INTEGER, "low" INTEGER, "close" INTEGER );
''')
