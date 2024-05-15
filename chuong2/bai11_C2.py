class IntegerOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Cong(self):
        result = self.a + self.b
        if result < -1 or result > 1:
            return -1
        else:
            return result

# Example usage:
# Create an instance of the class with the integers a and b
operation = IntegerOperation(1, 0)

# Call the Cong method and print the result
print(operation.Cong())  # Output should be 1
