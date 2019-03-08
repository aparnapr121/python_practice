def maxSpecialProduct(A):
        mlsp = 0
        mrsp = 0
        splprod = 0

        maxl = 0
        minr = 0
        for i in range(len(A)):
            if i > 0:
                if A[i-1] > A[i]:
                    maxl = i-1
                elif A[maxl] > A[i]:
                    maxl = maxl
                else:
                    maxl = 0
            mlsp = maxl 

            # if i > 0:
            #     if A[i+1] > A[i]:
            #         minr = i+1
            #     elif A[minr] > A[i]:
            #         minr = minr
            #     else:
            #         minr = 0

            print("for element :",A[i],"maxl :",mlsp)
            for j in range(i+1,len(A)):
                if A[j] > A[i] :
                    minr = j
                    if minr > 0 :
                        break
            mrsp = minr
            splprod=max(splprod,mlsp*mrsp)
        return splprod

if __name__ == "__main__":
    A=[7,5,7,9,8,7]
    #A=[ 5, 9,2, 8, 6, 4, 6, 9, 5, 4, 9 ]
    print(maxSpecialProduct(A))