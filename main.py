#Rock paper scissors game utilizing nested if loops:
player_1 = input('''
-----------------------------------
Welcome to Rock paper scissors game!
------------------------------------
You are player one, please pick one:
------------------------------------
Rock(r)
Paper(p)
Scissors(s)
''')
player_2 = input('''
------------------------------------
You are player two, please pick one:
------------------------------------
Rock(r)
Paper(p)
Scissors(s)
''')
if player_1 == "r":
    if player_2 == "r":
        print("Player one's rock has bumped into player two's rock, it's a draw! ")
    elif player_2 == "p":
        print("Paper has wrapped up the rock, player 2 wins!")
    elif player_2 == "s":
        print("Rock has smashed up the scissors, player 1 wins!")
    else:
        print("Player two has made an invalid move!")
elif player_1 == "p":
    if player_2 == "r":
        print("Paper has wrapped up the rock, player 1 wins! ")
    elif player_2 == "p":
        print("Both have picked paper, it's a draw!")
    elif player_2 == "s":
        print("Scissors have cut up the paper into pieces, player 2 wins!")
    else:
        print("Player two has made an invalid move!")
elif player_1 == "s":
    if player_2 == "r":
        print("Rock has smashed up the scissors, player 2 wins!")
    elif player_2 == "p":
        print("Scissors have cut up the paper into pieces, player 1 wins!")
    elif player_2 == "s":
        print("Both of you have picked scissors, it's a draw!")
    else:
        print("Player two has made an invalid move!")
else:
    print("Player one has made an invalid move!")

