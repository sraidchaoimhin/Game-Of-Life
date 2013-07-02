import random


''' 
                                      Classes

First we create our classes.'''

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
    
    
''' Every cell has an x position, a y position and can be alive or dead. '''
class Cell(object):
    def __init__(self, xposition, yposition, isliving=False):
        self.xposition = xposition
        self.yposition = yposition
        self.isliving = isliving
        self.willLive = False
        
        
''' This method advances a cell to the next step. '''
def doNextStep(self):
        self.isliving = self.willLive
        
''' This method checks how many neighbours a cell has. '''        
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

''' In this method we are checking will a cell live or die.  Then we carry out the doNextStep function and print the grid. '''
def checkNextStep(self, grid):
        
        if self.isliving == False:
            if self.checkNearbyCells(grid) == 3:
                self.willLive = True
        if self.isliving == True:
            if self.checkNearbyCells(grid) < 2 or self.checkNearbyCells(grid) > 3:
                self.willLive = False
           
        
'''
                         Functions

The nextStep function takes the grid, runs through all its functions and advances it to the next step.

So it does two things:

1.  It tells every cell in the grid to check the next step as if to make a ghost grid so that each cell
    is making an image of itself on this invisible grid before advancing to the next step.

2.  Then it tells every cell in the grid to 'jump together' and advance to the next step.
                                         '''                
def nextStep(grid):
    for row in grid.fullgrid:
        for cell in row:
            cell.checkNextStep(grid)
    for row in grid.fullgrid:
        for cell in row:
            cell.doNextStep()  
    '''
    The code below wasn't working to I decided to try a while loop instead.
    for cell in row in grid.fullgrid:
        
        (for every cell in every row) deleted earlier
      
        cell.checkNextStep(grid)
    for cell in row in grid.fullgrid:
        cell.doNextStep()
       ''' 
    
''' This function randomly places the requested number of cells. '''
def randomlyPlaceLivingCells(n, grid):
    i = 0
    while i < n:
        pickedCell = grid.fullgrid[random.randint(0, grid.gridheight-1)][random.randint(0, grid.gridwidth-1)]
        if pickedCell.isliving == False:
            pickedCell.isliving = True
            pickedCell.willLive = True
            i +=1
            
''' This is a function that sets up a new grid and places the cells. '''
def newGrid():
    
    check = False
    while check == False:
        i = raw_input("Enter grid height: ")
        if int(i) > 0:
            i = int(i)
            check = True
        else:
            print "Bad number"
            
    check = False
    while check == False:
        j = raw_input("Enter grid width: ")
        if int(j) > 0:
            j = int(j)
            check = True
        else:
            print "Bad number."
                
    grid = Grid(i, j)
    
    check = False
    while check == False:
        n = raw_input("Select number of randomly placed living cells: ")
        n = int(n)
        if i*j > n and n > 0:
            randomlyPlaceLivingCells(n, grid)
            check = True
        else:
            print "Bad number."
            
    print grid
    return grid

''' 
                                              Main programme

This starts a new grid.                             '''
myGrid = newGrid()

check = False
while check == False:
    m = raw_input("Type 'next' to move to next step, or 'new' to start a new grid: ")
    m = str(m)
    if m == "next":
        nextStep(myGrid)
        print myGrid
    elif m =="new":
        myGrid = newGrid()
    elif m == "quit":
        check = True
    