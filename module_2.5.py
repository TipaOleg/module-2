numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.remove(1)
primes = []
not_primes = []


for i in numbers:
    if i == 2 or i == 3:
        primes.append(i)
    elif i % 2 == 0:
        not_primes.append(i)
    elif i % 3 == 0:
        not_primes.append(i)
    else:
        primes.append(i)


print(primes)
print((not_primes))