menu={
      'pizza':500,
       'burger':250,
       'french fries':150,
       'tea':20
}
for item in menu:
    print(item, ': ', menu[item])

item_name=input("can you please order your item?")
quantity=int(input("enter how much quantity (numbers only)"))

if item_name in menu:
    cost=menu[item_name]*quantity
    total_bill=0
    total_bill += cost
    print("item added successfully")
    print("your cost is ",cost)
    print("total bill is ",total_bill)
else:
    print("item is not available")



choice=input("do you want to order another item?(y/n)")
if choice=='n':
    print("Thank you for your order")

    print("total bill is ",total_bill)
