Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[2,6,2,4,7,3,0]
>>> 
>>> len(numbers)
7
>>> # 6 - indexes / 7 - values
>>> 
>>> simple=['a','b','c','d','e']
>>> 
>>> len(simple)
5
>>> # 5 - values / 4 addresses-indexes
>>> 
>>> simple
['a', 'b', 'c', 'd', 'e']
>>> simple[0]
'a'
>>> simple[1]
'b'
>>> simple[2]
'c'
>>> 
>>> simple[99]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    simple[99]
IndexError: list index out of range
>>> 
>>> 
>>> simple
['a', 'b', 'c', 'd', 'e']
>>> 
>>> simple=[2]
>>> simple
[2]
>>> simple(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    simple(2)
TypeError: 'list' object is not callable
>>> 
>>> 
>>> simple[]
SyntaxError: invalid syntax
>>> simple[1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    simple[1]
IndexError: list index out of range
>>> 
>>> simple[0]
2
>>> scientists=['nikola tesla','srinivasa ramanujam','chandrashekar azad','abdul kalaam','sri sreedhar']
>>> 
>>> 
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'chandrashekar azad', 'abdul kalaam', 'sri sreedhar']
>>> 
>>> 
>>> scientists[3]
'abdul kalaam'
>>> 
>>> 
>>> scientists[1]
'srinivasa ramanujam'
>>> 
>>> 
>>> type(scientists[1])
<class 'str'>
>>> 
>>> 
>>> scientists[3]
'abdul kalaam'
>>> 
>>> 'abdul kalaam'.upper()
'ABDUL KALAAM'
>>> 
>>> scientists[3].upper()
'ABDUL KALAAM'
>>> 
>>> 
>>> name="python"
>>> 
>>> name.upper()
'PYTHON'
>>> 
>>> 
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'chandrashekar azad', 'abdul kalaam', 'sri sreedhar']
>>> 
>>> 
>>> 
>>> scientists.pop()
'sri sreedhar'
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'chandrashekar azad', 'abdul kalaam']
>>> scientists.pop()
'abdul kalaam'
>>> 
>>> 
>>> scientists.pop()
'chandrashekar azad'
>>> scientists
['nikola tesla', 'srinivasa ramanujam']
>>> 
>>> x=scientists.pop()
>>> x
'srinivasa ramanujam'
>>> 
>>> 
>>> 
>>> scientists=['nikola tesla','srinivasa ramanujam','chandrashekar azad','abdul kalaam','sri sreedhar']
>>> 
>>> 
>>> scientists.pop(2)
'chandrashekar azad'
>>> 
>>> 
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar']
>>> 
>>> scientists.append("albert einstein")
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar', 'albert einstein']
>>> 
>>> scientists.append("charles darwin")
>>> 
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar', 'albert einstein', 'charles darwin']
>>> 
>>> scientists.insert(1,"nagasai")
>>> 
>>> scientists
['nikola tesla', 'nagasai', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar', 'albert einstein', 'charles darwin']
>>> len(scientists)
7
>>> 
>>> scientists.insert(6,"nagasai")
>>> 
>>> scientists
['nikola tesla', 'nagasai', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar', 'albert einstein', 'nagasai', 'charles darwin']
>>> 
>>> 
>>> scientists.index('abdul kalaam')
3
>>> scientists[3]
'abdul kalaam'
>>> 
>>> 
>>> scientists.index('abdul kalaam')
3
>>> 
>>> 
>>> 
>>> 
>>> scientists.index('abdul kalaam')+3
6
>>> 
>>> scientists[scientists.index('abdul kalaam')]
'abdul kalaam'
>>> 
>>> 
>>> 
>>> scientists
['nikola tesla', 'nagasai', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar', 'albert einstein', 'nagasai', 'charles darwin']
>>> 
>>> 
>>> 'nagasai' == 'nagasai'
True
>>> 
>>> 
>>> scientists.remove('nagasai')
>>> 
>>> scientists
['nikola tesla', 'srinivasa ramanujam', 'abdul kalaam', 'sri sreedhar', 'albert einstein', 'nagasai', 'charles darwin']
>>> 
>>> 
>>> [1,1,1,1,1,1,1,1,1,1,1,1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> 
>>> [1,1,1,1,1,1,1,1,1,1,1,1].remove(1)
>>> 
>>> # sorted(n) is working n.sort() is not working sir why?
>>> 
>>> 
>>> simple
[2]
>>> numbers=[3,9,1,7,3,6,4]
>>> numbers
[3, 9, 1, 7, 3, 6, 4]
>>> sorted(number)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    sorted(number)
NameError: name 'number' is not defined
>>> sorted(numbers)
[1, 3, 3, 4, 6, 7, 9]
>>> numbers
[3, 9, 1, 7, 3, 6, 4]
>>> 
>>> numbers.sort()
>>> numbers
[1, 3, 3, 4, 6, 7, 9]
>>> 
>>> 
>>> 
>>> 
>>> numbers
[1, 3, 3, 4, 6, 7, 9]
>>> 
>>> numbers.pop()
9
>>> numbers
[1, 3, 3, 4, 6, 7]
>>> numbers.pop()
7
>>> numbers
[1, 3, 3, 4, 6]
>>> numbers.pop()
6
>>> 
>>> numbers
[1, 3, 3, 4]
>>> x=numbers.pop()
>>> x
4
>>> 
>>> 
>>> numbers.pop(0)
1
>>> numbers
[3, 3]
>>> 