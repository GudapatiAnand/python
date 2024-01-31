def max_sum_subsequence_non_adjacent(arr):

    dp=[0]*len(arr)

    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])

    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])
    return dp[len(arr)-1]
arr=[3,2,5,4,7,6,9,8,11,10]
print(max_sum_subsequence_non_adjacent(arr))