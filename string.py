Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(9999)
<class 'int'>
>>> type('9999')
<class 'str'>
>>> 
>>> 
>>> sentence='this is a beautiful morning'
>>> sentence
'this is a beautiful morning'
>>> 
>>> sent='this's a beautiful morning'
SyntaxError: invalid syntax
>>> sent="this's a beautiful morning"
>>> 
>>> sent
"this's a beautiful morning"
>>> 
>>> para="this is a beautiful morning, see the wind, its about to rain here.
SyntaxError: EOL while scanning string literal
>>> para='''this is a beautiful morning, see the wind, its about to rain here.->
and after the class->
i'll go play in the rain'''
>>> 
>>> para
"this is a beautiful morning, see the wind, its about to rain here.->\nand after the class->\ni'll go play in the rain"
>>> 
>>> 
>>> 1111 + 9999
11110
>>> 
>>> 
>>> 
>>> "python" + "language"
'pythonlanguage'
>>> "python" + "   " + "language"
'python   language'
>>> 
>>> 
>>> '1111' + '9999'
'11119999'
>>> 
>>> 
>>> 
>>> string="sphoorthi oum"
>>> 
>>> # UPPER CASE
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'para', 'sent', 'sentence', 'string']
>>> 
>>> type(sent)
<class 'str'>
>>> 
>>> 
>>> string
'sphoorthi oum'
>>> 
>>> string.upper()
'SPHOORTHI OUM'
>>> 
>>> string
'sphoorthi oum'
>>> 
>>> "UPPER".lower()
'upper'
>>> 
>>> 
>>> string.title()
'Sphoorthi Oum'
>>> 
>>> 
>>> para.title()
"This Is A Beautiful Morning, See The Wind, Its About To Rain Here.->\nAnd After The Class->\nI'Ll Go Play In The Rain"
>>> 
>>> 
>>> 1111.upper()
SyntaxError: invalid syntax
>>> 
>>> "1111".upper()
'1111'
>>> 
>>> 
>>> "   ".upper()
'   '
>>> 
>>> 
>>> 
>>> 
>>> string
'sphoorthi oum'
>>> 
>>> string.upper()
'SPHOORTHI OUM'
>>> 
>>> string
'sphoorthi oum'
>>> 
>>> 
>>> x=string.upper()
>>> x
'SPHOORTHI OUM'
>>> x
'SPHOORTHI OUM'
>>> 
>>> 
>>> string=string.upper()
>>> string
'SPHOORTHI OUM'
>>> 
>>> 
>>> 
>>> # print stuff , write our first program
>>> 
>>> str1="python programming"
>>> str2="java programming"
>>> 
>>> "python java"
'python java'
>>> 