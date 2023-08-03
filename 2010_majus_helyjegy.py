def feladat_leiras(sorszam,szoveg):
    print('{}. feladat - {}'.format(sorszam,szoveg))
         
feladat_leiras(1,'Adatok beolvasása')

beolvasas = open('eladott.txt','r')
elsosor = beolvasas.readline()
elsosor = elsosor.strip().split()

eladott_jegyek = int(elsosor[0])
print(eladott_jegyek)
tavolsag = int(elsosor[1])
ar = int(elsosor[2])

adatok=[]
for sor in beolvasas:
    sor=sor.strip().split()
    ules=int(sor[0])
    tol=int(sor[1])
    ig=int(sor[2])
    adatok.append([ules,tol,ig])
print(adatok)
beolvasas.close()



feladat_leiras(2,'Legutolsó jegyvásárló adatai')

index = eladott_jegyek-1
print('Utolsó jegyvásárló ülése: ',adatok[index][0])
print('Utolsó jegyvásárló által megtett távolság: {} km'.format(adatok[index][2]-adatok[index][1]))


feladat_leiras(3,'A teljes utat végig utazók')

print('Végig utazók sorszáma:')

for i in range(len(adatok)):
    if adatok[i][2]-adatok[i][1]== tavolsag:
        print(i+1,end=' ')
print()


feladat_leiras(4,'Mennyi a bevétel?')

def kerekit(osszeg):
    kerek = 0;
    maradek = osszeg%5;
    
    if maradek<3:
        kerek = osszeg-maradek;
    else:
        kerek = osszeg-maradek+5;
   
    return kerek;

bevetel = 0
for adat in adatok:
    tavolsag = adat[2]-adat[1]
    if tavolsag % 10 == 0:
        fizetendo = (tavolsag//10) * ar
    else:
        fizetendo = ((tavolsag//10)+1) * ar
    bevetel += kerekit(fizetendo)

print('A társaságnak ', bevetel, ' Ft bevétele keletkezett.')


feladat_leiras(5,'Végállomás előtti fel- és leszállók')

# Ezt nem sikerült megoldani.

#-----------------------------------------------------------------------------
# 6. Adja meg, hogy hány helyen állt meg a busz a kiinduló állomás és a
#    célállomás között! Az eredményt írja a képernyőre!
#-----------------------------------------------------------------------------
feladat_leiras(6,'Hány helyen állt meg a busz?')

#lehet úgy gondolkodni, hogy a 0-tól eltérő és a végállomástól eltérő fel- és
#leszállások km adatait egy halmazba "dobáljuk", ezzel az ismétlődéseket
#kivédjük és a halmaz elemszáma lesz a megoldás! De biztosan lehet máshogyan is.

halmaz=set()
halmaz2=set()

for adat in adatok:
    if adat[1]!=0 and adat[1]!=tavolsag:
        halmaz.add(adat[1])
    if adat[2]!=0 and adat[2]!=tavolsag:
        halmaz.add(adat[2])

print('A megállók száma: ', len(halmaz))

feladat_leiras(7,'Ki hol')

ki = open('kihol.txt','w')

ulesek=[' ']*48
megadottkm = int(input('Adja meg, hogy hányadik km-nél kéri az utasok listáját: '))
for i in range(len(adatok)):
    if megadottkm >= adatok[i][1] and megadottkm < adatok[i][2]:
        ulesek[adatok[i][0]-1] = i+1     

for ules in ulesek:
    if ules==' ':
        print('üres',file = ki)
    else:
        print(ules,file = ki)

ki.close()