#If statements with "FizzBuzz"
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16

for n in range (1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 ==0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)
                