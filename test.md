```python
sum=0


if root :
    sum+=root.val
    
if root.left==None and root.right==None:
    if tree_sum==target_sum:
        return True
    else:
        return
    
if root.left:
    sum+=root.left.val
    travelsal(root.left)
    sum-=root.left.val
)



```