import random
List=["rock","paper","scissor"]
score1=0
score2=0
print("Let's Welcome to Rock-Paper-Scissor Game")

def player():
    try:
        user=int(input('Enter 1 to play with Computer or Enter 2 to play with Player2'))
        if user==1:
            user1=input('Enter your Name:')
            user2='Computer'
            return user1,user2
        elif user==2:
            user1=input('Enter your User 1 Name:')
            user2=input('Enter your User 2 Name:')
            return user1,user2
        else:
            print('Invalid Input.Enter Correctly.')
            return player()
    except Exception as e:
            print('Invalid Input.Enter Correctly.')
            return player()

def game_check(data1,data2):
    global score1
    global score2
    combinations={'rock':'scissor','scissor':'paper','paper':'rock'}
    if data1==data2:
        print('No one gets points\n')
    elif combinations[data1]==data2:
        score1+=1
        print(f'{user1} got one point\n')
    else:
        score2+=1
        print(f'{user2} got one point\n')

def game_play(user1,user2):

    def input_user1():
        print(f"{user1}'s Turn")
        data1=input('Enter rock/paper/scissor:')
        User1=validate(data1)#data checking
        if User1==True:
            return data1
        else:
            print('Enter Valid Input: Rock/Paper/Scissor')
            return input_user1()
    def input_user2():
        if user2=='Computer':
            data2=random.choice(List)
            print(f"Computer's turn:{data2}")
            return data2
        else:
            print(f"{user2}'s Turn")
            data2=input('Enter rock/paper/scissor:')
            User2=validate(data2)#data checking
            if User2==True:
                return data2
            else:
                print('Enter Valid Input: Rock/Paper/Scissor')
                return input_user2()
    data1=input_user1()
    data2=input_user2()
    game_check(data1,data2)
def validate(data):
    if data in List:
        return True
    else:
        return False
def main():
    global user1
    global user2
    user=player()
    user1=user[0]
    user2=user[1]
    print(user1,'vs',user2)
    count=int(input('How many round you want to play:'))
    print("Let's start a game")
    print('Enter paper/rock/scissor in upper case or lower case')
    for i in range(1,count+1):
        game_play(user1,user2)
    if score1==score2:
        print(f'Match Draw.Score Points are\n{user1}:{score1}\n{user2}:{score2}')
    elif score1>score2:
        print(f'{user1} won a Match.\nScore Points are\n{user1}:{score1}\n{user2}:{score2}')
    else:
        print(f'{user2} won a Match.\nScore Points are\n{user1}:{score1}\n{user2}:{score2}')
main()
