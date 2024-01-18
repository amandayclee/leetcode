# double linked list
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_node = ListNode(homepage)


    def visit(self, url: str) -> None:
        self.current_node.next = ListNode(url, self.current_node)
        self.current_node = self.current_node.next


    def back(self, steps: int) -> str:
        while self.current_node.prev and steps > 0:
            self.current_node = self.current_node.prev
            steps -= 1
        return self.current_node.val


    def forward(self, steps: int) -> str:
        while self.current_node.next and steps > 0:
            self.current_node = self.current_node.next
            steps -= 1
        return self.current_node.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)