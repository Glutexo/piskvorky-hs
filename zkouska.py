#radek=input('Zadej hrací pole o 20 polích: ')
def vyhodnot(radek):
    'Vrátí jednoznakový řetezec podle stavu hry'
    #radek=radek.lower()
    if  'xxx' in radek:
        return ('\'x\'')
    elif 'ooo' in radek:
        return('\'o\'')
    elif '-' not in radek:
        return('\'!\'')
    else:
        return('\'-\'')

#print(vyhodnot(radek))

def tah(retezec, cislo_pole, symbol):
    return retezec[:cislo_pole] + symbol + retezec[cislo_pole + 1:]

def tah_hrace(retezec, otazka):
    while True:
        cislo_pole=int(input(otazka))
        if cislo_pole<0:
            print ('Nelze zadat zápornou hodnotu')
        elif cislo_pole>19:
            print ('Takové pole neexistuje, Hrej ještě jednou')
        elif '-' not in retezec[:cislo_pole]:
            print('Pole je obsazeno. Hrej znovu.')
        else:
            return tah(retezec,cislo_pole,'x')

#print(tah_hrace('Zadej číslo pole od 0 do 19:'))

from random import randrange
def tah_pocitace(retezec):
    while True:
        pole=randrange(19)
        if '-' in retezec[:pole]:
            return tah(retezec,pole,'o')

#print(tah_pocitace(pole))

def piskvorky1d():
    retezec='-'*20 # cyklus, co uloží řetezec s novými hodnotami
    while '-' in retezec:
        print(retezec)
        retezec = tah_hrace(retezec, 'Zadej číslo pole od 0 do 19:')
        retezec = tah_pocitace(retezec)
        vysledek = vyhodnot(retezec)
        if vysledek != '\'-\'':
            print(vysledek)
            break

piskvorky1d()
