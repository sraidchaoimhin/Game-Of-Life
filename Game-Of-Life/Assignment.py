import random


''' Define our classes'''

class  Grid(object):
    def __init__(self, gridwidth, gridheight):
    
        self.gridwidth = gridwidth
        self.gridheight = gridheight
        
        
        i = 0
        j = 0
        
        row = []
        column = []
        
        while i < gridheight:
            while j < gridwidth:
                row.append(Cell(i, j))
                j += 1
                
            column.append(row)
            row =[]

            j = 0
            i += 1 
        self.fullgrid = column
        
    def __str__(self):
        gridString = ""
        for row in self.fullgrid:
            for cell in row:
                if cell.isliving == True:
                    gridString += "*"

                else:
                    gridString += "-"
                if cell.yposition == self.gridwidth -1:
                    gridString += "\n"
                    
        return gridString
    
class Cell(object):
    def __init__(self, xposition, yposition, isliving=False):
        self.xposition = xposition
        self.yposition = yposition
        self.isliving = isliving
        
    def doNextStep():
        self.isAlive =self.willLive
        self.willLive = False
        
    def checkNearbyCells(self, grid):
        count = 0
        
        x = self.xposition -1
        y = self.yposition -1
        i = 0
        j = 0
        while i < 3:
            while j < 3:
                if -1 < x <grid.gridheight and -1 < y <grid.gridwidth:
                    if grid.fullgrid[x][y].isliving == True:
                        count += 1
                y += 1
                j += 1
            j = 0
            y -= 2
            i += 1
            x += 1  
        if self.isliving == True:
            return count -1
        else:
            return count

    def checkNextStep():
        
        if checkNearbyCells => 2 => 3
            return self.willLive = True:
           
        
'''Define our functions'''
 
def PrintTheGrid():
    pass
    

def GetAdjacentCells():
    pass

def nextStep():
    pass

def randomlyPlaceLivingCells(n, grid):
    i = 0
    while i < n:
        pickedCell = grid.fullgrid[random.randint(0, grid.gridheight-1)][random.randint(0, grid.gridwidth-1)]
        if pickedCell.isliving == False:
            pickedCell.isliving = True
            i +=1
def isEmptyGrid():
    pass

''' Main programme'''

myGrid = Grid(8,12)
print myGrid
randomlyPlaceLivingCells(20, myGrid)
print myGrid
print myGrid.fullgrid[9][7].checkNearbyCells(myGrid)
print checkNextStep.checkNearbyDells(3)
