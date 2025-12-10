# Ints and Floats

print(20 / 4) #division will alway rusults in float

print(4 + 4.0) #addition with floats will always be float

print(2 ** 2.0) #number to the power of X.0 will be a float as well

# to convert float to integer (Int)

print(int(2.0))

print(int(8.9999999999)) # in this case the value does not get round correctly, the correct response should be 9, this is not a capability from python 

# to fix the round issue we need to use round to correct it 
print(round(8.99999999))

print(round(14/3, 2)) # we can use round as well to tell the amount of decimals we want 
# 4.67 in this response we se two decimal as we specified 
