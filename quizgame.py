correct_username='@harsha_3456'
username=input("enter your username")
password=input("enter your password")

if correct_username==username:
    print("login successful")
else:
    print("invalid username")

Questions=[
    {"q":"what is  2+3?",
     "optins":"a.6,b.5,c.7",
     "ans":'b'},
    {"q":"what is 2*4?",
     "optins":"a.8,b.9,c.7",
     'ans':'a'},
    {"q":"what is 3*4?",
     "optins":"a.12,b.9,c.5",
     'ans':'a' }
]
scores=0
for q in Questions:
    print("\n"+q["q"])
    for opt in q["optins"]:
         print(opt)
    user_ans=input("enter your answer:")
    if 'user_ans'=='correct':
        print("correct")
        scores=scores+1
    else:
        print("incorrect")

print("your final score is",scores)