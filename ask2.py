import random 
tet=[]
steps=0
for i in range(100):
      tet.clear()
      for p in range(9):
        tet.append(0)
      f= True
      while f==True:
            x= random.randint(0, 8)
            kap=random.randint(1,3)
            if  (tet[0]!=0 and tet[1]!=0 and tet[2]!=0):
                if  (tet[0]==tet[1]==tet[2]) or (tet[0]<tet[1]<tet[2]) or (tet[0]>tet[1]>tet[2]):
                   break
            if  (tet[3]!=0 and tet[4]!=0 and tet[5]!=0):
                if  (tet[3]==tet[4]==tet[5]) or (tet[3]<tet[4]<tet[5]) or (tet[3]>tet[4]>tet[5]):
                   break
            if  (tet[6]!=0 and tet[7]!=0 and tet[8]!=0):
                if  (tet[6]==tet[7]==tet[8]) or (tet[6]<tet[7]<tet[8]) or (tet[6]>tet[7]>tet[8]):
                   break
            if  (tet[0]!=0 and tet[3]!=0 and tet[6]!=0):
                if  (tet[0]==tet[3]==tet[6]) or (tet[0]<tet[3]<tet[6]) or (tet[0]>tet[3]>tet[6]):
                    break
            if  (tet[1]!=0 and tet[4]!=0 and tet[7]!=0):
                if  (tet[1]==tet[4]==tet[7]) or (tet[1]<tet[4]<tet[7]) or (tet[1]>tet[4]>tet[7]):                   
                    break
            if  (tet[2]!=0 and tet[5]!=0 and tet[8]!=0):
                if  (tet[2]==tet[5]==tet[8]) or (tet[2]<tet[5]<tet[8]) or (tet[2]>tet[5]>tet[8]):
                    break
            if  (tet[0]!=0 and tet[4]!=0 and tet[8]!=0):
                if  (tet[0]==tet[4]==tet[8]) or (tet[0]<tet[4]<tet[8]) or (tet[0]>tet[4]>tet[8]):
                    break
            if  (tet[6]!=0 and tet[4]!=0 and tet[2]!=0):
                if  (tet[6]==tet[4]==tet[2]) or (tet[6]<tet[4]<tet[2]) or (tet[6]>tet[4]>tet[2]):
                    break
            if tet[x]==0 or kap>tet[x]:
                tet[x]=kap
                if x==1 :
                    steps=steps+1
                elif x==2:
                    steps=steps+1
                else:
                    steps=steps+1

print("avg steps : ",steps/100)
