# O(n)复杂度
def Fibonacci(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
          dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

if __name__ == '__main__':
    res=Fibonacci(5)
    print(res)