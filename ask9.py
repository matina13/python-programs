max0=0
max1=0
file=open('text.txt','r')
while 1:
    # read by character
    char = file.read(1)         
    if not char:
        break    
    max00=1
    max01=1
    x=ord(char)
    x=bin(x)
    x=[d for d in x]
    c=len(x)
    c=int(c)
    #print(c)
    #print(x)
    for i in range(2,c-2):
        if x[i]==x[i+1] and x[i]=="0":
            max00=max00+1
        if x[i]==x[i+1] and x[i]=="1":
            max01=max01+1
    if max00>max0:
        max0=max00
    if max01>max1:
        max1=max01
print("h megaluterh akolouthia apo sunexomena 0 htan : ", max0)
print("h megaluterh akolouthia apo sunexomena 1 htan : ", max1)
file.close()