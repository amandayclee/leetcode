class ListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class BrowserHistory:

    def __init__(self, homepage: str):
        self.whereami = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.whereami.next = new_node
        new_node.prev = self.whereami
        self.whereami = new_node

    def back(self, steps: int) -> str:
        while self.whereami.prev and steps > 0:
            self.whereami = self.whereami.prev
            steps -= 1    
        return self.whereami.val

    def forward(self, steps: int) -> str:
        while self.whereami.next and steps > 0:
            self.whereami = self.whereami.next
            steps -= 1
        return self.whereami.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)