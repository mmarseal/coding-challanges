class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0 
        
    def computeDifference(self):
        maximum = max(self.__elements)
        minimum = min(self.__elements)
        self.maximumDifference = maximum - minimum

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

"""
Sample Input:
STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]

Sample Output:
4
"""