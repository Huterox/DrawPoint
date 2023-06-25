
from Bord.BordPlace import Algorithm
from Bord.ShowDynamic import Board
import turtle
class ShowPlaceUI:
    def __init__(self,size,dr,dc):
        self.size = size
        self.dr = dr-1
        self.dc = dc-1
        self.algorithm = Algorithm()
        self.board = Board(self.size,self.dr,self.dc)
        self.colors = ["aqua","lime","yellow"]
    def run(self):

        routers = self.algorithm.GetRouters(self.size,self.dr,self.dc)
        # self.board.speed(10)
        for key in routers:
            points = routers.get(key)
            for point in points:
                color = self.colors[(key-1)%3]
                row,coloumn = point
                self.board.speed(100)
                self.board.drawfill(color,row,coloumn)

if __name__ == '__main__':

    showUi =  ShowPlaceUI(8,2,4)

    showUi.run()

    turtle.mainloop()

