import requests
from bs4 import BeautifulSoup
import datetime
import json
import pyecharts

baseUrl="https://data.cma.cn/dataGis/multiSource/getLiveDataInfo?"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

today=datetime.datetime.now()

n=5

raindat=[]
timedat=[]

for i in range(n,-n,-1):
    for j in range(0,23,1):
        selectDay=today-datetime.timedelta(days=i)
        selectYear=selectDay.date().year
        selectDate=selectDay.date().day
        selectMon=selectDay.date().month

        selectYear=str(selectYear)
        selectDate=str(selectDate).zfill(2)
        selectMon=str(selectMon).zfill(2)
        selectHr=str(j).zfill(2)

        #print(selectYear)
        url=baseUrl+"timeStr="+selectYear+selectMon+selectDate+selectHr+"0000&lat=23.125177&lon=113.28064&needLSB=0&funitemmenuid=1153100505000"
        response=requests.get(url,headers=headers)
        content=response.content
        text=json.loads(content.decode())
        rain1h=text['value']
        #print(rain1h)
        raindat.append(rain1h)
        timedat.append(selectYear+"/"+selectMon+"/"+selectDate+":"+selectHr)

print(raindat)
print(timedat)

dat=zip(timedat,raindat)

# map=pyecharts.charts.Map(pyecharts.options.InitOpts(width='1280px',height='720px'))
# seq=list(zip(["广州市","广州市"],[123,12315]))
# print(seq)
# map.add(series_name="GZ",maptype="广东",data_pair=seq)
# map.set_global_opts(visualmap_opts=pyecharts.options.VisualMapOpts(max_=1000000,min_=0))
# map.render(path="test.html")