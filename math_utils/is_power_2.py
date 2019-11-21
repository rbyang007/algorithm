def is_power_2(num):
    if num & (num - 1):
        return 1
    else:
        return 0
    
