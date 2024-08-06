import pandas as pd

df=pd.read_csv("G:/joyy2/joyy2/6/books_copy.csv",encoding="ANSI")

target=df["bookAuthor"]
cnt=0
for i in target:
    i=str(i)
    if(i.find("]")!=i.rfind("]")):
        print(i)
        cnt+=1
print(cnt)