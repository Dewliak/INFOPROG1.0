from universal_tools import *
import csv

class ShowManager():
    def __init__(self,file):
        self.file = file
        check_file(self.file, 'id,name,content')


    def add_show_manager(self):
        while True:
            name = (input('Give a name (max: 50): ')).strip()  # check if len name =< 50
            content = (input('Give the content (max: 300): ')).strip()  # chek if len leiras =< 300
            if check_if_length_right(name, 50) and check_if_length_right(content, 300):
                break
            else:
                print('The name or the content is too long.')
        add_row(file=self.file, content=[name, content])


class Show():
    def __init__(self,file,file_manager):
        self.file = file
        self.file_manager = file_manager
        check_file(self.file,'id,title,content,manager_id')

    def add_show(self):
        while True:
            column_id = return_column(file=self.file_manager, column='id')
            title = (input('Give a title to the show (max:50): ')).strip()  # check if len name =< 50
            content = (input('Write about the show (max:300): ')).strip()  # chek if len leiras =< 300
            print(column_id)
            manager_id = (input('The showrunners id:  ')).strip()
            if check_if_length_right(title, 50) and check_if_length_right(content, 300):
                if manager_id in column_id:
                    break
            else:
               print('The title, the content or the id is invalid.')
        add_row(file=self.file, content=[title, content,manager_id])
