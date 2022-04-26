import random

def wczytaj(name, lista):
    filepath=str(name)
    f=open(filepath, 'r')
    array = []
    
    line = f.readline()
    line = str(line.strip())
    while line!="":
        lista.append(line)
        line = f.readline()
        line = str(line.strip())
    return lista

def convert(line):

    dl=len(line)-1
    hash=0
    for i in range(dl):
        hash+=111*(ord(line[i]))
    
    return hash

def hashing(array, hashedArray, m):
    for line in array:
        h=convert(line)%m
        hashedArray[h].append(line)
    
    return hashedArray

def slabyHash(array, hashedArray, m):

    for line in array:
        h=(256*ord(line[0]))%m

        hashedArray[h].append(line)
    
    return hashedArray

def wbudowanyHash(array, hashedArray, m):
    
    for line in array:
        h=hash(line)
        h=h%m

        if h<0:
            h=h*-1

        hashedArray[h].append(line)
    
    return hashedArray

def main():

    sizes=[17, 1031, 1024]

    for w in range(3):

        for size in sizes:

            array=[]
            hashedArray=[]
            for i in range(size):
                hashedArray.append([])

            wczytaj('3700.txt', array)
            
            if(w==0):
                hashing(array, hashedArray, size)
                print("Hashowanie własne (dobre)")
            if(w==1):
                slabyHash(array, hashedArray, size)
                print("Hashowanie własne (słabe)")
            if(w==2):
                wbudowanyHash(array, hashedArray, size)
                print("Hashowanie wbudowane")

            suma=0
            sr=0
            max=0
            for line in hashedArray:
                if len(line)==0:
                    suma+=1
                if len(line)>max:
                    max=len(line)
                if len(line)!=0:
                    sr+=len(line)       

            sr=sr/(len(hashedArray)-suma)
            
            print("M =",size)
            print("Suma pustych list w tablicy:",suma)
            print("Srednia dlugosc niepustych list w tablicy:",sr)
            print("Maksymalna dlugosc listy w tablicy:",max)
            print("")
        

if __name__=="__main__":
    main()



"""
-----------------------------------------------------------------
M=17

Hashowanie własne (dobre)
Suma pustych list w tablicy: 0
Srednia dlugosc niepustych list w tablicy: 220.23529411764707
Maksymalna dlugosc listy w tablicy: 238

Hashowanie własne (słabe)
Suma pustych list w tablicy: 0
Srednia dlugosc niepustych list w tablicy: 220.23529411764707
Maksymalna dlugosc listy w tablicy: 543

Hashowanie wbudowane
Suma pustych list w tablicy: 0
Srednia dlugosc niepustych list w tablicy: 220.23529411764707
Maksymalna dlugosc listy w tablicy: 245

-----------------------------------------------------------------
M=1031

Hashowanie własne (dobre)
Suma pustych list w tablicy: 239
Srednia dlugosc niepustych list w tablicy: 4.7272727272727275
Maksymalna dlugosc listy w tablicy: 20

Hashowanie własne (słabe)
Suma pustych list w tablicy: 980
Srednia dlugosc niepustych list w tablicy: 73.41176470588235
Maksymalna dlugosc listy w tablicy: 343

Hashowanie wbudowane
Suma pustych list w tablicy: 27
Srednia dlugosc niepustych list w tablicy: 3.729083665338645
Maksymalna dlugosc listy w tablicy: 12

-----------------------------------------------------------------
M=1024

Hashowanie własne (dobre)
Suma pustych list w tablicy: 230
Srednia dlugosc niepustych list w tablicy: 4.7153652392947105
Maksymalna dlugosc listy w tablicy: 20

Hashowanie własne (słabe)
Suma pustych list w tablicy: 1020
Srednia dlugosc niepustych list w tablicy: 936.0
Maksymalna dlugosc listy w tablicy: 1051

Hashowanie wbudowane
Suma pustych list w tablicy: 31
Srednia dlugosc niepustych list w tablicy: 3.770392749244713
Maksymalna dlugosc listy w tablicy: 10

-----------------------------------------------------------------

1. Rozmiar 1024 w dobrym hashowaniu własnym dawał lepsze wyniki, w słabym własnym lepsze wyniki dawał rozmiar 1031, natomiast w hashowaniu wbudowanym wyniki te były porównywalne.
2. Wybór funkcji hashującej wpływał na jakość wyniku (słaba miała największą ilość pustych list oraz największa maksymalną długośc listy, po niej była własna dobra, 
a najlepiej wypada wbudowana funkcja hash(). )

"""