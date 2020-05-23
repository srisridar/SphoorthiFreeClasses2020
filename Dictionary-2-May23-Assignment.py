Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp={
"day": 42.15,
"min": 37.75,
"max": 45.29,
"night": 37.75,
"eve": 44.39,
"morn": 39.61
}
>>> 
>>> temp
{'day': 42.15, 'min': 37.75, 'max': 45.29, 'night': 37.75, 'eve': 44.39, 'morn': 39.61}
>>> 
>>> # dictName["KeyName"]
>>> 
>>> temp["max"]
45.29
>>> 
>>> temp["min"]
37.75
>>> 
>>> 
>>> 
>>> listofTemp=[

{
"day": 42.15,
"min": 37.75,
"max": 45.29,
"night": 37.75,
"eve": 44.39,
"morn": 39.61
},

{
"day": 45.72,
"min": 33.81,
"max": 47.01,
"night": 37.38,
"eve": 45.36,
"morn": 33.81
},

{
"day": 46.72,
"min": 34.76,
"max": 47.71,
"night": 37.38,
"eve": 45.98,
"morn": 34.76
},
]
>>> 
>>> 
>>> listofTemp
[{'day': 42.15, 'min': 37.75, 'max': 45.29, 'night': 37.75, 'eve': 44.39, 'morn': 39.61}, {'day': 45.72, 'min': 33.81, 'max': 47.01, 'night': 37.38, 'eve': 45.36, 'morn': 33.81}, {'day': 46.72, 'min': 34.76, 'max': 47.71, 'night': 37.38, 'eve': 45.98, 'morn': 34.76}]
>>> 
>>> 
>>> # extract the max temparatures from all the dictionaries in the list above
>>> # print all the min & max temparatures
>>> # print the third dictionary's morning temp- "morn" key
>>> 
>>> type(listofTemp)
<class 'list'>
>>> len(listofTemp)
3
>>> listofTemp[0]
{'day': 42.15, 'min': 37.75, 'max': 45.29, 'night': 37.75, 'eve': 44.39, 'morn': 39.61}
>>> type(listofTemp[0])
<class 'dict'>
>>> 
>>> 
>>> 
>>> 
>>> https://openweathermap.org/api
SyntaxError: invalid syntax
>>> 