def factorial(i):
    if i <=1:
        return 1
    else:
        return i * factorial(i-1)
    
 
def ncr(n, r):
    return int(factorial(n) / (factorial(n - r) * factorial(r)))
 
n = int(input("Nhap so n: "))

if n <= 0:
    print("Nhap lai n")
else:
    print("Ve tam giac Pascal:")
    for i in range(0, n + 1):    
        for j in range(0, n + 1):
            if(ncr(i, j) != 0):
                print(" {:<3}".format(ncr(i, j)), end="")
        print("")