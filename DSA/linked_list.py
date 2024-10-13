class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def set_next(self,next):
        self.next=next


class LinkedList(object):
    def __init__(self):
        self.head=None

    def print_fuc(self):
        temp=self.head
        while(temp):
            print(f"{temp.data}-->",end=" ")
            temp=temp.next

        print('Null')

    def search_list(self,key):
        temp=self.head
        while(temp):
            if temp.data == key:
                print("KEY FOUND")
                return
            temp=temp.next
        print('KEY Not FOund')
    def insert_at_first(self,data):
        if self.head==None:
            newNode=Node(data)
            self.head=newNode
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
    
    def insert_at_end(self,data):
        newNode=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newNode
    
    def insert_btn(self,previeusNode,data):
        if previeusNode.next is None:
            print("Previeus Node cannot be Done ")
        else:
            newNode=Node(data)
            newNode.next=previeusNode.next
            previeusNode.next=newNode



if __name__=="__main__":
    list=LinkedList()
    list.head=Node(1)
    node2=Node(2)
    list.head.set_next(node2)
    node3=Node(3)
    node2.set_next(node3)
    list.insert_btn(node2,100)
    list.insert_at_end(15)
    list.print_fuc()
    list.search_list(45)