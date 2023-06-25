

class Algorithm:
    def __init__(self):
        self.TIMES = 1
        self.ROUTERS = dict()

    def showBordinConsole(self,bord: list):
        for rows in bord:
            for j in rows:
                print(j, end=" ")
            print("")

    def AddRouter(self,key: int, value: tuple):

        if (self.ROUTERS.get(key)):
            temp = self.ROUTERS.get(key)
            temp.append(value)
        else:
            self.ROUTERS[key] = list()
            temp1 = self.ROUTERS.get(key)
            temp1.append(value)

    def ChessBord(self,tr: int, tc: int, dr: int, dc: int, size: int, BORD: list):

        # 不断分割，知道size为1
        if (size == 1):
            return
        T = self.TIMES  # 当前覆盖的玩意
        self.TIMES += 1

        s = int(size / 2)  # 开始做分割

        # 开始四个方位去判断那个有木有方格子，没有就继续分割，如果没有那么就在那边标记一下
        # 左上角
        if (dr < tr + s and dc < tc + s):
            self.ChessBord(tr, tc, dr, dc, s, BORD)
        else:
            BORD[tr + s - 1][tc + s - 1] = T
            self.AddRouter(T, (tr + s - 1, tc + s - 1))
            self.ChessBord(tr, tc, tr + s - 1, tc + s - 1, s, BORD)

        # 右上角
        if (dr < tr + s and dc >= tc + s):
            self.ChessBord(tr, tc + s, dr, dc, s, BORD)
        else:
            BORD[tr + s - 1][tc + s] = T
            self.AddRouter(T, (tr + s - 1, tc + s))
            self.ChessBord(tr, tc + s, tr + s, tc + s - 1, s, BORD)

        # 左下角
        if (dr >= tr + s and dc < tc + s):
            self.ChessBord(tr + s, tc, dr, dc, s, BORD)
        else:
            BORD[tr + s][tc + s - 1] = T
            self.AddRouter(T, (tr + s, tc + s - 1))
            self.ChessBord(tr + s, tc, tr + s, tc + s - 1, s, BORD)

        # 右下角
        if (dr >= tr + s and dc >= tc + s):
            self.ChessBord(tr + s, tc + s, dr, dc, s, BORD)
        else:
            BORD[tr + s][tc + s] = T
            self.AddRouter(T, (tr + s, tc + s))
            self.ChessBord(tr + s, tc + s, tr + s, tc + s, s, BORD)

    def GetRouters(self,SIZE,dr,dc,show=False)->dict:
        BORD = [[0 for x in range(SIZE)] for i in range(SIZE)]  # 初始化棋盘
        self.ChessBord(0,0,dr,dc,SIZE,BORD)
        if(show):
            self.showBordinConsole(BORD)
        return self.ROUTERS


if __name__ == '__main__':
    algorithm= Algorithm()
    routers = algorithm.GetRouters(4,1,3,show=True)
    for i in routers.keys():
        print(routers.get(i),"-----",i)
