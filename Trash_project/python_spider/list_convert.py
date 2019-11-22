import pandas as pd
import  numpy as np
data = pd.read_csv(r'E:\Trash_project\data\weather.csv')
data_wind = data['风寒'].replace('无需防护','normal').replace('冷','cold').replace('凉','cool').tolist()
data_sun = data['紫外线'].replace('最弱','very_low').replace('弱','low').replace('中等','medium').replace('强','high').tolist()
data_transportation = data['交通'].replace('较好','good').replace('良好','great').tolist()
data_road = data['路况'].replace('干燥','dry').replace('潮湿','misty').tolist()
data_cold = data['感冒'].replace('较易发','possible').replace('易发','usually').replace('极易发','extremely').tolist()
data_air = data['空气污染扩散'].replace('良','good').replace('中','medium').tolist()
data_res = data['运动'].replace('适宜','yes').replace('不适宜','no').replace('较适宜','both').tolist()
#data_id = data['RID'].tolist()
d = {'风寒':data_wind,'空气':data_air,'感冒':data_cold,'路况':data_road,'紫外线':data_sun,'交通':data_transportation,'出行':data_res}
data_new = pd.DataFrame(d)
#print(np.array([data_id,data_wind,data_air,data_cold,data_road,data_sun,data_transportation,data_res]))
data_new.to_csv('E:\Trash_project\data\weather_pd.csv',sep=',')
'''
for i in list_wind:
    if(i=='无需防护'):
        i='normal'
    elif(i=='冷'or i=='凉'):
        i='cold'
'''
#print(data_wind)