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

## Function to Print the Matrixes.
def print_matrix(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print(row)

## Function to Add Two Matrixes.
def add_matrices(firstMatrix, secondMatrix):
    rows = len(firstMatrix)
    cols = len(firstMatrix[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(firstMatrix[i][j] + secondMatrix[i][j])
        result.append(row)
    return result

# Get matrix dimensions from the User
rows = int(input("Enter Total Rows for the Matrices "))
cols = int(input("Enter Total Columns for the Matrices "))

# Calling the get Matrix function
matrix_a = get_matrix(rows, cols, "A")
matrix_b = get_matrix(rows, cols, "B")

## Verifying that the dimensions of the matrices match to ensure addition
if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
    # Adding Matrices
    result_matrix = add_matrices(matrix_a, matrix_b)
    
    # Printing
    print_matrix(matrix_a, "A:")
    print_matrix(matrix_b, "B:")
    print_matrix(result_matrix, "A + B:")
else:
    print("Error: Matrices must be of the same dimensions to be added")
