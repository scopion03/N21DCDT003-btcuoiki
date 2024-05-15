def duynhat(mang_a):
    # Dùng set để loại bỏ các phần tử trùng nhau
    cac_phan_tu_khac_nhau = set(mang_a)
    
    # Chuyển set thành list và sắp xếp theo thứ tự tăng dần
    mang_b = sorted(list(cac_phan_tu_khac_nhau))
    
    return mang_b

# Ví dụ
mang_a = [1, 5, 3, 7, 5, 9, 7]
mang_b = duynhat(mang_a)
print(mang_b)  # Output: [1, 3, 5, 7, 9]
