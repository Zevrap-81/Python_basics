print("This is a string")

# a multi line string
print(""" 
This 
    is a 
        Multi-line 
                String!""")

# Getting an input
# name= input("What is your name?")
# print("The name is %s" % name)

# joining strings with some seperator
name1= "Parvez"
name2= "Sneha"
name3= "Omar"
name4= "Mazin"

print(",".join([name1,name2, name3, name4]))

#list of all built in string methods
dir("")

print("     This string has no blanks!      ".strip())

# string is just as a immutable list 
print("print 'Only'"[-6:])

# the code below is taken from https://docs.python.org/3/library/string.html
#string substitution and text formatting 
print("The names of friends are {0},{2},{1}".format(name2, name3, name4))
point= (3,2)
print("x_cord:{0[0]}, y_cord: {0[1]}".format(point)) ## accessing the arguments

print("{:<30}".format("left aligned"))
print("{:>30}".format("right aligned"))
print("{:^30}".format("centered"))
print("{:-^30}".format("centered"))

print("{:,}".format(1234567890))    ## using comma as a thousands seperator

print("Percentage(correct upto 4th decimal): {:.4%}".format(4567890/7684234))

#type formatting
import datetime
d= datetime.datetime(2020, 12, 27, 18, 30, 55)
print("the date and time is {: %d.%m.%Y %H:%M:%S}".format(d))
