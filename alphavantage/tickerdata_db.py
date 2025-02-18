import requests
import json
import sqlite3
from vars import key,months,ticker,timeinterval

print(ticker+'Data.sqlite')
conn = sqlite3.connect(ticker+'Data.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS data;
CREATE TABLE "data" ( "date" TEXT, "time" TEXT, "open" INTEGER, "high" INTEGER, "low" INTEGER, "close" INTEGER, "wl" INTEGER );
''')


for month in months:
    month = str(month)
    if len(month)<2:
        month = '0'+month
    if int(month) > 7:
        year = '2023'
    else:
        year = '2024'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ticker+'&interval='+timeinterval+'&month='+year+'-'+month+'&outputsize=full&datatype=json&apikey='+key
    r = requests.get(url)
    data = r.text
    data = json.loads(data)
    data = data['Time Series ('+timeinterval+')']
    times = list(data)

    for time in times:
        stats = data[time]
        stats = list(stats.values())
        date_pieces = time.split()
        date = date_pieces[0]
        time = date_pieces[1]
        if stats[3] > stats[0]:
            wl = 1
        elif stats[3] == stats[0]:
            wl = 0
        else:
            wl = -1
        cur.execute('INSERT INTO data (date, time, open, high, low, close, wl ) VALUES (?, ?, ?, ?, ?, ?, ?)',(date, time, stats[0], stats[1],stats[2],stats[3], wl ) )

    conn.commit()
    print('commited:',year,month)




print('\n\ndone\n\n')