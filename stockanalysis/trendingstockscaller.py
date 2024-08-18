from bs4 import BeautifulSoup
import requests
import re


url = 'https://stockanalysis.com/'
print('\n\n')
afterhours = input('Afterhours?\n(True or False)\n>> ')
print('\n\n')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tags = soup.find_all(name='div')
for tag in tags:
    if re.search('Trending',str(tag)):
        extract = tag
        extracts = extract.find_all(name='a')

links = list()
for tag in extracts:
    url = list(tag.attrs.values())[0]
    url = 'https://stockanalysis.com'+str(url)
    url = url.strip()
    links.append(url)


names = list()
prices = list()
volumes = list()
for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all()
    nametag = soup.find_all(name='h1')[0]
    #<h1 class="mb-0 text-2xl font-bold text-default sm:text-[26px]">NVIDIA Corporation (NVDA)</h1>   -   the ticker symbol will always be in this format
    name = str(nametag.text)
    names.append(name)
    if afterhours == True:
        pricetag = soup.find_all(attrs='block text-[1.7rem] font-semibold leading-5 text-faded sm:inline')
        #<div class="block text-[1.7rem] font-semibold leading-5 text-faded sm:inline">97.66</div>   -   the price will always be in this format afterhours
        price = pricetag[0].text
        prices.append(price)
    else:
        pricetag = soup.find_all(attrs="text-4xl font-bold inline-block")
        #<div class="text-4xl font-bold block sm:inline">98.91</div>   -   the price will always be in this format during market hours
        price = pricetag[0].text
        prices.append(price)
    volumetag = soup.find_all(attrs="whitespace-nowrap px-0.5 py-[1px] xs:px-1 sm:py-2")[9]
    volumetag = tags[tags.index(volumetag) + 1]
    volume = volumetag.text
    volumes.append(volume)
    #<td class="whitespace-nowrap px-0.5 py-[1px] text-left text-smaller font-semibold tiny:text-base xs:px-1 sm:py-2 sm:text-right sm:text-small">398,880,731</td>    -    the volume will always be in this format
    #<td class="whitespace-nowrap px-0.5 py-[1px] xs:px-1 sm:py-2">Volume</td>   -   the volume name will always be in this format

for name in names:
    print(name,' Price: ',prices[names.index(name)])
print('\n\n')
for name in names:
    print(name,' Volume: ',volumes[names.index(name)])




print('\n\ndone')