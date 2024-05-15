def is_upper_triangular(matrix):
    """
    Checks if the given matrix is upper triangular (all elements below the main diagonal are zero).
    Args:
        matrix (list of lists): The input matrix (square matrix).

    Returns:
        bool: True if the matrix is upper triangular, False otherwise.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True

# Example usage
my_matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

print(is_upper_triangular(my_matrix))  # Output: True

another_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(is_upper_triangular(another_matrix))  # Output: False
