file_name = input("Please enter the file name:")
file = open(file_name, 'r')
print(file.read())
file.close()
