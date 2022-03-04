from math import pow
import matplotlib.pyplot as plt

def multiple_horizontal_plot(*args):
    columns = len(args)
    plot_nr = 1
    for obj in args:
        plt.subplot(1, columns, plot_nr)
        plot_nr += 1
        obj.plot_un_horizontal_n_vertical()
    plt.show()
    
def multiple_un1_un_plot(*args):
    columns = len(args)
    plot_nr = 1
    for obj in args:
        plt.subplot(1, columns, plot_nr)
        plot_nr += 1
        obj.plot_un1_horizontal_un_vertical()
    plt.show()
    
def multiple_plot3d(*args):
    columns = len(args)
    plot_nr = 1
    for obj in args:
        plt.subplot(1, columns, plot_nr)
        plot_nr += 1
        obj.plot_3d()
    plt.show()

class Prng:
    def __init__(self, a, c, m, x) -> None:
        self.a = a
        self.c = c
        self.m = m
        self.x = x
        self.randoms = []
    
    def next_x(self):
        self.x = (self.a * self.x + self.c) % self.m
        self.randoms.append(self.x / self.m) # append U
    
    def show_sequence(self):
        print(self.randoms)
    
    def generate_sequence(self, seq_len: int):
        [self.next_x() for _ in range(seq_len)]
        
    def save_sequence(self):
        with open("LGC1-N1000U0.txt", "w") as f:
            for num in self.randoms:
                f.write(str(num) + '\n')
                
    def plot_hist(self):
        plt.hist(self.randoms, bins = 40, edgecolor = 'black')
        plt.show()
        
    def read_sequence(self, filename: str):
        with open(filename, "r") as f:
            self.randoms = list(map(lambda x: float(x.rstrip()), f.readlines()))
        
    def plot_un_horizontal_n_vertical(self):
        plt.plot(self.randoms, [_ for _ in range(len(self.randoms))],'-o', markersize=2, linewidth=0.6)
        
    def plot_un1_horizontal_un_vertical(self):
        plt.plot(self.randoms[1::2], self.randoms[::2], '.')
        
    def plot_3d(self):
        fig = plt.figure()
 
        # syntax for 3-D projection
        ax = plt.axes(projection ='3d')
        plot_list = self.randoms[:-1]
        # plotting
        ax.plot3D(plot_list[2::3], plot_list[1::3], plot_list[::3], '.')
        ax.set_title('')
        plt.show()
    
r = Prng(23, 0, pow(10, 8) + 1, 1)
r.read_sequence('LGC1-N1000U0.txt')
print(len(r.randoms))

r1 = Prng(23, 0, pow(10, 8) + 1, 2)
r1.generate_sequence(1000)
print(len(r1.randoms))

r2 = Prng(23, 0, pow(10, 8) + 1, 10)
r2.generate_sequence(1000)
print(len(r2.randoms))

r3 = Prng(23, 0, pow(10, 8) + 1, 1000)
r3.generate_sequence(1000)
print(len(r3.randoms))

multiple_horizontal_plot(r,r1,r2,r3)
multiple_un1_un_plot(r,r1,r2,r3)
r2.plot_3d()


