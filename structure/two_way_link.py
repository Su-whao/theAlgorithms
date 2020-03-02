# -*- conding: utf-8 -*-

class TwoWayLink:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

    def show(self):
        if self.prev:
            return
        cur = self
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def remove(self, val):
        if self.prev:
            return
        prev = None
        cur = self
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
                cur.prev = cur
            prev = cur
            cur = cur.next

if __name__ == "__main__":
    link = TwoWayLink(1)
    node_2 = TwoWayLink(2)
    node_3 = TwoWayLink(3)
    link.next = node_2
    node_2.next = node_3
    node_2.prev = link
    node_3.prev = node_2

    link.show()
    link.remove(2)
    link.show()

