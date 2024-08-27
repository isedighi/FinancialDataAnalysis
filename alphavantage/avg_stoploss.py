from vars import ticker
import sqlite3

conn = sqlite3.connect(ticker+'Data.sqlite')
cur = conn.cursor()

cur.execute('SELECT open,low FROM data WHERE wl=1')
data = cur.fetchall()

pchange = list()
for item in data:
    pchange.append((item[1]-item[0])/item[0])

avg = sum(pchange)/len(pchange)
print('Stop Loss:',str(avg * 100)[0:5]+'%')

print('\n\ndone\n')