import csv
from universal_tools import *

days_of_week = {
    '1' : 'Hetfo',
    '2' : "Kedd",
    '3' : "Szerda",
    '4' : "Csutortok",
    '5' : "Pentek",
    '6' : "Szombat",
    '7' : "Vasarnap"
}

def check_time_format(data):
    time = data.split(':')
    if ':' not in data:
        print(": is not in the data")
        return False
    if int(time[0]) < 0 or int(time[0]) > 23:
        print('Hour is invalid')
        return False
    if int(time[1]) < 0 or int(time[1]) > 59:
        print('Minutes are invalid')
        return False
    return True

def check_time(data):
    """"Return time in seconds, if the time is in format 23:59"""
    new_data = data.split(':')
    time = int(new_data[0]) * 3600 + int(new_data[1]) * 60
    return time

class ShowTime():
    def __init__(self,file,file_show):
        self.file = file
        self.file_show = file_show
        check_file(self.file, 'id,day,start,end,show')

    def add_show_time(self):
        while True:
            day = input('Which day 1-7 ')
            if int(day) < 1 or int(day) > 7:
                print('Incorrect')
            else:
                break
        while True:
            start = input('The starting time(format: 23:59): ')
            end = input('The ending time(format: 23:59): ')
            if check_time_format(start) and check_time_format(end):
                if check_time(start) < check_time(end):
                    break
                else:
                    print('Start is later then the end')
            else:
                pass
        print(return_column(file=self.file_show, column = 'id'))
        while True:
            show = input('What which show do you want to add?: ')
            if show in return_column(file=self.file_show, column='id'):
                break
            else:
                print('Invalid show.')
        # add alert if time is already locked
        add_row(self.file,[days_of_week[day],start,end,show])

#if __name__ == "__main__":
#    ShowTime.add_show_time()