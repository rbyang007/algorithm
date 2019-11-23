def divmod_a2b(a, b):
    if b & (b - 1) == 0:
        result = a & (b - 1)
    else:
        result = a % b
    return result

