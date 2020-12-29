my_list= list()
print(my_list)

my_list.append('x')
my_list1=['x']
my_list2= ['a', 'b', "name"]

my_list.extend(my_list2)
my_list1+= my_list2

print(my_list)
print(my_list1)

my_list= [2,1,4,6,1,3,7,0,3,9,0,8,2,5,10,9]

my_list= list(set(my_list))     #removing duplicates
my_list.sort()                  #sorting
print(my_list)

#dictionaries 
my_dict= {'key1':'value1', 'key2':'value2', 'key3': 'value3'}

for key in my_dict:
    print(my_dict[key])

#iterate over keys and values
my_dict= {values:keys for keys,values in my_dict.items()} #swaps values for keys
print(my_dict)
