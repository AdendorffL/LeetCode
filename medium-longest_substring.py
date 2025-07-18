# Longest Substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max = 0
        
        chars = list(str(s))
        iteration_list = []

        while len(chars) != 0:
            for i in chars:
                # When dupe is found
                if i in iteration_list:
                    if count > max:
                        max = count
                        
                    iteration_list.clear()
                    count = 1
                    iteration_list.append(i)

                # When no dupe is found
                else:  
                    iteration_list.append(i) 
                    count += 1
                    if count > max:
                        max = count
           
            if len(chars) != 0:
                chars.pop(0)
                iteration_list.clear()
                count = 0

        return(max)


print(Solution().lengthOfLongestSubstring("asjrgapa"))
