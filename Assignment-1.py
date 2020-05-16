Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> 
>>> 
>>> type(dir())
<class 'list'>
>>> 
>>> string="what a beautiful morning this is"
>>> 
>>> string
'what a beautiful morning this is'
>>> 
>>> # a string startswith
>>> string.startswith("w")
True
>>> # a string endswith
>>> string.endswith("s")
True
>>> string.startswith("W")
False
>>> 
>>> # contains
>>> 
>>> 
>>> # membership checking operator
>>> 
>>> # value in collection
>>> 
>>> 'm' in string
True
>>> 'M' in string
False
>>> 
>>> # negation
>>> 'M' not in string
True
>>> # "sreedhar" in Faulties
>>> 
>>> 
>>> 
>>> 
>>> string
'what a beautiful morning this is'
>>> 
>>> string.split()
['what', 'a', 'beautiful', 'morning', 'this', 'is']
>>> 
>>> # stringName.split(Delimitter)
>>> $ delimitter is space y default
SyntaxError: invalid syntax
>>> # delimitter is space by default
>>> 
>>> 
>>> 
>>> row="Age,Gender,Impressions,Clicks,Signed_In"
>>> 
>>> row.split()
['Age,Gender,Impressions,Clicks,Signed_In']
>>> 
>>> 
>>> row.split(',')
['Age', 'Gender', 'Impressions', 'Clicks', 'Signed_In']
>>> row.split(',')[-2]
'Clicks'
>>> var=row.split(',')
>>> var
['Age', 'Gender', 'Impressions', 'Clicks', 'Signed_In']
>>> var[-2]
'Clicks'
>>> 
>>> 
>>> # stringName[len(stringName)-1]
>>> 
>>> 
>>> name = " python "
>>> name
' python '
>>> 
>>> name[0]
' '
>>> name[-1]
' '
>>> name[1]
'p'
>>> name[-2]
'n'
>>> 
>>> name.lstrip()
'python '
>>> name.rstrip()
' python'
>>> name
' python '
>>> 
>>> name.strip()
'python'
>>> 
>>> "his fav topic is python.".strip('.')
'his fav topic is python'
>>> 
>>> 
====== RESTART: C:/Users/User/Desktop/SphoorthiOum/DELETETHIS-SCRAPFILE.py =====
Traceback (most recent call last):
  File "C:/Users/User/Desktop/SphoorthiOum/DELETETHIS-SCRAPFILE.py", line 1, in <module>
    ASDAsdadaSDAdaSDAsdasdaSDasdaDAsdaSDAsdaSDadASD
NameError: name 'ASDAsdadaSDAdaSDAsdasdaSDasdaDAsdaSDAsdaSDadASD' is not defined
>>> 
>>> 
>>> 
>>> 
>>> # listname[0].upper()
>>> 
>>> names=["sri","albert","nikola","srinivasa","ramanujam"]
>>> 
>>> names.upper()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    names.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> names[0].upper()
'SRI'
>>> names[1].upper()
'ALBERT'
>>> 
>>> uppernames=[]
>>> 
>>> 
>>> 
>>> 
>>> # assignment
>>> # convert all the valus to uppercase and save them in a seperate list, upperNames
>>> 
>>> # convert all the values in names and save them in uppernames list
>>> 