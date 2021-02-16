# author : Wang JiaNing(18201)
from random import randint, seed , choice , shuffle
from itertools import combinations

OutputEnable = 0
seedNum = 60223
# EnuLimit = 30    #枚举极限
# 算法方面的工具箱

def layMine(Row , Column , MineNum , X0 , Y0 , Min3BV = 0 , Max3BV = 1e6 , MaxTimes = 1e6):
    #布雷，参数依次是行、列、雷数、起手位置的第几行-1、第几列-1
    #起手不开空，必不为雷
    #返回二维列表，0~8代表数字，-1代表雷
    # seed(160)
    area = Row*Column-1
    Times = 0
    Parameters = []
    while Times < MaxTimes:
        if MineNum < area/2:
            Board1Dim = [0]*(area-MineNum)
            Board1Dim = Board1Dim+[-1]*MineNum
            for i in range(area-MineNum,area):
                idd=randint(0,i-1)
                if Board1Dim[idd]!=-1:
                    Board1Dim[idd]=-1
                    Board1Dim[i]=0
        else:
            Board1Dim = [-1]*MineNum
            Board1Dim = Board1Dim+[0]*(area-MineNum)
            for i in range(MineNum,area):
                idd=randint(0,i-1)
                if Board1Dim[idd] != 0:
                    Board1Dim[idd] = 0
                    Board1Dim[i] = -1
        #插入起手位置
        Board1Dim.insert(X0+Y0*Row , 0)
        #1维转2维同时算数字
        Board=[[0]*Column for _ in range(Row)]
        for i in range(0,area):
            if Board1Dim[i] < 0:
                x = i % Row
                y = i // Row
                Board[ x ][ y ] = -1
                for j in range(max(0 , x-1), min(Row , x+2)):
                    for k in range(max(0 , y-1), min(Column , y+2)):
                        if Board[ j ][ k ]>=0:
                            Board[ j ][ k ] += 1
        Times += 1
        Num3BV = cal3BV(Board)
        if Num3BV >= Min3BV and Num3BV <= Max3BV:
            Parameters.append(1)
            Parameters.append(Num3BV)
            Parameters.append(Times)
            return Board , Parameters
    Parameters.append(0)
    Parameters.append(Num3BV)
    Parameters.append(Times)
    return Board , Parameters

def layMineOp(Row , Column , MineNum , X0 , Y0 , Min3BV = 0 , Max3BV = 1e6 , MaxTimes = 1e6):
    #布雷，参数依次是行、列、雷数、起手位置的第几行-1、第几列-1
    #起手必开空，不校验雷数是否超过空格数
    #返回二维列表，0~8代表数字，-1代表雷
    if X0 == 0 or Y0 == 0 or X0 == Row-1 or Y0 == Column-1:
        if X0 == 0 and Y0 == 0 or X0 == 0 and Y0 == Column-1 or X0 == Row-1 and Y0 == 0 or X0 == Row-1 and Y0 == Column-1:
            areaOp = 4
        else:
            areaOp = 6
    else:
        areaOp = 9
    area = Row*Column-areaOp
    Times = 0
    Parameters = []
    while Times < MaxTimes:
        if MineNum < area/2:
            Board1Dim = [0]*(area-MineNum)
            Board1Dim = Board1Dim+[-1]*MineNum
            for i in range(area-MineNum,area):
                idd=randint(0,i-1)
                if Board1Dim[idd]!=-1:
                    Board1Dim[idd]=-1
                    Board1Dim[i]=0
        else:
            Board1Dim = [-1]*MineNum
            Board1Dim = Board1Dim+[0]*(area-MineNum)
            for i in range(MineNum,area):
                idd=randint(0,i-1)
                if Board1Dim[idd] != 0:
                    Board1Dim[idd] = 0
                    Board1Dim[i] = -1
        #1维转2维同时算数字
        Board=[[0]*Column for _ in range(Row)]
        i = 0
        while i < area + areaOp:
            x = i % Row
            y = i // Row
            if abs(x-X0)<=1 and abs(y-Y0)<=1:
                Board1Dim.insert(i,0)
            if Board1Dim[i] < 0:
                Board[ x ][ y ] = -1
            i += 1
        for x in range(0,Row):
            for y in range(0,Column):
                for j in range(max(0 , x-1), min(Row , x+2)):
                    for k in range(max(0 , y-1), min(Column , y+2)):
                        if Board[ j ][ k ]<0 and Board[ x ][ y ]>=0:
                            Board[ x ][ y ] += 1
        Times += 1
        Num3BV = cal3BV(Board)
        if Num3BV >= Min3BV and Num3BV <= Max3BV:
            Parameters.append(1)
            Parameters.append(Num3BV)
            Parameters.append(Times)
            return Board , Parameters
    Parameters.append(0)
    Parameters.append(Num3BV)
    Parameters.append(Times)
    return Board , Parameters

def refreshBoard(Board , BoardofGame , ClickedPoses):
    # 给出点击位置，刷新局面
    # 参数：局面，游戏局面，点击位置，可以同时点多个位置
    # ClickedPoses一定不能是雷,(也不能是空???),是序列格式
    Row=len(Board)
    Column=len(Board[0])
    for i,j in ClickedPoses:
        if Board[i][j] > 0:
            BoardofGame[i][j] = Board[i][j]
        if Board[i][j] == 0:
            BoardofGame[i][j] = 0
            for m in range(max(0 , i-1), min(Row , i+2)):
                for n in range(max(0 , j-1), min(Column , j+2)):
                    if (i!=m or j!=n) and BoardofGame[m][n] == 10:
                        BoardofGame= refreshBoard(Board , BoardofGame , [(m,n)])
    return BoardofGame


def refreshMatrix(BoardofGame):
    # BoardofGame必须且肯定是正确标雷的游戏局面
    # 根据游戏局面生成矩阵
    Row=len(BoardofGame)
    Column=len(BoardofGame[0])
    MatrixA=[]
    Matrixx=[]
    Matrixb=[]
    MatrixARowNum = 0
    MatrixAColumnNum = 0
    for i , oneRow in enumerate(BoardofGame[:]):
        for j , oneCell in enumerate(oneRow[:]):
            if oneCell > 0 and oneCell < 10:
                flag = 0
                for m in range(max(0 , i-1), min(Row , i+2)):
                    for n in range(max(0 , j-1), min(Column , j+2)):
                        if BoardofGame[m][n] == 10:
                            flag = 1
                if flag:
                    MatrixA.append([0]*MatrixAColumnNum)
                    Matrixb.append(BoardofGame[i][j])
                    MatrixARowNum += 1
                    for m in range(max(0 , i-1), min(Row , i+2)):
                        for n in range(max(0 , j-1), min(Column , j+2)):
                            if BoardofGame[m][n] == 11:
                                Matrixb[MatrixARowNum-1] -= 1
                            elif BoardofGame[m][n] == 10:
                                try:
                                    temp = Matrixx.index((m,n))
                                    MatrixA[MatrixARowNum-1][temp] = 1
                                except:
                                    for ii in range(MatrixARowNum):
                                        MatrixA[ii].append(0)
                                    Matrixx.append((m,n))
                                    MatrixAColumnNum += 1
                                    MatrixA[MatrixARowNum-1][MatrixAColumnNum-1] = 1
    return MatrixA , Matrixx , Matrixb

def SolveDirect(MatrixA , Matrixx , Matrixb , BoardofGame):
    #考虑只一个方程判雷，比如3个方格，雷数也是正好是3，等等
    #返回MatrixA , Matrixx , Matrixb , BoardofGame , NotMine , flag
    # flag=1表明有所动作，比如标雷或发现NotMine
    #NotMine存储非雷的位置
    #注意：处理结束后的矩阵可能有重复的行(?)
    flag = 0
    NotMine = []
    MatrixColumn = len(Matrixx)
    MatrixRow = len(Matrixb)
    for i in range(MatrixRow-1 , -1 , -1):#第一轮循环，找是雷的位置
        if sum(MatrixA[i][:]) == Matrixb[i]:
            flag = 1
            for k in range(MatrixColumn-1 , -1 , -1):
                if MatrixA[i][k] == 1:
                    m,n = Matrixx[k]
                    BoardofGame[m][n] = 11#在游戏局面中标雷
                    Matrixx.pop(k)
                    for t in range(0,MatrixRow):
                        if MatrixA[t][k] == 0:
                            MatrixA[t].pop(k)
                        else:
                            MatrixA[t].pop(k)
                            Matrixb[t] -= 1
                    MatrixColumn -= 1
            MatrixA.pop(i)
            Matrixb.pop(i)
            MatrixRow -= 1
    for i in range(MatrixRow-1 , -1 , -1):#第二轮循环，找不是雷的位置
        if Matrixb[i]==0:
            flag = 1
            for k in range(MatrixColumn-1 , -1 , -1):
                if MatrixA[i][k] == 1 and Matrixx[k] not in NotMine:
                    NotMine.append(Matrixx[k])
    
    return BoardofGame , NotMine , flag
    
    
def SolveMinus(MatrixA , Matrixx , Matrixb , BoardofGame):
    #用减法和集合的包含关系判雷
    #返回BoardofGame , NotMine , flag
    #如果发现IsMine而没有发现NotMine，会再用单集合找一遍。如果发现NotMine，则不调用方法1
    #因此，若方法2没有发现NotMine，则方法1也不可能发现NotMine；
    #若方法2发现NotMine，则方法1还可能发现NotMine
    #注意：处理结束后的矩阵可能有重复的行
    flag = 0
    NotMine = []
    NotMineRel = []
    IsMineRel = []  #先找到是雷和非雷的ID，最后才处理
    MatrixColumn = len(Matrixx)
    MatrixRow = len(Matrixb)
    if MatrixRow<=1:
        return BoardofGame , NotMine , 0
    for i in range(MatrixRow-1 , 0 , -1):
        for j in range(i-1 , -1 , -1):
            ADval1=[]  #记录相减后为1和-1的列索引
            ADvaln1=[]
            FlagAdj = 0 #两个方程是否相邻的标志
            for k in range(0 , MatrixColumn): #开始相减
                if MatrixA[i][k] and MatrixA[j][k]:
                    FlagAdj=1
                    continue
                if MatrixA[i][k] - MatrixA[j][k] == 1:
                    ADval1.append(k)
                elif MatrixA[i][k] - MatrixA[j][k] == -1:
                    ADvaln1.append(k)
            if FlagAdj:
                bDval = Matrixb[i] - Matrixb[j]
                if len(ADval1) == bDval:  #减法过后，剩余格数等于剩余雷数
                    IsMineRel = IsMineRel + ADval1
                    NotMineRel = NotMineRel + ADvaln1
                elif len(ADvaln1) == -bDval:
                    IsMineRel = IsMineRel + ADvaln1
                    NotMineRel = NotMineRel + ADval1 #此时集合中有重复的元素
    if len(IsMineRel) > 0 or len(NotMineRel) > 0:
        flag = 1
    IsMineRel = list(set(IsMineRel))
    NotMineRel = list(set(NotMineRel))#去除重复的元素
    IsMineRel.sort(reverse = True)
    for i in range(0,len(NotMineRel)):
        NotMine.append(Matrixx[NotMineRel[i]])#相对索引改成绝对索引
  
    #完成双集合判雷，开始处理
    for i in IsMineRel:
        m,n = Matrixx[i]
        BoardofGame[m][n] = 11
    return BoardofGame , NotMine , flag

def SolveEnumerate(MatrixA , Matrixx , Matrixb , BoardofGame , enuLimit=30):
    #枚举法判雷
    flag = 0
    NotMine = []
    NotMineRel = []
    IsMineRel = []
    MatrixColumn = len(Matrixx)
    MatrixRow = len(Matrixb)
    #第一步，删去重复的行
    for i in range(MatrixRow-1 , 0 , -1):
        for j in range(i-1 , -1 , -1):
            if MatrixA[i] == MatrixA[j]:
                MatrixA.pop(i)
                Matrixb.pop(i)
                break
    MatrixRow = len(Matrixb)
    #第二步，整理成分块矩阵
    ColId = list(range(0,MatrixColumn))
    RowId = list(range(0,MatrixRow))
    TempCol = [] # 与深度优先搜索有关
    TempRow = []
    while ColId:# 每一个未知格都要分组完
        TempCol.append(ColId.pop())
        Groupb = []
        Groupx = []
        GroupCol = []  #单个组的临时索引
        GroupRow = []
        while TempCol or TempRow:
            if TempCol:
                for i in range(0,MatrixRow):
                    if MatrixA[i][TempCol[-1]] == 1:
                        if i in RowId:
                            TempRow.append(i)
                            RowId.remove(i)
                temp = TempCol.pop()
                GroupCol.append(temp)
                Groupx.append(Matrixx[temp])
            if TempRow:
                for j in range(0,MatrixColumn):
                    if MatrixA[TempRow[-1]][j] == 1:
                        if j in ColId:
                            TempCol.append(j)
                            ColId.remove(j)
                temp = TempRow.pop()
                GroupRow.append(temp)
                Groupb.append(Matrixb[temp])
        
        if len(GroupCol) >= enuLimit:#枚举法的极限
            continue
        AllTable = [[2]*len(GroupCol)]
        for i in GroupRow:
            b = Matrixb[i]
            TableId = []
            for j in GroupCol:
                if MatrixA[i][j] == 1:
                    TableId.append(GroupCol.index(j))
            AllTable = enuOneStep(AllTable , TableId , b) # 一块区域枚举完成
        
        for j in range(0,len(GroupCol)):#找用枚举法找到这一块区域的雷或非雷
            if AllTable[0][j] == 0:
                NotMineRel.append(GroupCol[j])
                for i in range(1,len(AllTable)):
                    if AllTable[i][j] == 1:
                        NotMineRel.pop()
                        break
            else:
                IsMineRel.append(GroupCol[j])
                for i in range(1,len(AllTable)):
                    if AllTable[i][j] == 0:
                        IsMineRel.pop()
                        break
    
    IsMineRel = list(set(IsMineRel))
    NotMineRel = list(set(NotMineRel))#去除重复的元素
    IsMineRel.sort(reverse = True)
    for i in range(0,len(NotMineRel)):
        NotMine.append(Matrixx[NotMineRel[i]])#相对索引改成绝对索引  
  
    #完成双集合判雷，开始处理
    for i in IsMineRel:
        m,n = Matrixx[i]
        BoardofGame[m][n] = 11
           
    return BoardofGame , NotMine , flag


def enuOneStep(AllTable , TableId , b):
    #AllTable中，0表示非雷，1表示雷，2表示暂未枚举
    #TableId保存了AllTable的索引，AllTable的列和GroupCol的列一致
    #b表示TableId指向的位置中有几个雷
    NewId = []
    for i in TableId:
        # try:
        if AllTable[0][i] == 2:
            NewId.append(i)
        # except:
        #     print(AllTable)
        #     print(i)
    DelId = []
    for i in range(0,len(AllTable)):
        ExtraMine = b
        for j in TableId:
            if AllTable[i][j] == 1:
                ExtraMine -= 1
        if ExtraMine < 0 or ExtraMine > len(NewId):
            #当前方案的雷数超过方程的限制，则删除该方案
            #当前方案的雷数超过方格数，也要删除该方案
            DelId.append(i)
            continue
        AddedTable = enumerateSub(len(NewId) , ExtraMine)
        #给当前表格增加方案
        for t in range(0,len(NewId)):
            AllTable[i][NewId[t]] = AddedTable[0][t]
        for m in range(1,len(AddedTable)):
            AllTable.append(AllTable[i][:])
            for t in range(0,len(NewId)):
                AllTable[-1][NewId[t]] = AddedTable[m][t]
    
    DelId.sort(reverse=True)
    for i in DelId:
        AllTable.pop(i)
    return AllTable
      
def refreshMatrixWithNotMine(MatrixA,Matrixx,Matrixb,NotMine):
    # 用非雷刷新三个矩阵，同时删掉全为0的行
    # MatrixA,Matrixx,Matrixb = refreshMatrixWithNotMine(MatrixA,Matrixx,Matrixb,NotMine)
    MatrixRow = len(Matrixb)
    # MatrixColumn = len(Matrixx)
    NotMineRel = []
    for j in NotMine:
        NotMineRel.append(Matrixx.index(j))
    NotMineRel.sort(reverse=True)
    for m in NotMineRel:
        Matrixx.pop(m)
    for i in range(MatrixRow-1 , -1 , -1):
        if sum(MatrixA[i][:]) == 0:
            MatrixA.pop(i)
            Matrixb.pop(i)
            continue
        for m in NotMineRel:
            MatrixA[i].pop(m)
        
    return MatrixA , Matrixx , Matrixb    
  
def Victory(BoardofGame,Board):
    #判断当前是否获胜
    #游戏局面中必须没有标错的雷
    #这个函数不具备普遍意义
    Row = len(BoardofGame)
    Col = len(BoardofGame[0])
    for i in range(0,Row):
        for j in range(0,Col):
            if BoardofGame[i][j] == 10 and Board[i][j] != -1:
                return 0
    return 1

def enumerateSub(Col , MineNum):
    #返回长度为Col，其中含有MineNum个1的所有01序列，形状为[[][][][]]
    Out=[]
    List=range(0,Col)
    for i in combinations(List, MineNum):
        Out.append([0]*Col)
        for j in range(0,MineNum):
            Out[-1][i[j]]=1
    return Out

def enumerateChangeBoard(mineLabel,BoardofGame,xx,yy,enuLimit=30):
    # 等可能给出全部可能情况中(i,j)不为雷的随机一种情况,此时(i,j)一定是未打开状态；
    # 但若超过最大枚举长度，
    # 将返回非随机的某一种可能的情况（暂未实现），若剩余位置数少于雷数，则返回原图
    # 直接返回改好的图和flag，0是改图失败，1是成功
    # 理论上（xx,yy）原本必须是雷
    # 局限：有时候，重排需要用更多的雷，但内部方格里没有这么多雷，本算法不能从
    #       边缘方格中抽取雷
    
    MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
    # mineLabel0 = mineLabel.copy() # 备份，重排失败后启用
    
    #先判定是否是必然的雷，即有没有枚举的必要
    BoardofGame,NotMine,flag= SolveDirect(MatrixA , Matrixx , Matrixb , BoardofGame)
    if BoardofGame[xx][yy] == 11:
        return mineLabel , 0
    else:
        MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
        BoardofGame , NotMine,flag= SolveMinus(MatrixA , Matrixx , Matrixb , BoardofGame)
        if BoardofGame[xx][yy] == 11:
            return mineLabel , 0
    MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
    MatrixColumn = len(Matrixx)
    MatrixRow = len(Matrixb)
    
    #统计一下一共有几个雷
    MineNum0 = 0
    Mineinside = 0  # 内部的雷数
    for idm, m in enumerate(mineLabel):
        for idn, n in enumerate(m):
            if n.num == -1:
                MineNum0 += 1
                if (idm, idn) not in Matrixx:
                    Mineinside += 1
    
    #再判断是不是内部的雷
    if (xx,yy) not in Matrixx:
        mineLabel[xx][yy].num = 9
        # 如果是内部的雷，就直接改成非雷,而且是正常情况绝不会出现的数做记号
        mineLabel = refreshMineLable(mineLabel , MineNum0 , BoardofGame)  
        return mineLabel, 1
          
    Id = Matrixx.index((xx,yy))
    MatrixRow = len(Matrixb)
    #第二步，整理成分块矩阵
    ColId = list(range(0,MatrixColumn))
    RowId = list(range(0,MatrixRow))
    GroupCol = []  #单个组的临时索引
    GroupRow = []
    Groupb = []
    Groupx = []
    TempCol = []
    TempRow = []
    TempCol.append(Id)
    ColId.remove(Id)
    while TempCol or TempRow:
        if TempCol:
            for i in range(0,MatrixRow):
                if MatrixA[i][TempCol[-1]] == 1:
                    if i in RowId:
                        TempRow.append(i)
                        RowId.remove(i)
            temp = TempCol.pop()
            GroupCol.append(temp)
            Groupx.append(Matrixx[temp])
        if TempRow:
            for j in range(0,MatrixColumn):
                if MatrixA[TempRow[-1]][j] == 1: #越界，当只剩最后一个2*2的二选一时
                    if j in ColId:
                        TempCol.append(j)
                        ColId.remove(j)
            temp = TempRow.pop()
            GroupRow.append(temp)
            Groupb.append(Matrixb[temp])
    
    if len(GroupCol) >= enuLimit:#枚举法的极限
        #超过枚举极限时，暂时不能给出可能的解，有待升级
        return mineLabel, 0
        # newTable , flag = boardFastSol(MatrixA,Matrixx,Matrixb,GroupCol,GroupRow,Id)
        
    AllTable = [[2]*len(GroupCol)]
    for i in GroupRow:
        b = Matrixb[i]
        TableId = []
        for j in GroupCol:
            if MatrixA[i][j] == 1:
                TableId.append(GroupCol.index(j))
        # if not AllTable:
        #     return mineLabel0 , 0
        AllTable = enuOneStep(AllTable , TableId , b)
    
    for index , item in enumerate(AllTable[:]):
        # 删除重排后原位置还是雷的情况
        # 前面的步骤保证AllTable的第一列一定是代表(xx,yy)，所以只要删除首位是雷的可能
        if item[0] == 1:
            AllTable.remove(item)
    if not AllTable:
        return mineLabel, 0
    newTable = choice(AllTable)#随机抽取列表中某个元素
    #随机重排后可能雷数有增减
    
    deltaMine = 0  # 重排前后相差的雷数不能超过内部的雷数
    for index , item in enumerate(GroupCol):
        (m,n) = Matrixx[item]
        deltaMine = deltaMine + newTable[index] - (mineLabel[m][n].num == -1)
    if deltaMine > Mineinside:
        return mineLabel, 0
    
    for index , item in enumerate(GroupCol):
        (m,n) = Matrixx[item]
        mineLabel[m][n].num = -newTable[index]
    
    
    mineLabel[xx][yy].num = 9
    mineLabel = refreshMineLable(mineLabel , MineNum0 , BoardofGame)
         
    return mineLabel , 1

def refreshMineLable(mineLabel , MineNum0 , BoardofGame):
    # 该刷新用在局面重排后
    # 根据真实局面和游戏局面，以及总雷数，刷新真实局面
    # 游戏局面是不变的，真实局面的未打开的数字会刷新
    # 如果有雷数的增减，则内部的雷会重排
    # 请保证雷数不多于内部格数
    Row = len(mineLabel)
    Column = len(mineLabel[0])
    MineNum1 = 0
    for i in mineLabel:
        for j in i:
            if j.num == -1:
                MineNum1 += 1
    #如果雷数不一样，内部就要重排
    if not MineNum1 == MineNum0:
        posInside = []
        mineNumInside = 0
        for x , itemx in enumerate(mineLabel[:]):
            for y , itemy in enumerate(itemx[:]):
                insideFlag = 1
                for i in range(max(0,x-1) , min(Row,x+2)):
                    for j in range(max(0,y-1) , min(Column,y+2)):
                        if not BoardofGame[i][j] == 10:
                        # BoardofGame 和 mineLabel.status的区别是后者可能乱标雷
                        # 而前者的雷都是算法标上去的
                            insideFlag = 0
                if insideFlag and itemy.num != 9:
                    posInside.append((x , y))
                    if itemy.num == -1:
                        mineNumInside += 1
        #改正总的雷数
        mineNumInside = mineNumInside+MineNum0-MineNum1
        posNum = len(posInside) - mineNumInside
        # if posNum < 0: # 这种情况是内部格子数比雷数少，重排失败
        #     return mineLabel , 0
        #重新布内部的雷
        newInsideBoard = [-1] * mineNumInside + [0] * (posNum)
        shuffle(newInsideBoard)
        for index , (x,y) in enumerate(posInside[:]):
            mineLabel[x][y].num=newInsideBoard[index]
    # 重排完毕，开始刷新
    for x , itemx in enumerate(mineLabel[:]):
        for y , itemy in enumerate(itemx[:]):
            if not itemy.num == -1:
                boardNum = 0
                for i in range(max(0,x-1) , min(Row,x+2)):
                    for j in range(max(0,y-1) , min(Column,y+2)):
                        if mineLabel[i][j].num == -1:
                            boardNum += 1
                itemy.num = boardNum
    return mineLabel

def isSolvable(Board , X0 , Y0 , enuLimit):
    #从指定位置开始扫，判断局面是否无猜
    #周围一圈都是雷，那么中间是雷不算猜，中间不是雷算猜
    if unsolvableStructure(Board):#若包含不可判雷结构，则不是无猜
        return 0
    BoardofGame = [[10]*len(Board[0]) for _ in range(len(Board))]
    #10是未打开，11是标雷
    #局面大小必须超过6*6
    MatrixA = []
    Matrixx = []
    Matrixb = []
    BoardofGame = refreshBoard(Board , BoardofGame , [(X0,Y0)])
    MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
    if Victory(BoardofGame,Board):
        return 1 # 暂且认为点一下就扫开也是可以的
    while 1:
        BoardofGame,NotMine,flag= SolveDirect(MatrixA , Matrixx , Matrixb , BoardofGame)       
        if flag == 0:
            BoardofGame , NotMine,flag= SolveMinus(MatrixA , Matrixx , Matrixb , BoardofGame)
            if flag == 0:
                BoardofGame,NotMine,flag= SolveEnumerate(MatrixA , Matrixx , Matrixb , BoardofGame , enuLimit)
                if flag == 0:
                    return 0
        BoardofGame = refreshBoard(Board , BoardofGame , NotMine)
        # print2(BoardofGame)
        MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
        if Victory(BoardofGame,Board):
            return 1

def unsolvableStructure(BoardCheck):
    #用几种模板，检测局面中是否有明显的死猜的结构
    #不考虑起手位置，因为起手必开空
    #局面至少大于4*4
    #返回0或1
    Board = [[0]*len(BoardCheck[0]) for _ in range(len(BoardCheck))]
    Row = len(Board)
    Column = len(Board[0])
    for i in range(0,Row):
        for j in range(0,Column):
            if BoardCheck[i][j] == -1:
                Board[i][j] = -1
    for i in range(0,Row-2):#检查左右两侧
        if i < Row-3:
            if Board[i][0] == -1 and Board[i][1] == -1 and Board[i+3][0] == -1 and Board[i+3][1] == -1 and Board[i+1][0]+Board[i+2][0] == -1 \
            or Board[i][Column-1] == -1 and Board[i][Column-2] == -1 and Board[i+3][Column-1] == -1 and Board[i+3][Column-2] == -1 and Board[i+1][Column-1]+Board[i+2][Column-1] == -1:
                return 1
        if Board[i][2] == -1 and Board[i+1][2] == -1 and Board[i+2][2] == -1 and Board[i+1][0]+Board[i+1][1] == -1 \
        or Board[i][Column-3] == -1 and Board[i+1][Column-3] == -1 and Board[i+2][Column-3] == -1 and Board[i+1][Column-1]+Board[i+1][Column-2] == -1 \
        or Board[i][0] == -1 and Board[i][1] == -1 and Board[i+1][1] == -1 and Board[i+2][1] == -1 and Board[i+2][0] == -1 and Board[i+1][0] == 0 \
        or Board[i][Column-1] == -1 and Board[i][Column-2] == -1 and Board[i+1][Column-2] == -1 and Board[i+2][Column-2] == -1 and Board[i+2][Column-1] == -1 and Board[i+1][Column-1] == 0:
            return 1
        if i < Row-3:
            if Board[i][2] == -1 and Board[i+3][2] == -1 and Board[i+1][0]+Board[i+1][1] == -1 and Board[i+1][1]+Board[i+2][1] == -1 and Board[i+2][1]+Board[i+2][0] == -1 \
            or Board[i][Column-3] == -1 and Board[i+3][Column-3] == -1 and Board[i+1][Column-1]+Board[i+1][Column-2] == -1 and Board[i+1][Column-2]+Board[i+2][Column-2] == -1 and Board[i+2][Column-2]+Board[i+2][Column-1] == -1:
                return 1
            
    for j in range(0,Column-2):#检查上下两侧
        if j < Column-3:
            if Board[0][j] == -1 and Board[1][j] == -1 and Board[0][j+3] == -1 and Board[1][j+3] == -1 and Board[0][j+1]+Board[0][j+2] == -1 \
            or Board[Row-1][j] == -1 and Board[Row-2][j] == -1 and Board[Row-1][j+3] == -1 and Board[Row-2][j+3] == -1 and Board[Row-1][j+1]+Board[Row-1][j+2] == -1:
                return 1
        if Board[2][j] == -1 and Board[2][j+1] == -1 and Board[2][j+2] == -1 and Board[0][j+1]+Board[1][j+1] == -1 \
        or Board[Row-3][j] == -1 and Board[Row-3][j+1] == -1 and Board[Row-3][j+2] == -1 and Board[Row-1][j+1]+Board[Row-2][j+1] == -1 \
        or Board[0][j] == -1 and Board[1][j] == -1 and Board[1][j+1] == -1 and Board[1][j+2] == -1 and Board[0][j+2] == -1 and Board[0][j+1] == 0 \
        or Board[Row-1][j] == -1 and Board[Row-2][j] == -1 and Board[Row-2][j+1] == -1 and Board[Row-2][j+2] == -1 and Board[Row-1][j+2] == -1 and Board[Row-1][j+1] == 0:
            return 1
        if j < Column-3:
            if Board[2][j] == -1 and Board[2][j+3] == -1 and Board[0][j+1]+Board[1][j+1] == -1 and Board[1][j+1]+Board[1][j+2] == -1 and Board[1][j+2]+Board[0][j+2] == -1 \
            or Board[Row-3][j] == -1 and Board[Row-3][j+3] == -1 and Board[Row-1][j+1]+Board[Row-2][j+1] == -1 and Board[Row-2][j+1]+Board[Row-2][j+2] == -1 and Board[Row-2][j+2]+Board[Row-1][j+2] == -1:
                return 1
    if Board[0][2] == -1 and Board[1][2] == -1 and Board[0][0]+Board[0][1] == -1 \
    or Board[2][0] == -1 and Board[2][1] == -1 and Board[0][0]+Board[1][0] == -1 \
    or Board[0][Column-3] == -1 and Board[1][Column-3] == -1 and Board[0][Column-1]+Board[0][Column-2] == -1 \
    or Board[2][Column-1] == -1 and Board[2][Column-2] == -1 and Board[0][Column-1]+Board[1][Column-1] == -1 \
    or Board[Row-1][2] == -1 and Board[Row-2][2] == -1 and Board[Row-1][0]+Board[Row-1][1] == -1 \
    or Board[Row-3][0] == -1 and Board[Row-3][1] == -1 and Board[Row-1][0]+Board[Row-2][0] == -1 \
    or Board[Row-1][Column-3] == -1 and Board[Row-2][Column-3] == -1 and Board[Row-1][Column-1]+Board[Row-1][Column-2] == -1 \
    or Board[Row-3][Column-1] == -1 and Board[Row-3][Column-2] == -1 and Board[Row-1][Column-1]+Board[Row-2][Column-1] == -1 \
    or Board[0][1]+Board[1][1]+Board[1][0] == -3 and Board[0][0] == 0 \
    or Board[0][Column-2]+Board[1][Column-2]+Board[1][Column-1] == -3 and Board[0][Column-1] == 0 \
    or Board[Row-1][Column-2]+Board[Row-2][Column-2]+Board[Row-2][Column-1] == -3 and Board[Row-1][Column-1] == 0 \
    or Board[Row-1][1]+Board[Row-2][1]+Board[Row-2][0] == -3 and Board[Row-1][0] == 0 \
    or Board[2][2] == -1 and Board[0][1]+Board[1][1] == -1 and Board[1][0]+Board[1][1] == -1 \
    or Board[Row-3][2] == -1 and Board[Row-1][1]+Board[Row-2][1] == -1 and Board[Row-2][0]+Board[Row-2][1] == -1 \
    or Board[Row-3][Column-3] == -1 and Board[Row-1][Column-2]+Board[Row-2][Column-2] == -1 and Board[Row-2][Column-1]+Board[Row-2][Column-2] == -1 \
    or Board[2][Column-3] == -1 and Board[0][Column-2]+Board[1][Column-2] == -1 and Board[1][Column-1]+Board[1][Column-2] == -1:#检查四个角
        return 1
    for i in range(0,Row-2):   #找中间的工、回、器形结构
        for j in range(0,Column-2):
            if j < Column-3:
                if Board[i][j] == -1 and Board[i+1][j] == -1 and Board[i+2][j] == -1 and Board[i][j+3] == -1 and Board[i+1][j+3] == -1 and Board[i+2][j+3] == -1 and Board[i+1][j+1]+Board[i+1][j+2] == -1:
                    return 1
            if i < Row-3:
                if Board[i][j] == -1 and Board[i][j+1] == -1 and Board[i][j+2] == -1 and Board[i+3][j] == -1 and Board[i+3][j+1] == -1 and Board[i+3][j+2] == -1 and Board[i+1][j+1]+Board[i+2][j+1] == -1:
                    return 1
            if Board[i][j] == -1 and Board[i+1][j] == -1 and Board[i+2][j] == -1 and Board[i][j+1] == -1 and Board[i+2][j+1] == -1 and Board[i][j+2] == -1 and Board[i+1][j+2] == -1 and Board[i+2][j+2] == -1 and Board[i+1][j+1] == 0:
                return 1
            if j < Column-3 and i < Row-3:
                if Board[i][j] == -1 and Board[i+3][j] == -1 and Board[i][j+3] == -1 and Board[i+3][j+3] == -1 and Board[i+1][j+1]+Board[i+2][j+1] == -1 and Board[i+1][j+1]+Board[i+1][j+2] == -1 and Board[i+2][j+1]+Board[i+2][j+2] == -1:
                    return 1
    return 0

def print2(arr, mode = 0):
    #调试时便于打印 print2(BoardofGame)
    if mode == 0:
        for i in arr:
            for j in i:
                print('%3.d'%j, end='')
            print()
    elif mode == 1:
        for i in arr:
            for j in i:
                print('%3.d'%j.num, end='')
            print()
    elif mode == 2:
        for i in arr:
            for j in i:
                print('%3.d'%j.status, end='')
            print()

def layMineSolvable(Row , Column , MineNum , X0 , Y0 , Min3BV = 0 , Max3BV = 1e6 , 
                    MaxTimes = 1e6 , enuLimit = 30):
    # 3BV下限、上限，最大尝试次数，返回是否成功。
    # 若不成功返回最后生成的局面（不一定无猜），默认尝试十万次
    Times = 0
    Parameters = []
    while Times < MaxTimes:
        Board , _ = layMineOp(Row , Column , MineNum ,X0, Y0)
        Times += 1
        Num3BV = cal3BV(Board)
        if Num3BV >= Min3BV and Num3BV <= Max3BV:
            if isSolvable(Board , X0, Y0,enuLimit):
                Parameters.append(1)
                Parameters.append(Num3BV)
                Parameters.append(Times)
                return Board , Parameters
    Parameters.append(0)
    Parameters.append(Num3BV)
    Parameters.append(Times)
    return Board , Parameters

def calOp(Board):
    # 0的8连通域数
    Row = len(Board)
    Column = len(Board[0])
    Op = 0
    BoardCopy = [[0]*Column for _ in range(Row)]
    for i in range(0 , Row):
        for j in range(0 , Column):
            BoardCopy[i][j] = Board[i][j]
    for i in range(0 , Row):
        for j in range(0 , Column):
            if BoardCopy[i][j] == 0:
                BoardCopy[i][j] = 1
                BoardCopy = infectBoard(BoardCopy , i , j)
                Op += 1
    return Op

def infectBoard(BoardCopy , x , y):
    # 递归算连通域
    Row = len(BoardCopy)
    Column = len(BoardCopy[0])
    for i in range(max(0 , x-1), min(Row , x+2)):
        for j in range(max(0 , y-1), min(Column , y+2)):
            if BoardCopy[i][j] == 0:
                BoardCopy[i][j] = 1
                BoardCopy = infectBoard(BoardCopy , i , j)
    return BoardCopy

def cal3BV(Board):
    Row = len(Board)
    Column = len(Board[0])
    Num3BV = 0
    for i in range(0 , Row):
        for j in range(0 , Column):
            if Board[i][j] > 0:
                flag = 1
                for x in range(max(0 , i-1), min(Row , i+2)):
                    for y in range(max(0 , j-1), min(Column , j+2)):
                        if Board[x][y] == 0:
                            flag = 0
                if flag:
                    Num3BV += 1
    return Num3BV + calOp(Board)

    
def isJudgeable(BoardofGame , EnuLimit=30):
    # 返回此时是否存在可判的格子，如果还能判返回1
    # 这个过程中，如果AI见到的游戏局面中有未标的雷，会标雷，但仍然可能有漏标的
    # flag = 0
    MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
    BoardofGame , NotMine , flag = SolveDirect(MatrixA , Matrixx , Matrixb , BoardofGame)       
    if not NotMine:
        MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
        BoardofGame , NotMine , flag = SolveMinus(MatrixA , Matrixx , Matrixb , BoardofGame)
        if not NotMine:
            MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
            BoardofGame , NotMine , flag = SolveEnumerate(MatrixA , Matrixx , Matrixb , BoardofGame , EnuLimit)
            if not NotMine:
                return BoardofGame , 0
    return BoardofGame , 1
    
def xyisJudgeable(BoardofGame , x , y , EnuLimit=30):
    # (x,y)是否必然不是雷，如果必然不是雷，返回1
    MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
    
    if (x,y) not in Matrixx:  # 内部的非雷按理无法判出
        return 0
    
    BoardofGame , NotMine , flag = SolveDirect(MatrixA , Matrixx , Matrixb , BoardofGame)       
    if (x,y) not in NotMine:
        MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
        BoardofGame , NotMine , flag = SolveMinus(MatrixA , Matrixx , Matrixb , BoardofGame)
        if (x,y) not in NotMine:
            MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
            BoardofGame , NotMine , flag = SolveEnumerate(MatrixA , Matrixx , Matrixb , BoardofGame , EnuLimit)
            if (x,y) not in NotMine:
                return 0
    return 1

def calBoardIndex(Board):
    # 原则上计算局面中所有指标，比较慢（毫秒级）
    # 3BV, Ops, Isls
    # 以后会加各个数字出现次数等等
    # 返回字典
    indexes = {}
    Row = len(Board)
    Column = len(Board[0])
    Num3BV = 0
    for i in range(0, Row):
        for j in range(0, Column):
            if Board[i][j] > 0:
                flag = 1
                for x in range(max(0, i - 1), min(Row, i + 2)):
                    for y in range(max(0, j - 1), min(Column, j + 2)):
                        if Board[x][y] == 0:
                            flag = 0
                if flag:
                    Num3BV += 1
    indexes['Ops'] = calOp(Board)
    indexes['3BV'] = Num3BV + indexes['Ops']
    indexes['Isls'] = '还在写'
    return indexes

def calScores(mode, winflag, time, operationStream, Board):
    # 计算游戏得分，展示用，返回一个字典，都是字符串
    # gameBoard是带数字的
    scores = {}
    indexes = calBoardIndex(Board)
    scores['Time'] = '{:.3f}'.format(time)
    scores['eTime'] = '{:.3f}'.format(time) if winflag else '还在写'
    scores['3BV'] = str(indexes['3BV'])
    scores['Ops'] = str(indexes['Ops'])
    scores['Isls'] = str(indexes['Isls'])
    scores['Left'] = '还在写'
    scores['Right'] = '还在写'
    scores['Cl'] = '还在写'
    scores['IOE'] = '还在写'
    scores['Thrp'] = '还在写'
    scores['Corr'] = '还在写'
    scores['3BV/s'] = '{:.2f}'.format(indexes['3BV']/time) if winflag else '还在写'
    scores['RQP'] = '{:.2f}'.format(time**2/indexes['3BV']) if winflag else '---'
    scores['STNB'] = '还在写'
    scores['Ces'] = '还在写'
    scores['Mode'] = '还在写'
    scores['Difficulty'] = '还在写'
    return scores


def ai(mineLabel , BoardofGame , gameMode,i,j):
    #0，1，2，3，4，5，6，7代表：标准、win7、
    #竞速无猜、强无猜、弱无猜、准无猜、强可猜、弱可猜
    #根据模式处理一次点击的全部流程
    #返回的最后一个值是一个flag，无论是不是雷，都代表是否失败，1为失败
    # 该函数维护BoardofGame，具体为标雷
    # （i，j）一定是未打开状态
    if mineLabel[i][j].num == -1:
        # MatrixA , Matrixx , Matrixb = refreshMatrix(BoardofGame)
        if gameMode <= 3:
            return mineLabel,BoardofGame,1
        elif gameMode == 4 or gameMode == 5:
            BoardofGame , flagJ = isJudgeable(BoardofGame)
            if flagJ:
                return mineLabel,BoardofGame,1
            else:
                mineLabel , flag = enumerateChangeBoard(mineLabel,BoardofGame,i,j)
                #上面这个函数，返回1是改图成功，0是改图失败（由于没有多余的空位等）
                return mineLabel,BoardofGame, not flag
        else:
            mineLabel , flag = enumerateChangeBoard(mineLabel,BoardofGame,i,j)
            return mineLabel,BoardofGame, not flag
    else:
        if gameMode <= 2 or gameMode >= 5:
            return mineLabel,BoardofGame,0
        else:
            if xyisJudgeable(BoardofGame , i,j):
                return mineLabel,BoardofGame,0
            else:
                if gameMode == 4:
                    BoardofGame , flagJ = isJudgeable(BoardofGame)
                    if not flagJ:
                        return mineLabel,BoardofGame,0
                    else:
                        return mineLabel,BoardofGame,1
                else:
                    return mineLabel,BoardofGame,1


def main():
    seed(seedNum)
    
    Board , Parameters=layMineSolvable(16,30,99,0,0 , 10 , 150 ,1000)
    print2(Board)
    print(Parameters[2])
#     # print(calOp(Board))
#     print(cal3BV(Board))
# #    print(isSolvable(Board , 5 , 9))
#     print2(Board)
    
    
    
    
#     Board = [[0, 1,-1, 1,0,0],
#             [1, 2, 2, 2,1,0],
#             [-1,2, 3,-1,2,0],
#             [1, 2,-1,-1,2,0],
#             [0, 1, 2, 2,1,0]]
#     BoardofGame = [[10]*len(Board[0]) for _ in range(len(Board))]
# ##    #10是未打开，11是标雷
# ##    #局面大小必须超过6*6
#     MatrixA = []
#     Matrixx = []
#     Matrixb = []
#     X0 = 0
#     Y0 = 0
#     BoardofGame , AddedCell = addedCellId(Board , BoardofGame , [(X0,Y0)] )
#     MatrixA , Matrixx , Matrixb = calMatrix(AddedCell , BoardofGame , MatrixA , Matrixx , Matrixb)
#     MatrixA , Matrixx , Matrixb , BoardofGame , NotMine = SolveEnumerate(MatrixA , Matrixx , Matrixb , BoardofGame)         
    # enumerateChangeBoard(mineLabel,MatrixA,Matrixx,Matrixb,BoardofGame,0,2,enuLimit=30)
#    SolveDirect   SolveEnumerate
#    print(NotMine)
    
    
    
    
if __name__ == '__main__':
    main()










