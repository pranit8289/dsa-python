class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
class LinkedList():
    def __init__(self):
        self.head = None

    def print_linekd_list(self):
        if self.head is None:
            print("linked list is empty...!")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data)+"-->"
            itr = itr.next
        return llstr

    def insert_at_the_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data=data, next=None)

    def insert_values_in_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data=data)

    def get_length_of_ll(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_element_from_index(self, index):
        if index < 0 or index >= self.get_length_of_ll():
            raise Exception("this is not valid index")
        
        if index ==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length_of_ll():
            raise Exception("this is not valid index")
        
        if index == 0:
            self.insert_at_the_beginning(data=data)

        count = 0
        itr = self.head
        while itr:

            if count == index-1:
                itr.next = Node(data=data, next=itr.next)
                break

            itr = itr.next
            count += 1



if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_the_beginning(5)
    # ll.insert_at_the_beginning(15)
    # ll.insert_at_the_beginning(56)
    # ll.insert_at_end(10)
    ll.insert_values_in_list([10, 165, "Fruit", 568, 9, "Bear", 653, 97])

    print(ll.print_linekd_list())
    print("length of LL - {}".format(ll.get_length_of_ll()))
    ll.remove_element_from_index(2)
    print(ll.print_linekd_list())
    print("length of LL - {}".format(ll.get_length_of_ll()))
    # ll.remove_element_from_index(20) #just to test the exception
    ll.insert_at_index(2, "ninghty")
    print(ll.print_linekd_list())
    print("length of LL - {}".format(ll.get_length_of_ll()))