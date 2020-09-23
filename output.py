Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is <Timo Zandbergen>')
Mijn naam is <Timo Zandbergen>
>>> print(naam)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(naam)
NameError: name 'naam' is not defined
>>> naam = '<Timo Zandbergen>'
>>> print(naam)
<Timo Zandbergen>
>>> print(naam.upper())
<TIMO ZANDBERGEN>
>>> print(naam[0:2])
<T
>>> print(naam[::-1])
>negrebdnaZ omiT<
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo <Timo Zandbergen> ben je al 16 jaar?
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> ja
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ja
NameError: name 'ja' is not defined
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')

Hallo <Timo Zandbergen> ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' 2 jaar')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>>     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')

SyntaxError: unexpected indent
>>> hoelang_tot18jaar = 18 - leeftijd
>>> print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
Over 2 jaar wordt je 18
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)'
					      
SyntaxError: invalid syntax
>>> if leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')

    
>>> else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    
SyntaxError: invalid syntax
>>> 
>>> 
KeyboardInterrupt
>>> from random import randint
>>> randint(0,1000)
273
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
934
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 934
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-16 12:11:22.066402
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 16 settembre 2020'
>>> 