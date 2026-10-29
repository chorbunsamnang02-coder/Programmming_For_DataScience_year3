###   part A
# a=int("7") + 3.5
# b=str(10) * 3
# c=bool(""), bool(" ")
# d=int(3.99)
# e=float("1e3")
# f=int(True) + float("2.5")
# g=round(2.5), round(3.5)
# h=type(10 / 2)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)

### Part B
def safe_int(text):
    try:
        num = float(text)
        return int(num)
    except ValueError:
        return None

for sample in ["42", " -8 ", "3.9", "abc", ""]: 
    print(repr(sample), "->", safe_int(sample))

#### cnumber

enter = input(" enter two data :")
data1, data2 = enter.split()
num1 = safe_int(data1)
num2 = safe_int(data2)
if num1 is not None and num2 is not None:
    print("The sum is:", num1 + num2)
else:
    print("One or both inputs are not valid numbers.")