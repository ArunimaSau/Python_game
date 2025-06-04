import random


def game_check():
    print("Enter R for rock,P for paper,S for scissor :")
    user_input=input()
    if(user_input=="R" or user_input=="P" or user_input=="S"):
          
        
        L=['R','P','S']
        comp_input=random.choice(L)
        print("computer's choice is: ",comp_input)
        if(comp_input==user_input):
           print("Draw")
        if(comp_input=="R" and user_input=="P"):
           print("You win")
        if(comp_input=="P" and user_input=="R"):
           print("You lose")
        if(comp_input=="S" and user_input=="P"):
           print("You lose") 
        if(comp_input=="P" and user_input=="S"):
           print("You win")
        if(comp_input=="R" and user_input=="S"):
           print("You lose")
        if(comp_input=="S" and user_input=="R"):
           print("You win")
    else:
       print("Invalid choice.Enter again." ) 
       game_check()      
     
print("WELCOME TO THE GAME OF ROCK-PAPER-SCISSOR")
print("\n")
game_check()
val=int(input("press 1 to play again :"))
if(val==1):
   game_check()
else:
   print("Game ends.Thank you for playing.")
   
       




                            





