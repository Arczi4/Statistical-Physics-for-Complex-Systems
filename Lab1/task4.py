
# from cProfile import label
import random
import matplotlib.pyplot as plt


class Node:
    black = 0
    white = 0
    def __init__(self, color, u) -> None:
        self.color = color
        self.u = u
        self.next = None
        
        if self.color == 'black':
            Node.black += 1
        else:
            Node.white += 1
    
    def change_color(self):
        if self.color == 'black':
            self.color = 'white'
            Node.black -= 1
            Node.white += 1
        else:
            self.color = 'black'
            Node.black += 1
            Node.white -= 1
        
def init(N, u, init_color) -> list:
    root = Node(init_color, u)
    head = root
    circles = [root]
    for x in range(N):
        head.next = Node(init_color, u)
        if head.next != None:
            head = head.next
            circles.append(head)
    circles.append(root) # add connection last element to the root
    
    return circles # list of nodes, number of black balls, white balls

def plot_number_of_balls(N, u, init_color):
    circle = init(N, u, init_color)
    
    balls = [circle[0].black - circle[0].white]
    for time in range(M):
        for node in circle:
            decision = random.choices([0, 1], weights=[1-node.u, u]) # 0 dont change, 1 change color
            if decision[0]:
                node.change_color()
                balls.append(circle[0].black - circle[0].white)

    plt.plot(balls, label='black - white')
    plt.title(f'N={N} u={u}')
    plt.legend()
    plt.show()

# Task 1:
M = 400
N = 1000
u = 0.009
# All black balls
init_color = 'black'

plot_number_of_balls(500, u, init_color)
plot_number_of_balls(1000, u, init_color)
plot_number_of_balls(2000, u, init_color)
