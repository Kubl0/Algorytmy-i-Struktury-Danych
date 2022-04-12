class Node:
    def __init__(self,k):
        self.value=k
        self.next=None
        self.prev=None 

class LinkedList:
    def __init__(self):
        self.head=None

    def wstaw(self, x):
        x.next=self.head  
        if self.head!=None:
           self.head.prev=x 
        self.head=x
        x.prev=None

    def drukuj(self):
        x=self.head
        while x!=None:
            print(x.value, end='->')
            x=x.next

    def szukaj(self,k):
        x = self.head
        idx=0
        while x!=None and x.value!=k:
            x = x.next
            idx+=1
        """if x!=None:
            print(idx)
        """
        return x   

    def usun(self,x):      
        if x.prev != None:
           x.prev.next = x.next
        else:
           self.head = x.next
        if x.next != None:
           x.next.prev = x.prev
    
    def bezpowtorzen(self, lista):
        duplikaty=[]
        x=lista.head

        print()

        while x!=None:
            if x.value not in duplikaty:
                y=lbp.head
                if y==None:
                    lbp.wstaw(Node(x.value))
                else:
                    while(y.next!=None):
                        y=y.next
                    y.next=Node(x.value)   

                duplikaty.append(x.value)
            x=x.next
        return lbp


    def scal(self, lista1, lista2):
        l3.head=lista1.head
        x=l3.head
        while x.next!=None:
            x=x.next
        y=lista2.head      
        x.next=y

        return l3

        

  


l=LinkedList()
lbp=LinkedList()
l3=LinkedList()

l.wstaw(Node(2)) 
l.wstaw(Node(3))  
l.wstaw(Node(5)) 
l.wstaw(Node(8)) 
l.wstaw(Node(12)) 
l.wstaw(Node(3))
l.wstaw(Node(6))

l.drukuj()

l.usun(l.szukaj(5))

print()

l.drukuj()

l.bezpowtorzen(l)

lbp.drukuj()

print()

l.scal(l,lbp)

l3.drukuj()

