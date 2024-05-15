def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def neper(n):
    sum_ak = 0
    for k in range(n + 1):
        ak = 1 / factorial(k)
        sum_ak += ak
    return sum_ak

n = int(input("Nhap so nguyen n (n >= 0): "))

if n < 0:
    print("Nhap so nguyen khong am.")
else:
    result = neper(n)
    print("Tong cua cac so hang tu a0 den a{} là: {:.10f}".format(n, result))