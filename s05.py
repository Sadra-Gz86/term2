s = 0
for i in range(100): 
    a = int(input(f"Enter item {i+1} price: "))
    s = s+a
    if a==0:
        break

print(f"Jam poole factor shoma: {s}")