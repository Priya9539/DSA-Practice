def set_zeroes(matrix):
    """
    Problem: Set Matrix Zeroes

    Time Complexity: O(m * n)
        - We traverse the matrix a constant number of times.

    Space Complexity: O(1)
        - No extra data structures used.
        - We use first row and first column as markers.
    """

    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zero = False
    first_col_zero = False

    # Step 1: Check if first row has zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Step 2: Check if first column has zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Step 3: Use first row & column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 4: Set cells to zero based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 5: Zero out first row if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Step 6: Zero out first column if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


# Example
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(set_zeroes(matrix))

