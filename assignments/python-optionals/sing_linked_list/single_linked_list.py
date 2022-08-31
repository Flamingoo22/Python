class SList:
    def __init__(self):
        self.head = None
        
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        index = 1
        runner = self.head
        while(index < n):
            runner = runner.next
            index +=1
        temp = runner.next
        new_node = SLNode(val)
        runner.next = new_node
        new_node.next = temp
        return self
    
    def remove_val(self, val):
        if self.head.value == val:
            self.head = self.head.next
            return self
        runner = self.head
        while(runner.next.value != val):
            print(runner.value)
            runner = runner.next
        runner.next = runner.next.next
        
    def remove_from_front(self):
        self.head = self.head.next
        # print(self.head)
        return self
        
    def remove_from_back(self):
        runner = self.head
        while(runner.next.next != None):
            runner = runner.next
        runner.next = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
        
        
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()

my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.insert_at("dsa",2).print_values()

# my_list.remove_val("are")

# my_list.print_values()




