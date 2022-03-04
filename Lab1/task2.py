# Random walkers

import random

direction = [-1, 1]

d = 10

kate_pos = 0 # Kate position
john_pos = d # John pos

time = 0
while kate_pos != john_pos:
    # Update positions
    kate_update = random.choice(direction)
    john_update = random.choice(direction)
        
    if (kate_pos + kate_update) < 0 or (kate_pos + kate_update) > d:
        continue
    else:
        kate_pos += kate_update
        
    if (john_pos + john_update) < 0 or (john_pos + john_update) > d:
        continue
    else:
        john_pos += john_update
    
    print(kate_pos, john_pos)
    time += 1

print(f"met after {time}")

