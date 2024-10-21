class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        
        while curr and index > 0:
            print(curr.val)
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            return curr.val
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.tail == self.head: # empty list
            self.tail = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head
        
        for _ in range(index):
            if not curr.next:
                return
            curr = curr.next
            
        new_node.next = curr.next
        curr.next = new_node
        
        if curr == self.tail:
            self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for _ in range(index):
            if not curr.next:
                return
            curr = curr.next

        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next


    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

def test_linked_list():
    def assert_equal(actual, expected, message):
        assert actual == expected, f"{message}: expected {expected}, but got {actual}"

    # Test case 1: 基本操作
    print("Test case 1: Basic operations")
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    assert_equal(ll.get(2), 3, "Get element at index 1")
    ll.deleteAtIndex(1)
    assert_equal(ll.get(1), 3, "Get element at index 1 after deletion")

    # Test case 2: 邊界情況
    print("Test case 2: Edge cases")
    ll = MyLinkedList()
    assert_equal(ll.get(0), -1, "Get from empty list")
    ll.addAtIndex(1, 2)
    assert_equal(ll.get(0), -1, "Get after invalid insert")
    ll.addAtIndex(0, 1)
    assert_equal(ll.get(0), 1, "Get after valid insert at start")
    ll.deleteAtIndex(0)
    assert_equal(ll.get(0), -1, "Get after delete only element")

    # Test case 3: 複雜操作序列
    print("Test case 3: Complex operation sequence")
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    assert_equal(ll.get(1), 2, "Get middle element")
    ll.deleteAtIndex(1)
    assert_equal(ll.get(1), 3, "Get after delete middle")
    ll.addAtHead(4)
    ll.addAtTail(5)
    ll.deleteAtIndex(3)
    assert_equal(str(ll), "[4, 1, 3]", "Final list state")

    # Test case 4: 大量操作
    print("Test case 4: Bulk operations")
    ll = MyLinkedList()
    for i in range(1000):
        ll.addAtTail(i)
    assert_equal(ll.get(500), 500, "Get middle element after bulk insert")
    for i in range(0, 1000, 2):
        ll.deleteAtIndex(i)
    assert_equal(ll.get(250), 501, "Get element after bulk delete")

    print("All test cases passed!")

# 運行測試
test_linked_list()