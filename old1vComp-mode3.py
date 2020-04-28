Array=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
k = 0 # global k helps store the first move of the player
      # since the entire game is based on it and what happens after it
x = 1

def Xdisplay(arr):
    print("Top Layer")
    print(arr[1] + '|' + arr[2] + '|' + arr[3])
    print('-+-+-')
    print(arr[4] + '|' + arr[5] + '|' + arr[6])
    print('-+-+-')
    print(arr[7] + '|' + arr[8] + '|' + arr[9])
    print("     ")
    print("=========================================================")
    print("Middle Layer")
    print(arr[10] + '|' + arr[11] + '|' + arr[12])
    print('-+-+-')
    print(arr[13] + '|' + arr[14] + '|' + arr[15])
    print('-+-+-')
    print(arr[16] + '|' + arr[17] + '|' + arr[18])
    print("     ")
    print("=========================================================")
    print("Bottom Layer")
    print(arr[19] + '|' + arr[20] + '|' + arr[21])
    print('-+-+-')
    print(arr[22] + '|' + arr[23] + '|' + arr[24])
    print('-+-+-')
    print(arr[25] + '|' + arr[26] + '|' + arr[27])
    print("     ")
    print("=========================================================")

def Xcheckposition(u, x, Array): # a gives the turn number
    if u==11 or u==13 or u==15 or u==17 or u==5 or u==23:
        Xsidemove(u, x, Array) 
    elif u==1 or u==3 or u==7 or u==9 or u==19 or u==21 or u==25  or u==27:
        Xbodydiagonal(u, x, Array)
    else:
        Xweirddiagonal(u, x, Array) # different possitions have been segregated

def XinputY(y, Array):
    if Array[y]==" " :
        if y <= 27: # position value has to be less than 28
            if y >= 1: # position has to be greater than 0
                Array[y]="O"
                Xdisplay(Array)
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
        
    Xdisplay(Array)                           
    XcheckwinX(Array)

        
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


def Xmain():
    Xdisplay(Array)
    Xturnbot()

Xmain()


# ADITI
