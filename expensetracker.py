import json
expenses={
          'amount':1000,'category':'food',
          'amount':2000,'category':'travel'
}

expenses={}
expenses["food"]= [1000,1500]
expenses["travel"]= [2000,2500]
print(expenses)

total=0
for category in expenses:
    for amount in expenses[category]:
     total+=amount
    print("total expense:",total)

total_category=[]
for expense in expenses:
    print(expense)
