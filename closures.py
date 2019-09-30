def outer():
    x = 10
    def inner():
        return x+10
    return inner

inner_f = outer()
print(inner_f())
print(inner_f.__closure__)

print(outer.__closure__)


# no reference to enclosing scope inn inner func's body here
def outer():
    x = 10
    def inner():
        return 10
    return inner

inner_f = outer()
print(inner_f())
print(inner_f.__closure__)

print(outer.__closure__)


