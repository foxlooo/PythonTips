# Tutorial on Decorator Functions

def decorator_function(orig_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(orig_func.__name__))
        return orig_func(*args, **kwargs)
    return wrapper_func

class decorator_class(object):
    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        print('Call Method Executed this before {}'.format(self.orig_func.__name__))
        return self.orig_func(*args, **kwargs)

@decorator_function # @decorator_class works as well
def display():
    print('display function ran')

@decorator_class # @decorator_function works
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display()
display_info("John", 25)

# Practical Uses Below

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper

@my_logger
def display_info_time(name, age):
    print('display_info_time ran with arguments ({}, {})'.format(name, age))

display_info_time("Check", 12)