# Dictionary_in_python
A Python dictionary is an implementation of the hash table,which is traditionally an unordered data structure.
Dictionaries are used to store data values in key:value pairs.
Dictionaries are written with curly brackets, and have keys and values
A dictionary is a collection which is ordered*, changeable and do not allow duplicates
Dictionaries cannot have two items with the same key
To determine how many items a dictionary has, use the len() function
It is also possible to use the dict() constructor to make a dictionary,example:
d = dict(name = "John", age = 36, country = "Norway")
print(d)
output: {'name': 'John', 'age': 36, 'country': 'Norway'}

example for dictionary:
Question:-  Initialize dictionary with default values | employees = ['Kelly', 'Emma'],
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

Methods for dictionary with their	Description:
clear():- Removes all the elements from the dictionary
copy():- Returns a copy of the dictionary
fromkeys():- Returns a dictionary with the specified keys and value
get():- Returns the value of the specified key
items():-	Returns a list containing a tuple for each key value pair
keys():- Returns a list containing the dictionary's keys
pop():-	Removes the element with the specified key
popitem():-	Removes the last inserted key-value pair
setdefault():- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update():- Updates the dictionary with the specified key-value pairs
values():- Returns a list of all the values in the dictionary
