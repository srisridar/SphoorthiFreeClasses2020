Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> " his name is %s"%("sreedhar")
' his name is sreedhar'
>>> " his name is %s and he is %d years old"%("sreedhar",15)
' his name is sreedhar and he is 15 years old'
>>> 
>>> 
>>> " his name is %d and he is %s years old"%("sreedhar",59)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    " his name is %d and he is %s years old"%("sreedhar",59)
TypeError: %d format: a number is required, not str
>>> 
>>> " his name is %d and he is %s years old"%(59,"sreedhar")
' his name is 59 and he is sreedhar years old'
>>> 
>>> 
>>> " his name is %s and he is %s years old"%(59,"sreedhar")
' his name is 59 and he is sreedhar years old'
>>> 
>>> 
>>> 
>>> name="sredhar"
>>> age=25
>>> 
>>> "his name is %s he is %s years old"%(name,age)
'his name is sredhar he is 25 years old'
>>> 
>>> print("his name is %s he is %s years old"%(name,age))
his name is sredhar he is 25 years old
>>> """
to,
the station master,
dist

dear %s ,

i put my kerchief to reserve a place. kindly assign the same.
i'm %s years old and i know jagan """%(name,age)
"\nto,\nthe station master,\ndist\n\ndear sredhar ,\n\ni put my kerchief to reserve a place. kindly assign the same.\ni'm 25 years old and i know jagan "
>>> 
>>> 
>>> print("""
to,
the station master,
dist

dear %s ,

i put my kerchief to reserve a place. kindly assign the same.
i'm %s years old and i know jagan """%(name,age))

to,
the station master,
dist

dear sredhar ,

i put my kerchief to reserve a place. kindly assign the same.
i'm 25 years old and i know jagan 
>>> 
======== RESTART: C:/Users/User/Desktop/SphoorthiOum/stringformatting.py =======
Enter your Name sreedhar
Enter your age 51
Enter your education mba
Enter your math marks 90
Enter your telugu marks 99
Enter your science marks 89

Hi,
Your name : SREEDHAR
Your Age : 51
you've studied : MBA
your total is : 278 
>>> 
>>> 
>>> 
>>> age=input()
10
>>> age
'10'
>>> int(age)
10
>>> 
>>> 
>>> age=int(input())
29
>>> age
29
>>> 
>>> age=int(input())
fifty
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    age=int(input())
ValueError: invalid literal for int() with base 10: 'fifty'
>>> 