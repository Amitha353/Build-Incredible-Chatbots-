Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 65
>>> a
65
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a']
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 65}
>>> type(a)
<class 'int'>
>>> id(a)
1794140256
>>> a.__sizeof__()
14
>>> import sys
>>> sys
<module 'sys' (built-in)>
>>> sys.getrefcount(a)
6
>>> b = a
>>> sys.getrefcount(a)
7
>>> a = 70
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'sys']
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 70, 'sys': <module 'sys' (built-in)>, 'b': 65}
>>> sys.getrefcount(a)
12
>>> sys.getrefcount(b)
6
>>> c = 65
>>> id(a)
1794140336
>>> id(c)
1794140256
>>> id(b)
1794140256
>>> a = 65
>>> sys.getrefcount(a)
8
>>> id(a)
1794140256
>>> a = "1234
SyntaxError: EOL while scanning string literal
>>> a = "1234"
>>> a
'1234'
>>> int(a)
1234
>>> float(a)
1234.0
>>> list(a)
['1', '2', '3', '4']
>>> b
65
>>> string(b)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    string(b)
NameError: name 'string' is not defined
>>> str(b)
'65'
>>> a = (10, 20, 30, 40, 50)
>>> list(a)
[10, 20, 30, 40, 50]
>>> set(a)
{40, 10, 50, 20, 30}
>>> e = (10, "hei", "hey")
>>> list(e)
[10, 'hei', 'hey']
>>> set(e)
{10, 'hey', 'hei'}
>>> a = ["today" , "is" , "a", "Wednesday"]
>>> b = "-".join(a)
>>> b
'today-is-a-Wednesday'
>>> c = " ".join(a)
>>> c
'today is a Wednesday'
>>> a = ("today" , "is" , "a", "Wednesday")
>>> "*".join(a)
'today*is*a*Wednesday'
>>> num = 5678
>>> list(str(num))
['5', '6', '7', '8']
>>> ''.join(str(num))
'5678'
>>> name = input("Enter your name : ")
Enter your name : Amitha
>>> name
'Amitha'
>>> a = 10
>>> b = 10
>>> res = a + b
>>> print(res)
20
>>> print("Result is ", res)
Result is  20
>>> a = 10
>>> b = "20"
>>> c = a + b
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c = a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a = 10
>>> b = 10
>>> a = 10
>>> b = "20"
>>> str(a)+b
'1020'
>>> a+int(b)
30
>>> a = 10
>>> b = 10
>>> res = a + b
>>> print("Result is " + res)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print("Result is " + res)
TypeError: can only concatenate str (not "int") to str
>>> print("Result is " + str(res))
Result is 20
>>> print("Result = %s %s %s" %(a, b, res))
Result = 10 10 20
>>> print("Result = {0} {1} {2}" %(a, b, res))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print("Result = {0} {1} {2}" %(a, b, res))
TypeError: not all arguments converted during string formatting
>>> print("Result = {0} {1} {2}".format(a, b, res))
Result = 10 10 20
>>> 
==== RESTART: C:/Users/Administrator/Desktop/Python Programs/FirstPrg.py ====

==== RESTART: C:/Users/Administrator/Desktop/Python Programs/FirstPrg.py ====
Enter a val: 10
Enter a val: 20
Final ans = 10 + 20 = 30
>>> 
