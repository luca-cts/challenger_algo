class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tag: bfs, binary-search-tree
class Codec:
    """
    https://leetcode.com/problems/serialize-and-deserialize-bst
    직렬화:
    전위 순회(preorder) 로 노드를 순서대로 저장 → [root, left, right]
    문자열로 저장: "5,3,2,4,7" 같은 형태

    역직렬화:
    전위 순회 결과를 이용하여, BST 조건 (min < val < max) 을 활용해서 재구성
    """

    def serialize(self, root):
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        values = list(map(int, data.split(",")))
        self.index = 0  # 전역 인덱스 (preorder 순서)

        def build(min_val, max_val):
            if self.index >= len(values):
                return None
            val = values[self.index]
            if val < min_val or val > max_val:
                return None

            self.index += 1
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node

        return build(float("-inf"), float("inf"))
