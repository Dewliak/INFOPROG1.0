import random
import csv
import datetime
from universal_tools import search_for,write_full_csv

class Playlist():

    def __init__(self,file):
        self.file = file

    def random_music(self):

        now = datetime.datetime.now()
        playlist = []

        with open(self.file, 'r', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile)
            tags = []
            next(csvfile)
            for row in reader:
                elements = row[5].split(';')
                for element in elements:
                    if element not in tags and element:
                       tags.append(element)
                    else:
                        pass
            print(tags)
            while True:
                searchtag = input('What music tags ')
                found_items = search_for(search_tag=searchtag, file=self.file)
                choice = input(f'How many numbers do you want to be in a playlist (max:{len(found_items)}):')
                if int(choice) <= len(found_items):
                    break
                else:
                    print('The input is incorrect.')
            random.shuffle(found_items)
            for i in range(int(choice)):
                playlist.append(found_items[i])
            write_full_csv(now.strftime(f'{searchtag}-{choice}-%Y-%m-%d-%H-%M.lista'),playlist)
            return playlist

