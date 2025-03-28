# tag: bfs, binary_tree
class Solution:
    """
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
    LCA: 두 노드가 모두 하위 노드로 존재하는 가장 낮은 노드
    왼쪽 자식은 항상 작음: left.val < root.val
    오른쪽 자식은 항상 큼: right.val > root.val
    이걸 이용하면 p, q가 서로 다른 방향으로 갈라지는 지점이 바로 LCA가 됨!
    """

    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
