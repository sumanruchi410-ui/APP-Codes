# Program to find the Longest Common Subsequence (LCS)
# between two sequences

def lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create a DP table
    # dp[i][j] stores the length of LCS of
    # first i elements of seq1 and first j elements of seq2
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                # If elements match, add 1 to diagonal value
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Otherwise, take the maximum of left and top values
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the DP table
    i = m
    j = n
    result = []

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            result.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse because we constructed it backwards
    result.reverse()

    return result, dp[m][n]


# Take input from the user
seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

# Find LCS
subsequence, length = lcs(seq1, seq2)

# Display output
print("Longest Common Subsequence:", "".join(subsequence))
print("Length of LCS:", length)