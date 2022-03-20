n = int(input("please enter the number："))
for i in range(2, n):
    if n % i == 0:
        print(" %d is not a prime number！" % n)
        break
else:
    print(" %d is a prime number！" % n)
