# Random walkers

import random
import matplotlib.pyplot as plt

direction = [-1, 1]

d = 10

kate_pos = [0] # Kate position
john_pos = [d] # John pos

N = 4
for x in range(1, N+1):
    time = 0
    while kate_pos[-1] != john_pos[-1]:
        # Update positions
        kate_update = random.choice(direction)
        john_update = random.choice(direction)
            
        if (kate_pos[-1] + kate_update) < 0 or (kate_pos[-1] + kate_update) > d:
            kate_pos.append(kate_pos[-1])
        else:
            kate_pos.append(kate_pos[-1] + kate_update)
            
        if (john_pos[-1] + john_update) < 0 or (john_pos[-1] + john_update) > d:
            john_pos.append(john_pos[-1])
        else:
            john_pos.append(john_pos[-1] + john_update)
        
        print(kate_pos[-1], john_pos[-1])
        time += 1

    plt.subplot(2,2,x)
    plt.plot(kate_pos,'-o', markersize=4)
    plt.plot(john_pos,'-o', markersize=4)
    plt.plot([0, len(kate_pos)-1], [kate_pos[-1], kate_pos[-1]], color='red', marker='o')
    plt.title(f"Met after {time}")
    kate_pos = [0] # Kate position
    john_pos = [d] # John pos
    
plt.show()

