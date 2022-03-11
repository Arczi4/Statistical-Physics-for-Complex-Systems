# Random walkers

import random
import matplotlib.pyplot as plt

direction = [-1, 1]

# For Kate, John plot display
d = 10
N = 4

kate_pos = [0] # Kate position
john_pos = [d] # John pos

avg_time = 0
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
        
        # print(kate_pos[-1], john_pos[-1])
        time += 1

    # # Kate, John plot    
    # plt.subplot(2,2,x)
    # ax = plt.gca()
    # plt.plot(kate_pos,'-o', markersize=4, label='Kate')
    # plt.plot(john_pos,'-o', markersize=4, label='John')
    # plt.xlabel("Time")
    # ax.xaxis.set_label_coords(.9, -.1)
    # plt.ylabel("Positon")
    # plt.legend()
    # # plt.plot([0, len(kate_pos)-1], [kate_pos[-1], kate_pos[-1]], color='red', marker='o')
    # plt.title(f"Met after {time}")
    
    # Avg time plot
    
    kate_pos = [0] # Kate position
    john_pos = [d] # John pos
    avg_time += time


# plt.show()

# add plot of avg time for d[0, 100]

# For avg time in steps plot display
d = 1
N = 5

kate_pos = [0] # Kate position
john_pos = [d] # John pos

avg_time = 0
avg_time_list = []
while d < 100:
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
            
            # print(kate_pos[-1], john_pos[-1])
            time += 1
        kate_pos = [0] # Kate position
        john_pos = [d] # John pos
        avg_time += time
    d += 1
    avg_time_list.append(avg_time/N)
    avg_time = 0

# Avg time plot
plt.plot(avg_time_list, '.')
plt.show()
    
    
