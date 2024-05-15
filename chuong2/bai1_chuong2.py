def mang_DoiXung(mang):
    n = len(mang)
    for i in range(n):
        for j in range(n):

            if mang[i][j] != mang[j][i]:
                return False
            
    return True 

ma_tran = [
    [3, 2, 5],
    [2, 1, 4],
    [5, 4, 1]
]
print(mang_DoiXung(ma_tran))
        