from TreeNode import  TreeNode

def preOrder(root, result):
    if root is None:
        return
    result.append(root.val)
    preOrder(root.left, result)
    preOrder(root.right, result)

def inOrder(root, result):
    if root is None:
        return

    inOrder(root.left, result)
    result.append(root.val)
    inOrder(root.right, result)

def postOrder(root, result):
    if root is None:
        return

    postOrder(root.left, result)
    postOrder(root.right, result)
    result.append(root.val)


root = TreeNode(9)
root.left = TreeNode(7)
root.right = TreeNode(11)
root.left.left = TreeNode(3)

result = []
preOrder(root, result)

print 'preorder : ', [x for x in result]

result = []
inOrder(root, result)
print 'inorder : ', [x for x in result]

result = []
postOrder(root, result)
print 'postorder : ', [x for x in result]
