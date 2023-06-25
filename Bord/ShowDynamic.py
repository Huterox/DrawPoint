from turtle import Turtle

import turtle

Size = 8
turtle.screensize(800,800,"white")

class Board(Turtle):
    def __init__(self,size,dr,dc):

        Turtle.__init__(self)
        self.shape('square')
        self.hideturtle()
        self.speed(30)
        self.width = 600
        self.height = 800
        self.size = size

        self.boxsize = 50

        self.startx = -int((self.size * self.boxsize)/2)
        self.starty = int((self.size * self.boxsize)/2)


        self.rebound()

        self.drawboard() #绘制棋盘
        self.drawfill("red",dr,dc)
        # self.drawfill("aqua",0,5)

    def drawrowline(self):

        for i in range(self.size+1):
            self.pendown()
            self.forward(self.size*self.boxsize)
            self.penup()
            self.goto(self.startx,self.starty-((i+1)*self.boxsize))

        self.rebound()

    def drawcolumnline(self):
        self.right(90) #调换方向
        for i in range(self.size+1):
            self.pendown()
            self.forward(self.boxsize*self.size)
            self.penup()
            self.goto(self.startx+self.boxsize*(i+1),self.starty)
        self.rebound()

    def drawboard(self):
        self.drawrowline()
        self.drawcolumnline()
        self.rebound()

    def move(self,UI_x,UI_y):
        self.penup()
        self.goto(UI_x,UI_y)
    def transforuipos(self,row,column):

        #负责把那个矩阵上面的坐标换算为在UI界面的坐标
        UI_y = (self.starty - row*self.boxsize)
        UI_x = self.startx + self.boxsize*column

        return UI_x,UI_y
    def drawfill(self,color,row,column):
        UI_x,UI_y= self.transforuipos(row,column)
        self.move(UI_x,UI_y)

        #给方格上色
        self.pendown()
        self.begin_fill()
        self.fillcolor(color)
        for i in range(4):
            self.forward(self.boxsize)
            self.right(90)
        self.end_fill()

        self.rebound()

    def rebound(self):
        #复原
        if(self.isdown()):
            self.penup()
        self.home()
        self.goto(self.startx, self.starty)  # 起始点

if __name__ == '__main__':
    board = Board(8,2,2)

    turtle.mainloop()