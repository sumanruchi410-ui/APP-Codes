# 0/1 Knapsack Problem for 5 items
# Find the maximum value within a given weight capacity.

# TOP-DOWN APPROACH 
# Recursion + Memoization

def knapsack_top_down(weights, values, capacity):
    n = 5

    # Create memoization table
    dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

    def solve(i, remaining):
        # Base case
        if i == 0 or remaining == 0:
            return 0

        # Return already calculated value
        if dp[i][remaining] != -1:
            return dp[i][remaining]

        # If item is too heavy, exclude it
        if weights[i - 1] > remaining:
            dp[i][remaining] = solve(i - 1, remaining)

        else:
            # Include the item
            include = values[i - 1] + solve(
                i - 1, remaining - weights[i - 1]
            )

            # Exclude the item
            exclude = solve(i - 1, remaining)

            # Select the maximum value
            dp[i][remaining] = max(include, exclude)

        return dp[i][remaining]

    return solve(n, capacity)


# BOTTOM-UP APPROACH 
# Iterative Dynamic Programming

def knapsack_bottom_up(weights, values, capacity):
    n = 5

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                # Include or exclude the item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                # Item cannot be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# MAIN PROGRAM 

# Exactly 5 items
weights = []
values = []

print("Enter weight and value for 5 items:")

for i in range(5):
    weight = int(input(f"Weight of item {i + 1}: "))
    value = int(input(f"Value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter maximum weight capacity: "))

# Calculate maximum value using both methods
top_down = knapsack_top_down(weights, values, capacity)
bottom_up = knapsack_bottom_up(weights, values, capacity)

# Display results
print("\nMaximum value using Top-Down:", top_down)
print("Maximum value using Bottom-Up:", bottom_up)