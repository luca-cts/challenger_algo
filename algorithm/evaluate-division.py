from collections import defaultdict


# tag: dfs, graph
class Solution:
    """
    https://leetcode.com/problems/evaluate-division
    - 연산관계 그래프로 모델링
    - 경로에 따라 비율 누적 계산 - 비선형 탐색
    - 가중치가 있는 방향 그래프! - dfs recursion
    - 노드는 변수 str, 간선(edge)는 나눗셈 방정식 - 기울기(weight)
    """

    def calcEquation(self, equations, values, queries):
        # Step 1: Build graph
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # Step 2: DFS to evaluate each query
        def dfs(curr, target, acc, visited):
            if curr == target:
                return acc
            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, acc * weight, visited)
                    if result != -1:
                        return result
            return -1

        results = []
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            elif a == b:
                results.append(1.0)
            else:
                results.append(dfs(a, b, 1, set()))

        return results
