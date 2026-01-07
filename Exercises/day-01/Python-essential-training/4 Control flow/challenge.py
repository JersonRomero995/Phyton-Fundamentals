'''
Docstring para Exercises.day-01.Python-essential-training.4 Control flow.challenge
Faster Prime Finding
Write a function that returns a list of all primes up to a given number.

For each number, in order to determine if it is prime, take the following steps:

Find the square root of the number
Find all the primes up to that square root
Test to see if any of those primes are divisors
If a number has no prime divisors, it is prime!
'''
print(['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)])


def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, number):
        sqrNum = number**0.5
        for factor in primes:
            if number %  factor  == 0:
                # not prime
                break
            if factor > sqrNum:
                # it's prime!
                primes.append(number)
                break
    return primes


print(allPrimesUpTo(100))

