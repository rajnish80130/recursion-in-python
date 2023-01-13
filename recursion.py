#************Recursion***********
# 1 program   --> Multiply
def mul(a,b):

    if b==1:
        return a
    else:
        return a + mul(a,b-1)

print(mul(3,4))

# 2 program  --> Factorial

def fact(num):

    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num-1)

print(fact(5))

# 3 program  --> pallindrome

def pallindrome(text):

    if len(text) <= 1:
        print("Pallindrome")
    else:
        if text[0] == text[-1]:
            pallindrome(text[1:-1])
        else:
            print("This is not pallindrome")

pallindrome("ava")
pallindrome("riya")
pallindrome("abba")

# 4 Program  ---> fibonacci series
import time
def fibb(num):

    if num == 0 or num == 1:
        return 1
    else:
        return fibb(num-1) + fibb(num-2)

start = time.time()

print(fibb(10))
# print(fibb(37))
print(time.time()-start)

# 5 program  --> Rabbit Problem

def memo(m,d):

    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1,d) + memo(m-2,d)
        return d[m]

start = time.time()
d = {0:1,1:1}
print(memo(900,d))
print(time.time() - start)