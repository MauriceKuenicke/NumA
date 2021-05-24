def isAxialSymmetricY(f, x):
    if f(x) == f(x*(-1)):
        return True
    else:
        return False
