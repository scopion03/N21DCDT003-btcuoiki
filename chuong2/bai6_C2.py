class Integer:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        self.value = value

    def Tru(self, b):
        if not isinstance(b, Integer):
            raise ValueError("b must be an instance of Integer class")
        return self.value - b.value

# Ví dụ sử dụng:
a = Integer(10)
b = Integer(5)
result = a.Tru(b)
print(result)  # Kết quả: 5
