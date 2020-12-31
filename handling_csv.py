import csv
'reading a csv file'
def csv_reader(file_obj):
    reader= csv.reader(file_obj, delimiter=',')
    for row in reader:
        print(" ".join(row))

'creating a dictionary from csv'
def csv_dict(file_obj):
    reader= csv.DictReader(file_obj, delimiter=',')
    local_dict={key:[] for key in reader.fieldnames}
    for line in reader:
        for key in reader.fieldnames:
            local_dict[key].append(line[key])
    print(local_dict)

'creating a dialect'
def csv_dialect_reader(file_obj):
    csv.register_dialect('colon', delimiter=';')
    reader= csv.reader(file_obj, dialect='colon')
    for row in reader:
        print(row)

'write to a csv file '
def csv_writer(file_obj, data):
    writer= csv.writer(file_obj, delimiter=';')
    writer.writerows(data)

'write a dictionary to csv'
def csv_dict_writer(file_obj, field_names, data):
    writer= csv.DictWriter(file_obj, delimiter=';', fieldnames= field_names)
    writer.writeheader()
    for line in data:
        writer.writerow(line)


if __name__== '__main__':
    print(dir(csv))          #List all the methods in csv module 
    print(help(csv.Dialect))  #List the class Dialect

    with open("data.csv","r") as file_obj:
        csv_reader(file_obj)
        csv_dict(file_obj)

    with open('test_data.csv', 'r') as file_obj:
        csv_dialect_reader(file_obj)
    
    data=[['S.No','Col1','Col2'],
        ['1','Parvez','Sneha'],
        ['2','Zaki','Tulin']]

    csv_writer(open('test_data.csv', 'w'), data)
    csv_dialect_reader(open('test_data.csv'))

    field_names=data[0]
    my_list=[]
    for values in data[1:]:
        local_dict= dict(zip(field_names, values))
        my_list.append(local_dict)
    
    csv_dict_writer(open('test_data.csv', 'w'), field_names, my_list)
    csv_dialect_reader(open('test_data.csv'))
    