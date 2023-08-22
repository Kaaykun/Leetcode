class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """Sliding window technique"""
        n = len(s)
        # "start" and "end" indices maintain the window
        start = 0
        end = 0
        # Tracker for unique characters in the current window
        unique_chars = set()
        # Tracker for longest substring
        max_len = 0
        # Tracker for starting position of the longest substring without duplicates
        max_start = 0

        while end < n:
            if s[end] not in unique_chars:
                # Add new character at the end of the set
                unique_chars.add(s[end])
                curr_len = end - start +1
                if curr_len > max_len:
                    # Update maximum length and starting index of longest substring
                    max_len = curr_len
                    max_start = start
                # Expand window to the next character towards the end
                end += 1
            else:
                # Remove first occurance of duplicate charcater
                unique_chars.remove(s[start])
                # Contract window to the next character from the start
                start += 1
        # Return length of longest substring by slicing the original string
        return(len(s[max_start:(max_start+max_len)]))

def main():
    s = "abcdabc"

    solution = Solution() 
    print(solution.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()