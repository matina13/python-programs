import numpy as np
import random
player1=0
player2=0
p1tower=1
p1bishop=2
p2queen=3
for i in range(99):
        chessboard=np.zeros((8,8))
        for j in range(1,4):
             x=random.randint(0,7)
             y=random.randint(0,7)
             while chessboard[x,y]!=0:
                 x=random.randint(0,7)
                 y=random.randint(0,7)
             chessboard[x,y] = j
        #make list for each pawn's index 
        tower=np.nonzero(chessboard==1)
        bishop=np.nonzero(chessboard==2)
        queen=np.nonzero(chessboard==3)
        #each pawn's coordinates 
        towerx=int(tower[0])
        towery=int(tower[1])
        bishopx=int(bishop[0])
        bishopy=int(bishop[1])
        queenx=int(queen[0])
        queeny=int(queen[1])
        if towerx==queenx or towery==queeny:
            player1=player1+1
        #https://www.geeksforgeeks.org/check-whether-bishop-can-take-down-pawn-or-not/
        diagonios=(queeny-bishopy==queenx-bishopx) or (-queeny+bishopy==queenx-bishopx)
        if diagonios == True:
             player1=player1+1  
        diagoniosqueen=(towery-queeny==towerx-queenx) or (-towery+queeny==towerx-queenx)
        if towerx==queenx or towery==queeny or diagoniosqueen==True:
            player2=player2+1
        if bishopx==queenx or bishopy==queeny or diagonios==True:
            player2=player2+1
print("player1 score: " , player1)
print("player2 score: " , player2)
    





