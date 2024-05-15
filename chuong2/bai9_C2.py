def TrungCot(matrix):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return False
    
    # Get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])
    
    # Iterate over each column
    for col in range(cols):
        # Create a set to store unique elements of the column
        unique_elements = set()
        
        # Iterate over each row and add the element to the set
        for row in range(rows):
            unique_elements.add(matrix[row][col])
        
        # If the number of unique elements is less than the number of rows,
        # it means there are duplicate elements in the column
        if len(unique_elements) < rows:
            return True
    
    # If no column has duplicate elements, return False
    return False

# Example usage:
# Define a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 3]  # This column has duplicate element '3'
]

# Call the function and print the result
print(TrungCot(matrix))
