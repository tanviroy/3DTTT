#GLOBAL========================================================
Array=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
#GLOBAL========================================================


def display(arr):
    print("===========================================================================================================")
    print("                Game                                                Controls")
    print("            ____________                                         ____________ ")
    print("           / "+arr[1]+" / "+arr[2]+" / "+arr[3]+" /|                                       / 1 / 2 / 3 /|")
    print("          /___/___/___/ |                                      /___/___/___/ |")
    print("         / "+arr[4]+" / "+arr[5]+" / "+arr[6]+" /  |                                     / 4 / 5 / 6 /  |")
    print("        /___/___/___/   |                                    /___/___/___/   |")
    print("       / "+arr[7]+" / "+arr[8]+" / "+arr[9]+" /    |                                   / 7 / 8 / 9 /    |")
    print("      /___/___/___/     |                                  /___/___/___/     |")
    print("     |     |______|_____|                                 |     |______|_____|")
    print("     |     / "+arr[10]+" / "+arr[11]+"|/ "+arr[12]+" /|                                 |     / 10/11|/ 12/|")
    print("     |    /___/___|___/ |                                 |    /___/___|___/ |")
    print("     |   / "+arr[13]+" / "+arr[14]+" /|"+arr[15]+" /  |                                 |   / 13/ 14/|15/  |")
    print("     |  /___/___/_|_/   |                                 |  /___/___/_|_/   |")
    print("     | / "+arr[16]+" / "+arr[17]+" / "+arr[18]+"|/    |                                 | / 16/ 17/18|/    |")
    print("     |/___/___/___|     |                                 |/___/___/___|     |")
    print("     |     |______|_____|                                 |     |______|_____|")
    print("     |     / "+arr[19]+" / "+arr[20]+"|/ "+arr[21]+" /                                  |     / 19/20|/ 21/ ")
    print("     |    /___/___|___/                                   |    /___/___|___/  ")
    print("     |   / "+arr[22]+" / "+arr[23]+" /|"+arr[24]+" /                                    |   / 22/ 23/|24/   ")
    print("     |  /___/___/_|_/                                     |  /___/___/_|_/    ")
    print("     | / "+arr[25]+" / "+arr[26]+" / "+arr[27]+"|/                                      | / 25/ 26/27|/     ")
    print("     |/___/___/___|                                       |/___/___/___|      ")
    
    


def inputX(k,Array):
    if Array[k]==" " :
        if k <= 27:
            if k >= 1:
                Array[k]="X"
                display (Array)
            else:
                print ("invalid input")
                a=int(float(input("Enter position:")))
                inputX (a,Array)
        else:
            print ("invalid input")
            b=int(float(input("Enter position:")))
            inputX (b,Array)
    else:
        print ("Space Taken")
        c=int(float(input("Enter position:")))
        inputX (c,Array)

def inputY(k,Array):
    if Array[k]==" " :
        if k <= 27:
            if k >= 1:
                Array[k]="O"
                display (Array)
            else:
                print ("invalid input")
                x=int(float(input("Enter position:")))
                inputY (x,Array)
        else:
            print ("invalid input")
            y=int(float(input("Enter position:")))
            inputY (y,Array)
    else:
        print ("Space Taken")
        z=int(float(input("Enter position:")))
        inputY (z,Array)

def turnX():
    print ("Player 1 Make your move (1-27)")
    k=int(float(input("Enter position:")))
    inputX (k,Array)
    checkwinX(Array)

def turnY():
    print ("Player 2 Make your move (1-27)")
    k=int(float(input("Enter position:")))
    inputY (k,Array)
    checkwinY(Array)
    
def checkwinX(Arr):
    if Arr[7]=="X" and Arr[8]=="X" and Arr[9]=="X":
        print("Victory: Player 1")        
    elif Arr[4]=="X" and Arr[5]=="X" and Arr[6]=="X":
        print("Victory: Player 1")        
    elif Arr[1]=="X" and Arr[2]=="X" and Arr[3]=="X":
        print("Victory: Player 1")        
    elif Arr[7]=="X" and Arr[4]=="X" and Arr[1]=="X":
        print("Victory: Player 1")        
    elif Arr[8]=="X" and Arr[5]=="X" and Arr[2]=="X":
        print("Victory: Player 1")        
    elif Arr[9]=="X" and Arr[6]=="X" and Arr[3]=="X":
        print("Victory: Player 1")        
    elif Arr[7]=="X" and Arr[5]=="X" and Arr[3]=="X":
        print("Victory: Player 1")        
    elif Arr[9]=="X" and Arr[5]=="X" and Arr[1]=="X":
        print("Victory: Player 1")
    elif Arr[10]=="X" and Arr[11]=="X" and Arr[12]=="X":
        print("Victory: Player 1")
    elif Arr[13]=="X" and Arr[14]=="X" and Arr[15]=="X":
        print("Victory: Player 1")
    elif Arr[16]=="X" and Arr[17]=="X" and Arr[18]=="X":
        print("Victory: Player 1")
    elif Arr[10]=="X" and Arr[13]=="X" and Arr[16]=="X":
        print("Victory: Player 1")
    elif Arr[11]=="X" and Arr[14]=="X" and Arr[17]=="X":
        print("Victory: Player 1")
    elif Arr[12]=="X" and Arr[15]=="X" and Arr[18]=="X":
        print("Victory: Player 1")
    elif Arr[10]=="X" and Arr[14]=="X" and Arr[18]=="X":
        print("Victory: Player 1")
    elif Arr[12]=="X" and Arr[14]=="X" and Arr[16]=="X":
        print("Victory: Player 1")
    elif Arr[19]=="X" and Arr[20]=="X" and Arr[21]=="X":
        print("Victory: Player 1")
    elif Arr[22]=="X" and Arr[23]=="X" and Arr[24]=="X":
        print("Victory: Player 1")
    elif Arr[25]=="X" and Arr[26]=="X" and Arr[27]=="X":
        print("Victory: Player 1")
    elif Arr[19]=="X" and Arr[22]=="X" and Arr[25]=="X":
        print("Victory: Player 1")
    elif Arr[20]=="X" and Arr[23]=="X" and Arr[26]=="X":
        print("Victory: Player 1")
    elif Arr[21]=="X" and Arr[24]=="X" and Arr[27]=="X":
        print("Victory: Player 1")
    elif Arr[19]=="X" and Arr[23]=="X" and Arr[27]=="X":
        print("Victory: Player 1")
    elif Arr[21]=="X" and Arr[23]=="X" and Arr[25]=="X":
        print("Victory: Player 1")
    elif Arr[1]=="X" and Arr[10]=="X" and Arr[19]=="X":
        print("Victory: Player 1")
    elif Arr[2]=="X" and Arr[11]=="X" and Arr[20]=="X":
        print("Victory: Player 1")
    elif Arr[3]=="X" and Arr[12]=="X" and Arr[21]=="X":
        print("Victory: Player 1")
    elif Arr[4]=="X" and Arr[13]=="X" and Arr[22]=="X":
        print("Victory: Player 1")
    elif Arr[5]=="X" and Arr[14]=="X" and Arr[23]=="X":
        print("Victory: Player 1")
    elif Arr[6]=="X" and Arr[15]=="X" and Arr[24]=="X":
        print("Victory: Player 1")
    elif Arr[7]=="X" and Arr[16]=="X" and Arr[25]=="X":
        print("Victory: Player 1")
    elif Arr[8]=="X" and Arr[17]=="X" and Arr[26]=="X":
        print("Victory: Player 1")
    elif Arr[9]=="X" and Arr[18]=="X" and Arr[27]=="X":
        print("Victory: Player 1")    
    elif Arr[1]=="X" and Arr[13]=="X" and Arr[25]=="X":
        print("Victory: Player 1")
    elif Arr[7]=="X" and Arr[13]=="X" and Arr[19]=="X":
        print("Victory: Player 1")
    elif Arr[1]=="X" and Arr[11]=="X" and Arr[21]=="X":
        print("Victory: Player 1")
    elif Arr[3]=="X" and Arr[11]=="X" and Arr[19]=="X":
        print("Victory: Player 1")
    elif Arr[3]=="X" and Arr[15]=="X" and Arr[27]=="X":
        print("Victory: Player 1")
    elif Arr[9]=="X" and Arr[15]=="X" and Arr[21]=="X":
        print("Victory: Player 1")
    elif Arr[9]=="X" and Arr[17]=="X" and Arr[25]=="X":
        print("Victory: Player 1")
    elif Arr[7]=="X" and Arr[17]=="X" and Arr[27]=="X":
        print("Victory: Player 1")    
    elif Arr[2]=="X" and Arr[14]=="X" and Arr[26]=="X":
        print("Victory: Player 1")
    elif Arr[8]=="X" and Arr[14]=="X" and Arr[20]=="X":
        print("Victory: Player 1")
    elif Arr[4]=="X" and Arr[14]=="X" and Arr[24]=="X":
        print("Victory: Player 1")
    elif Arr[6]=="X" and Arr[14]=="X" and Arr[22]=="X":
        print("Victory: Player 1")
    elif Arr[1]=="X" and Arr[14]=="X" and Arr[27]=="X":
        print("Victory: Player 1")
    elif Arr[9]=="X" and Arr[14]=="X" and Arr[19]=="X":
        print("Victory: Player 1")
    elif Arr[3]=="X" and Arr[14]=="X" and Arr[25]=="X":
        print("Victory: Player 1")
    elif Arr[7]=="X" and Arr[14]=="X" and Arr[21]=="X":
        print("Victory: Player 1")
    else:
        checktieX(Array)
        
def checkwinY(Arr):
    if Arr[7]=="O" and Arr[8]=="O" and Arr[9]=="O":
        print("Victory: Player 2")        
    elif Arr[4]=="O" and Arr[5]=="O" and Arr[6]=="O":
        print("Victory: Player 2")        
    elif Arr[1]=="O" and Arr[2]=="O" and Arr[3]=="O":
        print("Victory: Player 2")        
    elif Arr[7]=="O" and Arr[4]=="O" and Arr[1]=="O":
        print("Victory: Player 2")        
    elif Arr[8]=="O" and Arr[5]=="O" and Arr[2]=="O":
        print("Victory: Player 2")        
    elif Arr[9]=="O" and Arr[6]=="O" and Arr[3]=="O":
        print("Victory: Player 2")        
    elif Arr[7]=="O" and Arr[5]=="O" and Arr[3]=="O":
        print("Victory: Player 2")        
    elif Arr[9]=="O" and Arr[5]=="O" and Arr[1]=="O":
        print("Victory: Player 2")
    elif Arr[10]=="O" and Arr[11]=="O" and Arr[12]=="O":
        print("Victory: Player 2")
    elif Arr[13]=="O" and Arr[14]=="O" and Arr[15]=="O":
        print("Victory: Player 2")
    elif Arr[16]=="O" and Arr[17]=="O" and Arr[18]=="O":
        print("Victory: Player 2")
    elif Arr[10]=="O" and Arr[13]=="O" and Arr[16]=="O":
        print("Victory: Player 2")
    elif Arr[11]=="O" and Arr[14]=="O" and Arr[17]=="O":
        print("Victory: Player 2")
    elif Arr[12]=="O" and Arr[15]=="O" and Arr[18]=="O":
        print("Victory: Player 2")
    elif Arr[10]=="O" and Arr[14]=="O" and Arr[18]=="O":
        print("Victory: Player 2")
    elif Arr[12]=="O" and Arr[14]=="O" and Arr[16]=="O":
        print("Victory: Player 2")
    elif Arr[19]=="O" and Arr[20]=="O" and Arr[21]=="O":
        print("Victory: Player 2")
    elif Arr[22]=="O" and Arr[23]=="O" and Arr[24]=="O":
        print("Victory: Player 2")
    elif Arr[25]=="O" and Arr[26]=="O" and Arr[27]=="O":
        print("Victory: Player 2")
    elif Arr[19]=="O" and Arr[22]=="O" and Arr[25]=="O":
        print("Victory: Player 2")
    elif Arr[20]=="O" and Arr[23]=="O" and Arr[26]=="O":
        print("Victory: Player 2")
    elif Arr[21]=="O" and Arr[24]=="O" and Arr[27]=="O":
        print("Victory: Player 2")
    elif Arr[19]=="O" and Arr[23]=="O" and Arr[27]=="O":
        print("Victory: Player 2")
    elif Arr[21]=="O" and Arr[23]=="O" and Arr[25]=="O":
        print("Victory: Player 2")
    elif Arr[1]=="O" and Arr[10]=="O" and Arr[19]=="O":
        print("Victory: Player 2")
    elif Arr[2]=="O" and Arr[11]=="O" and Arr[20]=="O":
        print("Victory: Player 2")
    elif Arr[3]=="O" and Arr[12]=="O" and Arr[21]=="O":
        print("Victory: Player 2")
    elif Arr[4]=="O" and Arr[13]=="O" and Arr[22]=="O":
        print("Victory: Player 2")
    elif Arr[5]=="O" and Arr[14]=="O" and Arr[23]=="O":
        print("Victory: Player 2")
    elif Arr[6]=="O" and Arr[15]=="O" and Arr[24]=="O":
        print("Victory: Player 2")
    elif Arr[7]=="O" and Arr[16]=="O" and Arr[25]=="O":
        print("Victory: Player 2")
    elif Arr[8]=="O" and Arr[17]=="O" and Arr[26]=="O":
        print("Victory: Player 2")
    elif Arr[9]=="O" and Arr[18]=="O" and Arr[27]=="O":
        print("Victory: Player 2")    
    elif Arr[1]=="O" and Arr[13]=="O" and Arr[25]=="O":
        print("Victory: Player 2")
    elif Arr[7]=="O" and Arr[13]=="O" and Arr[19]=="O":
        print("Victory: Player 2")
    elif Arr[1]=="O" and Arr[11]=="O" and Arr[21]=="O":
        print("Victory: Player 2")
    elif Arr[3]=="O" and Arr[11]=="O" and Arr[19]=="O":
        print("Victory: Player 2")
    elif Arr[3]=="O" and Arr[15]=="O" and Arr[27]=="O":
        print("Victory: Player 2")
    elif Arr[9]=="O" and Arr[15]=="O" and Arr[21]=="O":
        print("Victory: Player 2")
    elif Arr[9]=="O" and Arr[17]=="O" and Arr[25]=="O":
        print("Victory: Player 2")
    elif Arr[7]=="O" and Arr[17]=="O" and Arr[27]=="O":
        print("Victory: Player 2")    
    elif Arr[2]=="O" and Arr[14]=="O" and Arr[26]=="O":
        print("Victory: Player 2")
    elif Arr[8]=="O" and Arr[14]=="O" and Arr[20]=="O":
        print("Victory: Player 2")
    elif Arr[4]=="O" and Arr[14]=="O" and Arr[24]=="O":
        print("Victory: Player 2")
    elif Arr[6]=="O" and Arr[14]=="O" and Arr[22]=="O":
        print("Victory: Player 2")
    elif Arr[1]=="O" and Arr[14]=="O" and Arr[27]=="O":
        print("Victory: Player 2")
    elif Arr[9]=="O" and Arr[14]=="O" and Arr[19]=="O":
        print("Victory: Player 2")
    elif Arr[3]=="O" and Arr[14]=="O" and Arr[25]=="O":
        print("Victory: Player 2")
    elif Arr[7]=="O" and Arr[14]=="O" and Arr[21]=="O":
        print("Victory: Player 2")
    else:
        checktieY(Array)

def checktieX(Array):
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        turnY()
    else:
        print ("Tie: GAME OVER")
        

def checktieY(Array):
    if Array[1]==" " or Array[2]==" " or Array[3]==" " or Array[4]==" " or Array[5]==" " or Array[6]==" " or Array[7]==" " or Array[8]==" " or Array[9]==" " or Array[10]==" " or Array[11]==" " or Array[12]==" " or Array[13]==" " or Array[14]==" " or Array[15]==" " or Array[16]==" " or Array[17]==" " or Array[18]==" " or Array[19]==" " or Array[20]==" " or Array[21]==" " or Array[22]==" " or Array[23]==" " or Array[24]==" " or Array[25]==" " or Array[26]==" " or Array[27]==" ":
        turnX()
    else:
        print ("Tie: GAME OVER")

def main():
    display (Array)
    turnX()
    
#========================================================================    
main()
