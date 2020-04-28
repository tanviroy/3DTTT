from random import randint
import random
###################################################################  Global

Array=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]





#############################################  DIsplay the Tic Tac Toe Maze

def DisplayMaze():
    print("Top Layer")
    print(Array[1] + '|' + Array[2] + '|' + Array[3])
    print('-+-+-')
    print(Array[4] + '|' + Array[5] + '|' + Array[6])
    print('-+-+-')
    print(Array[7] + '|' + Array[8] + '|' + Array[9])
    print("     ")
    print("=========================================================")
    print("Middle Layer")
    print(Array[10] + '|' + Array[11] + '|' + Array[12])
    print('-+-+-')
    print(Array[13] + '|' + Array[14] + '|' + Array[15])
    print('-+-+-')
    print(Array[16] + '|' + Array[17] + '|' + Array[18])
    print("     ")
    print("=========================================================")
    print("Bottom Layer")
    print(Array[19] + '|' + Array[20] + '|' + Array[21])
    print('-+-+-')
    print(Array[22] + '|' + Array[23] + '|' + Array[24])
    print('-+-+-')
    print(Array[25] + '|' + Array[26] + '|' + Array[27])
    print("     ")
    print("=========================================================")



#########################################################  Move of Player 1

def TurnX(Mode):
    print ("Player 1 Make your move (1-27):")
    k=int(input("Enter position:"))
    InputX(k)
    CheckWinX(Mode)


def InputX(k):
    if Array[k]==" " :
        if k <= 27:
            if k >= 1:
                Array[k]="X"
                DisplayMaze()
            else:
                print ("Invalid Input!")
                a=int(input("Enter Position:"))
                InputX(a)
        else:
            print ("Invalid Input!")
            b=int(input("Enter Position:"))
            InputX(b)
    else:
        print ("Space Taken!")
        c=int(input("Enter Position:"))
        InputX(c)




#########################################################  Move of Player 2

def TurnY(Mode):
    if(Mode==1):
        print ("Player 2 Makes its move (1-27):")
        k=WinningMove()
        if(k==0):
            k=SaveMove()
        InputY(Mode,k)
        CheckWinY(Mode)
    else: # when Mode==2
        print ("Player 2 Make your move (1-27):")
        k=int(input("Enter position:"))
        InputY(Mode,k)
        CheckWinY(Mode)

def InputY(Mode,k):
    if(Mode==1):
        if Array[k]==" " :
            if k <= 27:
                if k >= 1:
                    print("Selected Position: ",k)
                    Array[k]="O"
                    DisplayMaze()
                else:
                    x=randint(1,27)
                    InputY(Mode,x)
            else:
                y=randint(1,27)
                InputY(Mode,y)
        else:
            z=randint(1,27)
            InputY(Mode,z) 
    elif (Mode==2): # when Mode==2
        if Array[k]==" " :
            if k <= 27:
                if k >= 1:
                    Array[k]="O"
                    DisplayMaze()
                else:
                    print ("Invalid Input!")
                    x=int(input("Enter Position:"))
                    InputY(Mode,x)
            else:
                print ("Invalid Input!")
                y=int(input("Enter Position:"))
                InputY(Mode,y)
        else:
            print ("Space Taken!")
            z=int(input("Enter Position:"))
            InputY(Mode,z)
#########################################  To Check Winning Move for Player 2
            
def WinningMove():
    if Array[7]=="O" and Array[8]=="O" and Array[9]==" ":
        return 9
    elif Array[7]=="O" and Array[8]==" " and Array[9]=="O":
        return 8
    elif Array[7]==" " and Array[8]=="O" and Array[9]=="O":
        return 7

    elif Array[4]=="O" and Array[5]=="O" and Array[6]==" ":
        return 6
    elif Array[4]=="O" and Array[5]==" " and Array[6]=="O":
        return 5
    elif Array[4]==" " and Array[5]=="O" and Array[6]=="O":
        return 4
    
    elif Array[1]=="O" and Array[2]=="O" and Array[3]==" ":
        return 3
    elif Array[1]=="O" and Array[2]==" " and Array[3]=="O":
        return 2
    elif Array[1]==" " and Array[2]=="O" and Array[3]=="O":
        return 1
    
    elif Array[7]=="O" and Array[4]=="O" and Array[1]==" ":
        return 1
    elif Array[7]=="O" and Array[4]==" " and Array[1]=="O":
        return 4
    elif Array[7]==" " and Array[4]=="O" and Array[1]=="O":
        return 7
    
    elif Array[8]=="O" and Array[5]=="O" and Array[2]==" ":
        return 2
    elif Array[8]=="O" and Array[5]==" " and Array[2]=="O":
        return 5
    elif Array[8]==" " and Array[5]=="O" and Array[2]=="O":
        return 8
    
    elif Array[9]=="O" and Array[6]=="O" and Array[3]==" ":
        return 3
    elif Array[9]=="O" and Array[6]==" " and Array[3]=="O":
        return 6
    elif Array[9]==" " and Array[6]=="O" and Array[3]=="O":
        return 9
    
    elif Array[7]=="O" and Array[5]=="O" and Array[3]==" ":
        return 3
    elif Array[7]=="O" and Array[5]==" " and Array[3]=="O":
        return 5
    elif Array[7]==" " and Array[5]=="O" and Array[3]=="O":
        return 7
    
    elif Array[9]=="O" and Array[5]=="O" and Array[1]==" ":
        return 1
    elif Array[9]=="O" and Array[5]==" " and Array[1]=="O":
        return 5
    elif Array[9]==" " and Array[5]=="O" and Array[1]=="O":
        return 9
    
    elif Array[10]=="O" and Array[11]=="O" and Array[12]==" ":
        return 12
    elif Array[10]=="O" and Array[11]==" " and Array[12]=="O":
        return 11
    elif Array[10]==" " and Array[11]=="O" and Array[12]=="O":
        return 10
    
    elif Array[13]=="O" and Array[14]=="O" and Array[15]==" ":
        return 15
    elif Array[13]=="O" and Array[14]==" " and Array[15]=="O":
        return 14
    elif Array[13]==" " and Array[14]=="O" and Array[15]=="O":
        return 13
    
    elif Array[16]=="O" and Array[17]=="O" and Array[18]==" ":
        return 18
    elif Array[16]=="O" and Array[17]==" " and Array[18]=="O":
        return 17
    elif Array[16]==" " and Array[17]=="O" and Array[18]=="O":
        return 16
    
    elif Array[10]=="O" and Array[13]=="O" and Array[16]==" ":
        return 16
    elif Array[10]=="O" and Array[13]==" " and Array[16]=="O":
        return 13
    elif Array[10]==" " and Array[13]=="O" and Array[16]=="O":
        return 10
    
    elif Array[11]=="O" and Array[14]=="O" and Array[17]==" ":
        return 17
    elif Array[11]=="O" and Array[14]==" " and Array[17]=="O":
        return 14
    elif Array[11]==" " and Array[14]=="O" and Array[17]=="O":
        return 11
    
    elif Array[12]=="O" and Array[15]=="O" and Array[18]==" ":
        return 18
    elif Array[12]=="O" and Array[15]==" " and Array[18]=="O":
        return 15
    elif Array[12]==" " and Array[15]=="O" and Array[18]=="O":
        return 12
    
    elif Array[10]=="O" and Array[14]=="O" and Array[18]==" ":
        return 18
    elif Array[10]=="O" and Array[14]==" " and Array[18]=="O":
        return 14
    elif Array[10]==" " and Array[14]=="O" and Array[18]=="O":
        return 10
    
    elif Array[12]=="O" and Array[14]=="O" and Array[16]==" ":
        return 16
    elif Array[12]=="O" and Array[14]==" " and Array[16]=="O":
        return 14
    elif Array[12]==" " and Array[14]=="O" and Array[16]=="O":
        return 12
    
    elif Array[19]=="O" and Array[20]=="O" and Array[21]==" ":
        return 21
    elif Array[19]=="O" and Array[20]==" " and Array[21]=="O":
        return 20
    elif Array[19]==" " and Array[20]=="O" and Array[21]=="O":
        return 19
    
    elif Array[22]=="O" and Array[23]=="O" and Array[24]==" ":
        return 24
    elif Array[22]=="O" and Array[23]==" " and Array[24]=="O":
        return 23
    elif Array[22]==" " and Array[23]=="O" and Array[24]=="O":
        return 22
    
    elif Array[25]=="O" and Array[26]=="O" and Array[27]==" ":
        return 27
    elif Array[25]=="O" and Array[26]==" " and Array[27]=="O":
        return 26
    elif Array[25]==" " and Array[26]=="O" and Array[27]=="O":
        return 25
    
    elif Array[19]=="O" and Array[22]=="O" and Array[25]==" ":
        return 25
    elif Array[19]=="O" and Array[22]==" " and Array[25]=="O":
        return 22
    elif Array[19]==" " and Array[22]=="O" and Array[25]=="O":
        return 19
    
    elif Array[20]=="O" and Array[23]=="O" and Array[26]==" ":
        return 26
    elif Array[20]=="O" and Array[23]==" " and Array[26]=="O":
        return 23
    elif Array[20]==" " and Array[23]=="O" and Array[26]=="O":
        return 20
    
    elif Array[21]=="O" and Array[24]=="O" and Array[27]==" ":
        return 27
    elif Array[21]=="O" and Array[24]==" " and Array[27]=="O":
        return 24
    elif Array[21]==" " and Array[24]=="O" and Array[27]=="O":
        return 21
    
    elif Array[19]=="O" and Array[23]=="O" and Array[27]==" ":
        return 27
    elif Array[19]=="O" and Array[23]==" " and Array[27]=="O":
        return 23
    elif Array[19]==" " and Array[23]=="O" and Array[27]=="O":
        return 19
    
    elif Array[21]=="O" and Array[23]=="O" and Array[25]==" ":
        return 25
    elif Array[21]=="O" and Array[23]==" " and Array[25]=="O":
        return 23
    elif Array[21]==" " and Array[23]=="O" and Array[25]=="O":
        return 21
    
    elif Array[1]=="O" and Array[10]=="O" and Array[19]==" ":
        return 19
    elif Array[1]=="O" and Array[10]==" " and Array[19]=="O":
        return 10
    elif Array[1]==" " and Array[10]=="O" and Array[19]=="O":
        return 1
    
    elif Array[2]=="O" and Array[11]=="O" and Array[20]==" ":
        return 20
    elif Array[2]=="O" and Array[11]==" " and Array[20]=="O":
        return 11
    elif Array[2]==" " and Array[11]=="O" and Array[20]=="O":
        return 2
    
    elif Array[3]=="O" and Array[12]=="O" and Array[21]==" ":
        return 21
    elif Array[3]=="O" and Array[12]==" " and Array[21]=="O":
        return 12
    elif Array[3]==" " and Array[12]=="O" and Array[21]=="O":
        return 3
    
    elif Array[4]=="O" and Array[13]=="O" and Array[22]==" ":
        return 22
    elif Array[4]=="O" and Array[13]==" " and Array[22]=="O":
        return 13
    elif Array[4]==" " and Array[13]=="O" and Array[22]=="O":
        return 4
    
    elif Array[5]=="O" and Array[14]=="O" and Array[23]==" ":
        return 23
    elif Array[5]=="O" and Array[14]==" " and Array[23]=="O":
        return 14
    elif Array[5]==" " and Array[14]=="O" and Array[23]=="O":
        return 5
    
    elif Array[6]=="O" and Array[15]=="O" and Array[24]==" ":
        return 24
    elif Array[6]=="O" and Array[15]==" " and Array[24]=="O":
        return 15
    elif Array[6]==" " and Array[15]=="O" and Array[24]=="O":
        return 6
    
    elif Array[7]=="O" and Array[16]=="O" and Array[25]==" ":
        return 25
    elif Array[7]=="O" and Array[16]==" " and Array[25]=="O":
        return 16
    elif Array[7]==" " and Array[16]=="O" and Array[25]=="O":
        return 7
    
    elif Array[8]=="O" and Array[17]=="O" and Array[26]==" ":
        return 26
    elif Array[8]=="O" and Array[17]==" " and Array[26]=="O":
        return 17
    elif Array[8]==" " and Array[17]=="O" and Array[26]=="O":
        return 8
    
    elif Array[9]=="O" and Array[18]=="O" and Array[27]==" ":
        return 27
    elif Array[9]=="O" and Array[18]==" " and Array[27]=="O":
        return 18
    elif Array[9]==" " and Array[18]=="O" and Array[27]=="O":
        return 9
    
    elif Array[1]=="O" and Array[13]=="O" and Array[25]==" ":
        return 25
    elif Array[1]=="O" and Array[13]==" " and Array[25]=="O":
        return 13
    elif Array[1]==" " and Array[13]=="O" and Array[25]=="O":
        return 1
    
    elif Array[7]=="O" and Array[13]=="O" and Array[19]==" ":
        return 19
    elif Array[7]=="O" and Array[13]==" " and Array[19]=="O":
        return 13
    elif Array[7]==" " and Array[13]=="O" and Array[19]=="O":
        return 7
    
    elif Array[1]=="O" and Array[11]=="O" and Array[21]==" ":
        return 21
    elif Array[1]=="O" and Array[11]==" " and Array[21]=="O":
        return 11
    elif Array[1]==" " and Array[11]=="O" and Array[21]=="O":
        return 1
    
    elif Array[3]=="O" and Array[11]=="O" and Array[19]==" ":
        return 19
    elif Array[3]=="O" and Array[11]==" " and Array[19]=="O":
        return 11
    elif Array[3]==" " and Array[11]=="O" and Array[19]=="O":
        return 3
    
    elif Array[3]=="O" and Array[15]=="O" and Array[27]==" ":
        return 27
    elif Array[3]=="O" and Array[15]==" " and Array[27]=="O":
        return 15
    elif Array[3]==" " and Array[15]=="O" and Array[27]=="O":
        return 3
    
    elif Array[9]=="O" and Array[15]=="O" and Array[21]==" ":
        return 21
    elif Array[9]=="O" and Array[15]==" " and Array[21]=="O":
        return 15
    elif Array[9]==" " and Array[15]=="O" and Array[21]=="O":
        return 9
    
    elif Array[9]=="O" and Array[17]=="O" and Array[25]==" ":
        return 25
    elif Array[9]=="O" and Array[17]==" " and Array[25]=="O":
        return 17
    elif Array[9]==" " and Array[17]=="O" and Array[25]=="O":
        return 9
    
    elif Array[7]=="O" and Array[17]=="O" and Array[27]==" ":
        return 27
    elif Array[7]=="O" and Array[17]==" " and Array[27]=="O":
        return 17
    elif Array[7]==" " and Array[17]=="O" and Array[27]=="O":
        return 7
    
    elif Array[2]=="O" and Array[14]=="O" and Array[26]==" ":
        return 26
    elif Array[2]=="O" and Array[14]==" " and Array[26]=="O":
        return 14
    elif Array[2]==" " and Array[14]=="O" and Array[26]=="O":
        return 2
    
    elif Array[8]=="O" and Array[14]=="O" and Array[20]==" ":
        return 20
    elif Array[8]=="O" and Array[14]==" " and Array[20]=="O":
        return 14
    elif Array[8]==" " and Array[14]=="O" and Array[20]=="O":
        return 8
    
    elif Array[4]=="O" and Array[14]=="O" and Array[24]==" ":
        return 24
    elif Array[4]=="O" and Array[14]==" " and Array[24]=="O":
        return 14
    elif Array[4]==" " and Array[14]=="O" and Array[24]=="O":
        return 4
    
    elif Array[6]=="O" and Array[14]=="O" and Array[22]==" ":
        return 22
    elif Array[6]=="O" and Array[14]==" " and Array[22]=="O":
        return 14
    elif Array[6]==" " and Array[14]=="O" and Array[22]=="O":
        return 6
    
    elif Array[1]=="O" and Array[14]=="O" and Array[27]==" ":
        return 27
    elif Array[1]=="O" and Array[14]==" " and Array[27]=="O":
        return 14
    elif Array[1]==" " and Array[14]=="O" and Array[27]=="O":
        return 1
    
    elif Array[9]=="O" and Array[14]=="O" and Array[19]==" ":
        return 19
    elif Array[9]=="O" and Array[14]==" " and Array[19]=="O":
        return 14
    elif Array[9]==" " and Array[14]=="O" and Array[19]=="O":
        return 9
    
    elif Array[3]=="O" and Array[14]=="O" and Array[25]==" ":
        return 25
    elif Array[3]=="O" and Array[14]==" " and Array[25]=="O":
        return 14
    elif Array[3]==" " and Array[14]=="O" and Array[25]=="O":
        return 3
    
    elif Array[7]=="O" and Array[14]=="O" and Array[21]==" ":
        return 21
    elif Array[7]=="O" and Array[14]==" " and Array[21]=="O":
        return 14
    elif Array[7]==" " and Array[14]=="O" and Array[21]=="O":
        return 7
    
    return 0






##########################################  To Check Saving Move for Player 2

def SaveMove():
    if Array[7]=="X" and Array[8]=="X" and Array[9]==" ":
        return 9
    elif Array[7]=="X" and Array[8]==" " and Array[9]=="X":
        return 8
    elif Array[7]==" " and Array[8]=="X" and Array[9]=="X":
        return 7

    elif Array[4]=="X" and Array[5]=="X" and Array[6]==" ":
        return 6
    elif Array[4]=="X" and Array[5]==" " and Array[6]=="X":
        return 5
    elif Array[4]==" " and Array[5]=="X" and Array[6]=="X":
        return 4
    
    elif Array[1]=="X" and Array[2]=="X" and Array[3]==" ":
        return 3
    elif Array[1]=="X" and Array[2]==" " and Array[3]=="X":
        return 2
    elif Array[1]==" " and Array[2]=="X" and Array[3]=="X":
        return 1
    
    elif Array[7]=="X" and Array[4]=="X" and Array[1]==" ":
        return 1
    elif Array[7]=="X" and Array[4]==" " and Array[1]=="X":
        return 4
    elif Array[7]==" " and Array[4]=="X" and Array[1]=="X":
        return 7
    
    elif Array[8]=="X" and Array[5]=="X" and Array[2]==" ":
        return 2
    elif Array[8]=="X" and Array[5]==" " and Array[2]=="X":
        return 5
    elif Array[8]==" " and Array[5]=="X" and Array[2]=="X":
        return 8
    
    elif Array[9]=="X" and Array[6]=="X" and Array[3]==" ":
        return 3
    elif Array[9]=="X" and Array[6]==" " and Array[3]=="X":
        return 6
    elif Array[9]==" " and Array[6]=="X" and Array[3]=="X":
        return 9
    
    elif Array[7]=="X" and Array[5]=="X" and Array[3]==" ":
        return 3
    elif Array[7]=="X" and Array[5]==" " and Array[3]=="X":
        return 5
    elif Array[7]==" " and Array[5]=="X" and Array[3]=="X":
        return 7
    
    elif Array[9]=="X" and Array[5]=="X" and Array[1]==" ":
        return 1
    elif Array[9]=="X" and Array[5]==" " and Array[1]=="X":
        return 5
    elif Array[9]==" " and Array[5]=="X" and Array[1]=="X":
        return 9
    
    elif Array[10]=="X" and Array[11]=="X" and Array[12]==" ":
        return 12
    elif Array[10]=="X" and Array[11]==" " and Array[12]=="X":
        return 11
    elif Array[10]==" " and Array[11]=="X" and Array[12]=="X":
        return 10
    
    elif Array[13]=="X" and Array[14]=="X" and Array[15]==" ":
        return 15
    elif Array[13]=="X" and Array[14]==" " and Array[15]=="X":
        return 14
    elif Array[13]==" " and Array[14]=="X" and Array[15]=="X":
        return 13
    
    elif Array[16]=="X" and Array[17]=="X" and Array[18]==" ":
        return 18
    elif Array[16]=="X" and Array[17]==" " and Array[18]=="X":
        return 17
    elif Array[16]==" " and Array[17]=="X" and Array[18]=="X":
        return 16
    
    elif Array[10]=="X" and Array[13]=="X" and Array[16]==" ":
        return 16
    elif Array[10]=="X" and Array[13]==" " and Array[16]=="X":
        return 13
    elif Array[10]==" " and Array[13]=="X" and Array[16]=="X":
        return 10
    
    elif Array[11]=="X" and Array[14]=="X" and Array[17]==" ":
        return 17
    elif Array[11]=="X" and Array[14]==" " and Array[17]=="X":
        return 14
    elif Array[11]==" " and Array[14]=="X" and Array[17]=="X":
        return 11
    
    elif Array[12]=="X" and Array[15]=="X" and Array[18]==" ":
        return 18
    elif Array[12]=="X" and Array[15]==" " and Array[18]=="X":
        return 15
    elif Array[12]==" " and Array[15]=="X" and Array[18]=="X":
        return 12
    
    elif Array[10]=="X" and Array[14]=="X" and Array[18]==" ":
        return 18
    elif Array[10]=="X" and Array[14]==" " and Array[18]=="X":
        return 14
    elif Array[10]==" " and Array[14]=="X" and Array[18]=="X":
        return 10
    
    elif Array[12]=="X" and Array[14]=="X" and Array[16]==" ":
        return 16
    elif Array[12]=="X" and Array[14]==" " and Array[16]=="X":
        return 14
    elif Array[12]==" " and Array[14]=="X" and Array[16]=="X":
        return 12
    
    elif Array[19]=="X" and Array[20]=="X" and Array[21]==" ":
        return 21
    elif Array[19]=="X" and Array[20]==" " and Array[21]=="X":
        return 20
    elif Array[19]==" " and Array[20]=="X" and Array[21]=="X":
        return 19
    
    elif Array[22]=="X" and Array[23]=="X" and Array[24]==" ":
        return 24
    elif Array[22]=="X" and Array[23]==" " and Array[24]=="X":
        return 23
    elif Array[22]==" " and Array[23]=="X" and Array[24]=="X":
        return 22
    
    elif Array[25]=="X" and Array[26]=="X" and Array[27]==" ":
        return 27
    elif Array[25]=="X" and Array[26]==" " and Array[27]=="X":
        return 26
    elif Array[25]==" " and Array[26]=="X" and Array[27]=="X":
        return 25
    
    elif Array[19]=="X" and Array[22]=="X" and Array[25]==" ":
        return 25
    elif Array[19]=="X" and Array[22]==" " and Array[25]=="X":
        return 22
    elif Array[19]==" " and Array[22]=="X" and Array[25]=="X":
        return 19
    
    elif Array[20]=="X" and Array[23]=="X" and Array[26]==" ":
        return 26
    elif Array[20]=="X" and Array[23]==" " and Array[26]=="X":
        return 23
    elif Array[20]==" " and Array[23]=="X" and Array[26]=="X":
        return 20
    
    elif Array[21]=="X" and Array[24]=="X" and Array[27]==" ":
        return 27
    elif Array[21]=="X" and Array[24]==" " and Array[27]=="X":
        return 24
    elif Array[21]==" " and Array[24]=="X" and Array[27]=="X":
        return 21
    
    elif Array[19]=="X" and Array[23]=="X" and Array[27]==" ":
        return 27
    elif Array[19]=="X" and Array[23]==" " and Array[27]=="X":
        return 23
    elif Array[19]==" " and Array[23]=="X" and Array[27]=="X":
        return 19
    
    elif Array[21]=="X" and Array[23]=="X" and Array[25]==" ":
        return 25
    elif Array[21]=="X" and Array[23]==" " and Array[25]=="X":
        return 23
    elif Array[21]==" " and Array[23]=="X" and Array[25]=="X":
        return 21
    
    elif Array[1]=="X" and Array[10]=="X" and Array[19]==" ":
        return 19
    elif Array[1]=="X" and Array[10]==" " and Array[19]=="X":
        return 10
    elif Array[1]==" " and Array[10]=="X" and Array[19]=="X":
        return 1
    
    elif Array[2]=="X" and Array[11]=="X" and Array[20]==" ":
        return 20
    elif Array[2]=="X" and Array[11]==" " and Array[20]=="X":
        return 11
    elif Array[2]==" " and Array[11]=="X" and Array[20]=="X":
        return 2
    
    elif Array[3]=="X" and Array[12]=="X" and Array[21]==" ":
        return 21
    elif Array[3]=="X" and Array[12]==" " and Array[21]=="X":
        return 12
    elif Array[3]==" " and Array[12]=="X" and Array[21]=="X":
        return 3
    
    elif Array[4]=="X" and Array[13]=="X" and Array[22]==" ":
        return 22
    elif Array[4]=="X" and Array[13]==" " and Array[22]=="X":
        return 13
    elif Array[4]==" " and Array[13]=="X" and Array[22]=="X":
        return 4
    
    elif Array[5]=="X" and Array[14]=="X" and Array[23]==" ":
        return 23
    elif Array[5]=="X" and Array[14]==" " and Array[23]=="X":
        return 14
    elif Array[5]==" " and Array[14]=="X" and Array[23]=="X":
        return 5
    
    elif Array[6]=="X" and Array[15]=="X" and Array[24]==" ":
        return 24
    elif Array[6]=="X" and Array[15]==" " and Array[24]=="X":
        return 15
    elif Array[6]==" " and Array[15]=="X" and Array[24]=="X":
        return 6
    
    elif Array[7]=="X" and Array[16]=="X" and Array[25]==" ":
        return 25
    elif Array[7]=="X" and Array[16]==" " and Array[25]=="X":
        return 16
    elif Array[7]==" " and Array[16]=="X" and Array[25]=="X":
        return 7
    
    elif Array[8]=="X" and Array[17]=="X" and Array[26]==" ":
        return 26
    elif Array[8]=="X" and Array[17]==" " and Array[26]=="X":
        return 17
    elif Array[8]==" " and Array[17]=="X" and Array[26]=="X":
        return 8
    
    elif Array[9]=="X" and Array[18]=="X" and Array[27]==" ":
        return 27
    elif Array[9]=="X" and Array[18]==" " and Array[27]=="X":
        return 18
    elif Array[9]==" " and Array[18]=="X" and Array[27]=="X":
        return 9
    
    elif Array[1]=="X" and Array[13]=="X" and Array[25]==" ":
        return 25
    elif Array[1]=="X" and Array[13]==" " and Array[25]=="X":
        return 13
    elif Array[1]==" " and Array[13]=="X" and Array[25]=="X":
        return 1
    
    elif Array[7]=="X" and Array[13]=="X" and Array[19]==" ":
        return 19
    elif Array[7]=="X" and Array[13]==" " and Array[19]=="X":
        return 13
    elif Array[7]==" " and Array[13]=="X" and Array[19]=="X":
        return 7
    
    elif Array[1]=="X" and Array[11]=="X" and Array[21]==" ":
        return 21
    elif Array[1]=="X" and Array[11]==" " and Array[21]=="X":
        return 11
    elif Array[1]==" " and Array[11]=="X" and Array[21]=="X":
        return 1
    
    elif Array[3]=="X" and Array[11]=="X" and Array[19]==" ":
        return 19
    elif Array[3]=="X" and Array[11]==" " and Array[19]=="X":
        return 11
    elif Array[3]==" " and Array[11]=="X" and Array[19]=="X":
        return 3
    
    elif Array[3]=="X" and Array[15]=="X" and Array[27]==" ":
        return 27
    elif Array[3]=="X" and Array[15]==" " and Array[27]=="X":
        return 15
    elif Array[3]==" " and Array[15]=="X" and Array[27]=="X":
        return 3
    
    elif Array[9]=="X" and Array[15]=="X" and Array[21]==" ":
        return 21
    elif Array[9]=="X" and Array[15]==" " and Array[21]=="X":
        return 15
    elif Array[9]==" " and Array[15]=="X" and Array[21]=="X":
        return 9
    
    elif Array[9]=="X" and Array[17]=="X" and Array[25]==" ":
        return 25
    elif Array[9]=="X" and Array[17]==" " and Array[25]=="X":
        return 17
    elif Array[9]==" " and Array[17]=="X" and Array[25]=="X":
        return 9
    
    elif Array[7]=="X" and Array[17]=="X" and Array[27]==" ":
        return 27
    elif Array[7]=="X" and Array[17]==" " and Array[27]=="X":
        return 17
    elif Array[7]==" " and Array[17]=="X" and Array[27]=="X":
        return 7
    
    elif Array[2]=="X" and Array[14]=="X" and Array[26]==" ":
        return 26
    elif Array[2]=="X" and Array[14]==" " and Array[26]=="X":
        return 14
    elif Array[2]==" " and Array[14]=="X" and Array[26]=="X":
        return 2
    
    elif Array[8]=="X" and Array[14]=="X" and Array[20]==" ":
        return 20
    elif Array[8]=="X" and Array[14]==" " and Array[20]=="X":
        return 14
    elif Array[8]==" " and Array[14]=="X" and Array[20]=="X":
        return 8
    
    elif Array[4]=="X" and Array[14]=="X" and Array[24]==" ":
        return 24
    elif Array[4]=="X" and Array[14]==" " and Array[24]=="X":
        return 14
    elif Array[4]==" " and Array[14]=="X" and Array[24]=="X":
        return 4
    
    elif Array[6]=="X" and Array[14]=="X" and Array[22]==" ":
        return 22
    elif Array[6]=="X" and Array[14]==" " and Array[22]=="X":
        return 14
    elif Array[6]==" " and Array[14]=="X" and Array[22]=="X":
        return 6
    
    elif Array[1]=="X" and Array[14]=="X" and Array[27]==" ":
        return 27
    elif Array[1]=="X" and Array[14]==" " and Array[27]=="X":
        return 14
    elif Array[1]==" " and Array[14]=="X" and Array[27]=="X":
        return 1
    
    elif Array[9]=="X" and Array[14]=="X" and Array[19]==" ":
        return 19
    elif Array[9]=="X" and Array[14]==" " and Array[19]=="X":
        return 14
    elif Array[9]==" " and Array[14]=="X" and Array[19]=="X":
        return 9
    
    elif Array[3]=="X" and Array[14]=="X" and Array[25]==" ":
        return 25
    elif Array[3]=="X" and Array[14]==" " and Array[25]=="X":
        return 14
    elif Array[3]==" " and Array[14]=="X" and Array[25]=="X":
        return 3
    
    elif Array[7]=="X" and Array[14]=="X" and Array[21]==" ":
        return 21
    elif Array[7]=="X" and Array[14]==" " and Array[21]=="X":
        return 14
    elif Array[7]==" " and Array[14]=="X" and Array[21]=="X":
        return 7
    
    return 0




#############################################  To Check The Win for Player 1
    
def CheckWinX(Mode):
    if Array[7]=="X" and Array[8]=="X" and Array[9]=="X":
        print("Victory: Player 1")  
        
    elif Array[4]=="X" and Array[5]=="X" and Array[6]=="X":
        print("Victory: Player 1")   
        
    elif Array[1]=="X" and Array[2]=="X" and Array[3]=="X":
        print("Victory: Player 1")   
        
    elif Array[7]=="X" and Array[4]=="X" and Array[1]=="X":
        print("Victory: Player 1")  
        
    elif Array[8]=="X" and Array[5]=="X" and Array[2]=="X":
        print("Victory: Player 1")   
        
    elif Array[9]=="X" and Array[6]=="X" and Array[3]=="X":
        print("Victory: Player 1")  
        
    elif Array[7]=="X" and Array[5]=="X" and Array[3]=="X":
        print("Victory: Player 1") 
        
    elif Array[9]=="X" and Array[5]=="X" and Array[1]=="X":
        print("Victory: Player 1")
        
    elif Array[10]=="X" and Array[11]=="X" and Array[12]=="X":
        print("Victory: Player 1")
        
    elif Array[13]=="X" and Array[14]=="X" and Array[15]=="X":
        print("Victory: Player 1")
        
    elif Array[16]=="X" and Array[17]=="X" and Array[18]=="X":
        print("Victory: Player 1")
        
    elif Array[10]=="X" and Array[13]=="X" and Array[16]=="X":
        print("Victory: Player 1")
        
    elif Array[11]=="X" and Array[14]=="X" and Array[17]=="X":
        print("Victory: Player 1")
        
    elif Array[12]=="X" and Array[15]=="X" and Array[18]=="X":
        print("Victory: Player 1")
        
    elif Array[10]=="X" and Array[14]=="X" and Array[18]=="X":
        print("Victory: Player 1")
        
    elif Array[12]=="X" and Array[14]=="X" and Array[16]=="X":
        print("Victory: Player 1")
        
    elif Array[19]=="X" and Array[20]=="X" and Array[21]=="X":
        print("Victory: Player 1")
        
    elif Array[22]=="X" and Array[23]=="X" and Array[24]=="X":
        print("Victory: Player 1")
        
    elif Array[25]=="X" and Array[26]=="X" and Array[27]=="X":
        print("Victory: Player 1")
        
    elif Array[19]=="X" and Array[22]=="X" and Array[25]=="X":
        print("Victory: Player 1")
        
    elif Array[20]=="X" and Array[23]=="X" and Array[26]=="X":
        print("Victory: Player 1")
        
    elif Array[21]=="X" and Array[24]=="X" and Array[27]=="X":
        print("Victory: Player 1")
        
    elif Array[19]=="X" and Array[23]=="X" and Array[27]=="X":
        print("Victory: Player 1")
        
    elif Array[21]=="X" and Array[23]=="X" and Array[25]=="X":
        print("Victory: Player 1")
        
    elif Array[1]=="X" and Array[10]=="X" and Array[19]=="X":
        print("Victory: Player 1")
        
    elif Array[2]=="X" and Array[11]=="X" and Array[20]=="X":
        print("Victory: Player 1")
        
    elif Array[3]=="X" and Array[12]=="X" and Array[21]=="X":
        print("Victory: Player 1")
        
    elif Array[4]=="X" and Array[13]=="X" and Array[22]=="X":
        print("Victory: Player 1")
        
    elif Array[5]=="X" and Array[14]=="X" and Array[23]=="X":
        print("Victory: Player 1")
        
    elif Array[6]=="X" and Array[15]=="X" and Array[24]=="X":
        print("Victory: Player 1")
        
    elif Array[7]=="X" and Array[16]=="X" and Array[25]=="X":
        print("Victory: Player 1")
        
    elif Array[8]=="X" and Array[17]=="X" and Array[26]=="X":
        print("Victory: Player 1")
        
    elif Array[9]=="X" and Array[18]=="X" and Array[27]=="X":
        print("Victory: Player 1")    
        
    elif Array[1]=="X" and Array[13]=="X" and Array[25]=="X":
        print("Victory: Player 1")
        
    elif Array[7]=="X" and Array[13]=="X" and Array[19]=="X":
        print("Victory: Player 1")
        
    elif Array[1]=="X" and Array[11]=="X" and Array[21]=="X":
        print("Victory: Player 1")
        
    elif Array[3]=="X" and Array[11]=="X" and Array[19]=="X":
        print("Victory: Player 1")
        
    elif Array[3]=="X" and Array[15]=="X" and Array[27]=="X":
        print("Victory: Player 1")
        
    elif Array[9]=="X" and Array[15]=="X" and Array[21]=="X":
        print("Victory: Player 1")
        
    elif Array[9]=="X" and Array[17]=="X" and Array[25]=="X":
        print("Victory: Player 1")
        
    elif Array[7]=="X" and Array[17]=="X" and Array[27]=="X":
        print("Victory: Player 1")   
        
    elif Array[2]=="X" and Array[14]=="X" and Array[26]=="X":
        print("Victory: Player 1")
        
    elif Array[8]=="X" and Array[14]=="X" and Array[20]=="X":
        print("Victory: Player 1")
        
    elif Array[4]=="X" and Array[14]=="X" and Array[24]=="X":
        print("Victory: Player 1")
        
    elif Array[6]=="X" and Array[14]=="X" and Array[22]=="X":
        print("Victory: Player 1")
        
    elif Array[1]=="X" and Array[14]=="X" and Array[27]=="X":
        print("Victory: Player 1")
        
    elif Array[9]=="X" and Array[14]=="X" and Array[19]=="X":
        print("Victory: Player 1")
        
    elif Array[3]=="X" and Array[14]=="X" and Array[25]=="X":
        print("Victory: Player 1")
        
    elif Array[7]=="X" and Array[14]=="X" and Array[21]=="X":
        print("Victory: Player 1")
        
    else:
        CheckTieX(Mode)

#############################################  To Check The Tie for Player 1

def CheckTieX(Mode):  
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        TurnY(Mode)
    else:
        print ("Tie: GAME OVER")
        









#############################################  To Check The Win for Player 2
        
def CheckWinY(Mode):
    if Array[7]=="O" and Array[8]=="O" and Array[9]=="O":
        print("Victory: Player 2")  
        
    elif Array[4]=="O" and Array[5]=="O" and Array[6]=="O":
        print("Victory: Player 2")   
        
    elif Array[1]=="O" and Array[2]=="O" and Array[3]=="O":
        print("Victory: Player 2")   
        
    elif Array[7]=="O" and Array[4]=="O" and Array[1]=="O":
        print("Victory: Player 2")  
        
    elif Array[8]=="O" and Array[5]=="O" and Array[2]=="O":
        print("Victory: Player 2")   
        
    elif Array[9]=="O" and Array[6]=="O" and Array[3]=="O":
        print("Victory: Player 2")  
        
    elif Array[7]=="O" and Array[5]=="O" and Array[3]=="O":
        print("Victory: Player 2") 
        
    elif Array[9]=="O" and Array[5]=="O" and Array[1]=="O":
        print("Victory: Player 2")
        
    elif Array[10]=="O" and Array[11]=="O" and Array[12]=="O":
        print("Victory: Player 2")
        
    elif Array[13]=="O" and Array[14]=="O" and Array[15]=="O":
        print("Victory: Player 2")
        
    elif Array[16]=="O" and Array[17]=="O" and Array[18]=="O":
        print("Victory: Player 2")
        
    elif Array[10]=="O" and Array[13]=="O" and Array[16]=="O":
        print("Victory: Player 2")
        
    elif Array[11]=="O" and Array[14]=="O" and Array[17]=="O":
        print("Victory: Player 2")
        
    elif Array[12]=="O" and Array[15]=="O" and Array[18]=="O":
        print("Victory: Player 2")
        
    elif Array[10]=="O" and Array[14]=="O" and Array[18]=="O":
        print("Victory: Player 2")
        
    elif Array[12]=="O" and Array[14]=="O" and Array[16]=="O":
        print("Victory: Player 2")
        
    elif Array[19]=="O" and Array[20]=="O" and Array[21]=="O":
        print("Victory: Player 2")
        
    elif Array[22]=="O" and Array[23]=="O" and Array[24]=="O":
        print("Victory: Player 2")
        
    elif Array[25]=="O" and Array[26]=="O" and Array[27]=="O":
        print("Victory: Player 2")
        
    elif Array[19]=="O" and Array[22]=="O" and Array[25]=="O":
        print("Victory: Player 2")
        
    elif Array[20]=="O" and Array[23]=="O" and Array[26]=="O":
        print("Victory: Player 2")
        
    elif Array[21]=="O" and Array[24]=="O" and Array[27]=="O":
        print("Victory: Player 2")
        
    elif Array[19]=="O" and Array[23]=="O" and Array[27]=="O":
        print("Victory: Player 2")
        
    elif Array[21]=="O" and Array[23]=="O" and Array[25]=="O":
        print("Victory: Player 2")
        
    elif Array[1]=="O" and Array[10]=="O" and Array[19]=="O":
        print("Victory: Player 2")
        
    elif Array[2]=="O" and Array[11]=="O" and Array[20]=="O":
        print("Victory: Player 2")
        
    elif Array[3]=="O" and Array[12]=="O" and Array[21]=="O":
        print("Victory: Player 2")
        
    elif Array[4]=="O" and Array[13]=="O" and Array[22]=="O":
        print("Victory: Player 2")
        
    elif Array[5]=="O" and Array[14]=="O" and Array[23]=="O":
        print("Victory: Player 2")
        
    elif Array[6]=="O" and Array[15]=="O" and Array[24]=="O":
        print("Victory: Player 2")
        
    elif Array[7]=="O" and Array[16]=="O" and Array[25]=="O":
        print("Victory: Player 2")
        
    elif Array[8]=="O" and Array[17]=="O" and Array[26]=="O":
        print("Victory: Player 2")
        
    elif Array[9]=="O" and Array[18]=="O" and Array[27]=="O":
        print("Victory: Player 2")    
        
    elif Array[1]=="O" and Array[13]=="O" and Array[25]=="O":
        print("Victory: Player 2")
        
    elif Array[7]=="O" and Array[13]=="O" and Array[19]=="O":
        print("Victory: Player 2")
        
    elif Array[1]=="O" and Array[11]=="O" and Array[21]=="O":
        print("Victory: Player 2")
        
    elif Array[3]=="O" and Array[11]=="O" and Array[19]=="O":
        print("Victory: Player 2")
        
    elif Array[3]=="O" and Array[15]=="O" and Array[27]=="O":
        print("Victory: Player 2")
        
    elif Array[9]=="O" and Array[15]=="O" and Array[21]=="O":
        print("Victory: Player 2")
        
    elif Array[9]=="O" and Array[17]=="O" and Array[25]=="O":
        print("Victory: Player 2")
        
    elif Array[7]=="O" and Array[17]=="O" and Array[27]=="O":
        print("Victory: Player 2")   
        
    elif Array[2]=="O" and Array[14]=="O" and Array[26]=="O":
        print("Victory: Player 2")
        
    elif Array[8]=="O" and Array[14]=="O" and Array[20]=="O":
        print("Victory: Player 2")
        
    elif Array[4]=="O" and Array[14]=="O" and Array[24]=="O":
        print("Victory: Player 2")
        
    elif Array[6]=="O" and Array[14]=="O" and Array[22]=="O":
        print("Victory: Player 2")
        
    elif Array[1]=="O" and Array[14]=="O" and Array[27]=="O":
        print("Victory: Player 2")
        
    elif Array[9]=="O" and Array[14]=="O" and Array[19]=="O":
        print("Victory: Player 2")
        
    elif Array[3]=="O" and Array[14]=="O" and Array[25]=="O":
        print("Victory: Player 2")
        
    elif Array[7]=="O" and Array[14]=="O" and Array[21]=="O":
        print("Victory: Player 2")
        
    else:
        CheckTieY(Mode)


        
#############################################  To Check The Tie for Player 2

def CheckTieY(Mode):
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        TurnX(Mode)
    else:
        print ("Tie: GAME OVER")
        



################################################  Menu
def menu():
    print("<<<<<  3DTTT >>>>\n\n\n")
    print("... Main Menu ...\n")
    print("1. One Player's Game\n")
    print("2. Two Players' Game\n\n")
    
 ################################################  Menu
def toss(Mode):
    choose=0
    print("Choose H/T\n\n")
    print("1.H\n")
    print("2.T\n")
    print("Winner plays first\n")
    while(choose!=1 and choose!=2):
        choose=int(float(input("Enter your Choice: ")))
    check = random.randint (1,2)
    if check==choose:
        print ("PLAYER GOES FIRST")
        Mode=1
        DisplayMaze()
        TurnX(Mode)
    else:
        print ("COMPUTER GOES FIRST")
        print ("NICE")
        exec(open("old1vComp-mode3.py").read())
            
    return(Mode)    
        

   
################################################  Opening Menu & Game Begins

def Main():
    Mode=0
    menu()    
    while(Mode!=1 and Mode!=2):
        Mode=int(float(input("Enter your Choice: ")))
    if (Mode==1):
        toss(Mode)            
        
    else:
        DisplayMaze()
        TurnX(Mode)
    print("\n\n\n\n")
    


#
#
#========================================================================    

Main()

