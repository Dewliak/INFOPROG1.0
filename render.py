import csv
# make a table:
#

"""
..............................
.id,
.   name
.   content
.   kesobb majd kep
................................

"""

def render_table(file):
    with open(file,'r', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            if i == 0:
                header = row
                line = '+'
                line += '-' * 35 + '+'
                i += 1
            else:
                print(line)
                for j in range(len(row)):
                    print(f'|{header[j]}: {row[j]}')
        print(line)


def render_choices(choices): # choices is a list of full of strings
    string = '|'
    for elements in choices:
        string += ' '*2 + str(elements) + ' ' * 2 + '|'
    row = '+' + '-' * (len(string) - 2) + '+'
    print(row + '\n' + string + '\n' + row)

"""
+-------------------------------------------------+
|  add  |  edit  |  delete  |  show_list |  exit  |
+-------------------------------------------------+

"""