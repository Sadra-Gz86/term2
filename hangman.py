# man sadra nistam
import random
import string
import pics
letters = list(string.ascii_lowercase)
letters.append(' ')
print(letters)
animals = ['horse', 'cow', 'cat', 'elephant', 'rakoon', 'fox', 'ant', 'crow']
fruits = ['orange', 'apple', 'pineapple', 'kiwi', 'banana']
colors = ['green', 'pink', 'red', 'blue', 'cyan', 'pink']
message = "Enter category:\n1 for animals\n2 for fruits\n3 for colors\n4 to exit\n?"
a = input(message)
while a not in ['1', '2', '3', '4']:
    a = input(message)
if a == '1':
    answer = random.choice(animals)
elif a == '2':
    answer = random.choice(fruits)
elif a == '3':
    answer = random.choice(colors)
elif a == '4':
    exit()
i = 0
guess = list("?"*len(answer))
while i<7:
    print(''.join(guess))
    letter = input("Enter one of alphabet letters:").lower()
    while letter not in letters:
        letter = input("Enter one of alphabet letters:").lower()
    letters.remove(letter)
    if letter not in answer:
        print(pics.HANGMANPICS[i])
        i = i+1
    else:
        index = -1
        while True:
            try:
                index = answer.index(letter, index+1)
                guess[index] = letter
            except:
                break
        if '?' not in guess:
            print(f"You win. Answer was {answer}")
            break
if i==7:
    print(f"You lost answer was {answer}")
