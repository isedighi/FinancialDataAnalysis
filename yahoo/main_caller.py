import time
from yahoo.stock_caller import call_stock

while True:
    call_stock('https://finance.yahoo.com/quote/MSFT/')
    #ans = input('Continue? >> ')
    time.sleep(1)

'''
call_stock('https://finance.yahoo.com/quote/NVDA/')


url = 'https://dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')
tags = soup('p')
print(tags)
#vvvv not needed vvvv


#for t in tags:
    #if t == 'title':
        #print(t)



#print(soup.title.string)  # Print the title tag's content
#print(soup.get("title"))

#html = html.unescape(html)
#soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#print(html.unescape(tags))
#for tag in tags:
    #print(tag.get('href', None))


#practice for algorithm maker

#<fin-streamer class="livePrice yf-mgkamr" data-symbol="NVDA" data-testid="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehint="2" data-value="121.935" active=""><span class="e3b14781 e59c8479">122.18</span></fin-streamer>

#url = 'https://finance.yahoo.com/quote/NVDA/'
#html = urllib.request.urlopen(url,context=ctx).read()
#print(html)
#pos1 = html.find('<fin-streamer class="livePrice')
#pos2 = html.find('>',pos1+1)
#priceline = html[pos1:pos2]
#price = re.findall('data-value="([0-9]+)',priceline)


'''
