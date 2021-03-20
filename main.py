import math

print('Zadanie1')
a='To zmienna łańcuchowa'
b=9 #zmienna integer
c=2.6 #zmienna float
d=5*3j #zmienna complex
print(a)
print(b)
print(c)
print(d)


print('Zadanie2')
c=5
c+=1
d=7
d-=2
f=3
f*=3
g=10
g/=4
h=25
h**=5
i=16
i%=6
print(c)
print(d)
print(f)
print(g)
print(h)
print(i)


print('Zadanie3')
e=int(input('a) Podaj liczbę: ')) #pierwsza wersja
print(e**10)
print(math.exp(10)) #druga wersja
print((math.log10(5+math.sin(8)**2))**(1/6))
print(math.floor(3.55))
print(math.ceil(4.80))


print('Zadanie4')
imie='NORBERT'
nazwisko='SZCZEPAŃSKI'
print(str.capitalize(imie))
print(str.capitalize(nazwisko))


print('Zadanie5')
tekst='coś tam, coś tam, coś tam, la la la la la la la coś tam'
print(tekst.count('la'))


print('Zadanie6')
indeks='Uniwersytet Warmińsko Mazurski w Olsztynie'
print(indeks[1])
print(indeks[41])


print('Zadanie7')
print(indeks.split())


print('Zadanie8')
stringowe = 'cześć'
floatowe = 5.4
szesnastkowe = 0x65
print('%s' % stringowe)
print('%.2f' % floatowe)
print('%x' % szesnastkowe)


print('Zadanie9')
sportlist = ['siatkówka', 'koszykówka', 'piłka ręczna', 'piłka nożna']
print(sportlist)
sportlist.reverse()
print(sportlist)
sportlist.append('tenis ziemny')
sportlist.append('hokej')
print(sportlist)


print('Zadanie10')
skroty = {'itd.': 'i tak dalej', 'itp.': 'i tym podobne', 'tzw.': 'tak zwany',
          'tzn.': 'to znaczy', 'dr': 'doktor', 'cdn.': 'ciąg dalszy nastąpi',
          'tj.': 'to jest'}
print(skroty)
print('cdn.: ' + skroty['cdn.'])
