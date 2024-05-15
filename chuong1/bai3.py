def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = int(input("Nhap so nguyen duong m:"))
n = int(input("Nhap so nguyen duong n: "))

print(f"GCD cua {m} và {n} la: {gcd(m, n)}")
