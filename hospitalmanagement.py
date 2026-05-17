patients={
          101:{'name':'ravi','age':45,'disease':'fever'},
          102:{'name':'harsha','age':23,'disease':'cold'},
          103:{'name':'ramesh','age':35,'disease':'heart'}
}

doctors={
         'fever':'dr.mehta',
          'cold':'dr.surya',
           'heart':'dr.subbu'
}
patient = input("what is your id?")
disease=input("enter your disease?")
while True:
    if disease in doctors:
        assigned_doctor=doctors[disease]
        print(f"{patient} is assigned to {assigned_doctor}")
    consultation_fee=600
    room_charges=500
    cost=consultation_fee+room_charges
    print("your cost is ",cost)
    test=input("would you like to do any other tests?(y/n)")
    if test=="y":
        extra_charges=150
        extra_charges=extra_charges+cost
        print("your extra charges is ",extra_charges)
    else:
        print("thank you")
    break