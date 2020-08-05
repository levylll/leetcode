#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-08-04 18:10:43

class Solution(object):
    def diff(self, a, b):
        res = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                res += 1
        return res

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        level = [beginWord]
        stop = set()
        res = 1
        while level:
            tmp_level = []
            for elem in level:
                i = 0
                while i < len(wordList):
                    q = wordList[i]
                    if self.diff(elem, q) == 0:
                        i += 1
                        continue
                    elif self.diff(elem, q) == 1:
                        if self.diff(endWord, q) == 0:
                            return res + 1
                        tmp_level.append(q)
                        wordList.remove(q)
                        continue
                        # stop.add(q)
                    i += 1

            res += 1
            level = tmp_level
        return 0

so = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dot","dog","lot","log"]
res = so.ladderLength(beginWord, endWord, wordList)
print res

beginWord = "a"
endWord = "c"
wordList = ['a', 'b', 'c']
# wordList = ["hot","dot","dog","lot","log"]
res = so.ladderLength(beginWord, endWord, wordList)
print res
