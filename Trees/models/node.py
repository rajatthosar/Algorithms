class Node:
    """
    Definition of Node class
    Each node is a part of the binary tree with root, left and right children
    When children nodes are not specified, the node is treated as leaf node
    """

    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        self.visited = False
        self.returning_visit = False

    def has_children(self):
        """
        A boolean function to check if a node has children nodes

        :return: Boolean [True/False]
        """
        return self.has_left_child() or self.has_right_child()

    def has_left_child(self):
        """
        A boolean function to check if a node has left children nodes

        :return: Boolean [True/False]
        """

        return True if self.left_child is not None else False

    def has_right_child(self):
        """
        A boolean function to check if a node has right children nodes

        :return: Boolean [True/False]
        """

        return True if self.right_child is not None else False

    def is_visited(self):
        """
        A flag to check if the node has been completely explored

        :return: Boolean [True/False]
        """
        return self.visited

    def is_returning_visit(self):
        """
        This function checks if the node has returned after exploration
        :return: Boolean [True/False]
        """
        return self.returning_visit
