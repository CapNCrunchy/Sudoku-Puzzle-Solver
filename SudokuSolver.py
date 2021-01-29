#My attempt at making a sudoku Solver

#Logic
#Sudoku Rules:
#           Given numbers cannot change,
#           The same number cannot appear twice in a COLUMN, ROW, or REGION
#
#Dictionary for Sudoku Spaces
#Key is read as first number is row and the second number is column
#Value will be 1-9 if it contains that value and 0 if it is empty
import pprint
pp = pprint.PrettyPrinter(indent=4)

SudokuBoard = {'R1C1':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C2':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C3':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C4':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C5':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C6':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C7':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C8':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C9':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #First row^
                'R2C1':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C2':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C3':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C4':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C5':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C6':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C7':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C8':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R2C9':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Second row^
                'R3C1':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C2':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C3':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C4':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C5':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C6':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C7':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C8':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R3C9':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Third row^
                'R4C1':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C2':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C3':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C4':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C5':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C6':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C7':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C8':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R4C9':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Fourth row^
                'R5C1':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C2':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C3':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C4':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C5':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C6':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C7':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C8':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R5C9':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Fifth row^
                'R6C1':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C2':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C3':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C4':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C5':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C6':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C7':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C8':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R6C9':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Sixth row^
                'R7C1':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C2':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C3':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C4':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C5':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C6':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C7':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C8':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R7C9':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Seventh row^
                'R8C1':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C2':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C3':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C4':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C5':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C6':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C7':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C8':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R8C9':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                #Eighth row^
                'R9C1':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C2':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C3':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C4':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C5':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C6':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C7':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C8':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R9C9':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Ninth row^
                }

inputBoard = '''
035|009|100
100|000|020
090|410|036
-----------
509|708|300
068|000|290
007|906|408
-----------
920|047|010
080|000|003
003|800|970
'''

emptyBoard= '''
000|000|000
000|000|000
000|000|000
-----------
000|000|000
000|000|000
000|000|000
-----------
000|000|000
000|000|000
000|000|000
'''

'''800|000|000
003|600|000
070|090|200
-----------
050|007|000
000|045|700
000|100|030
-----------
001|000|068
008|500|010
090|000|400'''


#creates the key using the number position (eg 12, row 1 column 2)
def numToSpace(num):
    position = 'R' + str(int(num/10)) + 'C' + str(num%10)
    return position

def importInputBoard(board):
    #loop through using regex to check for a number
    #counter to keep track of position on the input board

    counter = 11
    position = ''
    for i in range(len(board)):
        if(board[i] in ['0','1','2','3','4','5','6','7','8','9']):
            
            position = numToSpace(counter)
            
            #sets the value of the position to the dictionary, and the state
            SudokuBoard[position]['value'] = board[i]
            if(int(board[i]) != 0):
                 SudokuBoard[position]['state'] = 'solved'
            

            #counter skips multiples of 10 since there are 9 rows and columns
            counter += 1
            if(counter%10 == 0):
                counter +=1

    

def printCurrentBoard():
    NewBoard = ''''''
    counter = 11
    for i in range(len(emptyBoard)):
        if(emptyBoard[i] == '0'):
            position = numToSpace(counter)
            NewBoard = NewBoard + str(SudokuBoard[position]['value'])
            counter += 1
            
            if(counter%10 == 0):
                counter +=1
        else:
            NewBoard = NewBoard + emptyBoard[i]
        
        
    print(NewBoard)

#Functions for the logic
#loops through row, column, region and returns all values found there
#A remove impossible nums from a spaces posValues list (ie loop through the space's row, column, and region)

def SearchRegion(targetReg):
    #loops through the spaces with the target region and adds the value of the space to a list, returns list
    
    regValues = []

    for i in SudokuBoard:
        
        if(SudokuBoard[i]['region'] == targetReg) and SudokuBoard[i]['value'] != '0':
            regValues.append(SudokuBoard[i]['value'])
    
    return regValues

def SearchRow(targetRow):
    #loops through the spaces with the target row and adds the value of the space to a list, returns list
    
    rowValues = []

    for i in SudokuBoard:
        
        if(i[1] == targetRow and SudokuBoard[i]['value'] != '0'):
            rowValues.append(SudokuBoard[i]['value'])
    
    return rowValues

def SearchCol(targetCol):
    #loops through the spaces with the target Column and adds the value of the space to a list, returns list
    
    colValues = []

    for i in SudokuBoard:
        
        if(i[3] == targetCol and SudokuBoard[i]['value'] != '0'):
            colValues.append(SudokuBoard[i]['value'])
    
    return colValues

def delImpossibleValues(space):

    #searching/deleting row's values from list
    rowVals = SearchRow(space[1])
    
    for r in rowVals:
        if int(r) in SudokuBoard[space]['posValues']:
            SudokuBoard[space]['posValues'].remove(int(r))

    #searching/deleting column's values from list
    colVals = SearchCol(space[3])
    
    for c in colVals:
        if int(c) in SudokuBoard[space]['posValues']:
            SudokuBoard[space]['posValues'].remove(int(c))

    
    #searching/deleting region's values from list
    regVals = SearchRegion(SudokuBoard[space]['region'])
    
    for R in regVals:
        if int(R) in SudokuBoard[space]['posValues']:
            SudokuBoard[space]['posValues'].remove(int(R))    
    
    if(len(SudokuBoard[space]['posValues']) == 1):
        SudokuBoard[space]['value'] = SudokuBoard[space]['posValues'][0]


def baseLogicLoop(attempts):
    for i in range(attempts):
        for s in SudokuBoard:
            if(SudokuBoard[s]['value'] == '0'):
                delImpossibleValues(s)
        printCurrentBoard()





def Main():
    importInputBoard(inputBoard)
    printCurrentBoard()
    baseLogicLoop(3)
    
    print(SudokuBoard['R5C9'])

    
    



Main()