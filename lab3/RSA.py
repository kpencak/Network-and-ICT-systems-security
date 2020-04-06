def find_primes(n):
    for number in primes:
        if n%number == 0:
            p = n%number
            if p in primes:
                q = number
                return p, q;
    return -1


def private(p, q, e):
    for i in range(20):
        if (e*(i*3599+1)%(p-1)(q-1)) == 1:
            return i
    return -1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print("Write n: ")
n = int(input())
print("Write e: ")
e = int(input())
         
li = primes(n)



d = private(61, 59, 31)