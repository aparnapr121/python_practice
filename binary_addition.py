def add(x:str,y:str):
    max_len=max(len(x),len(y))
    x=x.zfill(max_len)
    y=y.zfill(max_len)
    ret_list=''
    r=0
    for i in range(max_len-1,-1,-1):
        sum = int(x[i])+int(y[i])+r

        if sum == 2:
            ret_list = '0' + ret_list
            r = 1
        elif sum == 3:
            ret_list='1'+ret_list
            r = 1
        else:
            ret_list=str(sum)+ret_list
            r=0
        print("r is",r)
        print(sum)
    if r == 1:
        ret_list='1'+ret_list




    return ret_list

print(add('1010','1011'))

