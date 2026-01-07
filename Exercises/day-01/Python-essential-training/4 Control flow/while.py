from datetime import datetime

#While loops
'''
print(datetime.now().second)

print(datetime.now())

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    print(f'we are at {wait_until} seconds!')

wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    1+1
print(f'we are at {wait_until} seconds!')
'''

#Pass

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    pass
print(f'we are at {wait_until} seconds!')


# Break
wait_until = (datetime.now().second + 2) % 60

while True:
    if datetime.now().second == wait_until:
        print(f'we are at {wait_until} seconds!')
        break

wait_until = (datetime.now().second + 2) % 60

'''
while True:
    while datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds!')
        break
'''

#Continue
wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    continue
    print('Still waiting!')
    
    
print(f'We are at {wait_until} seconds!')

wait_until = (datetime.now().second + 2) % 60

while True:
    if datetime.now().second < wait_until:
        continue
    break
    
    
print(f'We are at {wait_until} seconds!')
