"""

what is iterable vs iterator vs generator

Inorder to make a class iterable, a class needs to implements __iter__
__iter__() must return a iterator
In order to be an iterator, a class needs to be implement __next__() which must raise
StopIteration when there are no more items to return.

Scenario:
We have a server innstannce running service on different ports.
Some og them are active some are inactive
We want to loop over active services.

"""


class IterableServer:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]

    def __init__(self):
        self.current_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos += 1
            if service['active']:
                return service['protocol'], service['port']
        raise StopIteration


IterableServerInst = IterableServer()
iterator = iter(IterableServerInst)
print(next(iterator))

"""
If iterator doesnt need to maintain a lot of state use a generator.

"""

class IterableServer:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]

    def __init__(self):
        self.current_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        # we dont maintain current_pos here
        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']
        raise StopIteration


IterableServerInst = IterableServer()
iterator = iter(IterableServerInst)
print(next(iterator))


"""
generator comprehension/ generator expression, generator is an iterator
"""

my_gen = (num for num in range(1))
next(my_gen)
next(my_gen)
