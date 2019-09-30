import time
def make_timer():
    # This functionn creates a timer which when called returns the
    # elapsed time from the last call
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called:
            result = now - last_called
        else:
            result = None
        last_called = now
        return result
    return elapsed

# Execute the followinng commands in python console to see the true time difference
#
# t1 = make_timer()
# print(t1())
# print(t1())
# print(t1())
# t2 = make_timer()
# print(t2())
# print(t1())
# print(t2())
