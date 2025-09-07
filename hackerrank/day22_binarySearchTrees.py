class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root==None:
            return -1
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return 1 + max(left_height, right_height)
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       

"""
Sample Input:
7
3
5
2
1
4
6
7

Sample Output:
3
"""