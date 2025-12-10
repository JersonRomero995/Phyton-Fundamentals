# Casting Booleans
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(1j))
print(bool(0.0))
print(bool(0j))
print(bool('False'))
print(bool(''))
print(bool(None))

# the result is the same in the following examples therfore the bool is implicit 

my_list = [1,2]
if bool(my_list):
    print('My list has some values in it')

my_list = [1,2]
if (my_list):
    print('My list has some values in it')


a = 5
b = 5

if a - b:
    print('a and b are not equal')

print (a == b)

#Boolean Logic

weatherIsNice = True
haveUmbrella = False

if not (haveUmbrella or weatherIsNice):
    print('Stay inside')
else:
    print('Go for a walk')

weatherIsNice = True
haveUmbrella = False

if (not haveUmbrella) and (not weatherIsNice):
    print( 'Stay inside')
else:
    print('go for a walk')

weatherIsNice = True
haveUmbrella = False

if haveUmbrella or weatherIsNice:
    print('go for a walk')
else:
    print( 'Stay inside')
