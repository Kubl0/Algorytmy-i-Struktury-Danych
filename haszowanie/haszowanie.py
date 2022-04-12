
def main():
    filepath='input.txt'
    f=open(filepath, 'r')
    array = []
    
    line = f.readline()
    while line!="":
        line=str(line).replace("\n", "")
        array.append(line)
        line = f.readline()
        
    for element in array:
        print(element)

if __name__ == "__main__":
    main()