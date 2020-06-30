"""Functions for simpler display during demos."""

# use 'from functions import demo, placeholders, getinput, Status, Demo'

_placeholders = {
    'index': 1,
    'item': 'Hello',
    'true': True,
    'false': False,
    'function': do_stuff,
    'slice2': slice(1, 3),
    'slice3': slice(0, 4, 2),
    'empty_list': [],
    'empty_dict': {},
    'filled_list': [1, 'hello', 3.75, 'python', 'monkey'],
    'filled_dict': {'name': 'Bob', 'age': 32, 'job': 'farmer'}
}


def demo(name):
    """Line separation for demonstrations."""
    print('\n\n{:-^48}\n'.format(name.title()))


def placeholders(key):
    """Placeholders for demo use.

    Prevent NameErrors when writing example
    syntax code outside comments
    """
    return _placeholders.get(key)


def do_stuff(*args, **kwargs):
    """Dummy function."""
    pass


def getinput(prompt, answer):
    """Dummy input() function."""
    print(prompt)
    return answer


class Status:
    """Record the bool() value of an expression."""

    __slots__ = ['name', 'demo', 'func', 'op', 'value']

    def __init__(self, name, func, operator, value, obj=None):
        """Initialise Status object."""
        self.name = name
        self.demo = obj

        self.func = func
        self.op = operator
        self.value = value

    def __call__(self, msg):
        """Evaluate the status using function given."""
        val = False

        if self.op == 'is':
            val = self.func(self.demo) is self.value

        if self.op == '==':
            val = self.func(self.demo) == self.value

        if self.op == '!=':
            val = self.func(self.demo) != self.value

        if self.op == '>':
            val = self.func(self.demo) > self.value

        if self.op == '<':
            val = self.func(self.demo) < self.value

        if self.op == '>=':
            val = self.func(self.demo) >= self.value

        if self.op == '<=':
            val = self.func(self.demo) <= self.value

        if self.op == 'in':
            val = self.func(self.demo) in self.value

        if self.op == 'is not':
            val = self.func(self.demo) is not self.value

        if self.op == 'not in':
            val = self.func(self.demo) not in self.value

        print(msg)
        print('{}({}) {} {} returns {}\n'.format(self.func.__name__,
                                                 self.name,
                                                 self.op,
                                                 self.value,
                                                 val))
        return val

        # if self.func(self.demo) == self.value:
        #     print('{} is True'.format(self.name))
        #     return True
        # else:
        #     print('{} is False'.format(self.name))
        #     return False


class Demo:
    """Class which holds information for demonstrations.

    Helps to quickly print a consistent demo structure.
    """

    __slots__ = ['name', 'demo']

    def __init__(self, name, obj=None):
        """Inititalise a new Demo object."""
        self.demo = None  # the object it represents
        self.name = name

    def __call__(self, msg):
        """Display a message when called and object state."""
        print(msg)
        print('{}: {}\n'.format(self.name, self.demo))
