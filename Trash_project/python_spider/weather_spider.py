import requests
from bs4 import BeautifulSoup
url = 'https://tianqi.moji.com/weather/china/sichuan/chengdu'
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
res = requests.get(url,headers=hd)
res.encoding = res.apparent_encoding
html = res.text
soup = BeautifulSoup(html,'html.parser')
dt = soup.find('div',class_="live_index_grid").find('ul',class_="clearfix").find_all('dt')
dd = soup.find('div',class_="live_index_grid").find('ul',class_="clearfix").find_all('dd')
variables = []
index = []
for inx in dt:
    index.append(inx.string)
for var in dd:
    variables.append(var.string)
print(variables)
print(index)
