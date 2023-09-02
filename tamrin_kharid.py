from datetime import datetime

def add_item(n, i, p):
    f = open('mordad.txt', 'a')
    f.write(f"Item is: {i:30} Price is: {p:10}\
 date and time is: {n.year}-{n.month}-{n.day}\t{n.hour:02}\
:{n.minute:02}:{n.second:02}\n")
    f.close()

answer='y'
while answer not in ['no', 'na', 'n']:
    now = datetime.now()
    item = input("Enter item: ")
    price = input("Enter price: ")
    add_item(now, item, price)
    answer = input("Want to add another item? ")

