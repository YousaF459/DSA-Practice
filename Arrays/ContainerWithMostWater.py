## Input will be integer array of name height and will have length n


## There will be n number of vertical lines drawn 

## widht will be based on array index - we want to store maximum water so pick index who are far
## vertical lines show height so it will be best to pick bigger values - 
## verticles bigger values we will pick shorted for height
## width will be index like highest index - smaller index 
## vertical will be min() from two picked values
## we have to multiply width with vertical picked value

height = [1,8,6,2,5,4,8,3,7]
## First Pointer Start from First Index
p1=0
## Second Pointer Start from array Last Index
p2=len(height)-1

## Checking Width
width=p2-p1

## Calculating water Storage
max=min(height[p1],height[p2]) * (p2-p1)


for item in range(len(height)):
    ## Checking Width cause it will change in every loop
    width=p2-p1

    ## checking if storage is same or change for new pointer values
    if min(height[p1],height[p2]) * (p2-p1) > max:
        ## if new pointer values give more storage then they are copied in max
        max= min(height[p1],height[p2]) * (p2-p1)

    ## if left pointer values is small move left pointer forward
    if height[p1] < height[p2]:
        p1+=1
    else:
        ## if right pointer values is small move right pointer backward
        p2-=1

    ## BigO(n) for time complexity
    ## BigO(1) for space Complexity

print(max)


