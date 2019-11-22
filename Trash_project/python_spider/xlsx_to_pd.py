import pandas as pd
xlsx_Path = 'd:\weather_test4.xlsx'
csv_Path = 'd:\csv_4.csv'
data_xls = pd.read_excel(xlsx_Path)
data_xls.to_csv(csv_Path, encoding='utf-8')