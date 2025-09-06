import random
List=["rock","paper","scissor"]
score1=0
score2=0
user_name=input('Enter your Name:')
count=int(input('How many round you want to play:'))
def game_check(user1,com):
    global score1
    global score2
    combinations={'rock':'scissor','scissor':'paper','paper':'rock'}
    if user1==com:
        print('No one gets points\n')
    elif combinations[user1]==com:
        score1+=1
        print(f'{user_name} got one point\n')
    else:
        score2+=1
        print('computer got one point\n')
def game_play(user1):
    global com
    if user1 in List:
        com=random.choice(List)
        print(f"computer's turn:{com}")
        game_check(user1,com)
    else:
        print('Invalid Output\nAgain Enter Correctly:')
        user1=input(f"{user_name}'s turn:")
        user1=user1.lower()
        game_play(user1)
print("Let's start a game")
print('Enter paper/rock/scissor')
for i in range(1,count+1):
    user1=input(f"{user_name}'s turn:")
    user1=user1.lower()
    game_play(user1)
if score1==score2:
    print(f'Match Draw.Score Points are\n{user_name}:{score1}\ncomputer:{score2}')
elif score1>score2:
    print(f'{user_name} won a Match.\nScore Points are\n{user_name}:{score1}\ncomputer:{score2}')
else:
    print(f'Computer won a Match.\nScore Points are\n{user_name}:{score1}\ncomputer:{score2}')