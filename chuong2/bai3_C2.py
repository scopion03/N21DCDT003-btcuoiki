def has_identical_rows(matrix):
    # Convert each row of the matrix to a tuple and add it to a set
    # If a row is already in the set, it means there is an identical row
    rows_set = set()
    for row in matrix:
        row_tuple = tuple(row)
        if row_tuple in rows_set:
            return True
        rows_set.add(row_tuple)
    return False

# Example usage:
# Define a square matrix
square_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]  # This row is identical to the first row
]

# Call the function and print the result
print(has_identical_rows(square_matrix))
