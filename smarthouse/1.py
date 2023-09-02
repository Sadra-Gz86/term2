from asc import *
from random import choice
from time import sleep
import pygame
# from termcolor import colored, cprint

player = pygame.mixer
player.init()



def play(pc, user):
    if pc==user:
        print(tv_draw)
    elif (pc, user) == ('r', 's') or (pc, user) == ('s', 'p') \
    or (pc, user) == ('p', 'r'):
        print(tv_lose)
    else:
        print(tv_win)
        

def rsp():
    pc_choice = choice(['r', 's', 'p'])
    user_choice = input("Enter r for rock\nEnter s for scissors\nEnter p for paper:")
    while user_choice not in ['r', 's', 'p']:
        user_choice = input("Choose again:")
    play(pc_choice, user_choice)
    answer = input("Want to play again?")
    if answer == 'y':
        rsp()
    else:
        main_function('tv')

def get_item(items):
    temp = input(f"{items}")
    while temp not in items:
        temp = input(f"{items}")
    return temp
def main_function(item):
    if item == 'exit':
        exit()
    elif item == 'game':
        rsp()
    elif item == 'sleep':
        player.music.load('2.mp3')
        player.music.play()
        for i in range(1, 6):
            print(f"sleeping for {i} seconds")
            sleep(1)
        player.music.stop()
        main_function('bedroom')
    elif item in foods and item not in ['exit', 'kitchen']:
        player.music.load('1.mp3')
        print(names[item])
        foods.remove(item)
        player.music.play()
        sleep(1)
        main_function('fridge')
    print(names[item])
    item = get_item(actions[item])
    main_function(item)

foods = ['cheese', 'drink', 'egg', 'cake', 'apple',
 'icecream', 'chocolate', 'exit', 'kitchen']
names = {
    'out'       : out,
    'salon'     : salon,
    'house'     : salon,
    'kitchen'   : kitchen,
    'bedroom'   : room,
    'tv'        : television,
    'tv_off'    : television,
    'tv1'       : tv1,
    'tv2'       : tv2,
    'tv3'       : tv3,
    'tv4'       : tv4,
    'remote'    : remote,
    'apple'     : apple,
    'chocolate' : chocolate,
    'cake'      : cake,
    'icecream'  : icecream,
    'egg'       : egg,
    'drink'     : drink,
    'cheese'    : cheese,
    'fridge'    : Refrigerator,
}

actions = {
    'out'       : ['house', 'exit'],
    'salon'     : ['kitchen', 'bedroom', 'tv', 'exit'],
    'house'     : ['kitchen', 'bedroom', 'tv', 'exit'],
    'kitchen'   : ['salon', 'macrofer', 'fridge', 'exit'],
    'bedroom'   : ['salon', 'lamp', 'sleep', 'exit'],
    'tv'        : ['game', 'salon', 'remote', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'tv_off'    : ['game', 'salon', 'remote', 'tv1', 'tv2', 'tv3', 'tv4', 'exit'],
    'tv1'       : ['game', 'salon', 'remote', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv2'       : ['game', 'salon', 'remote', 'tv1', 'tv3', 'tv4', 'tv_off', 'exit'],
    'tv3'       : ['game', 'salon', 'remote', 'tv1', 'tv2', 'tv4', 'tv_off', 'exit'],
    'tv4'       : ['game', 'salon', 'remote', 'tv1', 'tv2', 'tv3', 'tv_off', 'exit'],
    'remote'    : ['game', 'salon', 'tv1', 'tv2', 'tv3', 'tv4', 'tv_off', 'exit'],
    'fridge'    : foods
}

main_function('out')
