def spiralOrder( A):
        ret_list=[]
        t=0
        b=len(A)
        l=0
        r=len(A[0])
        dir = 0
        while t < b and l <  r:
            print("direction")
            print(dir)
            if dir == 0:
                for i in range(l,r):
                    ret_list.append(A[t][i])
                t = t+1
            elif dir == 1:
                for i in range(t,b):
                    print("i is :",i)
                    print("r is :",r)
                    ret_list.append(A[i][r])
                r = r-1
            dir = (dir+1)%4
            
        return ret_list

if __name__ == "__main__":
    A=[
       [1, 2],
       [3, 4],
       [5, 6],
       ]
    print(spiralOrder(A))