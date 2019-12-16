q1.
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree (branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]
def branches (tree):
    return tree[1:]

def is_tree (tree):
    if type(tree) != list or len (tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree (branch):
            return False
    return True
def is_leaf (tree):
    return not branches(tree)


def search_leaves(tree,e):
    print(tree)
    if root(tree)==e:
        return 1
    if is_leaf(tree):
        return 0
    else:
        return sum([search_leaves(b,e) for b in branches(tree)])
        
        
def has_itm(t, e):
    result=search_leaves(t,e)
    if (result==1):
        return True
    else:
        return False
    
print(has_itm (tree(11, [tree(12), tree(13, [tree(14),tree(15)])] ), 14))
print(has_itm (tree(11, [tree(12), tree(13, [tree(14),tree(15)])] ), 16))

q2
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree (branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]
def branches (tree):
    return tree[1:]

def is_tree (tree):
    if type(tree) != list or len (tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree (branch):
            return False
    return True

def tem(lst):
    if type(lst) != list:
        
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])




def ave_itm(t):
    tree=tem(t)
    return sum(tree)/len(tree)


print(ave_itm(tree(11, [tree(12), tree(13, [tree(14),tree(15)])])))

q4

def triple(n):
    return 3*n
def square(m):
    return m*m
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree (branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]
def branches (tree):
    return tree[1:]

def is_tree (tree):
    if type(tree) != list or len (tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree (branch):
            return False
    return True
def is_leaf (tree):
    return not branches(tree)

def tem(lst):
    if type(lst) != list:
        
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])

def search_leaves(tree):
    
    if(len(tree)==1):
        return tree[0]
    if is_leaf(tree):
        return 0
    else:
        return [search_leaves(b) for b in branches(tree)]
def app_func_leaves(t, g):
    result=search_leaves(t)
    result=tem(result)
    t=[]
    for i in result:
        t.append(g(i))
    return t


print(app_func_leaves(tree(1, [tree(2), tree(3, [tree(4),tree(5)])] ), triple))

print(app_func_leaves(tree(1, [tree(2), tree(3, [tree(4),tree(5)])] ), square))

q6

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree (branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]
def branches (tree):
    return tree[1:]

def is_tree (tree):
    if type(tree) != list or len (tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree (branch):
            return False
    return True

def tem(lst):
    if type(lst) != list:
        
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])




def largest(t):
    tree=tem(t)
    print(tree)
    max=tree[0]
    for i in tree:
        if max<i:
            max=i
    return max


print(largest(tree(11, [tree(12), tree(13, [tree(14),tree(15)])])))

