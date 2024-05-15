class Mang:
    def __init__(self, matrix):
        self.matrix = matrix

    def TamGiacDuoi(self):
        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    return False
        return True

# Ví dụ sử dụng:
matrix = [
    [1, 0, 0],
    [4, 5, 0],
    [7, 8, 9]
]

mang = Mang(matrix)
print(mang.TamGiacDuoi())  # Kết quả: True
