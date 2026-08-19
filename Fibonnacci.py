# Program to find the nth Fibonacci number
# using Memoisation and Tabulation

# MEMOISATION 

def fibonacci_memo(n, memo={}):
    # Base cases
    if n <= 1:
        return n

    # If value is already calculated, return it
    if n in memo:
        return memo[n]

    # Calculate and store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# TABULATION 

def fibonacci_tab(n):
    # Base cases
    if n <= 1:
        return n

    # Create a table to store Fibonacci values
    fib = [0] * (n + 1)

    # Initial values
    fib[0] = 0
    fib[1] = 1

    # Fill the table from bottom to top
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


#  MAIN PROGRAM 

# Take input from the user
n = int(input("Enter the value of n: "))

# Calculate using Memoisation
memo_result = fibonacci_memo(n)

# Calculate using Tabulation
tab_result = fibonacci_tab(n)

# Display results
print("Fibonacci number using Memoisation:", memo_result)
print("Fibonacci number using Tabulation:", tab_result)