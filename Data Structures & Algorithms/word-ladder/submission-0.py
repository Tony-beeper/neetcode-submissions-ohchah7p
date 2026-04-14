class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord])
        visited = {beginWord}
        length = 1
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neighbor = word[:i] + c + word[i+1:]
                        if neighbor in wordSet and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            length += 1
        
        return 0