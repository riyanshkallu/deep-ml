def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    final = []
    for col in range(len(a[0])):
        inverse = []
        for row in range(len(a)):
            inverse.append(a[row][col])
        final.append(inverse)
    return final

    # Your code here
    pass