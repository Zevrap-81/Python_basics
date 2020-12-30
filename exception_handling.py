'To demonstrate error handling'
x=10
#divide by zero error
try:
    y=x/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always gets printed no matter what!")

#import error
try:
    import something
except ImportError:
    print("There is no module named something!")

try: 
    y=x
except:
    print("There is an error")
else:
    print("There is no error")

#The cool thing is you can raise errors on demand with custom messages
raise TypeError("You have an error!")
