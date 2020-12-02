# 270. Closest Binary Search Tree Value
#
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
# 4
# / \
#     2   5
# / \
#     1   3
#
# Output: 4
def closestValue(self, root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    list1=self.in_order(root,[])
    size=len(list1)
    if size==1:
        return list1[0]
    start=0
    end=size-1

    min_value=float("inf")
    closest=float("inf")
    while start<end:
        mid=(start+end)//2
        mid_num=abs(target-list1[mid])
        if mid+1<size:
            mid_num_more=abs(target-list1[mid+1])
            if mid_num_more>mid_num:
                end=mid
            else:
                start=mid
            if mid_num<closest:
                min_value=list1[mid]
                closest=mid_num
        if(end-start)==1:
            if abs(target-list1[end])<closest:
                min_value=list1[end]
                closest=abs(target-list1[end])
            if abs(target-list1[start])<closest:
                min_value=list1[start]
                closest=abs(target-list1[start])
            return min_value
    return min_value





def in_order(self,root,list1):
    if not root:return list1
    self.in_order(root.left,list1)
    list1.append(root.val)
    self.in_order(root.right,list1)
    return list1

# 71. Simplify Path

# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
#
# In a UNIX-style file system, a period '.' refers to the current directory. Furthermore, a double period '..' moves the directory up a level.
#
# Note that the returned canonical path must always begin with a slash '/', and there must be only a single slash '/' between two directory names. The last directory name (if it exists) must not end with a trailing '/'. Also, the canonical path must be the shortest string representing the absolute path.
#
#
#
# Example 1:
#
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:
#
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:
#
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
# Example 4:
#
# Input: path = "/a/./b/../../c/"
# Output: "/c"
#
#
# Constraints:
#
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid Unix path.
def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    actual_path=""
    list1=path.split("/")
    for index,elem in enumerate(list1):
        if elem=="":
            continue
        if elem==".":
            continue
        # When we reach .. we go to previous dir by deleting everything
        # from path till previous /
        if elem==".." and actual_path!="":
            i=len(actual_path)
            # We backtrack to get index of last /
            while actual_path[i-1]!="/":
                i-=1
            # Say we have /a/b.After this we have /a
            actual_path=actual_path[:i-1]
        # If we're t root do nothing'
        elif elem==".." and actual_path=="":
            continue
        # if it is adir we make path
        else:
            actual_path+="/"+elem
    # If we're at root we return "/' else return the actual string
    return "/" if actual_path=="" else actual_path