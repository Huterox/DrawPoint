




TIMES = 1 #放置的次数

ROUTERS = dict()

def showBord(bord:list):
    for rows in bord:
        for j in rows:
            print(j,end=" ")
        print("")


def AddRouter(key:int,value:tuple):
    global ROUTERS
    if(ROUTERS.get(key)):
        temp = ROUTERS.get(key)
        temp.append(value)
    else:
        ROUTERS[key] = list()
        temp1 = ROUTERS.get(key)
        temp1.append(value)





def ChessBord(tr:int,tc:int,dr:int,dc:int,size:int,BORD:list):
    global TIMES,ROUTERS
    #不断分割，知道size为1
    if(size == 1):
        return
    T = TIMES #当前覆盖的玩意
    TIMES +=1

    s = int(size/2) #开始做分割

    #开始四个方位去判断那个有木有方格子，没有就继续分割，如果没有那么就在那边标记一下
    #左上角
    if(dr<tr+s and dc<tc+s):
        ChessBord(tr,tc,dr,dc,s,BORD)
    else:
        BORD[tr+s-1][tc+s-1] = T
        AddRouter(T,(tr+s-1,tc+s-1))
        ChessBord(tr,tc,tr+s-1,tc+s-1,s,BORD)

    #右上角
    if (dr < tr + s and dc >= tc + s):
        ChessBord(tr, tc+s, dr, dc, s, BORD)
    else:
        BORD[tr + s - 1][tc + s] = T
        AddRouter(T,(tr + s - 1,tc + s))
        ChessBord(tr, tc+s, tr + s , tc + s - 1, s, BORD)

    #左下角
    if (dr >= tr + s and dc < tc + s):
        ChessBord(tr+s, tc, dr, dc, s, BORD)
    else:
        BORD[tr + s][tc + s - 1] = T
        AddRouter(T,(tr + s,tc + s - 1))
        ChessBord(tr+s, tc, tr + s, tc + s - 1, s, BORD)

    #右下角
    if (dr >= tr + s and dc >= tc + s):
        ChessBord(tr+s, tc+s, dr, dc, s, BORD)
    else:
        BORD[tr + s ][tc + s ] = T
        AddRouter(T,(tr + s ,tc + s ))
        ChessBord(tr + s, tc + s, tr + s, tc + s, s, BORD)


if __name__ == '__main__':

    SIZE = int(input("please input your size (the size must be 2^k："))
    dr = int(input("please input the barrier row"))
    dc = int(input("please input the barrier column"))
    BORD = [[0 for x in range(SIZE)] for i in range(SIZE)]  # 初始化棋盘

    ChessBord(0,0,dr,dc,SIZE,BORD)
    showBord(BORD)
    for i in ROUTERS.keys():
        print(ROUTERS.get(i))






