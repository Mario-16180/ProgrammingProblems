class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, val):
        node_val = Node(val)
        if self.tail is not None:
            self.tail.next = node_val
            self.tail = node_val
        else:
            self.head = node_val
            self.tail = node_val
        self.count += 1

    def search(self, val):
        i = self.head
        n = 0
        while i.val is not None:
            if i.val == val:
                return n
            else:
                i = i.next
                if i is None:
                    return 'No value was found in the linked list'
            n += 1

    def reverse(self):
        prev = None
        current = self.head
        self.tail = current
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return 'Reversed'
    
    # # Check if the linked list is palindrome
    # def isPalindrome(self):
    #     # Find the middle of the linked list
    #     slow = self.head
    #     fast = self.head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     # Reverse the second half of the linked list
    #     prev = None
    #     current = slow
    #     while current is not None:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     # Compare the first half and the second half of the linked list
    #     first = self.head
    #     second = prev
    #     while second is not None:
    #         if first.val != second.val:
    #             return False
    #         first = first.next
    #         second = second.next
    #     return True

if __name__ == "__main__":
    l = LinkedList()
    l.append('a')
    l.append('b')
    l.append('c')
    l.append('d')
    print(l.head.val, l.tail.val, l.search('g'))
    l.reverse()
    print(l.head.val, l.tail.val)