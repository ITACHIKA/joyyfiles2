import pandas as pd
import json
import numpy as np
df=pd.read_csv("G:/1/3/data.csv")

print(df["a.params"])

df["a.id"]=df["a.id"].astype(str)
df=df.drop("a.client_ip",axis=1)
df=df.drop("a.user_agent",axis=1)
df=df.drop("a.extra",axis=1)
#df=df.drop("a.create_time",axis=1)
df=df.drop("a.rdeleted",axis=1)
df=df.drop("a.rversion",axis=1)
df=df.drop("a.type",axis=1)

data=df.values

splitDat=[]

for i in range (len(data)):
    print(data[i])
    jsonRaw=data[i][4]
    jsonRaw=jsonRaw.replace("\r\n","")
    jsonRaw=jsonRaw.replace("\n","")
    jsonRaw=jsonRaw.replace("\r","")
    jsonRaw=jsonRaw.replace("\n\r","")
    jsonRaw=jsonRaw.replace("\t","")
    js=json.loads(jsonRaw)
    sortedJs=sorted(js.items()) #sorted for iteration
    curLineDat=[]
    for eachKey in sortedJs:
        if(eachKey[0]=='php_raw_input'):
            continue
        if(eachKey[0]=="request"):
            sortedEachKey=sorted(eachKey[1].items())
            for eachKeyInRequests in sortedEachKey:
                #print(eachKeyInRequests)
                key=eachKeyInRequests[0]
                value=str(eachKeyInRequests[1]).replace("\r\n",",")
                curLineDat.append([key,value])
        else:
            #print(eachKey)
            key=eachKey[0]
            try:
                value=str(eachKey[1]).replace("\r\n",",")
            except AttributeError:
                None
            curLineDat.append([key,value])
    splitDat.append(curLineDat)

#print(splitDat)

data=data.tolist()

for i in range(len(data)):
    data[i].pop(4)
    for j in range (len(splitDat[i])):
        data[i].append(str(splitDat[i][j][0])+":"+str(splitDat[i][j][1]))
# for i in data:
#     print(i)

data=sorted(data,key=lambda x:x[3])

ndf=pd.DataFrame(data)
print(ndf)

with pd.ExcelWriter("result.xlsx",engine="openpyxl") as writer:
    for i,df in ndf.groupby(3):
        print(i)
        print(df)
        df.columns=["a.id","a.operater","a.operater_name","a.route","a.create_time","params","params","params","params","params","params","params","params","params"]
        df.to_excel(writer,sheet_name=i.replace("/",""),index=False)