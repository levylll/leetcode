#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by levy@2021-05-20 20:30:17

class Solution(object):

    def process(self, res, grid, left, top):

        # print left, top, res, len(grid), len(grid[0])
        # print top, len(grid) - 1
        if left == len(grid[0]) - 1:
            for i in range(top, len(grid)):
                res += grid[i][left]
            return res

        if top == len(grid) - 1:
            # print '----'
            for i in range(left, len(grid[0])):
                res += grid[top][i]
            return res

        tmp = min(self.process(res, grid, left+1, top), self.process(res, grid, left, top+1))
        # print left, top, res , grid[left][top], tmp
        res = res + grid[top][left] + tmp
        return res


    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        return self.process(res, grid, 0, 0)

# grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[1,3,1],[1,5,1]]
# grid = [[5,1],[2,1]]
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
sol = Solution()
res = sol.minPathSum(grid)
print res
