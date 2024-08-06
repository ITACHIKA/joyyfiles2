import requests
from bs4 import BeautifulSoup as bs
import json

bookGroupIDList="https://www.ptpress.com.cn/hotBook/getParentTagIdList"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

groupID=[]

groupIdRaw=requests.get(bookGroupIDList,headers=headers)
groupIdList=json.loads(groupIdRaw.content)
groupIdListData=groupIdList["data"]
print(groupIdListData)
for eachId in groupIdListData:
    parentTagID=eachId["PARENTTAGID"]
    parentTagName=eachId["PARENTTAGNAME"]
    groupID.append([parentTagID,parentTagName])
#print(groupID)

getBookBaseUrl="https://www.ptpress.com.cn/hotBook/getHotBookList?parentTagId="
for eachID in groupID:
    curId=eachID[0]
    trialGet=requests.get(getBookBaseUrl+curId+"&rows=1&page=1",headers=headers)
    print(trialGet.content)
    break