def process_arrays(array1, array2):
    # Check if the arrays are of the same length
    if len(array1) != len(array2):
        return "Arrays must be of the same length"
    
    # Example operation: sum the products of corresponding elements
    result = sum(a * b for a, b in zip(array1, array2))
    
    # Return the result
    return result

# Example usage:
array1 = [1, 2, 3]
array2 = [4, 5, 6]
print(process_arrays(array1, array2))

# Note: The user should replace the example operation with the actual operation required by the problem.
