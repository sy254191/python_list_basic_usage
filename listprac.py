Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
>>> #list is  just like array in c but with a diffrence that it can input value of various data types. the value store in the list can be accessed using the slice operator([] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1.
>>> #it one of Standard  data type of the python
>>> #this is written as per tutorialpoint.com
>>> #now some example of list
>>> list1=['ph','che',1,2]
>>> print(list1)
['ph', 'che', 1, 2]
>>> print(list[0])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(list[0])
TypeError: 'type' object is not subscriptable
>>> print(list1[0])
ph
>>> print(list[0:2])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(list[0:2])
TypeError: 'type' object is not subscriptable
>>> print(list1[0:2])
['ph', 'che']
>>> #updating lists
>>> list1[2]=99
>>> print(list1)
['ph', 'che', 99, 2]
>>> print(list1[])
SyntaxError: invalid syntax
>>> #delete list elements
>>> del list1[2]
>>> print(list1)
['ph', 'che', 2]
>>> len(list1)
3
>>> #basic list operation
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> list2(5)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list2(5)
NameError: name 'list2' is not defined
>>> list2[5]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list2[5]
NameError: name 'list2' is not defined
>>> list[5]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list[5]
TypeError: 'type' object is not subscriptable
>>> 3 in [1,2,3]
True
>>> # repetition
>>> ['hi!']*4
['hi!', 'hi!', 'hi!', 'hi!']
>>> # membership
>>> 3 in [1,2,3]
True
>>> # iteration
>>> for x in [1,2,3]:
	print(x,end='')

	
123
>>> # indexing ,slicing matrixes
>>> l=['c','c++','java']
>>> l[2]
'java'
>>> l[-2]
'c++'
>>> l[1:]
['c++', 'java']
>>> l[-1]
'java'
>>> l[0]
'c'
>>> l[1]
'c++'
>>> # built in list function and methods
>>> #cmp no longer available in python 3
>>> len(l)
3
>>> max(l)
'java'
>>> min(l)
'c'
>>> atuple=(1,2,5,3)
>>> l2=list(atuple)
>>> l2
[1, 2, 5, 3]
>>> #method with description
>>> #list append()
>>> l3=[1,2,3,4,5]
>>> l3.append(l3)
>>> l3
[1, 2, 3, 4, 5, [...]]
>>> print(l3)
[1, 2, 3, 4, 5, [...]]
>>> l3.append(l22)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l3.append(l22)
NameError: name 'l22' is not defined
>>> l3.append('l22')
>>> l3
[1, 2, 3, 4, 5, [...], 'l22']
>>> #list count method
>>> l3.clear
<built-in method clear of list object at 0x000000D15A8A8408>
>>> l3
[1, 2, 3, 4, 5, [...], 'l22']
>>> l3.count(4)
1
>>> l3.count(l3)
1
>>> #list extend() method
>>> l3.extend(range(10))
>>> l3
[1, 2, 3, 4, 5, [...], 'l22', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #list index() method
>>> list.index(1)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list.index(1)
TypeError: descriptor 'index' requires a 'list' object but received a 'int'
>>> list.index('1')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    list.index('1')
TypeError: descriptor 'index' requires a 'list' object but received a 'str'
>>> l3.index(1)
0
>>> l3.index(0)
7
>>> #list insert method
>>> l3.extend(7,'ooohhhhh!')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l3.extend(7,'ooohhhhh!')
TypeError: extend() takes exactly one argument (2 given)
>>> l3.insert(7,'ooh!')
>>> l3
[1, 2, 3, 4, 5, [...], 'l22', 'ooh!', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #list pop method
>>> l3.pop()
9
>>> for x in l3:
	pop(x)

	
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    pop(x)
NameError: name 'pop' is not defined
>>> for x in range(10):
	l3.pop()

	
8
7
6
5
4
3
2
1
0
'ooh!'
>>> for x in l3:
	if (x==2):
		print("wefhweh")

		
wefhweh
>>> # list remove method
>>> l3.remove(l3)
>>> print(l3)
[1, 2, 3, 4, 5, 'l22']
>>> #list reverse method
>>> l3.reverse()
>>> l3
['l22', 5, 4, 3, 2, 1]
>>> #list sort method
>>> l3.sort()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    l3.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> str(l3)
"['l22', 5, 4, 3, 2, 1]"
>>> int(l3)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    int(l3)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> l3.sort()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    l3.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> range(-10)
range(0, -10)
>>> list=l4
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    list=l4
NameError: name 'l4' is not defined
>>> l4=list(range(-10))
>>> print(l4)
[]
>>> l4.sort()
>>> print(l4)
[]
>>> l5=list(range(10))
>>> print(l5)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l5.reverse()
>>> l5
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> l5.sort()
>>> l5
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
