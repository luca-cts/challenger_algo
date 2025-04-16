class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: dfs, binary_tree, recursive
class Solution:
    """
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    - 트리 재귀적 탐색 필요
        - root 기준 왼쪽에서 p,q treenode 있는지
        - root 기준 오른쪽에서 p,q treenoe 있는지
        - 결과 조건
            - p,q가 서로 다른 서브트리에 있으면 현재 노드가 공통조상
            - 현재 노드가 p or q이고, 하위 트리에 p or q가 있는경우 현재 노드 p or q가 공통조상
    """

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            print(f"Visit None → return None")
            return None
        print(f"Visit Node({root.val})")

        if root == p:
            print(f"Node({root.val}) == p({p.val}) → return {root.val}")
            return root
        if root == q:
            print(f"Node({root.val}) == q({q.val}) → return {root.val}")
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            print(f"Node({root.val}) is LCA of {p.val} and {q.val}")
            return root

        result = left if left else right
        if result:
            print(f"Return Node({result.val}) up from Node({root.val})")
        else:
            print(f"Return None up from Node({root.val})")
        return result


# 트리 구성
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# p, q 노드 선택
p = root.left  # Node(5)
q = root.right  # Node(1)

# 실행
sol = Solution()
lca = sol.lowestCommonAncestor(root, p, q)
print("\nLCA Result:", lca.val)
