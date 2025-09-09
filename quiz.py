import pandas as pd
import random
df=pd.read_excel("states.xlsx")
row_size=df.shape[0]
states=df['States']
capital=df['Capital'].str.strip().str.lower().tolist()
capital_original=df['Capital']
def quiz():
    score=0
    skipped=0
    missed=0
    print('Welcome to Quiz Game')
    user_name=input('Enter Your Name')
    print(f'Total {row_size} Questions You need to Answer. Each Question Carries one point.')
    try:
        for i in range(row_size):
            print(f'What is the Capital of {states[i]} ?')
            answer=input('Enter Your Answer:')
            answer=answer.lower()
            if answer=='':
                skipped+=1
            elif answer==capital[i].lower():
                print('Correct Answer!')
                score+=1
            else:
                print(f'You Missed it. Answer is {capital_original[i]}')
                missed+=1
        print(f'You Answered {score+missed} Questions. Correct Answer: {score} Wrong Answer: {missed} Skipped: {skipped}')
    except Exception as e:
        print(e)
quiz()