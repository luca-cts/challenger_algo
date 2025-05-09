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
        for (a, b), val in zip(equations, values):  # 양방향 그래프 만들기
            graph[a].append((b, val))  # a -> b
            graph[b].append((a, 1 / val))  # b -> a

        # Step 2: DFS to evaluate each query
        def dfs(curr, target, acc, visited):
            if curr == target:  # 목표값 도달 축적치 리턴
                return acc
            visited.add(curr)  # 노드(변수) 방문처리

            for neighbor, weight in graph[curr]:  # 위에서 만든 그래프 dict key의 list value
                if neighbor not in visited:  # 방문하지 않은 노드 - neighbor:변수(노드)
                    result = dfs(neighbor, target, acc * weight, visited)  # recursion
                    if result != -1:
                        return result
            return -1

        results = []
        for a, b in queries:  # 경우의 수 3가지
            if a not in graph or b not in graph:  # 노드(변수) 존재하지 않음
                results.append(-1.0)
            elif a == b:  # 같은 노드인경우
                results.append(1.0)
            else:  # 나머지 경우
                results.append(dfs(a, b, 1, set()))  # dfs recursion으로 탐색 마무리

        return results
