Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Maiz'
print(name)
Maiz
type(name)
<class 'str'>
friend = 'ging'
print('สวัสดี'.friend'สบายดีไหม')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('สวัสดี' + friend 'สบายดีไหม')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('สวัสดี' + friend + 'สบายดีไหม')
สวัสดีgingสบายดีไหม
>>> print('สวัสดี' + friend + ' สบายดีไหม')
สวัสดีging สบายดีไหม
>>> money = 10
>>> type(money)
<class 'int'>
>>> money1 - 10.25
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    money1 - 10.25
NameError: name 'money1' is not defined. Did you mean: 'money'?
>>> money1 = 10.25
>>> type(money1)
<class 'float'>
>>> print(friend + 'ยืมเงิน ' + str(money) + 'บาท')
gingยืมเงิน 10บาท
>>> print('{}ยืมเงิน {} บาท'.format(friend,money))
gingยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท')
gingยืมเงิน 10 บาท
>>> fstr
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    fstr
NameError: name 'fstr' is not defined. Did you mean: 'str'?
>>> money = 30000000000
>>> print(f'{money:,}')
30,000,000,000
>>> print(f'{money:,.2f}')
30,000,000,000.00
>>> print('{:,.2f}'.format(money))
30,000,000,000.00
>>> import math
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 2, 10, 7, 14, 58, 85903)
>>> datetime.now().strftime('%y%m%d %h:%m:%s')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    datetime.now().strftime('%y%m%d %h:%m:%s')
ValueError: Invalid format string
>>> datetime.now().strftime('%y%m%d %H:%M:%S')
'230210 07:16:17'
>>> import random
>>> random.randint(1,7)
2
>>> store = ['ป้าส้ม','ลุงแดง','น้าแม้น']
>>> random.choice(store)
'ป้าส้ม'
