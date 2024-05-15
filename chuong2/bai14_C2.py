def aDayConDauTien(a, b):
    result = []
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            result.extend(b)
            break
    return result

# Ví dụ sử dụng:
a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [6, 2]
print(aDayConDauTien(a,b))  # Kết quả: [6,2]


