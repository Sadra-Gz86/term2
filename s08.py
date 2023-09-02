price = int(input("Enter price: "))
s =0 
while price>100:
    print(price)
    price = int(input("Enter price: "))
    s = s+price
print(s)