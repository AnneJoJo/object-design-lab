"""
5 * 5 25 patches
water 7
sand 6
grass 1
forest 5
swamp 3 
cave 2 
castle 1

# initalize the borad with class patch 
"""

class patch:
    def __init__(self,name,n):
        self.name = name
        self.crown = n
        self.visited = False

class Solution:

    def count_point(self,board):
        total_points = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c].crown > 0 and not board[r][c].visited:
                    self.tmp_num_crowns = 0
                    patch_area = self.area(r,c,board,board[r][c].name)
                    total_points += self.tmp_num_crowns * patch_area
        return total_points

    def area(self,x,y,board,pattern):
        """
        
        :param board: 
        :return: how many patches with same type connected 
        """
        if x < 0 or y < 0 or x >len(board)-1 or y > len(board[0])-1 or board[x][y].name != pattern or board[x][y].visited or board[x][y].name == "castle":
            return 0

        board[x][y].visited = True
        self.tmp_num_crowns += board[x][y].crown
        return 1+self.area(x-1,y,board,pattern) + self.area(x+1,y,board,pattern) + self.area(x,y-1,board,pattern) + self.area(x,y+1,board,pattern)

board = [
    [patch("sand",0),patch("water",1),patch("water",1),patch("water",0),patch("grass",2)],
    [patch("water",0),patch("water",0),patch("forest",0),patch("forest",0),patch("forest",0)],
    [patch("water",0),patch("water",1),patch("forest",0),patch("swamp",2),patch("swamp",1)],
    [patch("sand",0),patch("castle",0),patch("sand",1),patch("sand",0),patch("sand",0)],
    [patch("swamp",0),patch("cave",2),patch("cave",0),patch("sand",1),patch("forest",0)]
]

s = Solution()
print(s.count_point(board))
