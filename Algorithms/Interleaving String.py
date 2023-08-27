def is_interleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]       # Create a DP table to store the results of subproblems
     
    if m + n != len(s3):
        return False
    
    dp[0][0] = True   # Base case: empty strings can form an empty string
    
    # Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]
    
    return dp[m][n]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(is_interleave(s1, s2, s3))  
