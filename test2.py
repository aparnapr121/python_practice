def compareFriends(frndsList):
    # Write your code here
    res = []

    f_len = len(frndsList) - 1
    i = 0
    j = 0
    l1 = []
    res = []
    for x in frndsList:
        l1.append(x.split(","))
    l1.sort(key=lambda x: (x[0], x[1]))
    print(l1)
    for x in l1:
        print(x)
        flag = 1
        for y in res:
            print(y)
            if x[0] == y[1] and x[1] == y[0]:
                flag = 0
                break
        print("flag ",flag)
        if flag == 1:
            res.append(x)
    res1 = []
    for x in res:
        res1.append(','.join(x))
    return res1

if __name__ == "__main__":
    A=[
       "A,B" , "B,C", "A,B"
       ]
    print(compareFriends(A))