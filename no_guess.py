import random
print("WECOME TO THE GAME OF NUMBER-GUESSING")
print("\n")

def game(comp_inp,ch):
  
    
    if(ch>0):
        guess=int(input("enter your guess :"))
        if(guess==comp_inp):
            print("You are correct")
            
        if(guess>comp_inp):
            ch-=1
            print("Too high")
            print("You have {} chances left".format(ch))
            game(comp_inp,ch)
        if(guess<comp_inp):
            ch-=1
            print("Too low")
            print("You have {} chances left".format(ch))
            game(comp_inp,ch)
    if(ch==0) :         
        print("Sorry,You lose")
        print("Computer input is :",comp_inp)
        
        

upper_lim=int(input("please enter the upper limit :"))
lower_lim=int(input("please enter the lower limit :"))
comp_inp=random.randint(lower_lim,upper_lim)
print("you have 3 chances to guess the correct number")
ch=3
game(comp_inp,ch)
print("\n")
print("Thank You for playing")