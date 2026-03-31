class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = {}
        for s in s1:
            target[s] = target.get(s,0) + 1
        cur = {}
        for s in s2[:len(s1)]:
            cur[s] = cur.get(s,0) + 1
        # print(cur)
        # print(target)
        # cur = s2[:len(target)+1]

        # print(cur)
        if target == cur:
            return True
        for i in range(len(s1), len(s2)):
            print(cur)
            print(target)
            # print(i-len(cur))
            # print(i)
            # print(len(cur))
            # print(len(cur))
            start_char = s2[i-len(s1)]

            cur[start_char] -= 1
            if cur[start_char]==0:
                cur.pop(start_char)
            # print(len(cur))
            cur[s2[i]] = cur.get(s2[i], 0) + 1
            # print(len(cur))
            # print("hi")
            
            if target == cur:
                # print("hi")
                # print(target)
                # print(cur)
                return True
        return False



                
