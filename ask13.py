from urllib.request import Request, urlopen
import json
kino = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
kino=urlopen(kino).read()
kino=kino.decode()
kino=json.loads(kino)
kino=kino["last"]
kino=kino['winningNumbers']
kino=kino['list']
print("winning numbers : " , kino)
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=data.decode()
a=json.loads(data)
data=a["randomness"]
num = []
n  = 2
for index in range(0, len(data), n):
    num.append(data[index : index + n])
for i in range(len(num)):
    num[i]=int(num[i],16)
for i in range(len(num)):
    num[i]=num[i]%80
num.sort()
num=list(dict.fromkeys(num))
print("random numbers : ", num)
ran_win=0
for i in range(len(kino)):
    for j in range(len(num)):
        if kino[i]==num[j]:
            ran_win=ran_win+1
print(ran_win,"random numbers were also kino winning numbers")

