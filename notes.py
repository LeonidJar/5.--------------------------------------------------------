import datetime

def init_menu():
    path = 'note.json'
    data = open(path, 'a', encoding='UTF-8')

    menu = {1: 'save notes',
            2: 'show notes',
            3: 'choose by date',
            4: 'add note',
            5: 'change note',
            6: 'delete note',
            7: 'exit'}

    print('\n'.join("{}: {}".format(k, v) for k, v in menu.items()))

    n = int(input())
    print()

    if n == 1:
        print('saved')
    elif n == 2:
        read_file(path)
    elif n == 3:
        choose_by_date(path)
    elif n == 4:
        add_into_file(path)
    elif n == 5:
        change_notes_file(path)
    elif n == 6:
        delete_notes_file(path)
    elif n == 7:
        quit()

def read_file(path):
    data = open(path, 'r', encoding='UTF-8')
    print(data.read())

    data.close()
    init_menu()

def choose_by_date(path):
    data = open(path, 'a', encoding='UTF-8')

    print('Enter date')
    date = input('Enter year ')
    date += '-' + input('Enter month ')
    date += '-' + input('Enter day ')

    with open(path) as f:
        datafile = f.readlines()
    for line in range(len(datafile)):
        if date in datafile[line][datafile[line].rfind(';') :]:
            print(datafile[line])
        
    init_menu()

def add_into_file(path):
    data = open(path, 'a', encoding='UTF-8')
    with open(path) as f:
        datafile = f.readlines()
    data.write(str(len(datafile)) + ';')
    data.write(input('Enter head of note ').capitalize() + ';')
    data.write(input('Enter note ').capitalize() + ';')
    data.write('Created at ' + str(datetime.datetime.now()) + '\n')

    data.close()
    init_menu()

def change_notes_file(path):
    data = open(path, 'r+', encoding='UTF-8')
    old_data = data.read()

    print('Enter which note you want to change')
    note = input('Enter id of note ').capitalize()
    note += ';' + input('Enter head of note ').capitalize()
    with open(path) as f:
        datafile = f.readlines()
    for line in datafile:
        if note in line:
            note = line

    print('Enter new note')
    with open(path) as f:
        datafile = f.readlines()
    changed_note = str(note[0:note.index(';')])
    changed_note += ';' + input('Enter head of note ').capitalize()
    changed_note += ';' + input('Enter note ').capitalize()
    changed_note += ';Changed at ' + str(datetime.datetime.now())  + '\n'

    data.seek(0)
    data.write(old_data.replace(note, changed_note))

    data.close()
    init_menu()

def delete_notes_file(path):
    data = open(path, 'r+', encoding='UTF-8')
    old_data = data.readlines()

    print('Enter which note you want to delete')
    note = input('Enter id of note ').capitalize()
    note += ';' + input('Enter head of note ').capitalize()
    with open(path) as f:
        datafile = f.readlines()
    for line in datafile:
        if note in line:
            note = line

    for i in range(len(old_data) - 1):
        if old_data[i] == note:
            old_data.pop(i)
            print('Note deleted!')

    open(path, 'w').close()
    data = open(path, 'r+', encoding='UTF-8')
    data.writelines(old_data)

    data.close()
    init_menu()


init_menu()