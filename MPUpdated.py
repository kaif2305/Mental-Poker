import random

# Generating Cards Deck
cardWeight=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"] 
cardShape=["Diamonds","Hearts","Spades","Clubs"] 
cardDeck=[]
for i in cardShape:
    for j in cardWeight:
        card=i+" "+j 
        cardDeck.append(card)
        
# Representing each card by numbers from 11 to 62 
numberDeck=[]
for i in range(11,63):
    numberDeck.append(i)
    

# Shuffling Cards function Fisher-Yates Shuffling Algorithm 
def shuffle(cardDeck):
    for i in range(51, 0, -1):
        j=random.randint(0, i + 1)
        cardDeck[i], cardDeck[j]=cardDeck[j], cardDeck[i]
    return cardDeck



#Function to add the Padding to any required Card while Encrypting
def padding(cardDeck):
    for i in cardDeck:
            j=random.randint(0, 4) 
            for k in range(0,j+1):
                l=random.randint(1,10)
                i=(i*10)+l 
    return cardDeck


#Function to check if the number entered is a Prime Number or Not
def prime_check(a): 
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)): 
        return False
    elif(a>2):
        for i in range(2,a): 
            if not(a%i):
                return False
    return True
    

  
#GCD
def egcd(a,b):
    if b==0: 
        return a
    else:
        return egcd(b,a%b)
    
    

#Extended Euclidean Algorithm 
def eea(a,b):
    if(a%b==0): 
        return(b,0,1)
    else:
        gcd,s,t=eea(b,a%b) 
        s=s-((a//b) * t) 
        return(gcd,t,s)
    


#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1): 
        return None
    else:
        return s%r
    
    

#encryption function
def encrypt(m,e,n):
    return ((m**e)%n) 


#decryption function
def decrypt(c,d,n): 
    return (c**d)%n



#This Function does the last verification where on entering the passcode, 
#the other Player's cards are displayed
def verify(arr,pn):
    d=int(input("Enter the Value of the Opponent's Shared key D: ")) 
    oCards=[]
    for i in range(0,5):
        m=decrypt(arr[i],d,pn) 
        oCards.append(cardDeck[int(str(m)[:2])-11])
    print("\nThe Cards that the Opponent has are: \n") 
    for i in oCards:
        print(i)
        
        
    
#Main Function
player=int(input("Enter your Choice\n1.To Continue as Player 1\n2. To Continue as Player 2"))
if player==1:
    p=int(input("Enter the Value of Prime Number P: ")) 
    check_p=prime_check(p) 
    while (check_p == False):
        p=int(input("The number Entered isn't prime, try again: "))
        check_p=prime_check(p)
    q=int(input("Enter the Value of the Second Prime Number Q:")) 
    check_q=prime_check(q)
    while (check_q == False):
            q=int(input("The number Entered isn't prime, try again: ")) 
            check_q=prime_check(q)
            
            
    n=p*q
    print("\nShare these Values with Player 2 to Continue the Game:n") 
    print("P Chosen: ",p)
    print("Q Chosen: ",q)
    print("Computed Value of N: ",n)
    print("\n")
    
    
    
    # Eulers Toitent
    r=(p - 1) * (q - 1) 
    
    
    # Taking e as input
    e=int(input("Enter the Value of E: (Should have GCD=1)")) 
    while(egcd(e,r)!=1):
        print("The Number Entered doesn't have its Euler's Toitent = 1, Try Again.")
        e=int(input("Enter the Value of E: (Should have GCD=1)"))
        
    
    # Calculating d
    d=mult_inv(e, r)
    
    
    #shuffling cards
    shuffledDeck=shuffle(numberDeck)
    
    
    #Adding padding to the shuffled deck
    finalDeck=padding(shuffledDeck)
    
    
    #creating encrypted deck
    encryptedDeck=[]
    for i in finalDeck: 
        encryptedDeck.append(encrypt(i,e,n))
    print("Send this text to Player 2\nAsk Player 2 to pick 5 cards at Random, by their Index Number.")
    for i in range(0,52): print((i+1),"-",encryptedDeck[i])
    
    
    
    #decrypting your cards
    yourCards=[]
    print("Enter the Index Numbers of the Cards sent by Player 2: ")
    for i in range(0,5):
        print("Recieved Index No. ",(i+1),": ") 
        c=int(input())
        m=decrypt(encryptedDeck[c-1],d,n) 
        yourCards.append(cardDeck[int(str(m)[:2])-11])
        
        
    #removing encryption from doubly encrypted player2's card
    p2Cards=[]
    for i in range(0,5):
        print("Recieved Card No. ",(i+1),": ")
        c=int(input())
        p2Cards.append(decrypt(c,d,n))
    print("\nSend this data to Player 2\nAsk them to Decrypt the 5 Cards Individually.\n")
    for i in range(0,5):
        print((i+1),"-",p2Cards[i])
    print("\nCards Drawn for You: \n") 
    for i in yourCards:
        print(i)
        
        
    #When betting is ended
    input("If the Bet has Ended, Enter 0.") 
    print("\nSend this data to Player 2:\n") 
    print("Value of Key d=",d)
    verify(p2Cards,n)
if player==2:
    p=int(input("Enter the Value of Prime No. P sent by Player 1: ")) 
    q=int(input("Enter the value of Prime No. Q sent by Player1: ")) 
    n=p*q
    print("Computed Value of N=",n,"\nMake sure this Value of N Matches to that of Player 1.")
    
    
    # Eulers Toitent
    r=(p - 1) * (q - 1)
    
    
    #waiting for the player 1 to send cards
    input("\nIf you have recieved the Shuffled and Encrypted List of Cards from Player 1, Press 1\n")
    print("\nPick 5 cards from the list sent by Player 1 at Random, Keeping their Index Numbers in Mind\n")
    selectedIndex=[]
    print("Now, Enter the Index Number of the Cards you've Picked.")
    for i in range(0,5):
        print("Card",(i+1),": ") 
        v=int(input()) 
        selectedIndex.append(v)
    print("Send this Data to Player 1:")
    print("The Index Values for your Cards are: ") 
    for i in selectedIndex:
        print(i)
       
    arr=[]
    print("Now Enter the Values of the Cards you've sent to Player 1 via Index:")
    for i in range(0, 5):
        print("Card",(i + 1),": ")
        j=int(input())
        arr.append(j)
        
        
    #Taking the value of e as input
    e=int(input("Enter the Value of E: (Should have GCD=1)")) 
    while (egcd(e, r) != 1):
        print("The Number Entered doesn't have its Euler's Toitent = 1, Try Again.")
        e=int(input("Enter the Value of E: (Should have GCD=1)")) 
        
        
    # Calculating d
    d=mult_inv(e, r)
    doubleEncryptedCards=[]
    print("\nNow, Pick 5 Cards at Random from the Deck for Yourself\n(Apart from the 5 you've chosen for Player 1): ")
    for i in range(0,5):
        print("Card",(i+1),": ")
        m=int(input()) 
        doubleEncryptedCards.append(encrypt(m,e,n))
        
        
    #Sending this Double Encrypted Cards to player1
    print("\nSend this Data to Player 1: \n")
    for i in doubleEncryptedCards: 
        print(i)
        
        
    #decrypting your cards
    yourCards=[]
    print("Now, enter the Values of the Cards you recieved from Player 1")
    for i in range(0,5):
        print("Card",(i+1),": ")
        c=int(input())
        m=decrypt(c, d, n)

        yourCards.append(cardDeck[int(str(m)[:2]) - 11]) 
        
        
    #printing player2 cards
    for i in yourCards: 
        print(i)
    input("If the Bet has Ended, Enter 0.") 
    print("\nSend this data to Player 2:\n") 
    print("Value of Key d=",d)
    verify(arr,n)
