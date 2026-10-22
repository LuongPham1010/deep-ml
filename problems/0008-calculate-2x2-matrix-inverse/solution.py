def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    det = (matrix[0][0] * matrix[1][1]) - ( matrix[1][0] * matrix[0][1] )
    if det == 0 :
        return None
    else :
        rows, cols = 2, 2 
        new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        new_matrix[0][0] = matrix[1][1]
        new_matrix[1][1]= matrix[0][0]
        new_matrix[0][1] = -matrix[0][1]
        new_matrix[1][0] = -matrix[1][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = (1/ det) * new_matrix[i][j]
                
        return new_matrix


    