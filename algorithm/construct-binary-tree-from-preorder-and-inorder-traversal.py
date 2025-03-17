from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: binary_tree, hash_table, tree_traversal
class Solution:
    """
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
    - 전위 순회에서 첫 번째 값을 루트 노드로 선택
    - 중위 순회에서 루트 노드의 위치를 찾아 왼쪽/오른쪽 서브트리 분할
    - 재귀적으로 왼쪽과 오른쪽 서브트리를 구성
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:  ## 재귀 과정에서 서브트리 없을 때 선택
            return None

        root_val = preorder[0]  # 전위 순회의 첫 번째 값이 루트
        root = TreeNode(root_val)

        mid_idx = inorder.index(
            root_val
        )  # 중위 순회에서 루트의 위치 찾기 # unique value라 가능

        # 재귀적으로 왼쪽과 오른쪽 서브트리 구성
        root.left = self.buildTree(
            preorder[1 : mid_idx + 1], inorder[:mid_idx]
        )  ## len(preorder) == len(inorder)
        root.right = self.buildTree(preorder[mid_idx + 1 :], inorder[mid_idx + 1 :])

        return root


def print_tree(root):
    if not root:
        return "None"
    return f"{root.val}, ({print_tree(root.left)}), ({print_tree(root.right)})"


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

tree = Solution().buildTree(preorder, inorder)
print(print_tree(tree))
