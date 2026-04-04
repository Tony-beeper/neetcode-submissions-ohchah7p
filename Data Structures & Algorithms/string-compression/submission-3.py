class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        read = 0 
        write = 0

        counter = 0
        prev = chars[0]

        for read, ch in enumerate(chars):
            # if prev != ch:
            if read == len(chars) - 1:
                

                # last one, same as prev
                if prev == ch:
                    counter += 1
                    chars[write] = prev
                    write += 1
                    if counter > 1:
                        for num in str(counter):
                            chars[write] = num
                            write += 1
                else:
                    # print("hi")
                    chars[write] = prev
                    write += 1
                    if counter > 1:
                        for num in str(counter):
                            chars[write] = num
                            write += 1
                    chars[write] = ch
                    write += 1


                # last one, diff from prev

            elif prev != ch:

                # prev last just different but not the last
                chars[write] = prev
                write += 1
                if counter > 1:
                    for num in str(counter):
                        chars[write] = num
                        write += 1
                prev = ch
                counter = 1
            else:
                # same
                counter += 1
        return write
            

