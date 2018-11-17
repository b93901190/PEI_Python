def searchBST(tree, key):
    return (tree
            if not tree or tree.data == key else searchBST(tree.left, key)
            if key < tree.data else searchBST(tree.right, key))