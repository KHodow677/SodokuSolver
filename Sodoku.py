import Board

problem = "780400120600075009000601078007040260001050930904060005070300012120007400049206007"
myBoard = Board.Board(problem)
myBoard.ResetBoard()
myBoard.GenerateSolution()
myBoard.RemoveNumbersFromBoard(2)
myBoard.PrintBoard()
print("___________________________________________________________")
'''mySodokuSolver.GenerateSolution(mySodokuSolver.board.board)
mySodokuSolver.PrintBoard(mySodokuSolver.board.board)'''
myBoard.Solve()
myBoard.PrintBoard()