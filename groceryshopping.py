store={
        'rice':{'price':450,'quantity':20},
        'oil':{'price':500,'quantity':30}
}

for key,value in store.items():
    price=value['price']
    quantity=value['quantity']
    print(key,price,quantity)

for key,value in store.items():
    print(f"item: {key} | price: {value['price']} | quantity: {value['quantity']}")

item=input("enter your item what you want to buy in store:")
quantity=int(input("enter quantity of your item:"))

if item in store:
    print(f"DEBUG:Found '{item}'.its data contains these keys: {list(store[item].keys())}")
    if quantity<=store[item]['stock']:
        store[item]['stock']-=quantity
        print(f"purchased {quantity} {item}(s)!")
    else:
        print("not enough stock")
else:
    print('item not found')

    total=price*quantity
    total_bill+=total
    print(total_bill)

