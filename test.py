#(不偷，偷)
def postorder(tree):
    if tree==None:
        return (0,0)
    left=postorder(tree.left)
    right=postorder(tree.right)
    #偷：
    dp1=left[0]+tree.val+right[0]
    #不偷：
    dp0=max(left[1],right[1])
    dp0=max(left[0], left[1]) + max(right[0], right[1])

    return (dp0,dp1)



