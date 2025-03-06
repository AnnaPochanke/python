def a(x):
    return x + 1


def b(x):
    '''
    x: int or float.
    '''
    return x + 1.0


def c(x, y):
    '''
    x: int or float. 
    y: int or float.
    '''
    return x + y


def e(x, y, z):
    '''
    x: Can be of any type.
    y: Can be of any type.
    z: Can be of any type.
    '''
    return x >= y and x <= z


print(e(a(3), b(4), c(3, 4)))
