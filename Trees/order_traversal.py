from models.tree_builder import Builder, GenMode, TraverseMode


class Traversal:
    """
    This class hosts methods to traverse the trees
    """

    cleaned_list = []

    def clear_cleaned_list(self):
        """
        Cleans the cleaned_list for future processing
        :return: nothing
        """
        self.cleaned_list.clear()

    def traverse(self, root, mode):
        """
        This function traverses the tree with pre-order traversal technique
        :param root: The root node of the tree
        :return: list of pre-order traversed node values
        """

        # Ensuring that the list cleaner code does not append to previous result
        if self.cleaned_list:
            self.clear_cleaned_list()

        if not root.has_children():
            return root.val

        left = (self.traverse(root.left_child, mode)) if root.has_left_child() else []
        right = (self.traverse(root.right_child, mode)) if root.has_right_child() else []

        order = []

        if mode == TraverseMode.PRE_ORDER:
            mode_order = [root.val, left, right]
        elif mode == TraverseMode.IN_ORDER:
            mode_order = [left, root.val, right]
        else:
            mode_order = [left, right, root.val]

        for data in mode_order:
            if isinstance(data, int) or not len(data) < 1:
                order.append(data)

        return order

    def clean_list(self, unclean_list):
        """
        Recursively flattens the list
        :param unclean_list: list of lists
        :return: flattened list
        """

        for data in unclean_list:
            if isinstance(data, int):
                self.cleaned_list.append(data)
            else:
                self.clean_list(data)

        return self.cleaned_list


if __name__ == '__main__':
    nodes = [10, 5, 7, 9, 12, 19, 8, 5, 21, 11]
    traversal_object = Traversal()
    builder = Builder(GenMode.BST, values=nodes)
    tree = builder.get_tree()
    preorder = traversal_object.traverse(root=tree, mode=TraverseMode.PRE_ORDER)
    print(traversal_object.clean_list(preorder))

    inorder = traversal_object.traverse(root=tree, mode=TraverseMode.IN_ORDER)
    print(traversal_object.clean_list(inorder))

    postorder = traversal_object.traverse(root=tree, mode=TraverseMode.POST_ORDER)
    print(traversal_object.clean_list(postorder))
