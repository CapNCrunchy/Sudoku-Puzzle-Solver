#My attempt at making a sudoku Solver

#Logic
#Sudoku Rules:
#           Given numbers cannot change,
#           The same number cannot appear twice in a COLUMN, ROW, or REGION
#
#Dictionary for Sudoku Spaces
#Key is read as first number is row and the second number is column
#Value will be 1-9 if it contains that value and 0 if it is empty


SudokuBoard = {'R1C1':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]},
                'R1C2':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C3':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C4':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C5':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C6':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C7':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C8':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R1C9':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #First row^
                'R2C1':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C2':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C3':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C4':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C5':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C6':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C7':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C8':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R2C9':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Second row^
                'R3C1':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C2':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C3':{'region':'NW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C4':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C5':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C6':{'region':'N', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C7':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C8':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R3C9':{'region':'NE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Third row^
                'R4C1':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C2':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C3':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C4':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C5':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C6':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C7':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C8':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R4C9':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Fourth row^
                'R5C1':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C2':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C3':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C4':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C5':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C6':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C7':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C8':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R5C9':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Fifth row^
                'R6C1':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C2':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C3':{'region':'W', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C4':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C5':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C6':{'region':'C', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C7':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C8':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R6C9':{'region':'E', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Sixth row^
                'R7C1':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C2':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C3':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C4':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C5':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C6':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C7':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C8':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R7C9':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Seventh row^
                'R8C1':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C2':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C3':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C4':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C5':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C6':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C7':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C8':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R8C9':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Eighth row^
                'R9C1':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C2':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C3':{'region':'SW', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C4':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C5':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C6':{'region':'S', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C7':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C8':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                'R9C9':{'region':'SE', 'State':'unsolved', 'value':'0', 'posValues':[1,2,3,4,5,6,7,8,9]}
                #Ninth row^
                }

inputBoard = '''
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
def importInputBoard(board){
    #loop through using regex to check for a number
    #counter to keep track of position on the input board

    #stuff
}