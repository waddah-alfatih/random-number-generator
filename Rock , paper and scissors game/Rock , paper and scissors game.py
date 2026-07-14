# Rock , paper and scissors game 
# take an input from user ( r, p , s ) and transform it to lower case
# if any input else print invalid message
# print the user choice and the computer choice
# use if loop to put the low and determine the winner
# ask the user if he'she want to play agane (break the loop if you get "no")


import random

while True :
    
    choices =("r" , "p" , "s")
    
   
    user_choices = input("let's play rock , paper or scissors \n choose (r, p or s) to start").lower()
    
    if user_choices not in choices :
      print ("invalid choice : you should choose r , s or p")
      continue
    
    computer_choice = random.choice(choices)
    
    print(f"you choose : {user_choices}")
    print(f"computer choose : {computer_choice}")
    
    if user_choices == computer_choice :
     print (" Oooh! it's a drow : let's try again")
    
    
    elif (user_choices == "r" and computer_choice =="s" or
          user_choices == "s" and computer_choice == "p" or
          user_choices == "p" and computer_choice == "r"  ) :
        print ("you won")
        more= input("do u wanna play again ?! (yes / no)")
        if more == "no" :
          break 
        
    else :
      print ("computer won")
      more= input("do u wanna play again ?! (yes / no)")
    if more == "no" :
          break 