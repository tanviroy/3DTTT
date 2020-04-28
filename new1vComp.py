from random import randint
import random
###################################################################  Global

Array=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
k = 0 # global k helps store the first move of the player
x = 1 # since the entire game is based on it and what happens after it





#############################################  DIsplay the Tic Tac Toe Maze

def Display():
    print("===========================================================================================================")
    print("                Game                                                Controls")
    print("            ____________                                         ____________ ")
    print("           / "+Array[1]+" / "+Array[2]+" / "+Array[3]+" /|                                       / 1 / 2 / 3 /|")
    print("          /___/___/___/ |                                      /___/___/___/ |")
    print("         / "+Array[4]+" / "+Array[5]+" / "+Array[6]+" /  |                                     / 4 / 5 / 6 /  |")
    print("        /___/___/___/   |                                    /___/___/___/   |")
    print("       / "+Array[7]+" / "+Array[8]+" / "+Array[9]+" /    |                                   / 7 / 8 / 9 /    |")
    print("      /___/___/___/     |                                  /___/___/___/     |")
    print("     |     |______|_____|                                 |     |______|_____|")
    print("     |     / "+Array[10]+" / "+Array[11]+"|/ "+Array[12]+" /|                                 |     / 10/11|/ 12/|")
    print("     |    /___/___|___/ |                                 |    /___/___|___/ |")
    print("     |   / "+Array[13]+" / "+Array[14]+" /|"+Array[15]+" /  |                                 |   / 13/ 14/|15/  |")
    print("     |  /___/___/_|_/   |                                 |  /___/___/_|_/   |")
    print("     | / "+Array[16]+" / "+Array[17]+" / "+Array[18]+"|/    |                                 | / 16/ 17/18|/    |")
    print("     |/___/___/___|     |                                 |/___/___/___|     |")
    print("     |     |______|_____|                                 |     |______|_____|")
    print("     |     / "+Array[19]+" / "+Array[20]+"|/ "+Array[21]+" /                                  |     / 19/20|/ 21/ ")
    print("     |    /___/___|___/                                   |    /___/___|___/  ")
    print("     |   / "+Array[22]+" / "+Array[23]+" /|"+Array[24]+" /                                    |   / 22/ 23/|24/   ")
    print("     |  /___/___/_|_/                                     |  /___/___/_|_/    ")
    print("     | / "+Array[25]+" / "+Array[26]+" / "+Array[27]+"|/                                      | / 25/ 26/27|/     ")
    print("     |/___/___/___|                                       |/___/___/___|      ")



#########################################################  Move of Player 1 When player playes first

def TurnX():
    print ("Player 1 Make your move (1-27):")
    k=int(input("Enter position:"))
    InputX(k)
    CheckWinX()


def InputX(k):
    if Array[k]==" " :
        if k <= 27:
            if k >= 1:
                Array[k]="X"
                Display()
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




#########################################################  Move of Player 2 When player playes first

def TurnY():
    print ("Player 2 Makes its move (1-27):")
    k=WinningMove()
    if(k==0):
        k=SaveMove()
    InputY(k)
    CheckWinY()


def InputY(k):
        if Array[k]==" " :
            if k <= 27:
                if k >= 1:
                    print("Selected Position: ",k)
                    Array[k]="O"
                    Display()
                else:
                    x=randint(1,27)
                    InputY(x)
            else:
                y=randint(1,27)
                InputY(y)
        else:
            z=randint(1,27)
            InputY(z) 


#########################################  Bot engine for When player playes first
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

#########################################  Bot engine for When player playes first
##########################################  To Block Move for Player 2

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




#############################################  To Check The Win for Player 1 when player plays first
    
def CheckWinX():
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
        CheckTieX()


def CheckTieX():  
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        TurnY()
    else:
        print ("Tie: GAME OVER")
        

#############################################  To Check The Win for Player 2 when player plays first
        
def CheckWinY():
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
        CheckTieY()


def CheckTieY():
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        TurnX()
    else:
        print ("Tie: GAME OVER")
        



################################################  bot plays first
def Xturnbot():
    global k
    u = k
    global x
    
    if x == 1:
        Array[14] = "X" # first move of the computer has been set
        print("The computers first move is: ")
        x = x + 1
    else:
        Xcheckposition(u, x, Array) # if anything but first, it checks the first
        print("The computers next move is:")# player's move to decide the future
        x = x + 1
        
    Display()                           
    XcheckwinX(Array)

################################################  Bot engine for when bot plays first
def Xcheckposition(u, x, Array): 
    if u==11 or u==13 or u==15 or u==17 or u==5 or u==23:
        Xsidemove(u, x, Array) 
    elif u==1 or u==3 or u==7 or u==9 or u==19 or u==21 or u==25  or u==27:
        Xbodydiagonal(u, x, Array)
    else:
        Xweirddiagonal(u, x, Array) 

def XinputY(y, Array):
    if Array[y]==" " :
        if y <= 27: # position value has to be less than 28
            if y >= 1: # position has to be greater than 0
                Array[y]="O"
                Display()
            else:
                print ("invalid input")
                a=int(float(input("Enter position:")))
                XinputY(a, Array)
        else:
            print ("invalid input")
            b=int(float(input("Enter position:")))
            XinputY(b, Array)
    else:
        print ("Space Taken")
        c=int(float(input("Enter position:")))
        XinputY(c, Array)

def XturnY(): 
    global k
    global x
    print ("Player 1 Make your move (1-27)")
    
    if x == 2:
        k = int(input("Enter position: ")) # first position is saved in the 
        XinputY(k, Array)
        x = x + 1                  # global k which reXmains untouched 
    else:                                  # after this
        u = int(input("Enter position: ")) # saves later values of position in u
        XinputY(u, Array)
        x = x + 1 
        
    XcheckwinY(Array)


def Xsidemove(u, a, arr): # a gives move number to help the computer decide
    if u==5 or u==23:    # what move should be made next to win
        if a==3:
            Array[8]="X"
        elif a==5:
            if Array[20]==" ":
                Array[20]="X"
            else:
                Array[26]="X"
        elif a==7:
            if Array[2]==" ":
                Array[2]="X"
            elif Array[17]==" ":
                Array[17]="X"
    elif u==11 or u==17:
        if a==3:
            Array[18]="X"
        elif a==5:
            if Array[10]==" ":
                Array[10]="X"
            else:
                Array[12]="X"
        elif a==7:
            if Array[15]==" ":
                Array[15]="X"
            elif Array[16]==" ":
                Array[16]="X"
    elif u==13 or u==15:
        if a==3:
            Array[18]="X"
        elif a==5:
            if Array[10]=="":
                Array[10]="X"
            else:
                Array[16]="X"
        elif a==7:
            if Array[12]=="":
                Array[12]="X"
            elif Array[17]=="":
                Array[17]="X" 
        

def Xbodydiagonal(u, a, arr):
    if u==1 or u==3:
        if a==3:
            Array[2]="X"
        elif a==5:
            if Array[26]==" ":
                Array[26]="X"
            else:
                Array[8]="X"
        elif a==7:
            if Array[5]==" ":
                Array[5]="X"
            elif Array[20]==" ":
                Array[20]="X"
    elif u==7 or u==9:
        if a==3:
            Array[8]="X"
        elif a==5:
            if Array[20]==" ":
                Array[20]="X"
            else:
                Array[2]="X"
        elif a==7:
            if Array[5]==" ":
                Array[5]="X"
            elif Array[26]==" ":
                Array[26]="X"
    elif u==19 or u==21:
        if a==3:
            Array[20]="X"
        elif a==5:
            if Array[8]==" ":
                Array[8]="X"
            else:
                Array[26]="X"
        elif a==7:
            if Array[23]==" ":
                Array[23]="X"
            elif Array[2]==" ":
                Array[2]="X"
    elif k==25 or k==27:
        if a==3:
            Array[26]="X"
        elif a==5:
            if Array[2]==" ":
                Array[2]="X"
            else:
                Array[20]="X"
        elif a==7:
            if Array[23]==" ":
                Array[23]="X"
            elif Array[8]==" ":
                Array[8]="X"
    
def Xweirddiagonal(u, a, arr):
    if u==10 or u==12 or u==16 or u==18 or u==2 or u==8:
        if a==3:
            Array[4]="X"
        elif a==5:
            if Array[24]==" ":
                Array[24]="X"
            else:
                Array[6]="X"
        elif a==7:
            if Array[5]==" ":
                Array[5]="X"
            elif Array[22]==" ":
                Array[22]="X"
    elif u==4 or u==6:
        if a==3:
            Array[2]="X"
        elif a==5:
            if Array[26]==" ":
                Array[26]="X"
            else:
                Array[8]="X"
        elif a==7:
            if Array[5]==" ":
                Array[5]="X"
            elif Array[20]==" ":
                Array[20]="X"
    elif u==20 or u==26:
        if a==3:
            Array[22]="X"
        elif a==5:
            if Array[6]==" ":
                Array[6]="X"
            else:
                Array[24]="X"
        elif a==7:
            if Array[23]==" ":
                Array[23]="X"
            elif Array[4]==" ":
                Array[4]="X"
    elif u==22 or u==24:
        if a==3:
            Array[20]="X"
        elif a==5:
            if Array[8]==" ":
                Array[8]="X"
            else:
                Array[26]="X"
        elif a==7:
            if Array[23]==" ":
                Array[23]="X"
            elif Array[2]==" ":
                Array[2]="X"

        
def XcheckwinX(Arr):
    if Array[7]=="X" and Array[8]=="X" and Array[9]=="X":
        print("Victory: Computer")  
        
    elif Array[4]=="X" and Array[5]=="X" and Array[6]=="X":
        print("Victory: Computer")   
        
    elif Array[1]=="X" and Array[2]=="X" and Array[3]=="X":
        print("Victory: Computer")   
        
    elif Array[7]=="X" and Array[4]=="X" and Array[1]=="X":
        print("Victory: Computer")  
        
    elif Array[8]=="X" and Array[5]=="X" and Array[2]=="X":
        print("Victory: Computer")   
        
    elif Array[9]=="X" and Array[6]=="X" and Array[3]=="X":
        print("Victory: Computer")  
        
    elif Array[7]=="X" and Array[5]=="X" and Array[3]=="X":
        print("Victory: Computer") 
        
    elif Array[9]=="X" and Array[5]=="X" and Array[1]=="X":
        print("Victory: Computer")
        
    elif Array[10]=="X" and Array[11]=="X" and Array[12]=="X":
        print("Victory: Computer")
        
    elif Array[13]=="X" and Array[14]=="X" and Array[15]=="X":
        print("Victory: Computer")
        
    elif Array[16]=="X" and Array[17]=="X" and Array[18]=="X":
        print("Victory: Computer")
        
    elif Array[10]=="X" and Array[13]=="X" and Array[16]=="X":
        print("Victory: Computer")
        
    elif Array[11]=="X" and Array[14]=="X" and Array[17]=="X":
        print("Victory: Computer")
        
    elif Array[12]=="X" and Array[15]=="X" and Array[18]=="X":
        print("Victory: Computer")
        
    elif Array[10]=="X" and Array[14]=="X" and Array[18]=="X":
        print("Victory: Computer")
        
    elif Array[12]=="X" and Array[14]=="X" and Array[16]=="X":
        print("Victory: Computer")
        
    elif Array[19]=="X" and Array[20]=="X" and Array[21]=="X":
        print("Victory: Computer")
        
    elif Array[22]=="X" and Array[23]=="X" and Array[24]=="X":
        print("Victory: Computer")
        
    elif Array[25]=="X" and Array[26]=="X" and Array[27]=="X":
        print("Victory: Computer")
        
    elif Array[19]=="X" and Array[22]=="X" and Array[25]=="X":
        print("Victory: Computer")
        
    elif Array[20]=="X" and Array[23]=="X" and Array[26]=="X":
        print("Victory: Computer")
        
    elif Array[21]=="X" and Array[24]=="X" and Array[27]=="X":
        print("Victory: Computer")
        
    elif Array[19]=="X" and Array[23]=="X" and Array[27]=="X":
        print("Victory: Computer")
        
    elif Array[21]=="X" and Array[23]=="X" and Array[25]=="X":
        print("Victory: Computer")
        
    elif Array[1]=="X" and Array[10]=="X" and Array[19]=="X":
        print("Victory: Computer")
        
    elif Array[2]=="X" and Array[11]=="X" and Array[20]=="X":
        print("Victory: Computer")
        
    elif Array[3]=="X" and Array[12]=="X" and Array[21]=="X":
        print("Victory: Computer")
        
    elif Array[4]=="X" and Array[13]=="X" and Array[22]=="X":
        print("Victory: Computer")
        
    elif Array[5]=="X" and Array[14]=="X" and Array[23]=="X":
        print("Victory: Computer")
        
    elif Array[6]=="X" and Array[15]=="X" and Array[24]=="X":
        print("Victory: Computer")
        
    elif Array[7]=="X" and Array[16]=="X" and Array[25]=="X":
        print("Victory: Computer")
        
    elif Array[8]=="X" and Array[17]=="X" and Array[26]=="X":
        print("Victory: Computer")
        
    elif Array[9]=="X" and Array[18]=="X" and Array[27]=="X":
        print("Victory: Computer")    
        
    elif Array[1]=="X" and Array[13]=="X" and Array[25]=="X":
        print("Victory: Computer")
        
    elif Array[7]=="X" and Array[13]=="X" and Array[19]=="X":
        print("Victory: Computer")
        
    elif Array[1]=="X" and Array[11]=="X" and Array[21]=="X":
        print("Victory: Computer")
        
    elif Array[3]=="X" and Array[11]=="X" and Array[19]=="X":
        print("Victory: Computer")
        
    elif Array[3]=="X" and Array[15]=="X" and Array[27]=="X":
        print("Victory: Computer")
        
    elif Array[9]=="X" and Array[15]=="X" and Array[21]=="X":
        print("Victory: Computer")
        
    elif Array[9]=="X" and Array[17]=="X" and Array[25]=="X":
        print("Victory: Computer")
        
    elif Array[7]=="X" and Array[17]=="X" and Array[27]=="X":
        print("Victory: Computer")   
        
    elif Array[2]=="X" and Array[14]=="X" and Array[26]=="X":
        print("Victory: Computer")
        
    elif Array[8]=="X" and Array[14]=="X" and Array[20]=="X":
        print("Victory: Computer")
        
    elif Array[4]=="X" and Array[14]=="X" and Array[24]=="X":
        print("Victory: Computer")
        
    elif Array[6]=="X" and Array[14]=="X" and Array[22]=="X":
        print("Victory: Computer")
        
    elif Array[1]=="X" and Array[14]=="X" and Array[27]=="X":
        print("Victory: Computer")
        
    elif Array[9]=="X" and Array[14]=="X" and Array[19]=="X":
        print("Victory: Computer")
        
    elif Array[3]=="X" and Array[14]=="X" and Array[25]=="X":
        print("Victory: Computer")
        
    elif Array[7]=="X" and Array[14]=="X" and Array[21]=="X":
        print("Victory: Computer")
        
    else:
        XchecktieX(Array)
        
def XcheckwinY(Arr):
    if Arr[7]=="O" and Arr[8]=="O" and Arr[9]=="O":
        print("Victory: Player")        
    elif Arr[4]=="O" and Arr[5]=="O" and Arr[6]=="O":
        print("Victory: Player")        
    elif Arr[1]=="O" and Arr[2]=="O" and Arr[3]=="O":
        print("Victory: Player")        
    elif Arr[7]=="O" and Arr[4]=="O" and Arr[1]=="O":
        print("Victory: Player")        
    elif Arr[8]=="O" and Arr[5]=="O" and Arr[2]=="O":
        print("Victory: Player")        
    elif Arr[9]=="O" and Arr[6]=="O" and Arr[3]=="O":
        print("Victory: Player")        
    elif Arr[7]=="O" and Arr[5]=="O" and Arr[3]=="O":
        print("Victory: Player")        
    elif Arr[9]=="O" and Arr[5]=="O" and Arr[1]=="O":
        print("Victory: Player")
    elif Arr[10]=="O" and Arr[11]=="O" and Arr[12]=="O":
        print("Victory: Player")
    elif Arr[13]=="O" and Arr[14]=="O" and Arr[15]=="O":
        print("Victory: Player")
    elif Arr[16]=="O" and Arr[17]=="O" and Arr[18]=="O":
        print("Victory: Player")
    elif Arr[10]=="O" and Arr[13]=="O" and Arr[16]=="O":
        print("Victory: Player")
    elif Arr[11]=="O" and Arr[14]=="O" and Arr[17]=="O":
        print("Victory: Player")
    elif Arr[12]=="O" and Arr[15]=="O" and Arr[18]=="O":
        print("Victory: Player")
    elif Arr[10]=="O" and Arr[14]=="O" and Arr[18]=="O":
        print("Victory: Player")
    elif Arr[12]=="O" and Arr[14]=="O" and Arr[16]=="O":
        print("Victory: Player")
    elif Arr[19]=="O" and Arr[20]=="O" and Arr[21]=="O":
        print("Victory: Player")
    elif Arr[22]=="O" and Arr[23]=="O" and Arr[24]=="O":
        print("Victory: Player")
    elif Arr[25]=="O" and Arr[26]=="O" and Arr[27]=="O":
        print("Victory: Player")
    elif Arr[19]=="O" and Arr[22]=="O" and Arr[25]=="O":
        print("Victory: Player")
    elif Arr[20]=="O" and Arr[23]=="O" and Arr[26]=="O":
        print("Victory: Player")
    elif Arr[21]=="O" and Arr[24]=="O" and Arr[27]=="O":
        print("Victory: Player")
    elif Arr[19]=="O" and Arr[23]=="O" and Arr[27]=="O":
        print("Victory: Player")
    elif Arr[21]=="O" and Arr[23]=="O" and Arr[25]=="O":
        print("Victory: Player")
    elif Arr[1]=="O" and Arr[10]=="O" and Arr[19]=="O":
        print("Victory: Player")
    elif Arr[2]=="O" and Arr[11]=="O" and Arr[20]=="O":
        print("Victory: Player")
    elif Arr[3]=="O" and Arr[12]=="O" and Arr[21]=="O":
        print("Victory: Player")
    elif Arr[4]=="O" and Arr[13]=="O" and Arr[22]=="O":
        print("Victory: Player")
    elif Arr[5]=="O" and Arr[14]=="O" and Arr[23]=="O":
        print("Victory: Player")
    elif Arr[6]=="O" and Arr[15]=="O" and Arr[24]=="O":
        print("Victory: Player")
    elif Arr[7]=="O" and Arr[16]=="O" and Arr[25]=="O":
        print("Victory: Player")
    elif Arr[8]=="O" and Arr[17]=="O" and Arr[26]=="O":
        print("Victory: Player")
    elif Arr[9]=="O" and Arr[18]=="O" and Arr[27]=="O":
        print("Victory: Player")    
    elif Arr[1]=="O" and Arr[13]=="O" and Arr[25]=="O":
        print("Victory: Player")
    elif Arr[7]=="O" and Arr[13]=="O" and Arr[19]=="O":
        print("Victory: Player")
    elif Arr[1]=="O" and Arr[11]=="O" and Arr[21]=="O":
        print("Victory: Player")
    elif Arr[3]=="O" and Arr[11]=="O" and Arr[19]=="O":
        print("Victory: Player")
    elif Arr[3]=="O" and Arr[15]=="O" and Arr[27]=="O":
        print("Victory: Player")
    elif Arr[9]=="O" and Arr[15]=="O" and Arr[21]=="O":
        print("Victory: Player")
    elif Arr[9]=="O" and Arr[17]=="O" and Arr[25]=="O":
        print("Victory: Player")
    elif Arr[7]=="O" and Arr[17]=="O" and Arr[27]=="O":
        print("Victory: Player")    
    elif Arr[2]=="O" and Arr[14]=="O" and Arr[26]=="O":
        print("Victory: Player")
    elif Arr[8]=="O" and Arr[14]=="O" and Arr[20]=="O":
        print("Victory: Player")
    elif Arr[4]=="O" and Arr[14]=="O" and Arr[24]=="O":
        print("Victory: Player")
    elif Arr[6]=="O" and Arr[14]=="O" and Arr[22]=="O":
        print("Victory: Player")
    elif Arr[1]=="O" and Arr[14]=="O" and Arr[27]=="O":
        print("Victory: Player")
    elif Arr[9]=="O" and Arr[14]=="O" and Arr[19]=="O":
        print("Victory: Player")
    elif Arr[3]=="O" and Arr[14]=="O" and Arr[25]=="O":
        print("Victory: Player")
    elif Arr[7]=="O" and Arr[14]=="O" and Arr[21]=="O":
        print("Victory: Player")
    else:
        XchecktieY(Array)

def XchecktieX(Array):  
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        XturnY()
    else:
        print ("Tie: GAME OVER")
        

def XchecktieY(Array):
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        Xturnbot()
    else:
        print ("Tie: GAME OVER")
    
 ################################################  Toss
def toss():
    choose=0
    print("  ______               ")
    print(" /_  __/___   __________")
    print("  / / / __ \ / ___/ ___/")
    print(" / / / /_/ |(__  |__  ) ")
    print("/_/  \____/ ____/____/  ")
    print("\n")
    print("Choose H/T\n\n")
    print("Winner plays first\n")
    print("Enter 1 to select HEADS\n")
    print("Enter 2 to select TAILS\n")
    while(choose!=1 and choose!=2):
        choose=int(float(input("Enter your Choice: ")))
    check = random.randint (1,2)
    if check==choose:
        print ("PLAYER GOES FIRST")
        Display()
        TurnX()
    else:
        print ("COMPUTER GOES FIRST")
        print ("NICE")
        Display()
        Xturnbot()
        
        

   
################################################  Opening Menu & Game Begins
toss()

