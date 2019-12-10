import numpy as np
x=("\n1.ROCK \n2.PAPER \n3.SCISSORS")


print(x)
player_choice=int(input("PICK YOUR CHOICE :"))

if player_choice==1:
    comp_choice=np.random.randint(1,4)
    if comp_choice==2:
        print("PAPER....!!!YOU LOSE")
    elif comp_choice==player_choice:
        print("ITS A TIE...!!!")
    else:
        comp_choice==3
        print("SCISSORS...!!!YOU WIN")
if player_choice == 2:
    comp_choice = np.random.randint(1,4)
    if comp_choice == 1:
        print("ROCK....!!!YOU WIN")
    elif comp_choice==player_choice:
        print("ITS A TIE...!!!")
    else:
        comp_choice == 3
        print("SCISSORS...!!!YOU LOSE")
if player_choice==3:
    comp_choice=np.random.randint(1,4)
    if comp_choice==1:
        print("ROCK....!!!YOU LOSE")
    elif comp_choice==player_choice:
        print("ITS A TIE...!!!")
    else:
        comp_choice==2
        print("PAPER...!!!YOU WIN")
