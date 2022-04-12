def heapify(array, size, i):
    left=2*i+1
    right=2*i+2

    if(left<size and array[left]>array[i]):
        largest=left
    else:
        largest=i
    if(right<size and array[right]>array[largest]):
        largest=right
    if(largest!=i):
        array[i], array[largest]=array[largest], array[i]
        heapify(array, size, largest)
    return array

def buildHeap(array):
    size=len(array)
    k=int((len(array)-2)/2)

    for i in range(k, -1, -1):
        heapify(array, size, i)

    return array

def heapSort(array):
    array=buildHeap(array)
    size=len(array)

    for i in range(len(array)-1, 0, -1):
        array[0], array[size-1]=array[size-1], array[0]
        size -= 1

        heapify(array, size, 0)

    return array

def main():
    filepath='input.txt'
    f=open(filepath, 'r')
    array = []
    
    line = f.readline()
    while line!="":
        line=int(line)
        array.append(line)
        line = f.readline()

    heapSort(array)

    filepath='output.txt'
    f=open(filepath, 'w')

    for element in array:
        element=str(element)
        f.write(element)
        f.write('\n')
        

if __name__ == "__main__":
    main()


