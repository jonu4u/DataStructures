# 269. Alien Dictionary
# Hard
#
#
# Example 1:
#
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
#
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
#
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
