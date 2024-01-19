#!/usr/bin/python3
''' This Module contain append_after Function. '''


def append_after(filename="", search_string="", new_string=""):
    '''
    Function that inserts a line of text to a file,
    after each line containing a specific string.
    '''
    # Read data
    with open(filename) as f:
        data = f.readlines()

    # Modify in Data readed
    for i in range(len(data)):
        for j in range(data[i].count(search_string)):
            data.insert(i+j+1, new_string)

    # update Data in file
    with open(filename, 'w') as f:
        f.write(''.join(data))
