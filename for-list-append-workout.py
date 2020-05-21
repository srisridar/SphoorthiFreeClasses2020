Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/User/Desktop/SphoorthiOum/if-elif.py ============
Please enter any number from 1-5: 3
you've entered three
>>> 
============ RESTART: C:/Users/User/Desktop/SphoorthiOum/if-elif.py ============
Please enter any number from 1-5: 5
you've entered  five
>>> 
============ RESTART: C:/Users/User/Desktop/SphoorthiOum/if-elif.py ============
Please enter any number from 1-5: 24
The number you've used is out of range
>>> 
>>> 
>>> names=['albert einstein',"sri sreedhar","nikola tesla"]
>>> 
>>> names
['albert einstein', 'sri sreedhar', 'nikola tesla']
>>> 
>>> 
>>> lastnames=[]
>>> 'albert einstein'.split()
['albert', 'einstein']
>>> 'albert einstein'.split()[0]
'albert'
>>> 
>>> 
>>> 
>>> for name in names:
	print(name.split()[1].upper())

	
EINSTEIN
SREEDHAR
TESLA
>>> for name in names:
	lastnames.append(name.split()[1].upper())

	
>>> lastnames
['EINSTEIN', 'SREEDHAR', 'TESLA']
>>> 
>>> 
>>> 
>>> 
>>> for name in names:
	lnames=[]
	lnames.append(name.split()[1].upper())

	
>>> lnames
['TESLA']
>>> 