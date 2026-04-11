class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        taken = {}
        passed_by = {}
        prereqs = defaultdict(list)

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        res = []
        print(prereqs)
        for i in range(numCourses):
            if i not in prereqs:
                # print(i)
                res.append(i)
                taken[i] = True
        
        def dfs(course):
            if taken.get(course) == True:
                return True
            if passed_by.get(course) == True:
                return False
            passed_by[course] = True
            
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            # print(course)
            taken[course] = True
            res.append(course)
            return True
            
        # print(prereqs)
        for course in list(prereqs.keys()):
            # print(course)
            if not dfs(course):
                return []
        
        return res


