from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            
        vis = [False] * numCourses
        path = [False] * numCourses
        def dfs_cycle(course: int) -> bool:
            nonlocal adj_list
            nonlocal vis
            nonlocal path
            vis[course] = True
            path[course] = True
            for related_course in adj_list[course]:
                if not vis[related_course]:
                    if (dfs_cycle(related_course)):
                        return True
                elif path[related_course]:
                    return True
            path[course] = False
            return False
        for course in range(numCourses):
            if not vis[course]:
                if (dfs_cycle(course)):
                    return False
        return True
