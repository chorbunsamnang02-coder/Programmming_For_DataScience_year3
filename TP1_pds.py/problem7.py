def digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n // 10)
def reverse(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse(n // 10)))
def palindrome(n):
    return n == reverse(n)

### part A
num =[2026 , 12321,9875]
for n in num:
    print(n, ": degit sum =", digit_sum(n), " , reverse = ", reverse(n), " , palindrome ", palindrome(n))

### Part B
count_palin=0
for i in range(10 ,999):
    if palindrome(i):
        count_palin+=1
print(count_palin)

