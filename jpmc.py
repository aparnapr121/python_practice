# -*- coding: utf-8 -*-
import sys


def modify_integer(input_list):
    """
    This function modifies the numbers in the input list
    args:input_list A list of characters which can be converted to int
    returns : a string
    """
    ret_list = []
    ret_list.append(input_list[0])
    i = 1
    while i < len(input_list):
        cur_num = int(input_list[i])
        prev_num = int(input_list[i - 1])
        if cur_num != 0 and prev_num != 0:
            if cur_num % 2 == 0 and prev_num % 2 == 0:
                ret_list.append('*')
            elif cur_num % 2 == 1 and prev_num % 2 == 1:
                ret_list.append('-')
        ret_list.append(input_list[i])
        i += 1
    return ''.join(ret_list)


for line in sys.stdin:
    l1 = len(line)
    list_int = list(line[:l1 - 1])
    print(modify_integer(list_int))