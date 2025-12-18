def matrix_chain_multiplication(dimensions):
    """
    Time: O(n^3)
    Space: O(n^2)
    """
    num_matrices = len(dimensions) - 1

    # dp[i][j] = minimum cost to multiply Ai..Aj
    dp = [[0] * num_matrices for _ in range(num_matrices)]

    # split[i][j] = index k where optimal split occurs
    split = [[0] * num_matrices for _ in range(num_matrices)]

    # chain_length is the length of the matrix sub-chain
    for chain_length in range(2, num_matrices + 1):
        for i in range(num_matrices - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost_left = dp[i][k]
                cost_right = dp[k + 1][j]
                cost_multiply = (
                    dimensions[i]
                    * dimensions[k + 1]
                    * dimensions[j + 1]
                )

                total_cost = cost_left + cost_right + cost_multiply

                if total_cost < dp[i][j]:
                    dp[i][j] = total_cost
                    split[i][j] = k

    return dp, split
