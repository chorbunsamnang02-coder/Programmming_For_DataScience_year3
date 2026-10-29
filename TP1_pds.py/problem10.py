### Part A
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

#### Part B
print("Primes below 50:", end=" ")
for i in range(2, 50):
    if is_prime(i):
        print(i, end=" ")
print()

count_100 = 0
for i in range(2, 100):
    if is_prime(i):
        count_100 += 1
print(f"Number of primes below 100: {count_100}")

#### Part C
def goldbach(n):
    for p in range(2, n):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                return (p, q)
    return None

for even in range(4, 32, 2):
    pair = goldbach(even)
    if pair:
        print(f"{even} = {pair[0]} + {pair[1]}")

### Part D
holds = True
for even in range(4, 10001, 2):
    if goldbach(even) is None:
        holds = False
        break

print(f"Goldbach holds for every even number from 4 to 10000: {holds}")

