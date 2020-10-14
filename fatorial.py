def fat(num):
    if(num == 0):
        return 1
    return num * fat(num-1)