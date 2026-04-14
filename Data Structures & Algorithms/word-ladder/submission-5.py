class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)

        length = 1

        q = deque([(beginWord,1)])
        visited = set()
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "qwertyuiopasdfghjklzxcvbnm":
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet and new_word not in visited:
                        q.append((new_word, length+1))
                        visited.add(new_word)
        return 0

