# Longest Substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max = 0
        
        chars = list(str(s))
        iteration_list = []

        while len(chars) != 0:
            for i in chars:
                print(iteration_list)
                print(f"count: {count}")
                # When dupe is found
                if i in iteration_list:
                    if count > max:
                        count = max
                        
                    iteration_list.clear()
                    count = 1
                    iteration_list.append(i)

                # When no dupe is found
                else:
                    print("Check")
                    iteration_list.append(i)
                    count += 1
                    if count > max:
                        max = count

            if len(chars) != 0:
                chars.pop(0)
                print(f"chars: {chars}")


        return(max)


print(Solution().lengthOfLongestSubstring("asjrgapa"))
print("Fin")
        