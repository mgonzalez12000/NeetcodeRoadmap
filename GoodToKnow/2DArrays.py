# To iterate through all the element of a 2d array you can do the following:
# Where sample[i] is the inner array.
# NOTE: how sameple[i][j] is similar to sample[i].
# NOTE: sameple[i][j] simply grabs the elements inside the current inner array
sample = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
for i in range(len(sample)):
    for j in range(len(sample[i])):
        print(sample[i][j])
