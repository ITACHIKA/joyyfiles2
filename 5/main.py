import pandas as pd
import json
import requests

df=pd.read_excel("G:/joyy2/joyy2/5/data.xlsx")

param_data=df['a.params'].values
print(param_data)
for text in param_data:
    jsString=json.loads(text,strict=False)
    fileUrl=jsString["file_url"]
    fileContent=requests.get(fileUrl).content
    fileName=fileUrl.split('/')[-1]
    print(fileName)
    with open(fileName,"wb") as file:
        file.write(fileContent)