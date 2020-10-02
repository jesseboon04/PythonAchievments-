Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Mijn naam is jesse')
Mijn naam is jesse
>>> naam = 'jesse'
>>> 
>>> print(naam)
jesse
>>> print(naam.upper())
JESSE
>>> print(naam[0:2])
je
>>> print(naam[::-1])
essej
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo jesse ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    
SyntaxError: unindent does not match any outer indentation level
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
262
>>> willekeurig_getal = randint(0,1000
			    willekeurig_getal
			    
SyntaxError: invalid syntax
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
374
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 374
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-10-02 11:37:20.006523
>>> datum.strftime('%A %d %B %Y')
'Friday 02 October 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 02 oktober 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'Venerdì 02 Ottobre 2020'
>>> 
|
}
>>> 