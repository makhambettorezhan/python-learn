def fib(n):
    if n < 2:
        return 1;
    else:
        return fib(n-1) + fib(n-2);

def fib_dp(n):
    if n == 1:
        return 1

    dp = []
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


        
    
n = int(input('enter a number'))

for i in range(0, n):
    print(fib_dp(i))


def step(n):
    return steps(0, n)

def steps(i, n):
    if(i > n):
        return 0
    if(i == n):
        return 1
    else:
        return steps(i+1, n) + steps(i+2,n)

print(step(3))



