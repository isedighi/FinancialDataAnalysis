import requests
import json
from vars import key,months,ticker,timeinterval
import shutil

fhandle = open(ticker+'Data.txt','w')
fhandle.write('{\n')
fhandle.write('    "Time Series ('+timeinterval+')": {\n')


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
    datalist = list()
    line = ''
    for char in data:
        if char == '\n':
            datalist.append(line)
            line = ''
            continue
        line = line + char
    index = 10
    for num in range(index):
        del datalist[0]
    del datalist[-1]
    del datalist[-1]
    if not month == months[-1]:
        datalist[-1] = datalist[-1] + ','
    for line in datalist:
        fhandle.write(line+'\n')
        if month == months[-1]:
            if line == datalist[-1]:
                fhandle.write('    }\n')
                fhandle.write('}')

    print('Writing:',month,year)

source = './'+ticker+'Data.txt'
destination = './'+ticker+'Data.json'
try:
    shutil.move(source,destination)
except:
    pass


print('\n\ndone\n\n')