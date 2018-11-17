import collections

def checkBST(tree, curMin=float('-inf'), curMax=float('inf')):
    if not tree:
        return True
    elif not curMin <= tree.data <= curMax:
        return False
    else:
        return checkBST(tree.left, curMin, tree.data) and checkBST(tree.right, tree.data, curMax)

def checkBSTQueue(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'curMin', 'curMax'))

    bfsQueue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])

    while bfsQueue:
        cur = bfsQueue.popleft()
        if cur:
            if not cur.curMin <= cur.node.data <= cur.curMax:
                return False
            bfsQueue += [QueueEntry(cur.node.left, cur.curMin, cur.node.data),
                         QueueEntry(cur.node.right, cur.node.data, cur.curMax)]
    return True
