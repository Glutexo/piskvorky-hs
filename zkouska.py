retezec='-'*20
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

def tah_hrace(otazka):
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
pole=randrange(19)
def tah_pocitace (pole):
    while True:
        pole=randrange(19)
        if '-' in retezec[:pole]:
            return tah(retezec,pole,'o')

#print(tah_pocitace(pole))

def piskvorky1d (hrac, pocitac):
    retezec='-'*20 # cyklus, co uloží řetezec s novými hodnotami
    while '-' in retezec:
        return(tah_hrace('Zadej číslo pole od 0 do 19:'))
        return (retezec)
        return (tah_pocitace(pole))
        return (vyhodot(radek))
print(piskvorky1d('-'*20))
