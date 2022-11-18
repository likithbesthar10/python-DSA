def pal(num):
    x = num[::-1]
    if num == x:
        return True
    else:
        return False
print(pal("madam"))           