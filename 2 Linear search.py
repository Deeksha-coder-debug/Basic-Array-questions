class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i in arr:
            if i==x:
                return arr.index(x)
        return -1
