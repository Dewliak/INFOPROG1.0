import csv

"""
check_file: ready
check_length: ready
search : ready
write_full_csv: ready
show header

add_new: ready
delete_row: ready # 
edit_row: ready #

to do list:
make show_ TIME 
the render of the things

the places where I could make it better is tagged with: &&&
"""


def check_file(file,tags):
    try:
        with open(file,'r',newline='',encoding='UTF-8'):
            pass
    except IOError:
        #print('file doesnt exits')
        with open(file,'w',newline='',encoding='UTF-8') as f:
            f.write(tags + '\n') # add kep later

#check for length
def check_if_length_right(string,max_length):
    return len(string) <= int(max_length)
    # if len(string) <= int(max_length):
    #     return True
    # else:
    #     return False


def show_header(file):
    dict_reader = csv.DictReader(open(file,'r',encoding='UTF-8'))
    return dict_reader.fieldnames


def return_column(file,column): # return the whole collumn in a list
    column_data = []
    dict_reader = csv.DictReader(open(file, 'r', newline='' ,encoding='UTF-8'), delimiter = ',')
    # check the header for the column
    if column in dict_reader.fieldnames:
        for row in dict_reader:
            column_data.append(row[column])
    else:
        print("The column doesn't exits")

    return column_data


def search_for(file,search_tag,specify=''): #kereses specify is a special tag on defualt is empty for a special tag e.g name, content, id

    def search_by_tag(x, search=str(search_tag)):
        return search in x

    with open(file, newline='', encoding = 'UTF-8') as csvfile:
        found_items = []
        reader = csv.reader(csvfile,delimiter=',')
        if specify != '' and specify in next(csvfile):
            csvfile.seek(0)
            for row in reader: # ezen van mit javitani, de meg nem talaltam jobb megoldast
                if str(search_tag) in row:
                    found_items.append(row)
                else:
                    pass
        else:
            csvfile.seek(0)
            found_items =  list(filter(search_by_tag, reader))

    return found_items


def write_full_csv(name,content): # content is a list
        with open(name,'w',encoding='UTF-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for elements in content:
                writer.writerow(elements)

# add row
def add_row(file,content): # this will append a new line
    with open(file, 'r+', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for rows in reader:
            pass
        id = 0
        ids = return_column(file, 'id')
        if len(ids) == 0:
            pass
        else:
            for i in ids:
                id = i
            id = int(id)
        id += 1

        appender = csv.writer(csvfile)
        content.insert(0, id)
        appender.writerow(content)


# edit row first we have to make the deletion
def edit_row(file,id,tag,content):
    if id == 0 or id == '0':
        print("You can't change the header.")
        return
    # if tag == "id":
    #     print("You can't change the id.")
    #     return
    try:
        data = []
        specific_row = search_for(file=file, search_tag=id, specify='id')
        reader = csv.reader(open(file,'r',encoding='UTF-8'))
        i = 0
        for row in reader: # ez a resz csunya van meg mit javitani rajta &&&
            if i == 0:
                first_row = row
                i += 1
            data.append(row)
        position = first_row.index(tag)
        writer = csv.writer(open(file, 'w', newline='', encoding='UTF-8'))
        for item in data:
            if item in specific_row:
                item[position] = content
                writer.writerow(item)
            else:
                writer.writerow(item)

    except ValueError:
        print('The tag what you wrote is invalid!')

# delete row
def delete_row(file,id): # ezen meg van mit javitani &&&
    if id == 0 or id == '0':
        print("You can't change the header.")
        return
    data = []
    specific_row = search_for(file=file,search_tag=str(id),specify='id')
    reader = csv.reader(open(file,'r',encoding='UTF-8'))
    for row in reader:
        data.append(row)
    writer = csv.writer(open(file,'w',newline='' ,encoding='UTF-8'))
    for item in data:
        if item in specific_row:
            pass
        else:
            writer.writerow(item)