class maze:
    grid = []
    def __init__(self, arry):
        self.grid = arry

    def solve(self,x,y):
        print (len(self.grid) )
        if x == len(self.grid) - 1 and y == len(self.grid) - 1:
            print("reached at end")
            return True
        if self.grid[x][y] == 1:
            print("blocked at %d %d" %(x,y))
            return False
        if self.grid[x][y] == 2:
            print("visited at %d %d " % (x,y))
            return False
        print("visiting %d %d " % (x,y))
        self.grid[x][y] == 2
        if ((x < len(self.grid) - 1 and self.solve(x + 1, y))
            or (y>0 and self.solve(x,y-1))
            or (x>0 and self.solve(x-1,y))
            or (y< len(self.grid) - 1 and self.solve(x,y+1))):
            return True
        return False

arry= input("enter maze")
M1 = maze(arry)
M1.solve(0,0)