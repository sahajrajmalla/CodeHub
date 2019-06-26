import random
p_h = 0
p_s = 0
st = "You have Won"
s = input("Enter start to play:")
if s == "start":
    print("TRY TO BEAT THE SYSTEM")
    i = 0
    while i < 10:
        k = ["paper", "sissor", "rock"]
        rand = random.choice(k)
        a = input("Enter Your Selection(paper, sissor, rock):\n")
        if a == "paper" and rand == "sissor":
            print(str(rand) + "\n")
            p_h += 1
            print(st+" computer score is "+str(p_s))
        elif a == "paper" and rand == "rock":
            print(str(rand) + "\n")
            p_s += 1
            print("You scored "+str(p_s))
        elif a == "paper" and rand == "paper":
            print(str(rand) + "\n")
            print("Its a Tie")
        elif a == "sissor" and rand == "paper":
            print(str(rand) + "\n")
            p_h += 1
            print("You won,you scored " + str(p_h))
        elif a == "sissor" and rand == "sissor":
            print(str(rand) + "\n")
            print("Its a Tie")
        elif a == "sissor" and rand == "rock":
            print(str(rand) + "\n")
            p_h += 1
            print(st + "computer score is" + str(p_s))
        elif a == "rock" and rand == "rock":
            print(str(rand) + "\n")
            print("Its a Tie")
        elif a == "rock" and rand == "paper":
            print(str(rand) + "\n")
            p_h += 1
            print(st + "computer score is" + str(p_s))
        elif a == "rock" and rand == "sissor":
            print(str(rand) + "\n")
            p_s += 1
            print("You won,you scored "+str(p_h))
        else:
            print("Please Enter Valid Character.")
        i += 1

if p_h > p_s:
    print("!!!YOU WON!!!")
elif p_h < p_s:
    print("!!!YOU HAVE LOST THE GAME!!!")
else:
    print("IT'S A TIE")
