Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # for each in dir():
>>> # 	print(each)
>>> 
>>> for each in [1,2,3,4]:
	print(each)

	
1
2
3
4
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'each']
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'each']
>>> dir()[0]
'__annotations__'
>>> 
>>> 
>>> 
>>> names=['albert einstein','charles darwin','sri sreedhar','nikola tesla']
>>> 
>>> 
>>> 
>>> for each in 'albert einstein':
	print(each),

	
a
(None,)
l
(None,)
b
(None,)
e
(None,)
r
(None,)
t
(None,)
 
(None,)
e
(None,)
i
(None,)
n
(None,)
s
(None,)
t
(None,)
e
(None,)
i
(None,)
n
(None,)
>>> for each in 'albert einstein':
	print(each)

	
a
l
b
e
r
t
 
e
i
n
s
t
e
i
n
>>> 'albert einstein'.split()
['albert', 'einstein']
>>> for each in 'albert einstein'.split():
	print(each)

	
albert
einstein
>>> for each in 'albert einstein'.split():
	print(each.title)

	
<built-in method title of str object at 0x00000082F2683B30>
<built-in method title of str object at 0x00000082F2683D70>
>>> for each in 'albert einstein'.split():
	print(each.title())

	
Albert
Einstein
>>> for each in 'albert einstein'.split():
	print(len(each))

	
6
8
>>> for each in 'albert einstein'.split():
	print(each,len(each))

	
albert 6
einstein 8
>>> 
>>> 
>>> # print all the lastnames of the list names in capitalized case
>>> names
['albert einstein', 'charles darwin', 'sri sreedhar', 'nikola tesla']
>>> 
>>> 
>>> # print all the lastnames of the list names in capitalized case and add all of them to a new list
>>> 
>>> lastnames=[]
>>> names
['albert einstein', 'charles darwin', 'sri sreedhar', 'nikola tesla']
>>> 
>>> for name in names:
	ln=name.split()[1]
	upp=ln.title()
	lastnames.append(upp)

	
>>> lastnames
['Einstein', 'Darwin', 'Sreedhar', 'Tesla']
>>> 
>>> 
>>> 
>>> # split the names into first name and last name
>>> # convert all first names to upper and last names to title cases
>>> # add first names to a seperate list
>>> # add last names to a seperate list
>>> 
>>> 
>>> 