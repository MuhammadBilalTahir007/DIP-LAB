## Muhammad Bilal Tahir
## 01-134211-054
## BS CS 7B
## Function to get the Matric from the user by taking input
def get_matrix(rows, cols, name):
    print(f"Enter the elements of {name} (row by row):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element At: [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def matrix_multiplication(A, B):
    # Number of rows in A, columns in A, rows in B, columns in B
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Check if matrix multiplication is possible
    if cols_A != rows_B:
        print("Matrix multiplication is not possible. Number of columns in A must equal the number of rows in B.")
        return None

    # Resultant matrix C with dimensions rows_A x cols_B
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B, since cols_A == rows_B
                C[i][j] += A[i][k] * B[k][j]

    return C

# Get dimensions and elements of matrix A
rows_A = int(input("Total Rows in Matrix A: "))
cols_A = int(input("Total Columns in Matrix A: "))
A = get_matrix(rows_A, cols_A, 'A')

# Get dimensions and elements of matrix B
rows_B = int(input("Total Rows in Matrix B: "))
cols_B = int(input("Total Columns in Matrix B: "))
B = get_matrix(rows_B, cols_B, 'B')

# Perform matrix multiplication
result = matrix_multiplication(A, B)

# Display matrices and result
if result:
    print("\nMatrix A:")
    for row in A:
        print(row)
    
    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nMatrix A * Matrix B:")
    for row in result:
        print(row)
