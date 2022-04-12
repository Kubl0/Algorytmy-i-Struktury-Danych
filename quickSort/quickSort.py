import sys 
import threading
import random
from timeit import default_timer as timer

sys.setrecursionlimit(1000000)
threading.stack_size(1000000)

def sortowanie_szybkie(A,p,r):


    def quickSort(A,p,r):
        if p<r :
            q = partition(A,p,r)
            quickSort(A,p,q)
            quickSort(A,q+1,r)

    def partition(A,p,r):
        x=A[r] 
        i=p-1
        for j in range (p, r+1):
            if A[j]<=x :
                i=i+1
                A[i], A[j] = A[j], A[i]
        if i<r :
            return i
        else:
            return i-1
    

    quickSort(A,p,r)

def createArray(size, sort):
    array=[]

    for i in range(0, size):
        array.append(random.randint(0,10000))
    
    if(sort==True):
            array=sorted(array, reverse=True)

    return array

def main():

    sizes=[333,667,1000,1333,1667,2000]

    for size in sizes:

        lista=createArray(size, False)
        dl=size-1

        start=timer()
        sortowanie = threading.Thread(target=sortowanie_szybkie(lista, 0, dl))
        sortowanie.start()
        stop=timer()

        time=stop-start
        print(time)


if __name__=="__main__":
    main()

