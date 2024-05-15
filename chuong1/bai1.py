# Phuong thuc de quy
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
   


n = int(input("Nhap so Fibonacci muon tinh: "))

if n <= 0:
    print("Nhap mot so nguyen duong:")
else:
    print("So Fibonacci tuong ung la:", fibonacci_recursion(n))