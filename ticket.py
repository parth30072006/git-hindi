age = int(input("enter age"))
day = (input("enter day"))

price=12 if age>=18 else 8

if day =="wednessday":
    price=price-2

print(price)