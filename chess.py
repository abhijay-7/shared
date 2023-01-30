def chess():
    chess=[]
    for i in range(8):
        line=[]
        for j in range(8):
            line.append([0])
        chess.append(line)
    for i in range(8):
        if (i==0):
            chess[i][i]=[1]
        vert=[]
        for j in range(8):
            vert.append(chess[i][j])
        pre=0
        for k in range(8):
            if([1] in vert):
               pre=1
               continue
            elif([1] in chess[i]):
                pre=1
                continue
            else:
                pre=k
                
        if(pre!=1):
            chess[i][pre]=1
    for i in range(8):
        print(chess[i])
