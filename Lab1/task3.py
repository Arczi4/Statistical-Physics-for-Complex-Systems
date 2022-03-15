import random
import matplotlib.pyplot as plt

class Dog:
    all_fleas = 0
    def __init__(self, name: str):
        self.name = name

class Flea:
    def __init__(self, on_dog) -> None:
        self.on_dog = on_dog
    
    def im_on_dog(self):
        print(f"i'm on dog {self.on_dog}")
        
    def jump_on_dog(self, dog):
        self.on_dog = dog
        
# init
N = 1000
time = 100000
p = [0.5, 0.5]

rex = Dog("Rex")
ace = Dog("Ace")

fleas = [Flea(rex.name) for x in range(N)]

fleas_on_rex = [N]
fleas_on_ace = [0]

for i in range(time):
    random_flea = random.choice(fleas)
    
    # 0 - stay on dog, 1 - jump
    decision = random.choices([0, 1], weights=p)
    if decision:
        if random_flea.on_dog == rex.name:
            random_flea.jump_on_dog(ace.name)
            fleas_on_ace.append(fleas_on_ace[i] + 1)
            fleas_on_rex.append(fleas_on_rex[i] - 1)
        else:
            random_flea.jump_on_dog(rex.name)
            fleas_on_rex.append(fleas_on_rex[i] + 1)
            fleas_on_ace.append(fleas_on_ace[i] - 1) 
            
plt.plot([x for x in range(time+1)], fleas_on_rex, label="Rex")
plt.plot([x for x in range(time+1)], fleas_on_ace, label="Ace")
plt.xlabel("Time")
plt.ylabel("Fleas number")
plt.legend()
plt.show()

with open(f"N{N}p{p[1]}t{time}.txt", 'w') as f:
    for s in range(time):
        f.writelines(f"{s}  {fleas_on_ace[s]}  {fleas_on_rex[s]}\n")

