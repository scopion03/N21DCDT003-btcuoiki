def is_symmetric(arr):
    """
    Checks if the given array is symmetric.
    Args:
        arr (list): The input array.

    Returns:
        bool: True if the array is symmetric, False otherwise.
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i][j] != arr[j][i]:
                return False
    return True

# Example usage
my_array = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

print(is_symmetric(my_array))  # Output: True

another_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(is_symmetric(another_array))  # Output: False
