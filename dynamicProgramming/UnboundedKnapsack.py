# The weight arra and vaue arr has same size.We need to maximise profit but
# we have weight W as constraint.Here we can pick same weight/value multiple times.But
# if we don't pick that value then that will never be picked
class KnapsackUnbounded:

    def tabulation_bottom_up(self,wt_arr,val_arr,target_weight,size):
        memo=[[0 for i in range(target_weight+1)]for i in range(size+1)]
        for row in range(1,size+1):
            for col in range(1,target_weight+1):
                if wt_arr[row-1]<=col:
                    # Here we can choose the ith row again even if we choose once
                    memo[row][col]= max(val_arr[row-1]+memo[row][col-wt_arr[row-1]],
                                        memo[row-1][col])
                else:
                    memo[row][col]= memo[row-1][col]
        return memo[size][target_weight]

    # Rod cutting Problem
    # Given a rod of length n inches and an array of prices
    # that contains prices of all pieces of size smaller than n.
    # Determine the locations where the cuts are to be made for maximum profit.
    def rod_cutting(self,N,prices):
        length_array=[]
        for i in range(1,N+1):
            length_array.append(i)
        def rod_cutting_top_down(length_arr,price_arr,N,size):
            memo=[[0 for i in range(N+1)]for i in range(size+1)]
            for row in range(1,size+1):
                for col in range(1,N+1):
                    if length_arr[row-1]<=col:
                        memo[row][col]=max(price_arr[row-1]+memo[row][col-length_arr[row-1]],
                                           memo[row-1][col])
                    else:
                        memo[row][col]= memo[row-1][col]
            return memo[size][N]

        return rod_cutting_top_down(length_array,prices,N,N)

    # Coin Change Problem
    # Coin Change Problem Maximum Number of ways
    # Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
    # Example:
    # for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.

    # This can be solved by unbounded knapsack, where arr=wt arr,W=N and size=len(arr)
    def max_ways_coin_change(self,N,coin_arr):
        def coin_change_top_down(coins, N, size):
            memo=[[0 for i in range(N+1)]for i in range(size+1)]
            for row in range(1,size+1):
                for col in range(0,N+1):
                    # When col is 0 we can create a coin change in 1 way whic is empty set
                    if col==0:
                        memo[row][col]=1
                    elif coins[row - 1]<=col:
                        memo[row][col]= memo[row][col - coins[row - 1]] + memo[row - 1][col]
                    else:
                        memo[row][col]= memo[row-1][col]
            return memo[size][N]

        return coin_change_top_down(coin_arr,N,len(coin_arr))

    # Coin Change Problem Minimum Numbers of coins
    # Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
    # Example:

    # Input: coins[] = {25, 10, 5}, V = 30
    # Output: Minimum 2 coins required
    # We can use one coin of 25 cents and one of 5 cents



s=KnapsackUnbounded()
print(s.tabulation_bottom_up([10, 20, 30],[60, 100, 120],50,3))
print(s.rod_cutting(8,[1 ,  5  , 8 ,  9 , 10 , 17 , 17,  20]))
print(s.max_ways_coin_change(4,[1,2,3]))