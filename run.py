from management import *
from render import *
from os import system

while True:
    system('cls')
    print(logo)
    t = False
    render_choices(['Managers', 'Shows', 'ShowTimes', 'Playlist', 'Exit'])
    choice = input('')
    if choice.lower() == 'managers':
        while True:
            t =user_input(['add', 'edit', 'delete', 'list', 'back'], show_manager)
            if t == True:
                break
    elif choice.lower() == 'shows':
        while True:
            t = user_input(['add', 'edit', 'delete', 'list', 'back'], show)
            if t == True:
                break
    elif choice.lower() == 'showtimes':
        while True:
            t = user_input(['add', 'edit', 'delete', 'list', 'back'], show_time)
            if t == True:
                break
    elif choice.lower() == 'playlist':
        while True:
            t = user_input(['add', 'back'], playlist)
            if t == True:
                break
    elif choice.lower() == 'exit':
        exit()