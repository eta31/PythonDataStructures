"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if(root == None):
            return []

        result = []
        stack = []
        stack.append(root)

        while len(stack) != 0:
            current = stack.pop()
            result.append(current.val)
            for x in range(len(current.children) - 1, -1, -1):
                stack.append(current.children[x])

        return result

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        result = []
        queue = []
        queue.append(root)
        tempsize = 0

        while(len(queue) != 0):
            tempsize = len(queue)
            child_result = []
            for x in range(tempsize):
                current = queue.pop(0)
                child_result.append(current.val)
                for child in current.children:
                    queue.append(child)

            result.append(child_result)

        return result

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if(root == None):
            return []
        result = []
        stack = []
        stack.append(root)

        while (len(stack) != 0):
            current = stack.pop()

            for x in current.children:
                stack.append(x)
            result.append(current.val)

        result.reverse()
        return result
