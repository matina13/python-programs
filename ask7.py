import json
from collections import Counter
with open("ask7.txt") as f:
    d=[]
    for line in f.readlines():
        d.append(json.loads(line))
listkeys=[]
for key in d[0].keys():
    listkeys.append(key)
print("dialekste ena apo ta diathesima kleidia : ",listkeys)
x=input()
for i in range(len(listkeys)):
    if x==listkeys[i]:
        f=str(d[0][x]).isnumeric()
        #print(f)
        v=[]
        for a in range(len(d)):
            v.append(d[a][x])
        if f ==True:
            max=max(v)
            min=min(v)
            print("max is : ", max)
            print("min is : ", min)
            data = Counter(v)
            x=data.most_common(1)[0][1]
            if x>1 :
                print("h dhmofilesterh timh einai: ",data.most_common(1)[0][0])
        else:
            data = Counter(v)
            x=data.most_common(1)[0][1]
            if x>1:
                print("h dhmofilesterh timh einai: ",data.most_common(1)[0][0])
