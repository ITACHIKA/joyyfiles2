import pandas as pd
df=pd.read_excel("g:/1/2/data.xlsx",index_col=False)
print(df)
data=df.values

users=[]
perms=[]

for i in range(len(data)):
    line=data[i]
    username=line[0]
    permission=str(line[1])
    permission=permission.split(",")
    for j in range(len(permission)):
        users.append(username)
        perms.append(permission[j])
print(users)
print(perms)

dict={
    "user":users,
    "permission":perms
}
ndf=pd.DataFrame(dict)
print(ndf)

ndf.to_excel('g:/1/2/userPerm_new.xlsx',index=False)