def counting_islands(matrix):
    """
    Counts the number of islands in a given matrix.

    Args:
    - matrix (list of lists of int): The matrix representing the map with 1s as islands and 0s as ocean.

    Returns:
    - int: The number of islands in the matrix.

    """
    def dfs(matrix, i, j):
        # Base case: If the cell is out of bounds or already visited, return
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
            return
        # Mark the cell as visited
        matrix[i][j] = 0  
        # Explore neighbors recursively
        dfs(matrix, i+1, j)
        dfs(matrix, i-1, j)
        dfs(matrix, i, j+1)
        dfs(matrix, i, j-1)
    
    # Initialize islands count
    islands_count = 0
    # Iterate through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # If the cell represents an island, explore it and increment the count
            if matrix[i][j] == 1:
                islands_count += 1
                dfs(matrix, i, j)
    # Return the total count of islands
    return islands_count

# Test cases
test_cases = [
    (3, 3, [
        [0,1,0],
        [0,0,0],
        [0,1,1]
    ]),
    (3, 4, [
        [0,0,0,1],
        [0,0,1,0],
        [0,1,0,0]
    ]),
    (3, 4, [
        [0,0,0,1],
        [0,0,1,1],
        [0,1,0,1]
    ])
]

for m, n, matrix in test_cases:
    print(f"Input: {m}x{n}")
    for row in matrix:
        print("".join(map(str, row)))
    print("Output:", count_islands(matrix))
    print()