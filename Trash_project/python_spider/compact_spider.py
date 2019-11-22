from bs4 import BeautifulSoup
import requests
import xlsxwriter
import pandas as pd
xlsx_Path = 'd:\weather_test4.xlsx'
csv_Path = 'd:\csv_4.csv'
workbook = xlsxwriter.Workbook(xlsx_Path)  # 创建一个Excel文件
worksheet = workbook.add_worksheet()
d = {'紫外线':[], '交通':[], '路况':[], '风寒':[], '感冒':[], '空气污染扩散':[], '运动':[]}
namelist = ['紫外线', '交通', '路况', '风寒', '感冒', '空气污染扩散', '运动']
def url_spider(main_url):
    #main_url = "https://tianqi.moji.com/forecast7/china/sichuan"
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
    linklist = linklist[10:len(linklist)-10]
    return linklist
def information_spider(d,url):
    #url = 'https://tianqi.moji.com/weather/china/sichuan/chengdu'
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    res = requests.get(url, headers=hd)
    res.encoding = res.apparent_encoding
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    dt = soup.find('div', class_="live_index_grid").find('ul', class_="clearfix").find_all('dt')
    index = []
    dd = soup.find('div', class_="live_index_grid").find('ul', class_="clearfix").find_all('dd')
    variables = []
    for var in dd:
        variables.append(var.string)
    for inx in dt:
        index.append(inx.string)
    for i in range(len(variables)):
        if variables[i] in d.keys():
            d.get(variables[i]).append(index[i])
        else:
            continue
    return d
def init_writer_xlsx(worksheet):
    namelist = ['紫外线', '交通', '路况', '风寒', '感冒', '空气污染扩散', '运动']
    worksheet.write_row(0,0,data=namelist)
def write_xlsx(worksheet,i,index):
    #worksheet.write_row(i,0,data=variables)
    worksheet.write_row(i,0,data=index)
def write_xlsx_col(worksheet,i,index):
    worksheet.write_column(1,i,data=index)
def xlsx_to_csv_pd(xlsx_Path,csv_Path):
    data_xls = pd.read_excel(xlsx_Path)
    data_xls.to_csv(csv_Path, encoding='utf-8')
if __name__ == '__main__':
    main_url = "https://tianqi.moji.com/forecast7/china/sichuan"
    #init_writer_xlsx(worksheet)
    ls_url = url_spider(main_url)
    shine = 0
    for i in range(5,196):
       d = information_spider(d,ls_url[i])
    data = pd.DataFrame(data=d)
    print(data)
    '''
    for name in namelist:
        write_xlsx_col(worksheet,shine,d[name])
        shine+=1
    '''
    #workbook.close()
    #xlsx_to_csv_pd(xlsx_Path,csv_Path)