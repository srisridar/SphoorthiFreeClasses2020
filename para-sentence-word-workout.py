Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text="""and therefore women, being the weaker vessels,
    are ever thrust to the wall. Therefore I will push Montague men
    from the wall and thrust his maids to the wall"""
>>> text
'and therefore women, being the weaker vessels,\n    are ever thrust to the wall. Therefore I will push Montague men\n    from the wall and thrust his maids to the wall'
>>> # print all the word which has more than 5 letters
>>> 
>>> # change this into a collection of words
>>> #apply condition to check the length of word
>>> 
>>> text.split('\n')
['and therefore women, being the weaker vessels,', '    are ever thrust to the wall. Therefore I will push Montague men', '    from the wall and thrust his maids to the wall']
>>> text.split('\n')[0]
'and therefore women, being the weaker vessels,'
>>> text.split('\n')[2]
'    from the wall and thrust his maids to the wall'
>>> 
>>> 
>>> 
>>> # splitting into words
>>> text.split('\n')[0].upper()
'AND THEREFORE WOMEN, BEING THE WEAKER VESSELS,'
>>> 
>>> 
>>> 
>>> 
>>> text.split('\n')[0].split()
['and', 'therefore', 'women,', 'being', 'the', 'weaker', 'vessels,']
>>> 
>>> 
>>> for each in text.split('\n'):
	print(each)

	
and therefore women, being the weaker vessels,
    are ever thrust to the wall. Therefore I will push Montague men
    from the wall and thrust his maids to the wall
>>> 
>>> 
>>> for sentence in text.split('\n'):
	for word in sentence.split()
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> for sentence in text.split('\n'):
	for word in sentence.split():
		print(word)

		
and
therefore
women,
being
the
weaker
vessels,
are
ever
thrust
to
the
wall.
Therefore
I
will
push
Montague
men
from
the
wall
and
thrust
his
maids
to
the
wall
>>> for sentence in text.split('\n'):
	for word in sentence.split():
		if len(word)>5:
			print(word)

			
therefore
women,
weaker
vessels,
thrust
Therefore
Montague
thrust
>>> 