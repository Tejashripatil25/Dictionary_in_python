""""""
"""
1.Convert two lists into a dictionary |
keys= ['Ten','Twenty','Thirty'],values=[10,20,30] expected o/p: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys= ['Ten','Twenty','Thirty']
values=[10,20,30]
d = dict(zip(keys,values))
print(d)
============================================================================
2.Merge two Python dictionaries into one |dict1={'Ten': 10, 'Twenty': 20, 'Thirty': 30},
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
expected o/p: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print("after updating :")
print(dict1)

##Ans2
dict3 = dict1.copy()
for key, value in dict2.items():
    dict3[key] = value
print(dict3)
===========================================================================
3.Print the value of key ‘history’ from the below dict |
dict1= {"class":{"student":{"name": "Mike","marks":{"physics": 70,"history": 80}}}} expected o/p: 80

print(dict1['class']['student']['marks']['history'])
==========================================================================
4.Initialize dictionary with default values | employees = ['Kelly', 'Emma'],
defaults = {"designation": 'Developer', "salary": 8000}, expected o/p:

{'Kelly':{'designation':'Developer','salary':8000},'Emma':{'designation':'Developer','salary':8000}}
answer:-
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d = {}
d1 = {}
key = [employees[0]]
d = d.fromkeys(key,defaults)
key2 = [employees[1]]
d1 = d1.fromkeys(key2,defaults)
d.update(d1)
print(d)
==========================================================================
5.Delete a list of keys from a dictionary |
dict1={"name":"Kelly","age": 25,"salary": 8000,"city": "New york"}
# following Keys to remove,  keys = ["name", "salary"]  expected o/p:{'city': 'New york', 'age': 25}.

dict1={"name":"Kelly","age": 25,"salary": 8000,"city": "New york"}
dict1.pop('name') and dict1.pop('salary')
print(dict1)
=======================================================================
6.Check if a value exists in a dictionary |dict1 = {'a': 100, 'b': 200, 'c': 300}
expected  o/p: 200 present in a dict

dict1 = {'a': 100, 'b': 200, 'c': 300}
if 200 in dict1.values():
    print("200 present in dictionary")
else:
    print("200 is not present in dictionary")
========================================================================
7.Rename key of a dictionary |sample_dict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
expected o/p:{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
sample_dict.pop('city')
sample_dict.update({'location':'New york'})
print(sample_dict)
=======================================================================
8.Change value of a key in a nested dictionary |
dict1= {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 500}}  expected o/p: {'emp1':{'name':'Jhon','salary':7500},
'emp2':{'name':'Emma','salary':8000},'emp3':{'name':'Brad','salary': 8500}}

dict1= {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}}
dict1['emp3']['salary'] = 8500
print(dict1)
========================================================================
9.Write a Python program to concatenate following dictionaries to create a new one|
dic1={1:10, 2:20},dic2={3:30, 4:40},dic3={5:50,6:60}
expected o/p: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
=======================================================================
10.Add a key to a dictionary | d = {0:10, 1:20}  expected o/p: {0: 10, 1: 20, 2: 30}

d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)
======================================================================
11.Print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.
expected o/p: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81,
10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

d = dict()
for value in range(1,16):
    d[value] = value**2
print(d)
==========================================================================
12.Write a Python program to iterate over dictionaries using for loops.
d = {'Red': 1, 'Green': 2, 'Blue': 3}expected
o/p: Red corresponds to 1 Green corresponds to  2  Blue corresponds to  3

d = {'Red': 1, 'Green': 2, 'Blue': 3}
for key, value in d.items():
    print(key,"corresponds to", value,end=',')
========================================================================
13.Write a Python program to sum all the items in a dictionary.|
my_dict = {'data1':100,'data2':-54,'data3':247} expected o/p:293

##ans1
print(sum(my_dict.values()))

##ans2
my_dict = {'data1':100,'data2':-54,'data3':247}
c = 0
for value in my_dict.values():
    c+=value
print(c)
========================================================================
14.Write a Python program to multiply all the items in a dictionary. |
my_dict = {'data1':100,'data2':54,'data3':247} expected o/p:1333800

my_dict = {'data1':100,'data2':54,'data3':247}
c = 1
for value in my_dict.values():
    c*=value
    print(c)
========================================================================
15.Write a Python program to convert given a dictionary to a list of tuples.  |
d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
expected o/p: [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
d1 = list(zip(d))
print(d1)
========================================================================
16.Write a Python program to invert a dictionary with unique hashable values.|
s = {'Theodore': 10,'Mathew': 11,'Roxanne': 9}expected o/p: {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}

ans 1:
s = {'Theodore': 10,'Mathew': 11,'Roxanne': 9}
print({value: key for key, value in s.items()})

ans2:
s = {'Theodore': 10,'Mathew': 11,'Roxanne': 9}
def sample(s):
    return {value: key for key, value in s.items()}
print(sample(s))
========================================================================
17.Write a Python program to access dictionary key's element by index.|
num = {'physics': 80, 'math': 90, 'chemistry': 86}
expected o/p: physics  math  chemistry

num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])
========================================================================
18.A Python Dictionary contains List as value.
Write a Python program to clear the list values in the said dictionary.
expected o/p: {'C1': [], 'C2': [], 'C3': []}

key = ['c1','c2','c3']
value = [[],[],[]]
d = dict(zip(key,value))
print(d,end='')
========================================================================
19.Write a Python program to drop empty Items from a given Dictionary.|
dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}  expected o/p: {'c1': 'Red', 'c2': 'Green'}

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
print({key:value for (key, value) in dict1.items()if value is not None})
"""
