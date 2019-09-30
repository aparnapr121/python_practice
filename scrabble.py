def find_next(char, word_list):
    index=word_list.index(char)
    return word_list[index+1]

def append_neighbours(neigh_list, matrix):
    retlist = []
    matrix_row=len(matrix)
    matrix_col=len(matrix[0])
    for x in neigh_list:
        i=x[0]
        j=x[1]
        if i >= 0 and i <= matrix_row and j >= 0 and j <= matrix_col:
            retlist.append(x)
    return retlist


def get_neighbour(i,j, matrix):
    matrix_row=len(matrix) - 1
    matrix_col=len(matrix[0]) - 1
    nei_list=[(i, j-1), (i,j+1),
              (i-1, j), (i + 1, j),
              (i-1, j-1), (i-1,j+1),
              (i+1, j-1), (i+1, j+1)
              ]

    retlist=append_neighbours(nei_list, matrix)
    return retlist


def check_if_word_exists(word, matrix=None):
    word_list=list(word)
    m=len(matrix)#row
    n=len(matrix[0])#col
    char_index=0
    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j] == word[char_index]:
                char_index+=1
                n_list=get_neighbour(i, j, matrix)
                for x in n_list:
                    k = x[0]
                    l = x[1]
                    #check if the second character matches one of the neighbours
                    if matrix[k][l] == word[char_index]:
                        if i == k and j > l:
                            k = k
                            l = l-1
                        elif i == k and j < l:
                            k = k
                            l = l + 1
                        elif i > k and j == l:
                            k = k-1
                            l=l
                        elif i < k and j == l:
                            k = k+1
                            l=l
                        elif i > k and j > l:
                            k = k-1
                            l = l - 1
                        elif i > k and j < l:
                            k = k-1

                            l=l+1
                        elif i<k and j > l:
                            k=k+1
                            l=l-1
                        elif i<k and j<l:
                            k=k+1
                            j=j+1
                        dir1=i-k
                        dir2=j-l
                        #Check if the rest of the characters match
                        for w in word[2:]:
                            if matrix[k][l] == w:
                                if dir1 == 0:
                                    k=k
                                    if dir2 < 0:
                                        l=l+1
                                    else:
                                        l=l-1
                                if dir2 == 0:
                                    l=l
                                    if dir1 < 0:
                                        k=k+1
                                    else:
                                        k=k-1
                                if dir1 < 0:









    print(list(word))

check_if_word_exists("aparna", None)