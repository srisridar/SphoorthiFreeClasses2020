Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> scientists=['nikola tesla','albert einstein','charles darwin','srinivas ramanujan']
>>> # convert each of the strings into upper case and add them to a seperate list
>>> 
>>> uppersci=[]
>>> scientists[0]
'nikola tesla'
>>> scientists[0].upper()
'NIKOLA TESLA'
>>> 
>>> x=scientists[0].upper()
>>> x
'NIKOLA TESLA'
>>> uppersci.append(x)
>>> uppersci
['NIKOLA TESLA']
>>> 
>>> x=scientists[1].upper()
>>> x
'ALBERT EINSTEIN'
>>> uppersci.append(x)
>>> uppersci
['NIKOLA TESLA', 'ALBERT EINSTEIN']
>>> 
>>> 
>>> scientists
['nikola tesla', 'albert einstein', 'charles darwin', 'srinivas ramanujan']
>>> 
>>> # for everyitem in scientists:
>>> 
>>> for value in scientists:
	print(value)

	
nikola tesla
albert einstein
charles darwin
srinivas ramanujan
>>> 
>>> 
>>> for value in scientists:
	print(value.upper())

	
NIKOLA TESLA
ALBERT EINSTEIN
CHARLES DARWIN
SRINIVAS RAMANUJAN
>>> 
>>> uppersci=[]
>>> scientists=['nikola tesla','albert einstein','charles darwin','srinivas ramanujan']
>>> for sreedhar in scientists:
	x=sreedhar.upper()
	uppersci.append(x)

	
>>> uppersci
['NIKOLA TESLA', 'ALBERT EINSTEIN', 'CHARLES DARWIN', 'SRINIVAS RAMANUJAN']
>>> 
>>> 
>>> for sri in scientists:
	print(scientists)
	'
	
SyntaxError: EOL while scanning string literal
>>> for sri in scientists:
	print(scientists)

	
['nikola tesla', 'albert einstein', 'charles darwin', 'srinivas ramanujan']
['nikola tesla', 'albert einstein', 'charles darwin', 'srinivas ramanujan']
['nikola tesla', 'albert einstein', 'charles darwin', 'srinivas ramanujan']
['nikola tesla', 'albert einstein', 'charles darwin', 'srinivas ramanujan']
>>> for sri in scientists:
	print(sri)

	
nikola tesla
albert einstein
charles darwin
srinivas ramanujan
>>> 
>>> 
>>> # for var in "python is awesome":
>>> # for var in 1234567890:
>>> # for var in 234.567
>>> # for var in str(1234567890):
>>> 
>>> 
>>> 
>>> 