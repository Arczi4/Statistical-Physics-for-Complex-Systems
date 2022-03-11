
class Node:
    def __init__(self, color, u) -> None:
        self.color = color
        self.u = u
        self.next = None

root = Node('white', 1)

head = root
circles = [root]
for x in range(5):
    head.next = Node('black', 0)
    if head.next != None:
        head = head.next
        circles.append(head)
        
circles.append(root)
for x in circles:
    print(f"({x.color, x.u}) =>", end="")