# File I/O
# reading and writing files we take a file as input and output the file

my_file = open('test.txt')

# allows you to read the file using .read()
# the open function has the idea of a cursor. You can read the file once. Once read() has been called, the "cursor" is now at the end of the file so if you do .read() a second time nothing will happen.

print(my_file.read())
# will give you nothing because cursor is at the EOF as it has been read once already, a blank line  will print
print(my_file.read())

# seek will go to a specific portion of the file 0 in this case indicates beginning of the file
my_file.seek()
# now the file will be read again as the cursor is basck to the beginning
print(my_file.read())

# this will give you one line at a time. However, it will repeat the same line if there are multiple lines so would have to copy paste for each line in file.
my_file.readline()

# by adding the "s" you will get a list with all the lines in the file
my_file.readlines()

# need to close the file after you are done using it.
my_file.close()
