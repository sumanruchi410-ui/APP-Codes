# Program to calculate the nth Fibonacci number
# using two efficient Dynamic Programming techniques

# TOP-DOWN APPROACH (MEMOIZATION) 

def fibonacci_memo(n, memo={}):
    # Base cases
    if n <= 1:
        return n

    # If already calculated, return stored value
    if n in memo:
        return memo[n]

    # Calculate and store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# BOTTOM-UP APPROACH (TABULATION) 

def fibonacci_tabulation(n):
    # Base cases
    if n <= 1:
        return n

    # Create a table to store Fibonacci numbers
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    # Fill the table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# MAIN PROGRAM 

# Take input from user
n = int(input("Enter the value of n: "))

# Calculate Fibonacci number using both methods
memo_result = fibonacci_memo(n)
tabulation_result = fibonacci_tabulation(n)

# Display results
print("Fibonacci number using Memoization:", memo_result)
print("Fibonacci number using Tabulation:", tabulation_result)