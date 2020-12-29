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

#string substitution 
print("The names of friends are {0},{2},{1}".format(name2, name3, name4))