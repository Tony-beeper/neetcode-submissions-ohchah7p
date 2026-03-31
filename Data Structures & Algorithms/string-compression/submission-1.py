class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0 
        write = 0

        prev = chars[0]
        counts = 0
        while read < len(chars):
            cur = chars[read]
            if cur == prev:
                counts += 1
            else:
                chars[write] = prev
                write += 1
                if counts > 1:
                    for digit in str(counts):
                        chars[write] = digit
                        write += 1
                counts = 1
                prev = cur
            read += 1
        chars[write] = prev
        write += 1
        if counts > 1:
            for digit in str(counts):
                chars[write] = digit
                write += 1

        return write





