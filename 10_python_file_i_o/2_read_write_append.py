# doing it this way is more common and now you no longer need to worry about closing the file with .close

# standard way to read a file
with open('test.txt') as my_file:
    print(my_file.readlines())

# mode default is 'r' which is read. it is the second argument of open so you can specifcy what you would like to be able to do.

# behaviors of read, write, append
# read just reads the file
# write writes to the file and overrides what is there, it assumes it is a new file so overwrites because of that. write will also create a new file if it doesn't already exist.
# read/write reads the file and writes but when it writes it starts at character 0 and will overwrite what exists.
# append will write to the end of the file. will also create a file if it doesn't exist.

# r - read
# w - write
# r+ - read and write
# a - append

# caveat - it writes text wherever the cursor is at. So it can write over text that already exists.
# note that because we are doing the open statment above on line 4-5 the cursor is at the end of the file so will just add to the end of the line of text rather than overwriting.
# if you change test.txt to a file that doesn't exist and use mode='w' you will create a new file as well as write to it. also you can create .py files or other types not just .txt files.
with open('test.txt', mode='r+') as my_file:
    text = my_file.write("hey it's me")
    # 11 - this is the number of characters that were "written".
    print(text)
    print(my_file.readlines())


# FILE PATHS
# where test.txt is, you can simply add the correct path name. like if file is in a folder, you can just use app/test.txt if it's in an app folder. this is a relative path. can also do ./app/sad.txt. ./ just means from our current place.

# since the paths are different based on machine you are using, windows, linux, mac you can use a library called pathlib that comes with python
# https://docs.python.org/3/library/pathlib.html


# FILE IO ERRORS
try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
