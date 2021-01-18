from show_managment import *
from render import *
from playlist import Playlist
from os import system
from show_time_management import ShowTime

#needed objects
show_time = ShowTime('show_time.csv','shows.csv')
playlist = Playlist('zenek.csv')
show = Show('shows.csv','show_managers.csv')
show_manager = ShowManager('show_managers.csv')



# def adding(file):
#     header = show_header(file)
#     content = []
#     header.pop(0)
#     for item in header:
#         temp = input(f'{item}: ')
#         content.append(temp)
#     add_row(file=file,content=content)


def deleting(file):
    render_table(file)
    id = int(input('Which element do you want to delete? (give the id) '))
    delete_row(file,id)



def editing(file):
    render_table(file)
    id = int(input('What is the id of the element what you want to edit: '))
    tag = input('What tag do you want to edit: ')
    content = input('What do you want to replace with: ')
    edit_row(file=file, id=id,tag=tag,content=content)


def listing(file):
    render_table(file)


def back(file):
    return True


"""
UPDATE IT: to be able to work as object, example 'add': add => object.add(), this not works for now. 
If this works this will be almost fully OOP.
"""

# add_functions = {'add_show':show.add_show,
#              'add_manager':show_manager.add_show_manager,
#              'add_showtime':show_time.add_show_time,
#              'add_playlist':playlist.random_music
# }


add_functions = {
"<class 'show_managment.Show'>":show.add_show,
"<class 'show_managment.ShowManager'>":show_manager.add_show_manager,
"<class 'show_time_management.ShowTime'>":show_time.add_show_time,
"<class 'playlist.Playlist'>":playlist.random_music,
}

functions = {'edit':editing,
             'delete':deleting,
             'list':listing,
}

def user_input(choices,object): # &&&
    render_choices(choices)
    choice = input('')
    if choice == 'back':
        system('cls')
        return True
    try:
        if 'add' in choice:
            system('cls')
            add_functions[str(type(object))]()
        else:
            system('cls')
            functions[choice](object.file)
    except KeyError:
        print("You've got the wrong key.")


logo = '''
.______          ___       _______   __    ______      .___  ___.      ___      .__   __.      ___       _______  _______ .______      
|   _  \        /   \     |       \ |  |  /  __  \     |   \/   |     /   \     |  \ |  |     /   \     /  _____||   ____||   _  \     
|  |_)  |      /  ^  \    |  .--.  ||  | |  |  |  |    |  \  /  |    /  ^  \    |   \|  |    /  ^  \   |  |  __  |  |__   |  |_)  |    
|      /      /  /_\  \   |  |  |  ||  | |  |  |  |    |  |\/|  |   /  /_\  \   |  . `  |   /  /_\  \  |  | |_ | |   __|  |      /     
|  |\  \----./  _____  \  |  '--'  ||  | |  `--'  |    |  |  |  |  /  _____  \  |  |\   |  /  _____  \ |  |__| | |  |____ |  |\  \----.
| _| `._____/__/     \__\ |_______/ |__|  \______/     |__|  |__| /__/     \__\ |__| \__| /__/     \__\ \______| |_______|| _| `._____|

'''

#while True:
#    user_input(['add_showtime','edit','delete','list','exit'], show_time)
#editing(show_manager.file)