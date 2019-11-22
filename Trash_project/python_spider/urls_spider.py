from bs4 import BeautifulSoup
import requests
main_url = "https://tianqi.moji.com/forecast7/china/sichuan"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
res = requests.get(main_url,headers=headers)
res.encoding = res.apparent_encoding
html = res.text
soup = BeautifulSoup(html,'html.parser')
linklist = []
for x in soup.find_all('a'):
    link = x.get('href')
    if link:
        linklist.append(link)
print(linklist)