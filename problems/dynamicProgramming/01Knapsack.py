# The weight arra and vaue arr has same size.We need to maximise profit but
# we have weight W as constraint.
class Knapsack01:
    def __init__(self):
        # create a 2D grid of weight+1 and size+1
        self.memo=[[0 for i in range(100)]for i in range(100)]
    def recursive(self,wt_arr,val_arr,target_weight,size):
        # Base Condition
        if size==0 or target_weight==0:
            return 0
        # Choice Diagram
        if wt_arr[size-1]<=target_weight:
            # We can take this element for value calculation.Whether we take it or not
            # we need to reduce the size of the array
            return max(val_arr[size-1]+self.recursive(wt_arr,val_arr,target_weight-wt_arr[size-1],size-1),
                       self.recursive(wt_arr,val_arr,target_weight,size-1))
        return self.recursive(wt_arr,val_arr,target_weight,size-1)

    def recursive_memo(self,wt_arr,val_arr,target_weight,size):
        # Base Condition
        if size==0 or target_weight==0:
            return 0
        # If the value is already there we return it
        if self.memo[target_weight][size]!=0:
            return self.memo[target_weight][size]
        # Choice Diagram
        if wt_arr[size-1]<=target_weight:
            # We can take this element for value calculation.Whether we take it or not
            # we need to reduce the size of the array
            self.memo[target_weight][size]= max(val_arr[size-1]+self.recursive_memo(wt_arr,val_arr,target_weight-wt_arr[size-1],size-1),
                       self.recursive_memo(wt_arr,val_arr,target_weight,size-1))
            return self.memo[target_weight][size]
        self.memo[target_weight][size]=self.recursive_memo(wt_arr,val_arr,target_weight,size-1)
        return self.memo[target_weight][size]

    # This is the correct one
    def tabulation_bottom_up(self,wt_arr,val_arr,target_weight,size):
        memo=[[0 for i in range(target_weight+1)]for i in range(size+1)]
        for row in range(1,size+1):
            for col in range(1,target_weight+1):
                if wt_arr[row-1]<=col:
                    memo[row][col]= max(val_arr[row-1]+memo[row-1][col-wt_arr[row-1]],
                                        memo[row-1][col])
                else:
                    memo[row][col]= memo[row-1][col]
        return memo[size][target_weight]

    # Print weights as well as profit
    def tabulation_bottom_up_variation_print_weights(self,wt_arr,val_arr,target_weight,size):
        memo=[[(0,[]) for i in range(size+1)]for i in range(target_weight+1)]
        for row in range(1,target_weight+1):
            for col in range(1,size+1):
                if wt_arr[col-1]<=target_weight:
                    if (val_arr[col-1]+(memo[target_weight-wt_arr[col-1]][col-1])[0])> (memo[target_weight][col-1])[0]:
                        list=(memo[target_weight-wt_arr[col-1]][col-1])[1][:]
                        list.append(wt_arr[col-1])
                        max_val_grid= (val_arr[col-1]+(memo[target_weight-wt_arr[col-1]][col-1])[0],list)
                    else:
                        max_val_grid= memo[target_weight][col-1]
                    memo[row][col]= max_val_grid
                else:
                    memo[row][col]= memo[target_weight][col-1]
        return memo[target_weight][size]

s=Knapsack01()
print(s.tabulation_bottom_up([10, 20, 30],[60, 100, 120],50,3))
print(s.tabulation_bottom_up_variation_print_weights([10, 20, 30],[60, 100, 120],50,3))