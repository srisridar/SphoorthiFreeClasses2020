Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> s={}
>>> type(s)
<class 'dict'>
>>> 
>>> 
>>> s={
	'key1':'value1',
	'key2':12345,
	'key3':12.0980,
	'key4':['a','b','c'],
	'key5':{
		'a':1,'b':2,'c':3}
	}
>>> 
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key3': 12.098, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}}
>>> 
>>> 
>>> len(s)
5
>>> s
{'key1': 'value1', 'key2': 12345, 'key3': 12.098, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}}
>>> 
>>> 
>>> s.keys()
dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])
>>> 
>>> s.values()
dict_values(['value1', 12345, 12.098, ['a', 'b', 'c'], {'a': 1, 'b': 2, 'c': 3}])
>>> 
>>> 
>>> # dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])
>>> # dict_keys()
>>> # ['key1', 'key2', 'key3', 'key4', 'key5'] - list of keys
>>> 
>>> 
>>> 
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key3': 12.098, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}}
>>> 
>>> 
>>> s['key2']
12345
>>> 
>>> s['key4']
['a', 'b', 'c']
>>> 
>>> s[key5]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s[key5]
NameError: name 'key5' is not defined
>>> s['key5']
{'a': 1, 'b': 2, 'c': 3}
>>> 
>>> 
>>> 
>>> s['key6']="a sentence that makes o sense at all"
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key3': 12.098, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}, 'key6': 'a sentence that makes o sense at all'}
>>> 
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key3': 12.098, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}, 'key6': 'a sentence that makes o sense at all'}
>>> 
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key3': 12.098, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}, 'key6': 'a sentence that makes o sense at all'}
>>> s['key3']
12.098
>>> 
>>> del s['key3']
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}, 'key6': 'a sentence that makes o sense at all'}
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key4': ['a', 'b', 'c'], 'key5': {'a': 1, 'b': 2, 'c': 3}, 'key6': 'a sentence that makes o sense at all'}
>>> 
>>> 
>>> s['key4']="some random junk"
>>> 
>>> 
>>> s
{'key1': 'value1', 'key2': 12345, 'key4': 'some random junk', 'key5': {'a': 1, 'b': 2, 'c': 3}, 'key6': 'a sentence that makes o sense at all'}
>>> 
>>> 
>>> 
>>> 