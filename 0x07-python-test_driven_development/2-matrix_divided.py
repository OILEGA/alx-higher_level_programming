def matrix_divided(matrix, div):
    # Check that matrix is a list of lists of integers or floats
    if not all(type(row, list) and all(type(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check that each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check that div is a number
    if not type(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check that div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element of the matrix by div, rounded to 2 decimal places
    return [[round(x / div, 2) for x in row] for row in matrix]
