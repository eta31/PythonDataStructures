"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):

    def preorder(self, root):
        result = []
        """
        :type root: Node
        :rtype: List[int]
        """
        self.pre_travel(root, result)

        return result

    def pre_travel(self, node, result):
        if node != None:
            result.append(node.val)
            for x in node.children:
                self.pre_travel(x, result)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        self.post_travel(root, result)
        return result

    def post_travel(self, node, result):
        if(node != None):
            for x in node.children:
                self.post_travel(x, result)
            result.append(node.val)
