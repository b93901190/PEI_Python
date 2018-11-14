import collections

def isBalancedBinaryTree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def checkBalanced(tree):
        if not tree :
            return BalancedStatusWithHeight(True, -1)

        fromLeft = checkBalanced(tree.left)
        if not fromLeft.balanced:
            return BalancedStatusWithHeight(False, 0)

        fromRight = checkBalanced(tree.right)
        if not fromRight.balanced:
            return BalancedStatusWithHeight(False, 0)

        isBalanced = abs(fromLeft.height - fromRight) <= 1
        height = max(fromLeft.height, fromRight.height) + 1
        return BalancedStatusWithHeight(isBalanced, height)

    return checkBalanced(tree).balanced