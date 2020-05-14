Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=[]
>>> type(s)
<class 'list'>
>>> 
>>> 
>>> invitations=['rao','reddy','naidu','naidu','naidu','modi','modi']
>>> 
>>> invitations
['rao', 'reddy', 'naidu', 'naidu', 'naidu', 'modi', 'modi']
>>> 
>>> numbers=[1,9,2,8,3,7,4,5,0]
>>> 
>>> numbers
[1, 9, 2, 8, 3, 7, 4, 5, 0]
>>> 
>>> 
>>> 
>>> len(numbers)
9
>>> len(invitations)
7
>>> 
>>> "sreedhar".upper()
'SREEDHAR'
>>> 1111.upper()
SyntaxError: invalid syntax
>>> '1111'.upper()
'1111'
>>> 
>>> 
>>> states=[]
>>> states
[]
>>> states.append("telangana")
>>> states
['telangana']
>>> 
>>> states.append("karnataka")
>>> states
['telangana', 'karnataka']
>>> states.append("chennai")
>>> states.append("pune")
>>> 
>>> states
['telangana', 'karnataka', 'chennai', 'pune']
>>> 
>>> states.append(1111)
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 1111]
>>> states.append(9999)
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 1111, 9999]
>>> 
>>> 
>>> us=["california","sanfransisco","austin"]
>>> us
['california', 'sanfransisco', 'austin']
>>> 
>>> states.append(us)
>>> 
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 1111, 9999, ['california', 'sanfransisco', 'austin']]
>>> 
>>> len(states)
7
>>> 
>>> 
>>> us
['california', 'sanfransisco', 'austin']
>>> 
>>> states.extend(us)
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 1111, 9999, ['california', 'sanfransisco', 'austin'], 'california', 'sanfransisco', 'austin']
>>> 
>>> 
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 1111, 9999, ['california', 'sanfransisco', 'austin'], 'california', 'sanfransisco', 'austin']
>>> 
>>> 
>>> us
['california', 'sanfransisco', 'austin']
>>> 
>>> onemore='texas"
SyntaxError: EOL while scanning string literal
>>> onemore='texas'
>>> 
>>> us.append(onemore)
>>> us
['california', 'sanfransisco', 'austin', 'texas']
>>> 
>>> us.remove(onemore)
>>> us
['california', 'sanfransisco', 'austin']
>>> is
SyntaxError: invalid syntax
>>> us
['california', 'sanfransisco', 'austin']
>>> 
>>> 
>>> 
>>> states.remove(us)
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 1111, 9999, 'california', 'sanfransisco', 'austin']
>>> 
>>> 
>>> states.remove(1111)
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 9999, 'california', 'sanfransisco', 'austin']
>>> 
>>> states.remove(9999)
>>> states
['telangana', 'karnataka', 'chennai', 'pune', 'california', 'sanfransisco', 'austin']
>>> 
>>> numbers
[1, 9, 2, 8, 3, 7, 4, 5, 0]
>>> numbers.sort()
>>> numbers
[0, 1, 2, 3, 4, 5, 7, 8, 9]
>>> 
>>> numbers.sort(reverse=True)
>>> numbers
[9, 8, 7, 5, 4, 3, 2, 1, 0]
>>> 
>>> 