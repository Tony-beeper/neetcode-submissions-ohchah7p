class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)

        # print(wordSet)
        q = deque([beginWord])
        visited = {beginWord}
        length = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return length

                for j in range(len(cur)):
                    for c in "qwertyuiopasdfghjklzxcvbnm":
                        new = cur[:j] + c + cur[j+1:]
                        if new in wordSet and new not in visited:
                            q.append(new)
                            visited.add(new)

            length += 1
        return 0
