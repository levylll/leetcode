#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-07-31 15:37:01

class Solution(object):

    def process(self, board, word, start_i, start_j, stop):
        if not word:
            return True

        if start_i < 0 or start_i >= len(board):
            return False
        if start_j < 0 or start_j >= len(board[0]):
            return False
        # print start_i, start_j, len(board), len(board[0])

        tmp_record = '%s_%s' %(start_i, start_j)
        if tmp_record in stop:
            return False

        if board[start_i][start_j] == word[0]:
            stop.append(tmp_record)
            tmp1 = self.process(board, word[1:], start_i-1, start_j, stop)
            tmp2 = self.process(board, word[1:], start_i+1, start_j, stop)
            tmp3 = self.process(board, word[1:], start_i, start_j+1, stop)
            tmp4 = self.process(board, word[1:], start_i, start_j-1, stop)
            if any([tmp1, tmp2, tmp3, tmp4]):
                return True
            else:
                stop.remove(tmp_record)
                return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        stop = []
        for start_i in range(len(board)):
            for start_j in range(len(board[0])):
                res = self.process(board, word, start_i, start_j, stop)
                if res:
                    return True
        return False

so = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
# word = "ABCCED"
# word = "SEE"
word = "ABCB"
res = so.exist(board, word)
print res
