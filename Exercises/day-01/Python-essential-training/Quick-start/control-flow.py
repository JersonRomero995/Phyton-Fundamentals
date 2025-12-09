# If / Else statements
a = True
b = True
c = True
if a:
    print('it is true!')
    print('also print this')
    if b:
        print('Both are true')
        if c:
            print('all are true!')
else: 
    print('it is false!')
print('Always print this')

# For loops
a = [1,2,3,4,5]
for number in a:
    print(number)


print(4 in a)

# While loops

d = 0
while d < 5:
    print(d)
    d=d+1