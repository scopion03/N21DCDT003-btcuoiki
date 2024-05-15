def a_Nhan_b(a, b):
    if len(a) != len(b):
        return "The arrays must have the same length"
    
    result = 1
    for i in range(len(a)):
        result *= a[i] * b[i]
        
    if result > 0:
        return result
    else:
        return [0] * len(a)

# Ví dụ sử dụng:
a = [1, 2, 3]
b = [4, 5, 6]
print(a_Nhan_b(a, b))  
