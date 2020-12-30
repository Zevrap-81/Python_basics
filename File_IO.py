'Demonstrate file handling in Python'
#open an exsisting file
file_holder= open('./README.md')

#to read a line from a file
print(file_holder.readline())

#to read all the lines from the file

for line in file_holder:
    print(line)

#close a file
file_holder.close()

#writing to a file

file_holder= open("README.md", 'a')
file_holder.write("This line is written from an another program\n")
file_holder.close()

file_holder= open("README.md", 'r')
for line in file_holder:
    print(line)
file_holder.close()

#with the following methods you dont have to close the file
with open('README.md', 'r') as file_holder:
    for line in file_holder:
        print(line)

for line in open('README.md', 'r'):
    print(line)



