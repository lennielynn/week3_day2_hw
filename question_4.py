# <p>Write a recursion function to perform the fibonacci sequence up to the number passed in.</p>

# `Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8`

def fib(n, it=0, a=0, b=1):
    if it == n:
        return f"Iteration {it}: {b}\n"
    return f"Iteration {it}: {b}\n" + fib(n, it + 1, b, a + b)
result = fib(13)
print(result)