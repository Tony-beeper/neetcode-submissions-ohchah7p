class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0 
        write = 0
        prev = chars[0]
        counter =0 
        while read < len(chars):
            ch = chars[read]


            # reach the end
            if read == len(chars) - 1:
                # prev diff from ch
                if prev != ch:
                    chars[write] = prev
                    write += 1
                    if counter > 1:
                        for num in str(counter):
                            chars[write] = num
                            write += 1
                    chars[write] = ch
                    write += 1
                else:
                    counter += 1
                    chars[write] = ch
                    write += 1
                    if counter > 1:
                        for num in str(counter):
                            chars[write] = num
                            write += 1
                # prev same as ch
            # prev diff from ch
            elif prev != ch:
                chars[write] = prev
                write += 1
                if counter > 1:
                    for num in str(counter):
                        chars[write] = num
                        write += 1
                prev = ch
                counter = 1
            else:
                counter += 1
            read += 1
            # else just same as ch
        return write





