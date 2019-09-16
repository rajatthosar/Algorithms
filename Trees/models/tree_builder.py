from enum import Enum, auto
from Trees.models.node import Node


class Mode(Enum):
    """
    An enumerator to choose from the available modes
    """
    BST = auto()
    RANDOM = auto()


class Builder:
    """
    This class constructs the trees according to the
    called clauses
    """
    root_node = None

    def __init__(self, mode, values):
        if mode == Mode.BST and values is not None:
            leaves = [Node(val=value) for value in values]
            root = leaves[0]
            self.root_node = root
            for leaf in leaves[1:]:
                self.build_bst(root, leaf)

    def build_bst(self, root, node):
        """
        This function builds a Binary Search Tree with the given nodes

        :param node: list of nodes
        :return:
        """

        if node.val < root.val:
            if root.has_left_child():
                self.build_bst(root.left_child, node)
            else:
                root.left_child = node
        else:
            if root.has_right_child():
                self.build_bst(root.right_child, node)
            else:
                root.right_child = node

    def get_tree(self):
        """
        Returns the Binary Search Tree generated by the passed method
        :return: tree, Type: Node
        """
        return self.root_node


# nodes = [10, 5, 7, 9, 12, 19, 8, 5, 21, 11]
# tree_builder_object = Builder(Mode.BST, values=nodes)
# root = tree_builder_object.get_tree()
# print(root)