class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        taken = {}
        passed_by  = {}
        prereqs = defaultdict(list)

        for course , prereq in prerequisites:
            prereqs[course].append(prereq)
            taken[course] = False
            passed_by[course] = False

        def dfs(course):
            if taken.get(course) == True:
                return True
            if passed_by.get(course) == True:
                return False
            passed_by[course] = True
            # if prereqs.get(course) == :
            for preq in prereqs[course]:
                # print("hi")
                if taken.get(preq) != True:
                    succeed = dfs(preq)
                    if not succeed:
                        return False
            # print("hi")
            taken[course] = True
            return True

        # print(prereqs)
        for course in list(prereqs.keys()):
            if not dfs(course):
                return False
        # print(taken)
        num = 0
        return True
        