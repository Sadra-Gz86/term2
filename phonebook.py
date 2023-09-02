contacts = {
    'baba': '09112365474'
}
name = ''
while name!= 'end':
    name = input("Enter name: ")
    if name in contacts:
        print(contacts.get(name))
    else:
        a = input("Not in contacts. Want to add?")
        if a=='yes':
            number = input("Enter number: ")
            contacts[name]=number

file = open('contacts.txt', 'w') # w write       # r read       # a append
file.write(str(contacts))
