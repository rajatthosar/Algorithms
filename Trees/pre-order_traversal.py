from models.tree_builder import Builder, Mode


class Traversal:
    """
    This class hosts methods to traverse the trees
    """
    pre_order_traversal = []
    in_order_traversal = []
    post_order_traversal = []
    stack = []

    def clear_stack(self):
        """
        Clears the stack after performing operations

        :return: nothing. resets the values in class member
        """
        self.stack.clear()

    def traverse_pre_order(self, root):
        """
        This function traverses the tree with pre-order traversal technique
        :param root: The root node of the tree
        :return: list of pre-order traversed node values
        """

        if not root.is_visited():
            if not root.is_returning_visit():
                self.pre_order_traversal.append(root.val)

            if root.has_left_child() and not root.left_child.is_visited():
                self.stack.append(root)
                self.traverse_pre_order(root.left_child)
            elif root.has_right_child() and not root.right_child.is_visited():
                self.stack.append(root)
                self.traverse_pre_order(root.right_child)
            else:
                root.visited = True
                if self.stack:
                    root = self.stack.pop()
                    root.returning_visit = True
                    self.traverse_pre_order(root)

        return self.pre_order_traversal


if __name__ == '__main__':
    nodes = [10, 5, 7, 9, 12, 19, 8, 5, 21, 11]
    traversal_object = Traversal()
    builder = Builder(Mode.BST, values=nodes)
    tree = builder.get_tree()
    preorder = traversal_object.traverse_pre_order(root=tree)
    print(preorder)
