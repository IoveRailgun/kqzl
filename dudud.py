
def datte():
    cc=[]
    for e in range(2015,2019):
        for j in range(1,13):
            p=j
            if len(str(p))==1:
                p='0'+str(p)
                u = str(e)+p
            else:
                u=str(e)+str(p)
            cc.append(u)
            u=''
    print(cc)

datte()