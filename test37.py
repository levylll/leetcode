#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2020-04-25 16:38:11

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        tmp_dict = {}
        for i in range(9):
            r_i = i / 3
            for j in range(9):
                t = board[i][j]
                if t == '.':
                    continue
                c_j = j / 3

                title = 'r%s%s' %(i, i)
                if title not in tmp_dict:
                    tmp_dict[title] = [t]
                elif t in tmp_dict[title]:
                    print 'AAAAAAAAAA'
                    print title
                    print t
                    print tmp_dict[title]
                    return False
                else:
                    tmp_dict[title].append(t)

                title = 'm%s%s' %(j, j)
                if title not in tmp_dict:
                    tmp_dict[title] = [t]
                elif t in tmp_dict[title]:
                    print 'BBBBBBBBB'
                    print title
                    print t
                    print tmp_dict[title]
                    return False
                else:
                    tmp_dict[title].append(t)

                title = 'c%s%s' %(r_i, c_j)
                if title not in tmp_dict:
                    tmp_dict[title] = [t]
                elif t in tmp_dict[title]:
                    print 'CCCCCCCC'
                    print title
                    print t
                    print tmp_dict[title]
                    return False
                else:
                    tmp_dict[title].append(t)
        return True

s = Solution()
# a = [["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]
a=[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
print s.isValidSudoku(a)
