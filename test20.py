class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tools = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        cap = []
        for x in s:
            if x in tools:
                if not cap:
                    return False
                tmp = cap.pop(-1)
                if tools[x] == tmp:
                    continue
                else:
                    return False
            else:
                cap.append(x)
        if cap:
            return False
        else:
            return True
