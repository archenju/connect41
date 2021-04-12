from players import Human, ComputerRand, ComputerDef
from gameboard import Board
from gamerules import Checker

class Connect4:
    
    def __init__(self):
        self.col = -1
        self.board = -1
        self.checkre = -1
        self.player1 = -1
        self.player2 = -1
        
    def initgame(self):
        self.col = int( input("number of columns? (5--10): ") )
        self.board = Board(self.col)
        self.checker = Checker(self.board)
        self.board.display()
    
        pl = int( input("number of players? (0/1/2): ") )
        if pl == 0:
            self.player1 = ComputerRand(1, self.board, self.checker)
        else:
            self.player1 = Human(1, self.board, self.checker)
        if pl == 2:
            self.player2 = Human(-1, self.board, self.checker)
        else:
            self.player2 = ComputerDef(-1, self.board, self.checker)
        
    def startgame(self):
        while self.board.keepplaying:
            print("Player 1")
            self.player1.play()
            self.board.display()
            if self.board.keepplaying:
                print("Player 2")
                self.player2.play()
                self.board.display()
 


print("")
game = Connect4()
game.initgame()
game.startgame()

