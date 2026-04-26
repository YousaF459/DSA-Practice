class LinkedList:
    
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = {
            "value": value,
            "next": None
        }

        self.tail["next"] = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = {
            "value": value,
            "next": None
        }

        node["next"] = self.head
        self.head = node
        self.length += 1

    def print_List(self):
        current = self.head
        result = []

        while current is not None:
            result.append(current["value"])
            current = current["next"]

        return result

    def insert(self, index, value):
        
        if index < 0 or index > self.length:
            return

        
        if index == 0:
            self.prepend(value)
            return

        
        if index == self.length:
            self.append(value)
            return

        node = {
            "value": value,
            "next": None
        }

        currentNode = self.head
        current = 0

        while current < index - 1:
            currentNode = currentNode["next"]
            current += 1

        node["next"] = currentNode["next"]
        currentNode["next"] = node
        self.length += 1

    def remove(self, index):
        
        if index < 0 or index >= self.length:
            return

        
        if index == 0:
            self.head = self.head["next"]
            self.length -= 1

            
            if self.length == 0:
                self.tail = None
                self.head = None
            return

        currentNode = self.head
        current = 0

        while current < index - 1:
            currentNode = currentNode["next"]
            current += 1

        nodeToDelete = currentNode["next"]
        currentNode["next"] = nodeToDelete["next"]

        
        if nodeToDelete == self.tail:
            self.tail = currentNode

        self.length -= 1


# Example usage
myLinkedList = LinkedList(10)
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.prepend(5)
myLinkedList.insert(1, 8)
myLinkedList.insert(1, 6)
myLinkedList.insert(4, 18)
myLinkedList.remove(4)

print(myLinkedList.print_List())