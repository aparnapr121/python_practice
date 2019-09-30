from timeit import timeit
import re
def find_string(str,substr):
    if substr in str:
        return True
    else:
        return False

def find_re_string(str, substr):
    pattern = re.compile(substr)
    if pattern.search(str):
        return True
    else:
        return False

print(timeit("find_string(str,substr)", "from __main__ import find_string;str='lookforme';substr='look'"))
print(timeit("find_re_string(str,substr)", "from __main__ import find_re_string;str='lookforme';substr='look'"))
