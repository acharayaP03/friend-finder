
# Reading files

my_files = open('data.txt', 'r')
file_contents = my_files.read()

my_files.close()
print(file_contents)


user_name = input('Enter your name: ')
my_file = open('data.txt', 'w')
my_file.write(user_name)

my_file.close()

